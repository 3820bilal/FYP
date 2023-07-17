#!/bin/bash
create -f counter.sv -i increment decrement -ir None None -o count -or [3:0] #
plug -inst OR.sv -n OR_gate	#plug instance up_counter.sv
plug -m -im "count-1" "count+1" -om mux_out -sl increment #
plug -r -i mux_out -ir [3:0] -o count -en enable #
connect -i OR_gate -ip in1 in2 out -op increment decrement enable # Top_level_file inputs/outputs to instance ports