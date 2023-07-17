create -f up_counter.sv -o count -or "[WIDTH-1:0]" #create file
add -P WIDTH -v "32" # dfgdgh
add -w add_out -rn "[WIDTH-1:0]" # add reg
add -w reg_rst_out -rn "[WIDTH-1:0]" #ghjkkkl
##### plug reg_rst ########## 
plug -inst reg_rst.sv -n reg_rst_inst	#plug instance reg_rst.sv
add -ow WIDTH -nw WIDTH -inst reg_rst_inst #jkjkjkj
connect -i reg_rst_inst -ip clk reset -op clk reset #hdfghf
connect -w add_out -i reg_rst_inst -ip data_in # connect : wire to instance ports
##connect -i reg_rst_inst -op reg_rst_out -ip data_out #hdfghf
connect -w reg_rst_out -i reg_rst_inst -ip data_out # connect : wire to instance ports
###### plug add ##########
plug -inst add.sv -n add_inst	#plug instance reg_rst.sv
add -ow WIDTH -nw WIDTH -inst add_inst #jkjkjkj
connect -v "32'b1" -i add_inst -ip in1 #fhdh
##connect -i add_inst -op count -ip in2 #hdfghf
connect -w reg_rst_out -i add_inst -ip in2 # c
connect -w add_out -i add_inst -ip out # connect : wire to instance ports
##### combinational block ##########
plug -r -i reg_rst_out -o count #ghjhj