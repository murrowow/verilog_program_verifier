Install antlr4 

$pip install antlr4-tools

Run to generate parser and lexer files for your local machine

$antlr4 -Dlanguage=Python3 -visitor Verilog.g4

place into src your simple bit-level Verilog code

you can can the verilog2z3.py file in order to produce a z3 equivalent implementation of that file

$python verilog2z3.py verilog_spec=<your verilog file> 

This will produce some file called <your verilog file>.py

You can simply run that python file to produce your output

$python <your verilog file>.py
