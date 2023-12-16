from z3 import *

a0 ,a1 ,b0 ,b1 = Bools('a0 a1 b0 b1')

cout0 ,cout1 = Bools('cout0 cout1')

cout0 = And((a0),(b0),)
cout1 = Xor((Xor((a1),(b1),)),(And((a0),(b0),)),)

ensures = Not(cout0==Xor((a0),(b0)))

s = Solver()

s.add(cout0)
s.add(cout1)
s.add(ensures)

if s.check() == sat:
        m = s.model()
        print("found a counter example!")
else:
        print("UNSAT so satisfied")