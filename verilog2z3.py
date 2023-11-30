import sys

import antlr4
import argparse

from src.VerilogLexer import VerilogLexer
from src.VerilogParser import VerilogParser
from src.verilogToZ3Visitor import verilogVisitor


def preparez3(verilog_spec, verilog_spec_location):

    filename = verilog_spec_location+verilog_spec
    f = open(filename, "r")
    data = f.read()
    inputStream = antlr4.InputStream(data)
    lexer = VerilogLexer(inputStream)
    tokenStream = antlr4.CommonTokenStream(lexer)
    parser = VerilogParser(tokenStream)
    tree = parser.module_declaration()
    visitor = verilogVisitor(
        verilog_spec, verilog_spec_location)
    z3filecontent = visitor.visit(tree)
    with open('src/templateZ3Checker.py', 'r') as file:
        filedata = file.read()
        file.close()
    filedata = filedata.replace('#*#', z3filecontent)
    with open(verilog_spec+'.py', 'w') as file:
        file.write(filedata)
        file.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--verilog_spec", type=str)
    args = parser.parse_args()
    path = 'benchmarks/'
    preparez3(args.verilog_spec, path)
