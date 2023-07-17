module register 
(
	input 				clk,
	input 				reset,
	input 				en,
	input 	[3:0] 		data_in,
	output reg [3:0] 	data_out
);

always@(posedge clk)
	if(reset)	data_out <= 0;
	else if(en)	data_out <= data_in;

endmodule