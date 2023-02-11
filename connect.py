import argparse
import os
import json
import re
import colorama
from colorama import Fore
found = False
os.chdir('Baseboard')
with open('key_val_file.json', 'r') as f:
    data = json.load(f)
    for i in data:
        fileName = data['toplevelfile']['file_name']
        folder_name = data['toplevelfile']['folder_name']
        child_path = data['toplevelfile']['child_path']

def check_range_equality(inst1, inst2, k1, k2):
    global found 
    try:
        for i1, i2, k1, k2 in zip(args.instance1, args.instance2, args.input_ports, args.output_ports):
            range1 = data[inst1]['ports'][k1]['range']
            range2 = data[inst2]['ports'][k2]['range']
            if range1 == range2:
                found = True
            else:
                print(Fore.RED + f'Error: Range of {k1} is {range1} and range of {k2} is {range2}, which are not equal!' + Fore.RESET)
        return found
    except KeyError:
        for i1, i2, k1, k2 in zip(args.instance1, args.instance2, args.input_ports, args.output_ports):
            if inst1 not in data:
                print(Fore.RED + f'Error: Instance {inst1} not found' + Fore.RESET)
                # found = False
                # return found
            elif inst2 not in data:
                print(Fore.RED + f'Error: Instance {inst2} not found' + Fore.RESET)
                # found = False
                # return found
            elif k1 not in data[inst1]['ports']:
                print(Fore.RED + f'Error: Port {k1} not found for instance {inst1}' + Fore.RESET)
                # found = False
                # return found
            elif k2 not in data[inst2]['ports']:
                print(Fore.RED + f'Error: Port {k2} not found for instance {inst2}' + Fore.RESET)
            found = False
        return found

def change_line_in_instance(found,instance1, input_ports, output_ports):
    with open(f"{fileName}", 'r') as f:
        content = f.read()
    # Extract the block of code corresponding to the first instance
    pattern = rf'{instance1}\s*(([\s\S]*?));'
    match = re.search(pattern, content)
    if found and match:
        block = match.group()
        for input_port, output_port in zip(input_ports, output_ports):
            pattern = rf'\.{input_port}\s*\([\s\S]*?\)'
            match = re.search(pattern, block)
            if match:
                line = match.group()
                output_port_match = re.search(f'{input_port or output_port}', line)
                if output_port_match:
                    print(Fore.RED + f'Error:{input_port or output_port} Already connected to {input_port or output_port}.' + Fore.RESET)
                    return
                else:
                    block = re.sub(
                        pattern, f'.{input_port} \t\t\t\t({output_port})', block)
            else:
                print(Fore.RED + f'Error: {input_port} not found.' + Fore.RESET)
                return
        # Replace the original block of code with the modified one
        pattern = rf'{instance1}\s*(([\s\S]*?));'
        content = re.sub(pattern, block, content)
        print(Fore.BLUE + 'Ports Connection successfull.' + Fore.RESET)
    # Write the modified content back to the file
    with open(f"{fileName}", 'w') as f:
        f.write(content)



if __name__ == '__main__':
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description='Change lines in instances in a Verilog file')
    # Add arguments for the instances and ports
    parser.add_argument('-i', '--instance1', required=True,
                        help='Name of the first instance')
    parser.add_argument('-o', '--instance2', required=True,
                        help='Name of the second instance')
    parser.add_argument('-ip', '--input_ports', nargs='+', type=str,
                        required=True, help='Input ports of the first instance')
    parser.add_argument('-op', '--output_ports', nargs='+', type=str,
                        required=True, help='Output ports of the second instance')
    # Parse the arguments
    args = parser.parse_args()
    if len(args.input_ports) != len(args.output_ports):
        print(Fore.RED + 'Number of input ports is not equal to number of output ports.' + Fore.RESET)
        exit()
    found = check_range_equality(
        args.instance1, args.instance2, args.input_ports, args.output_ports)
    change_line_in_instance(found, args.instance1,
                            args.input_ports, args.output_ports)
