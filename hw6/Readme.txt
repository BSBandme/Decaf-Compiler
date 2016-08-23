README.txt:	this file
decaflexer.py	PLY/lex specification of Decaf tokens.
		Also defines "errorflag" used to signal error during scanning/parsing.
decafparser.py	PLY/yacc specification of Decaf grammar.
		The encoded grammar rules appear in the same order as in decaf manual.
		Defines "from_file" function that takes a file name
		and parses that file's contents. "from_file" returns
		True if no error, and False if error.

ast.py	Class structure and functions for AST construction and type checking

decafch.py	Driver: processes arguments and gets file name to pass
		to decafparser.from_file
		Decaf programs are assumed to be in files with ".decaf" suffix.
		Argument given to decafch may omit this suffix; e.g.
				python decafch test
		will read from test.decaf.

absmc.py  Some functions for building abstract machine 

cfg.py Some functions and classes for building CFG, register allocation and
		 translation to MIPS



Some tips:  

(1) there's one and only one 'ret' instruction for each function and
procedure in intermediate code, which is at the end of the funciton.

(2) more parameters than "a3" are stored in the ((i-4)*4)($fp), which i is the
index of parameters; more registers than "t9" are stored in ((i-10)*4)($sp), which i is
the index of registers

(3) ra is stored in -4($fp), last fp is stored in -8($fp)
