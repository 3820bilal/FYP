module processor
#(
	parameter DATA_END_ADDR = 5,
	parameter DATA_START_ADDR = 0,
	parameter DATA_FILE = "data_file.txt",
	parameter PROG_END_ADDR = 8,
	parameter PROG_START_ADDR = 0,
	parameter PROG_FILE = "program.hex",
	parameter RAM_ADDR_BITS = 9,
	parameter RAM_WIDTH = 32,
 	parameter WIDTH = 9
)
(
input               clk,
input               reset

);
parameter	SW	= 'd5;
parameter	LW	= 'd4;
parameter	zero	= 0;
parameter	single_bit0	= 1'b0;
parameter	single_bit1	= 1'b1;
parameter	opcode_2bit	= opcode[1:0];
parameter	instr_addr2	= instr[16:12];
parameter	instr_addr1	= instr[21:17];
parameter	wr_addr_instr	= instr[26:22];
parameter	datamem_addr_instr	= instr[8:0];
wire  	   	 ctl1;
wire  	   	 ctl2;
wire  	   	 ctl3;
wire  	 [WIDTH-1:0] 	 prog_cnt;
wire  	 [RAM_WIDTH-1:0] 	 op1;
wire  	 [RAM_WIDTH-1:0] 	 op2;
wire  	 [RAM_WIDTH-1:0] 	 dram_data_out;
wire  	 [RAM_WIDTH-1:0] 	 alu_out;
wire  	 [RAM_WIDTH-1:0] 	 reg_data_in;
wire  	 [RAM_WIDTH-1:0] 	 instr;
reg  	 [4:0] 	 opcode;


up_counter 
#(
	
.WIDTH             (WIDTH)
)
up_counter_inst
(
.clk                (clk),
.reset              (reset),
.count              (prog_cnt)
);



prg_mem 
#(
	
.RAM_WIDTH         (RAM_WIDTH),
.RAM_ADDR_BITS     (RAM_ADDR_BITS),
.PROG_FILE         (PROG_FILE),
.PROG_START_ADDR   (PROG_START_ADDR),
.PROG_END_ADDR     (PROG_END_ADDR)
)
prg_mem_inst
(
.clock              (clk),
.ram_enable          (single_bit1),
.write_enable        (single_bit0),
.address            (prog_cnt),
.in_data             (zero),
.out_data           (instr)
);



reg_file regfile_inst
(
.clk                (clk),
.rd_addr1            (instr_addr1),
.rd_addr2            (instr_addr2),
.rd_data1           (op1),
.rd_data2           (op2),
.wr_addr             (wr_addr_instr),
.wr_en              (ctl1),
.wr_data            (reg_data_in)
);



ALU 
#(
	
.RAM_WIDTH         (RAM_WIDTH)
)
ALU_inst
(
.clk                (clk),
.opcode              (opcode_2bit),
.op1                (op1),
.op2                (op2),
.result             (alu_out)
);



Mux 
#(
	
.RAM_WIDTH         (RAM_WIDTH)
)
Mux_inst
(
.s_l                (ctl2),
.in0                (alu_out),
.in1                (dram_data_out),
.out                (reg_data_in)
);



data_mem 
#(
	
.RAM_WIDTH         (RAM_WIDTH),
.RAM_ADDR_BITS     (RAM_ADDR_BITS),
.DATA_FILE         (DATA_FILE),
.DATA_START_ADDR   (INIT_START_ADDR),
.DATA_END_ADDR     (INIT_END_ADDR)
)
data_mem_inst
(
.clock              (clk),
.ram_enable          (single_bit1),
.write_enable       (ctl3),
.address             (datamem_addr_instr),
.in_data            (op1),
.out_data           (dram_data_out)
);



not_gate inst_not_gate
(
.in                 (ctl3),
.out                (ctl1)
);



comparator 
#(
	
.DATA_END_ADDR     (WIDTH)
)
inst_comparator
(
.in0                (opcode),
.in1                 (LW),
.out                (ctl2)
);



comparator 
#(
	
.DATA_END_ADDR     (WIDTH)
)
inst1_comparator
(
.in0                (opcode),
.in1                 (SW),
.out                (ctl3)
);

endmodule