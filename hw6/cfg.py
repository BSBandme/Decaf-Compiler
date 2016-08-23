currentBlock = None
blockmap = {}
blocklist = []
output = []
        
class Block :
    def __init__(self, rname):
        self.name = rname
        self.succ = []
        self.pred = []
        self.inReg = set([])
        self.outReg = set([])
        self.instructions = []
        self.define = set([])
        self.used = set([])
        
    def addInstruction(self, t):
        self.instructions.append(t)
    

class Instruction : 
    def __init__(self, rtype, rregList):
        global currentBlock
        self.define = set([]) 
        self.used = set([])
        self.outReg = set([])
        self.inReg = set([])
        self.type = rtype
        self.regList = rregList
        if rtype == 'move_immed_i' :
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
        elif rtype == 'move_immed_f':
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
        elif rtype == 'move':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1]])
        elif rtype == 'iadd':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'isub' :
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'imul' :
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'idiv' :
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'imod' :
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'igt':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'igeq':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'ilt':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'ileq':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'ieq':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'ineq':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1], rregList[2]])
        elif rtype == 'ftoi':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1]])
        elif rtype == 'itof':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1]])
        elif rtype == 'bz':
            currentBlock.succ.append(rregList[1])
            if(not (rregList[0] in currentBlock.define)) :
                currentBlock.used.add(rregList[0])
            self.used = set([rregList[0]])
        elif rtype == 'bnz':
            currentBlock.succ.append(rregList[1])
            if(not (rregList[0] in currentBlock.define)) :
                currentBlock.used.add(rregList[0])
            self.used = set([rregList[0]])
        elif rtype == 'jmp':
            currentBlock.succ.append(rregList[0])
        elif rtype == 'hload':
            if(rregList[1] != 'sap') :
                if(not (rregList[1] in currentBlock.define)) :
                    currentBlock.used.add(rregList[1])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            if(rregList[1] != 'sap') :
                self.used = set([rregList[1], rregList[2]])
            else :
                self.used = set([rregList[2]])
        elif rtype == 'hstore':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            if(rregList[0] != 'sap') :
                if(not (rregList[0] in currentBlock.define)) :
                    currentBlock.used.add(rregList[0])
            if(not (rregList[2] in currentBlock.define)) :
                currentBlock.used.add(rregList[2])
            self.define = set([])
            if(rregList[0] != 'sap') :
                self.used = set([rregList[1], rregList[0], rregList[2]])
            else : 
                self.used = set([rregList[1], rregList[2]])
        elif rtype == 'halloc':
            if(not (rregList[1] in currentBlock.define)) :
                currentBlock.used.add(rregList[1])
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            self.used = set([rregList[1]])
        elif rtype == 'call':
            pass
        elif rtype == 'ret':
            pass
        elif rtype == 'save':
            if(rregList[0] == 'all') :
                return
            if(not (rregList[0] in currentBlock.define)) :
                currentBlock.used.add(rregList[0])
            self.used = set([rregList[0]])
        elif rtype == 'restore':
            if(rregList[0] == 'all') :
                return
            currentBlock.define.add(rregList[0])
            self.define = set([rregList[0]])
            
class InferferenceGraphNode :
    def __init__(self, rname):
        self.edge = set([])
        self.name = rname
    def addedge(self, reg):
        self.edge.add(reg)
            
# auxiliary function for building interference graph 
def addedge(rmap, rset): 
    for i in rset :
        if(i[0] == 'a' or i[0] == 'v'):
            continue;
        if(not rmap.has_key(i)) :
            rmap[i] = InferferenceGraphNode(i)
        for j in rset :
            if(j[0] == 'a' or j[0] == 'v'):
                continue;
            if(j == i) :
                continue
            if(not rmap.has_key(j)) :
                rmap[j] = InferferenceGraphNode(j)  
            rmap[j].addedge(i)
            rmap[i].addedge(j)
             
# The main function to build CFG
def buildcfg():
    global blockmap,currentBlock,blocklist
    
    # deal with pred
    for i in blockmap :
        t = blockmap[i]  
        for j in t.succ:
            blockmap[j].pred.append(i)
#        rname = blockmap[i].name
#         st = 0;
#         while not (rname[st] == '_'):
#             st = st + 1
#         if(rname[st + 1:] == 'method_call') :
#             blockmap[i].define = set([])
#             blockmap[i].used = set([])   
        
    #calculate in and out of each block
    flag = True
    while flag :
        flag = False
        for i in blockmap : 
            if(blockmap[i] == currentBlock) :
                continue
            routset = set([])
            for j in blockmap[i].succ :
                routset = routset | blockmap[j].inReg
            if(blockmap[i].outReg != routset) :
                flag = True
                blockmap[i].outReg = routset
            rinset = blockmap[i].used | (blockmap[i].outReg - blockmap[i].define)
            if(blockmap[i].inReg != rinset) :
                flag = True
                blockmap[i].inReg = rinset
        if not flag:
            break;
    
    #build Interference Map
    map = {}
    for i in blockmap :
        rb = blockmap[i]
