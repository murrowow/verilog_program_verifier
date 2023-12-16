module adder(a0, a1, b0, b1,
	         cout0, cout1);
	input a0, a1, b0, b1;
	output cout0, cout1;

 	assign cout0 = a0 ^ b0;
	assign cout1 = (a1 ^ b1) ^ (a0 & b0);

endmodule
