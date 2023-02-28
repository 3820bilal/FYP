#!/usr/bin/python3
import colorama
from colorama import Fore
import re
import os
import argparse
import json
import fileinput
os.chdir('Baseboard')


def json_delete_port(filename,port_name):
    module_name = filename.replace(".sv","")
    with open('key_val_file.json', 'r') as f:
        data = json.load(f)

    # Delete the "clk" port from the "ports" object within the "Baseboard" object
    if module_name in data and "ports" in data[module_name] and f"{port_name}" in data[module_name]["ports"]:
        del data[module_name]["ports"][port_name]

    # Save the updated JSON file
    with open('key_val_file.json', 'w') as f:
        json.dump(data, f, indent=4)


def delete_port(filename, port_name):
    # Remove the line containing the string and print the previous line
    new_lines = []
    prev_line = ""
    deleted = False  # flag to track if the port has been deleted

    for line in fileinput.input(fileName, inplace=True):
        if port_name in line and not ',' in line:
            line = prev_line.rstrip(',\n') + "\n"
            new_lines[-1] = line
            deleted = True
        elif port_name in line and ",":
            line = prev_line.rstrip(',\n') + "\n"
            deleted = True
        else:
            new_lines.append(line)
            prev_line = line
    if deleted:  # print message only if port is deleted
        print(Fore.GREEN +
              f"Port {port_name} has been deleted successfully." + Fore.RESET)
    else:
        print(Fore.RED + "Port not found." + Fore.RESET)

    with open(filename, 'w') as file:
        file.writelines(new_lines)
    fileinput.close()


def json_delete_instance(instance):
    with open('key_val_file.json', 'r') as f:
        data = json.load(f)
    # Check if the object with the specified name exists and delete it if it does
    if instance in data:
        del data[instance]

    # Save the updated JSON file
    with open('key_val_file.json', 'w') as f:
        json.dump(data, f, indent=4)


def delete_instance(fileName, instance):
    with open(f"{fileName}", 'r') as f:
        content = f.read()
    pattern = rf'.*{instance}\s*(([\s\S]*?));'
    match = re.search(pattern, content)
    if match:
        block = match.group()
        block = block.replace(block, '')
        content = re.sub(pattern, block, content)
        print(Fore.GREEN +
              f"instance {instance} has been deleted successfully." + Fore.RESET)
    else:
        print(Fore.RED + f"instance {instance} is not found." + Fore.RESET)
    with open(fileName, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', "--file_name", help="Name of file where instance needs to be removed from")
    parser.add_argument("-d", "--delete", nargs='+',
                        help="Name of instance to be removed")
    arg = parser.parse_args()

    fileName = arg.file_name

    if arg.delete[0] == 'port':
        port = arg.delete[1]
        json_delete_port(fileName,port)
        delete_port(fileName, port)
    elif arg.delete[0] == 'instance':
        instance = arg.delete[1]
        delete_instance(fileName, instance)
        json_delete_instance(instance)
