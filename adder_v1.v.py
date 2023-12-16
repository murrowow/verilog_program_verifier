from z3 import *

a0 ,a1 ,b0 ,b1 = Bools('a0 a1 b0 b1')
cout0 ,cout1 = Bools('cout0 cout1')
cout0 = Xor((a0),(b0),)
cout1 = Xor((Xor((a1),(b1),)),(And((a0),(b0),)),)
	
