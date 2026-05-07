#!/usr/bin/env python3
from importlib.resources import files
import sys
import os
import glob

from parser import Parser
from translator import Translator

def find_vm_files(directory):
    
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)

    vm_files = []
    for f in glob.glob(os.path.join(directory, "**", "*.vm"), recursive=True):
        vm_files.append(f)

    
    #vm_files = [
     #   f for f in glob.glob(os.path.join(directory, "**", "*vm"), recursive=True)
    #]
    print(f"Found {len(vm_files)} '.vm' files in '{directory}':")
    for f in vm_files:
        print(f"  {f}")
    sys_vm_file = os.path.join(directory, "Sys.vm")

    if sys_vm_file not in vm_files:
        print(f"Warning: 'Sys.vm' not found in '{directory}'")
        sys.exit(1)
    else:
        vm_files.remove(sys_vm_file)
        vm_files.insert(0, sys_vm_file)


    return vm_files


def main():
    if len(sys.argv) < 2:
        print("Usage: python find_vm_files.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    print(f"Searching for files ending with 'vm' in: {directory}\n")

    vm_files = find_vm_files(directory)

    bootstrap = 'bootstrap.asm'
    
    output_file = vm_files[0].replace('.vm', '.asm')

    with open(output_file, 'w') as f:
        with open(bootstrap, 'r') as b:
            for line in b:
                f.write(line)

    for filename in vm_files:
        instrunctions = []
        parser = Parser(filename)

        parser.readFile()
        instrunctions = parser.returnParsedCommands()

        translator = Translator(parser.parseFilename(), instrunctions)

        text = translator.translateCommands()

        with open(output_file, 'a') as f:
            f.write(text)



if __name__ == "__main__":
    main()