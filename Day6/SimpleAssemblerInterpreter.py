#We want to create a simple interpreter of assembler which will support the following instructions:
#mov x y - copies y (either a constant value or the content of a register) into register x
#inc x - increases the content of the register x by one
#dec x - decreases the content of the register x by one
#jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward), but only if x (a constant or a register) is not zero
#def simple_assembler(program):
#Register names are alphabetical (letters only). Constants are always integers (positive or negative).
#Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

  dictt = {}
  for i in range(len(program)):
    splits = program[i].split(" ",1)
    if splits[0] == "mov":
      nr = splits[1].split(" ")
      dictt[nr[0]] = int(nr[1])
    elif splits[0] == "inc":
      dictt[nr[0]] += 1
    elif splits[0] == "dec":
      dictt[nr[0]] -= 1
    else:
      nr = splits[1].split(" ",1)
      while dictt[nr[0]] != 0:
        for j in range(i + int(nr[1]), i):
          splits = program[j].split(" ",1)
          if splits[0] == "mov":
            nr = splits[1].split(" ")
            dictt[nr[0]] = int(nr[1])
          elif splits[0] == "inc":
            dictt[nr[0]] += 1
          elif splits[0] == "dec":
            dictt[nr[0]] -= 1
  return dictt
  
print(simple_assembler(["mov a 5","inc a","dec a",'dec a','jnz a -1','inc a']))
#Result : {'a' : 1}
