module tb_add;
reg         clk;
reg         reset;
wire        Led;
wire        segments;
wire        anodes;


digital_clock DUt
(
.clk         (clk         ),
.reset       (reset       ),
.Led         (Led         ),
.segments    (segments    ),
.anodes      (anodes      )
);

initial begin
	clk = 0;
	forever #5 clk = ~clk;
end

initial begin 
	clk    = 0;
	reset  = 0;
	

	#30;
	$display("Led=%d,segments=%d,anodes=%d",Led,segments,anodes);

	#200 $finish;
end

endmodule