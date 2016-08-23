
def mvi(r,i):
    return "    move_immed_i %s, %d"%(r,i)

def mvf(r,i):
    return "    move_immed_f %s, %f"%(r,i)

def mv(r1,r2):
    return "    move %s, %s"%(r1,r2)

def iadd(r1,r2,r3):
    return "    iadd %s, %s, %s"%(r1,r2,r3)

def isub(r1,r2,r3):
    return "    isub %s, %s, %s"%(r1,r2,r3)

def imul(r1,r2,r3):
    return "    imul %s, %s, %s"%(r1,r2,r3)

def idiv(r1,r2,r3):
    return "    idiv %s, %s, %s"%(r1,r2,r3)

def imod(r1,r2,r3):
    return "    imod %s, %s, %s"%(r1,r2,r3)

def igt(r1,r2,r3):
    return "    igt %s, %s, %s"%(r1,r2,r3)

def igeq(r1,r2,r3):
    return "    igeq %s, %s, %s"%(r1,r2,r3)

def ilt(r1,r2,r3):
    return "    ilt %s, %s, %s"%(r1,r2,r3)

def ileq(r1,r2,r3):
    return "    ileq %s, %s, %s"%(r1,r2,r3)

def ftoi(r1,r2):
    return "    ftoi %s, %s"%(r1,r2)

def itof(r1,r2):
    return "    itof %s, %s"%(r1,r2)

def bz(r,l):
    return "    bz %s, %s"%(r,l) 

def bnz(r,l):
    return "    bnz %s, %s"%(r,l)

def jmp(l):
    return "    jmp %s"%(l)

def hload(r1,r2,r3):
    return "    hload %s, %s, %s"%(r1,r2,r3)
 
def hstore(r1,r2,r3):
    return "    hstore %s, %s, %s"%(r1,r2,r3)

def halloc(r1,r2):
    return "    halloc %s, %s"%(r1,r2)

def call(l):
    return "    call %s"%(l)

def ret():
    return "    ret"

def save(r):
    return "    save %s"%r

def restore(r):
    return "    restore %s"%r

def phi(r, llist, rlist):
    return "    phi %s, %s, %s"%(r,llist,rlist)

def comment(c):
    return "# %s"%c

def label(l):
    return "%s:"%l

temporary_cnt = -1
def generate_new_temporary():
    global temporary_cnt 
    temporary_cnt = temporary_cnt + 1
    return "t%d" %temporary_cnt 
def clear_temporary(t):
    global temporary_cnt
    temporary_cnt = t

temporary_label = 0
def generate_new_label(s):
    global temporary_label
    temporary_label = temporary_label + 1
    if(s == None) :
        s = ""
    return "l%d_%s" %(temporary_label,s)