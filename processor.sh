#!/bin/bash
create -f processor.sv	#create file
add -P WIDTH RAM_WIDTH -v "9" "32"  #adding parameters
add -w instr prog_cnt op1 op2 ctl1 ctl3 ctl2 reg_data_in alu_out dram_data_out  #adding wire 1-bit
plug -inst up_counter.sv -n up_counter_inst	#plug instance up_counter.sv
plug -inst prg_mem.sv -n prg_mem_inst	#plug instance up_counter.sv 
plug -inst regfile.sv -n regfile_inst       #plug instance up_counter.sv
plug -inst ALU.sv -n ALU_inst                 #plug instance up_counter.sv
plug -inst Mux.sv -n Mux_inst                 #plug instance up_counter.sv
plug -inst data_mem.sv -n data_mem_inst	#plug instance up_counter.sv
plug -inst not_gate.sv -n inst_not_gate	#plug instance up_counter.sv 
plug -inst comparator.sv -n inst_comparator	#plug instance up_counter.sv
plug -inst comparator.sv -n inst1_comparator	#plug instance up_counter.sv