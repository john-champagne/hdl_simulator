import io

import buf

from string_utils import *

class HDL_File:
    pins = dict()
    nodes = dict()
    wires = dict()
    submodules = dict()
    

    file_string = []
    file_string_reduced = []
    def read_hdl_file(self, filename):
        with io.open(filename, "r") as fin:
            for line in fin:
                # Remove empty lines and comment lines
                if startsWith(line, "//") or len(line.strip()) == 0:
                    continue
                else:
                    self.file_string.append(line)
        complete = False
        s = ""
        for line in self.file_string:
            line = removeComments(line.strip()).strip()
            s += removeComments(line.strip())
            if line.find(";") != -1:
                self.file_string_reduced.append(s)
                s = ""

    def read_pins(self):
        module_string = ""
        read_until_module_keyword = False
        for line in self.file_string:
            line = removeComments(line)
            if line.find("module") == -1 and read_until_module_keyword == False:
                continue
            if line.find(");") != -1:
                module_string += line.strip()
                break
            module_string += line.strip()
            read_until_module_keyword = True
        print(module_string)
        # Remove module name 
        module_string = removeUntil(module_string, "(")
        # Remove the ');' at the end
        module_string = module_string.replace(");","").strip()
        pin_list = module_string.split(",")
        for pin in pin_list:
            pin = pin.strip()
            P = pin.split(" ")
            # Non-bus form: input w
            if len(P) == 2:
                self.pins[P[1]] = dict(direction = P[0])
            # Bus form: input [3:0] w
            elif len(P) == 3:
                # Get the size of the bus
                bus_length = eval(P[1][P[1].find("[")+1:P[1].find(":")]) + 1
                print(bus_length)
                for i in range(bus_length):
                    self.pins[P[2] + "[" + str(i) + "]"] = dict(direction = P[0])
    def add_wire(self,wirename, driver=""):
        self.wires[wirename] = dict(driver = driver, driving = [])

    def add_connection(self,driver_wire, driving_wire):
        self.wires[driver_wire]['driving'].append(driving_wire)
        self.wires[driving_wire]['driver'] = driver_wire

    def read_wires(self):
        for line in self.file_string:
            line = removeComments(line)
            if startsWith(line, 'wire'):
                # Remove wire keyword and semicolon
                line = removeList(line, ['wire', ';'])
                wires = line.split(',')
                for wire in wires:
                    wire_name = wire.strip()
                    self.wires[wire_name] = dict( driver = "", driving = [])

    def read_submodules(self):
        for line in self.file_string_reduced:
            if startsWith(line, "module") == False and startsWith(line, "wire") == False:
                line_split = line.split(" ")
                submodule_type = line.split(" ")[0].strip()
                submodule_name = line_split[1][:line_split[1].find("(")].strip()
                exec("self.submodules[submodule_name] = " + submodule_type + ".submod(self, line)")
                print("{} => {}".format(submodule_type,submodule_name))

            



H = HDL_File()
H.read_hdl_file("test_modules/t1.v")
H.read_wires()
H.read_submodules()

pprint(H.wires)
