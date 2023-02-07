import argparse
import os
import json
import re
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
    for i1, i2, k1, k2 in zip(args.instance1, args.instance2, args.input_ports, args.output_ports):
        range1 = data[inst1]['ports'][k1]['range']
        range2 = data[inst2]['ports'][k2]['range']
        if range1 == range2:
            found = True
        else:
            print(f'Range {range1} is not equal to {range2}')
            exit()
    return found


def change_line_in_instance(found, instance1, input_ports, output_ports):
    with open(f"{fileName}", 'r') as f:
        content = f.read()
    # Extract the block of code corresponding to the first instance
    pattern = rf'{instance1}\s*(([\s\S]*?));'
    match = re.search(pattern, content)
    if found and match:
        block = match.group()
        for input_port, output_port in zip(input_ports, output_ports):
            pattern = rf'\.{input_port}\s*\([\s\S]*?\)'
            block = re.sub(
                pattern, f'.{input_port} \t\t\t\t({output_port})', block)
            # print(block)
        # Replace the original block of code with the modified one
        pattern = rf'{instance1}\s*(([\s\S]*?));'
        content = re.sub(pattern, block, content)
        # print(content)
        print('Ports Connected.')
    else:
        print('Error: Not connected.')
        exit()

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
    found = check_range_equality(
        args.instance1, args.instance2, args.input_ports, args.output_ports)
    change_line_in_instance(found, args.instance1,
                            args.input_ports, args.output_ports)
