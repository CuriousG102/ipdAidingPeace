from aidParserApp import Parser
from interface import TextInterface

def main():
    parser = Parser(TextInterface)
    parser.run()

if __name__ == '__main__': main()
