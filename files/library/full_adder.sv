module full_adder
(
	input 		x,
	input 		y,
	input 		z,
	output  reg	sum,
	output  reg	carry
);

wire sm;
wire cr;
wire crm;

half_adder inst1
(
.a		(x),
.b		(y),
.s		(sm),
.c		(cr)
);



half_adder inst2
(
.a		(sm),
.b		(z),
.s		(sum),
.c		(crm)
);

assign carry = cr | crm;


endmodule
