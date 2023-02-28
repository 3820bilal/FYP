#!/usr/bin/python3
import os
import argparse
import json
import Extracting_data
import add_in_out
import colorama
from colorama import Fore
os.chdir('..')
os.chdir('Baseboard')

with open("key_val_file.json", "r") as f:
    content = json.load(f)
    for i in content:
        fileName = content['toplevelfile']['file_name']
        folder_name = content['toplevelfile']['folder_name']

# os.chdir('..')
# os.chdir('library') 

def extract_data(file):
    with open(f"{file}", 'r') as f:
        lines = f.readlines()
    in_module = False
    input_or_output_count = 0
    output_string = ""
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
            if input_or_output_count == sum(('input' in line) or ('output' in line) for line in lines):
                output_string += '.' + x + '\t\t\t()\n'
            else:
                output_string += '.' + x + '\t\t\t(),\n'
    os.chdir('..')
    os.chdir('Baseboard')
    with open(f"{fileName}", "r") as f:
        content = f.read()
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if instance in line and ('input' or 'output') not in line:
                print(Fore.RED +
                      f'Error: instance {instance} already exists at line {i+1}. Please Enter different name!' + Fore.RESET)
                exit()
        with open(f"{fileName}", "a+") as f:
            if 'endmodule' in content:
                r_end = (f.tell())-9
                x = f.truncate(r_end)
                f.write('\n\n' + output_string)
                f.write(');')
                f.write('\n\nendmodule')
            print(
                Fore.GREEN + f'instance {instance} is successfully pluged in {fileName}.' + Fore.RESET)


# extract_data('reg.sv')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--instance_name', help='Name of instance')
    parser.add_argument('-p', '--plug', help='Name of instance')
    parser.add_argument('-f', '--file_name',
                        help='Name of file from which instance is taken',type=str)
    parser.add_argument('-i', '--inputs', type=str,
                        nargs='+', help='Input port name')
    parser.add_argument('-ir', '--input_ranges', type=str,
                        nargs='+', help='Input port range')
    parser.add_argument('-o', '--outputs', type=str,
                        nargs='+', help='Output port name')
    parser.add_argument('-or', '--output_ranges',
                        nargs='+', help='Output port range')
    args = parser.parse_args()
    file = args.file_name
    instance = args.instance_name
    
    if args.plug=='port':
        os.chdir('..')
        os.chdir('Baseboard')
        inputs = args.inputs
        input_ranges = args.input_ranges
        outputs = args.outputs
        output_ranges = args.output_ranges
        add_in_out.add_inputs_outputs(
        fileName, inputs, outputs, input_ranges, output_ranges)
    elif args.plug=='instance':
        os.chdir('..')
        os.chdir('library')
        extract_data(file)
        os.chdir('..')
        os.chdir('library')
        data = Extracting_data.get_ranges_from_file(file)
        os.chdir('..')
        os.chdir('Baseboard')
        with open("key_val_file.json", "rb") as f:
            content = f.read()
            f.seek(0, 2)
        with open('key_val_file.json', 'a+') as f:
            r_end = (f.tell())-1
            x = f.truncate(r_end)
            f.write(f',\n\"{instance}\":')
            json.dump(data, f, indent=4)
            f.write("\n}")


