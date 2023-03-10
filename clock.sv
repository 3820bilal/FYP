module clock (
input	logic		clk,
input	logic		reset,
input	logic		clk,
input	logic		reset,
input	logic		en,
input	logic	[5:0]	count_max_hrs,
input	logic		clr_sec,
input	logic	[5:0]	count_sec,
output	logic		clr_min,
output	logic	[5:0]	count_min,
output	logic		clr_hrs,
output	logic	[5:0]	count_hrs

);


up_counter Sec
(
.clk 				(clk),
.reset 				(reset),
.en 				(en),
.count_max 				(count_max),
.clr 				(clr_sec),
.count 				(count_sec)
);



up_counter Min
(
.clk 				(clk),
.reset 				(reset),
.en 				(en),
.count_max 				(count_max),
.clr 				(clr_min),
.count 				(count_min)
);



up_counter Hr
(
.clk 				(clk),
.reset 				(reset),
.en 				(en),
.count_max 				(count_max_hrs),
.clr 				(clr_hrs),
.count 				(count_hrs)
);

endmodule