module formula(a0,a1,b0,b1,out);
	input a0,a1,b0,b1;
	output cout0, cout1;

	assign cout0 = a0 ^ a1;
	assign cout1 = (b0 ^ b1) | (a0 & a1);

endmodule