#        rname = blockmap[i].name
#         st = 0;
#         while not (rname[st] == '_'):
#             st = st + 1
#         if(rname[st + 1:] == 'method_call') :
#             continue
        if(len(rb.instructions) == 0) :
            addedge(map, rb.outReg)
            continue
        rlastInst = rb.instructions[-1] 
        rlastInst.outReg = rlastInst.outReg | rb.outReg 
        rlastInst.inReg = rlastInst.used | (rlastInst.outReg - rlastInst.define)
        for j in range(len(blockmap[i].instructions) - 2, -1, -1):
            rnowInst = blockmap[i].instructions[j]
            rnxtInst = blockmap[i].instructions[j + 1]
            rnowInst.outReg = rnxtInst.inReg
            rnowInst.inReg = rnowInst.used | (rnowInst.outReg - rnowInst.define)
            addedge(map, rnowInst.outReg)
            addedge(map, rnowInst.inReg)
        
    # color the register
    st = []    
    ans = {}
    while len(map) > 0 :
        nxt = None
        for i in map :
            if(nxt == None or len(map[nxt].edge) > len(map[i].edge)) :
                nxt = i
        st.append(map[nxt])
        for i in map[nxt].edge :
            map[i].edge.remove(nxt)
        del map[nxt]
    for i in st[::-1] :
        p = set([])
        for j in i.edge :
            p.add(ans[j])
        nxt = 0;
        while(nxt in p) :
            nxt = nxt + 1
        ans[i.name] = nxt
        
    changeToSMIP(ans)
        
    currentBlock = None;
    blockmap = {}   
    blocklist = []
    return

# use the 'ans' rules to translate registers for the whole function
def changeToSMIP(ans): 
    global output
    maxc = 0
    for i in ans:
        maxc = max(ans[i], maxc)
    sum = 2;
    if(maxc > 9):
        sum = sum + maxc - 9;
    for rb in blocklist :
        rname = rb.name 
        output.append("%s:"%rname)
        
        # callee's initialization
        if(rb == blocklist[0]) :
            output.append("\tsubu $sp,$sp,%d"%(sum * 4))
            output.append("\tsw $ra,%d($sp)"%((sum - 1) * 4))
            output.append("\tsw $fp,%d($sp)"%((sum - 2) * 4))
            output.append("\taddu $fp,$sp,%d"%(sum * 4))
            
        # deal with method call block
        st = 0
        while (st < len(rname)) and (not (rname[st] == '_')):
            st = st + 1
        if(rname[st + 1:] == 'method_call') :
            buffer = []
            cnt = 0;
            for rinst in rb.instructions :
                if(rinst.type == 'move' and rinst.regList[0][0] == 'a') :
                    cnt = cnt + 1
            for rinst in rb.instructions : 
                if(rinst.type == 'save') :
                    for i in range(0, 4) :
                        t = Instruction('save', ['a%d'%i])
                        buffer.extend(Instruction2MIPS(t))
                    for i in range(0, 10) :
                        t = Instruction('save', ['t%d'%i])
                        buffer.extend(Instruction2MIPS(t))
                    if(cnt > 4) :
                        buffer.extend("subu $sp,$sp,%d"%(cnt - 4)*4)
                elif (rinst.type == 'restore') :
                    if(cnt > 4) :
                        buffer.extend("addu $sp,$sp,%d"%(cnt - 4)*4)
                    for i in range(9, -1, -1) :
                        t = Instruction('restore', ['t%d'%i])
                        buffer.extend(Instruction2MIPS(t))
                    for i in range(3, -1, -1) :
                        t = Instruction('restore', ['a%d'%i])
                        buffer.extend(Instruction2MIPS(t))
                elif (rinst.type == 'move') :
                    if(rinst.regList[0][0] == 'a') :
                        reg = rinst.regList[0]
                        no = int(reg[1:])
                        if(no > 3) :
                            reg = '%d($sp)'%((no-4)*4)
                        rinst.regList[0] = reg
                        rinst.regList[1] = 't%d'%ans[rinst.regList[1]]
                        buffer.extend(Instruction2MIPS(rinst))
                    else:
                        rinst.regList[0] = 't%d'%ans[rinst.regList[0]]
                        buffer.extend(Instruction2MIPS(rinst))
                else :
                    buffer.extend(Instruction2MIPS(rinst))
            output.extend(buffer)
            continue
        
        # deal with other blocks : translate the registers and add to output list
        for rinst in rb.instructions :
            flag = True
            for j in range(0, len(rinst.regList)):
                reg = rinst.regList[j]
                if(reg[0] == 'a' and reg != 'all') :
                    no = int(reg[1:])
                    if(no > 3) :
                        reg = '%d($fp)'%((no-4)*4)
                elif(reg[0] == 't') :
                    if(not ans.has_key(reg)) :
                        flag = False
                        break
                    no = ans[reg]
                    if(no > 9) :
                        reg = '%d($sp)'%((no-10)*4)
                    else :
                        reg = 't%d'%no
                rinst.regList[j] = reg
            if flag:
                if(rinst.type == 'ret') :
                    output.append("\tlw $ra,%d($sp)"%((sum-1)*4))
                    output.append("\tlw $fp,%d($sp)"%((sum-2)*4))
                    output.append("\taddu $sp,$sp,%d"%(sum*4))
                    output.append("\tjr $ra")
                else :
                    rinsts = Instruction2MIPS(rinst)
                    output.extend(rinsts)
            
    return

