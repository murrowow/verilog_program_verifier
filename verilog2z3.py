import sys

import antlr4
import argparse

from src.VerilogLexer import VerilogLexer
from src.VerilogParser import VerilogParser
from src.verilogToZ3Visitor import verilogVisitor


def z3(verilog_spec, verilog_spec_location):
    #read the Z3 file script
    file_name = verilog_spec_location + verilog_spec
    f = open(file_name, "r")
    data = f.read()

    #read the verilog data with ANTLR
    input_stream = antlr4.InputStream(data)
    lexer = VerilogLexer(input_stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = VerilogParser(token_stream)
    tree = parser.module_declaration()
    visitor = verilogVisitor(verilog_spec, verilog_spec_location)

    #convert the ANTLR parsing to Z3
    z3_file_content = visitor.visit(tree)

    #open a template for easy dumping of values into
    with open('src/templateZ3Checker.py', 'r') as file:
        filedata = file.read()
        file.close()
    filedata = filedata.replace('#*#', z3_file_content)

    #dump the converted Z3 implementation into a python script that the programmer can execute
    with open(verilog_spec+'.py', 'w') as file:
        file.write(filedata)
        file.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--verilog_spec", type=str)
    args = parser.parse_args()
    path = 'benchmarks/'
    z3(args.verilog_spec, path)
