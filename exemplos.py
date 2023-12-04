
codigoIf = '''
   varfloat a1
   a1 := 10.1
   varfloat b1
   b1 := 23.7
   if(a1 < b1){
       a1 := 10.15
       b1 := 23.76
   }
   out(a1)
   out(b1)
'''

codigoIfElse = '''
   varint a1
   a1 := 10
   varint b1
   b1 := 23
   if(a1 > b1 and a1 !! b1){
       a1 := 100
       b1 := 230
   }
   else{
       a1 := 106
       b1 := 236
   }
   out(a1)
   out(b1)
'''

codigoRepeticao = '''
   varfloat a1
   a1 := 10.1
   varfloat b1
   b1 := 23.7
   while(a1 < b1){
       a1 := a1 + a1     
   }
   for(5;+;1;<;10){
       b1 := b1 + b1 * b1 / b1
   }  
   out(a1)
   out(b1)
'''

codigoIn = '''
   varchar a1
   in(a1)
   out(a1)
'''



interpretar = codigoIn