# Translation from intermediate instruction to MIPS
def Instruction2MIPS(input):
    res = []
    type = input.type
    reg  = input.regList
    if type in ["iadd", "isub", "imul", "idiv", "fadd", "fsub", "fmul", "fdiv"]:
        if len(reg) is not 3:
            print("Error: Wrong register number")
            return
        else:
            output = "\t%s $%s,$%s,$%s"%(type[1:], reg[0],reg[1],reg[2])
            res.append(output)
    elif type in ["move_immed_i", "move_immed_f"]:
        if len(input.regList) is not 2:
            print("Error: Wrong register number")
            return
        else:
            output = "\tli $%s,%s"%(reg[0],reg[1])
            res.append(output)
    elif type == "move":
        if len(input.regList) is not 2:
            print("Error: Wrong register number")
            return
        else:
            output = "\tmove $%s,$%s"%(reg[0],reg[1])
            res.append(output)
    elif type in ["igt", "igeq", "ilt", "ileq", "ieq", "ineq"]:
        if len(input.regList) is not 3:
            print("Error: Wrong register number")
            return
        else:
            if type in ["igt","fgt"]:
                ope = "sgt"
            elif type in ["igeq","fgeq"]:
                ope = "sge"
            elif type in ["ilt","flt"]:
                ope = "slt"
            elif type in ["ileq", "fleq"]:
                ope = "sle"
            elif type in ["ieq"]:
                ope = "slt"
            elif type in ["ineq"]:
                ope = "sle"

            output = "\t%s $%s,$%s,$%s"%(ope,reg[0],reg[1],reg[2])
            res.append(output)
    elif type in ["bz", "bnz"]:
        if len(input.regList) is not 2:
            print("Error: Wrong register number")
            return
        else:
            if type == "bz":
                ope = "beqz"
            elif type == "bnz":
                ope = "bnez"
            output = "\t%s $%s,%s"%(ope, reg[0], reg[1])
            res.append(output)
    elif type == "jmp":
        if len(input.regList) is not 1:
            print("Error: Wrong register number")
            return
        else:
            output = "\tj %s"%(reg[0])
            res.append(output)
    elif type in ["hload", "hstore"]:
        if len(input.regList) is not 3:
            print("Error: Wrong register number")
            return
        else:
            if type == "hload":
                ope = "lw"
                output = "\tmul $%s,$%s,4"%(reg[2],reg[2])
                res.append(output)
                if(reg[1] == 'sap') :
                    output = "\tla $v0,sap"
                    res.append(output)
                    output = "\tadd $v0,$v0,$%s"%(reg[2])
                else :
                    output = "\tadd $v0,$%s,$%s"%(reg[1], reg[2])
                res.append(output)
                output = "\t%s $%s,0($v0)"%(ope, reg[0])
                res.append(output)
                if(reg[1] != reg[0] and reg[1] != reg[2]) :
                    output = "\tdiv $%s,$%s,4"%(reg[2],reg[2])
                    res.append(output)
            elif type == "hstore":
                ope = "sw"
                output = "\tmul $%s,$%s,4"%(reg[1],reg[1])
                res.append(output)
                if(reg[0] == 'sap') :
                    output = "\tla $v0,sap"
                    res.append(output)
                    output = "\tadd $v0,$v0,$%s"%(reg[1])
                else :
                    output = "\tadd $v0,$%s,$%s"%(reg[0], reg[1])
                res.append(output)
                output = "\t%s $%s,0($v0)"%(ope, reg[2])
                res.append(output)
                if(reg[1] != reg[0] and reg[1] != reg[2]) :
                    output = "\tdiv $%s,$%s,4"%(reg[1],reg[1])
                    res.append(output)
    elif type == "halloc":
        if len(input.regList) is not 2:
            print("Error: Wrong register number")
            return
        else:
            output = "\tsubu $sp,$sp,4"
            res.append(output)
            output = "\tsw $a0,0($sp)"
            res.append(output)
            output = "\tmul $%s,$%s,4"%(reg[1],reg[1])
            res.append(output)
            output = "\tmove $a0,$%s"%(reg[1])
            res.append(output)
            output = "\tli $v0,9"
            res.append(output)
            output = "\tsyscall"
            res.append(output)
            output = "\tdiv $%s,$%s,4"%(reg[1],reg[1])
            res.append(output)
            output = "\tmove $%s,$v0"%(reg[0])
            res.append(output)
            output = "\tlw $a0,0($sp)"
            res.append(output)
            output = "\taddu $sp,$sp,4"
            res.append(output)
    elif type == "save":
        if(reg[0] == 'all') :
            return ["save all"]
        if len(input.regList) is not 1:
            print("Error: Wrong register number")
            return
        else:
            output = "\tsubu $sp,$sp,4"
            res.append(output)
            output = "\tsw $%s,0($sp)"%(reg[0])
            res.append(output)
    elif type == "restore":
        if(reg[0] == 'all') :
            return ["restore all"]
        if len(input.regList) is not 1:
            print("Error: Wrong register number")
            return
        else:    # process with the pointer sp
            output = "\tlw $%s,0($sp)"%(reg[0])
            res.append(output)
            output = "\taddu $sp,$sp,4"
            res.append(output)
    elif type == "call":
        output = "\tjal %s"%reg[0]
        res.append(output)
    elif type == "ret":
        pass
    return res

  
