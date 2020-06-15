// A couple of blank lines to throw off the old program


// Comments too


module adder(
    input a,
    input b, // EOL comment
    output s,
    input cin,
    output cout,
    input [7:0] bus_in);

///////////////
// Wire Def. //
///////////////
    wire x_out, x_in, z, y, lut_out;

/////////////////
// Sub modules //
/////////////////
    buf buffer(x_out, x_in);

    lut4 lut4_asdf(
        #( .init(16'hffff) ),
        .a(),
        .b(),
        .c(z),
        .d(y),
        .out(lut_out));
endmodule
