import re, os
import json
os.chdir('Baseboard')
# fileName = 'Baseboard.sv'
# old_name = 'bilal'
# new_name = 'nn'

def rename_module(fileName,old_name,new_name):
    new_lines =[]
    with open(fileName,'r+') as f:
        content = f.readlines()
        for line in content:
            if f"{old_name}" in line:
                line = line.split()
                line[-1] = f" {new_name}"
                new_lines.append(' '.join(line) + '\n')
            else:
                new_lines.append(line)
        with open(fileName,'w+') as f:
            f.writelines(new_lines)


def update_key(old_name, new_name):
    with open('key_val_file.json', 'r') as json_file:
        data_dict = json.load(json_file)
    if old_name in data_dict:
        data_dict[new_name] = data_dict.pop(old_name)
        with open('key_val_file.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)
        return f"{old_name} key renamed to {new_name}."
    else:
        return f"{old_name} key not found."
    
    
update_key("Baseboard","base")
rename_module("Baseboard.sv","bilal","Base")