################ below are the main functions for cfg ######################

import re
wordpattern = "[ \t\n]+|,"    
def read_instr(str):
    # first take out comments.
    if ("#" in str):
        parts = str.split("#")
        instr = parts[0]
    else:
        instr = str
    #  Not take out label if any
    if (":" in instr):
        parts = instr.split(":")
        label = parts[:-1]
        instr = (parts[-1:])[0]  # only the last element
    else:
        label = ""
    # now instr contains the opcode and arguments.  Split with space, tab, comma:
    opargs = re.split(wordpattern, instr)
    opargs = [w for w in opargs if w != '']
    if (len(opargs) < 1):
        return (label, None, None)
    else:
        return (label, opargs[0], opargs[1:])

def directive(l, lineno):
    global heap, hp, sap
    l.strip()
    if (len(l) == 0) or (l[0] != '.'):
        return False  # not  a directive

    parts = l.split()
    if ((len(parts) == 2) and (parts[0] == '.static_data')):
        try:
            n = int(parts[1])
        except ValueError:
            print "Integer expected in static data directive in line %d, '%s' found"%(lineno,parts[1])
            return True
        heap = [0] * 10000
        sap = 0
        hp = n
    else:
        print "Error in processing directive '%s' in line %d"%(l, lineno)
    return True

def from_file(filename):
    '''load given file'''
    global currentBlock, blockmap, blocklist
    line = 0
    f = open(filename + ".ami", "rU")
    while (True):
        l=f.readline()
        if (l == ""):
            break  #end of file
        line += 1
        if directive(l, line):
            l.strip()
            parts = l.split()
            output.append(".data")
            output.append("")
            output.append("\tsap: .space %d"%(int(parts[1])*4))
            output.append("")
            output.append(".text")
            output.append("")
            continue
        (labels, opcode, args) = read_instr(l)
        if(len(labels) > 0):
            st = 0
            while labels[0][st] != '_':
                st = st + 1;
            if(labels[0][st + 1:] == 'main_foo_begin' or labels[0][st + 1:] == 'main_Foo_begin') :
                labels[0] = "main"
            t = Block(labels[0])
            blockmap[labels[0]] = t
            blocklist.append(t)
            if(currentBlock != None) : 
                currentBlock.succ.append(t.name)
            currentBlock = t
        if(opcode != None) :
            t = Instruction(opcode, args)
            currentBlock.instructions.append(t)
            if(t.type == 'ret') :
                buildcfg()
                output.append("")    

    f.close()
    f = open(filename + ".asm", "w")
    for i in output :
        print >>f, i
    # Check if every label appears in the program!
#     for (opcode, args, line) in program:
#         if (opcode in ["bz", "bnz"]):
#             dest = args[1]
#         elif (opcode in ["jmp", "call"]):
#             dest = args[0]
#         else:
#             dest = None
#         if (dest != None):
#             if (dest not in labelmap):
#                 print "Label '%s' at line %d not defined"%(dest, line)
#                 error = True
#                 
#     if (error):
#         program = []
#         labelmap = {}


if __name__ == "__main__":
    #    sys.exit(main())
    from_file("input")
    