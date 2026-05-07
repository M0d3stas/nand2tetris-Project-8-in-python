import os
from parser import Parser
from translator import Translator

def main():

    bootstrap = 'bootstrap.asm'
    filename1 = '08/StaticsTest/Sys.vm'
    filename2 = '08/StaticsTest/Class1.vm'
    filename3 = '08/StaticsTest/Class2.vm'
    output_file = filename1.replace('.vm', '.asm')

    with open(output_file, 'w') as f:
        with open(bootstrap, 'r') as b:
            for line in b:
                f.write(line)
    files = [filename1, filename2, filename3]

    for filename in files:
        instrunctions = []
        parser = Parser(filename)

        parser.readFile()
        instrunctions = parser.returnParsedCommands()

        translator = Translator(parser.parseFilename(), instrunctions)

        text = translator.translateCommands()



        with open(output_file, 'a') as f:
            f.write(text)

    
main()