import os
from parser import Parser
from translator import Translator

def main():

    
    filename = '08/NestedCall/Sys.vm'
    instrunctions = []
    parser = Parser(filename)

    with open(filename, 'r') as f:
        for line in f:
            parser.insertLine(line)
            instrunction = parser.parseCommand()
            if instrunction.getValid():
                instrunctions.append(instrunction)

    translator = Translator(parser.parseFilename(), instrunctions)

    text = translator.translateCommands()

    with open(filename.replace('.vm', '.asm'), 'w') as f:
        f.write(text)

main()