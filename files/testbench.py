global tabsize
tabsize = 12
mytab = 7

def myfun(file,instance):
    with open(f"{file}", 'r') as f:
        lines = f.readlines()
        
    in_module = False
    input_or_output_count = 0
    output_string = ""
    inp = ""
    opt = ""
    myinp = ""
    myout = ""
    simp_myout = ""
    clk_gen = ""
    for line in lines:
        if 'module' in line and not in_module:
            in_module = True
            module_name = line.split()[1]
            output_string += module_name + ' ' + f'{instance}' + '\n'
            output_string += "(\n"
        if 'input' in line or 'output' in line:
            input_or_output_count += 1
            words = line.strip().split()
            x = words[-1]
            if "," in x:
                x = x.split(",")[0]
            if x == "clk":
                clk_gen = "\ninitial begin\n\tclk = 0;\n\tforever #5 clk = ~clk;\nend\n"
            if input_or_output_count == sum(('input' in line) or ('output' in line) for line in lines):
                output_string += '.' + x.ljust(tabsize) + f'({x.ljust(tabsize)})\n'
                if words[0] == "input":
                    inp += "reg".ljust(tabsize) + f"{x};\n"
                    myinp += x.ljust(mytab) + "= 0;\n\t"
                elif  words[0] == "output":
                    opt += "wire".ljust(tabsize) + f"{x};\n"
                    myout += x + "=%d"
                    simp_myout += x
            else:
                output_string += '.' + x.ljust(tabsize) +  f'({x.ljust(tabsize)}),\n'
                if words[0] == "input":
                    inp += "reg".ljust(tabsize) + f"{x};\n"
                    myinp += x.ljust(mytab) + "= 0;\n\t"
                elif  words[0] == "output":
                    opt += "wire".ljust(tabsize) + f"{x};\n"
                    myout += x + "=%d,"
                    simp_myout += x + ","


    string = f"initial begin \n\t"
    string1 = f"#200 $finish;\nend"
    disp = f'$display('
    disp1 = f'"{myout}",{simp_myout}'
    # print(myinp)
    with open(f"myfile.sv", "r") as f:
        content = f.read()
        with open(f"myfile.sv", "a+") as f:  
            m_name = file.replace(".sv","")
            f.write(f"module tb_{m_name};\n")
            f.write(inp)
            f.write(opt)
            f.write('\n\n' + output_string)
            f.write(');')                                                               
            f.write("\n" + clk_gen)
            f.write("\n" + string)
            f.write(myinp + "\n\n\t#30;")
            f.write("\n\t" + disp)
            f.write(disp1 + ");\n")
            f.write("\n\t" + string1)
            f.write('\n\nendmodule')
            
myfun("add.sv","DUt")