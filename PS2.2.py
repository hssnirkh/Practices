a = 5
print("a=5: \t a = {0} \t type= {1}\n".format(a,type(a)))

b = '7'
print("b=\'7\': \t b = {0} \t type= {1}\n".format(b,type(b)))

c = 4.0
print("c=4.0: \t c = {0} \t type= {1}\n".format(c,type(c)))

k = a
print("k=a: \t k = {0} \t type= {1}\n".format(k,type(k)))

a = b
print("a=b: \t a = {0} \t type= {1}\n".format(a,type(a)))

b = a
print("b=a: \t b = {0} \t type= {1}\n".format(b,type(b)))

c = a + b # Elhaghe 2 str
print("c=a+b: \t c = {0} \t type= {1}\n".format(c,type(c)))

a = k
print("a=k: \t a = {0} \t type= {1}\n".format(a,type(a)))

a = c
print("a=c: \t a = {0} \t type= {1}\n".format(a,type(a)))

c = k
print("c=k: \t c = {0} \t type= {1}\n".format(c,type(c)))

