import sys
import os
from parser import Parser
from translator import Translator

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename.vm>")
        sys.exit(1)

    vm_file = sys.argv[1]

    if not os.path.exists(vm_file):
        print(f"Error: file '{vm_file}' not found")
        sys.exit(1)

    if not vm_file.endswith('.vm'):
        print("Error: file must have .vm extension")
        sys.exit(1)

    instructions = []
    parser = Parser(vm_file)

    parser.readFile()
    instructions = parser.returnParsedCommands()

    translator = Translator(parser.parseFilename(), instructions)
    text = translator.translateCommands()

    # write .asm in same directory as the .vm file
    asm_file = vm_file.replace('.vm', '.asm')

    with open(asm_file, 'w') as f:
        f.write(text)

    print(f"Written to {asm_file}")

main()