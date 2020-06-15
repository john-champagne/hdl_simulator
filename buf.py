# buf.py

# buf buf_name(x_out, x_in);

from string_utils import *

class submod():
    name = ""
    def __init__(self,hdl,line):
        line_split = line.split(" ")
        self.name = line_split[1][:line_split[1].find("(")]

        # Extract arguments
        args = removeUntil(line, "(")
        args = removeList(args, [");"])
        args = args.split(",")

        input_name = args[1].strip()
        output_name = args[0].strip()

        hdl.add_wire(self.name + ".i")
        hdl.add_wire(self.name + ".o")

        hdl.add_connection(input_name, self.name + ".i")
        hdl.add_connection(self.name + ".o", output_name)

    def get_output(self, hdl, output_name):
        if output_name == "o":
            # Return the value of the input
            return hdl.get_value(self.name + ".i")
        else:
            return
        

