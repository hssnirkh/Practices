a = 5
b = '7'
c = 4.0

print("a = {0} type {3} \00 | \00 b = {1} type {4} \00 | \00 c = {2} type {5}"\
.format(a,b,c,type(a),type(b),type(c)))


#print("a+b:{4} \t a = {0} ba type {1} \t va b = {2} ba type {3}\n".format(a,type(a),b,type(b),(a+b)))
# not execute or error str+int ghabel ghabool nist
print("....................................................................................")

print("a*b::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}\twith type {7}"\
.format('a',a,type(a),'b',b,type(b),(a*b),type(a*b)))
# 5 * '7'     77777
print("....................................................................................")

print("a+a::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}\twith type {7}"\
.format('a',a,type(a),'a',a,type(a),(a+a),type(a+a))) 
"""print("a+a::>> \t a = {0} with type {1} \t and a = {2} with type {3}\nAns = {4}"\
.format(a,type(a),a,type(a),(a+a)))"""
print("....................................................................................")

print("a+c::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}\twith type {7}"\
.format('a',a,type(a),'c',c,type(c),(a+c),type(a+c)))
print("....................................................................................")

"""print("b+c::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}"\
.format('b',b,type(b),'c',c,type(c),(b+c))) """
# str + int invalid
print("....................................................................................")

print("b+b::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}\twith type {7}"\
.format('b',b,type(b),'b',b,type(b),(b+b),type(b+b))) 
print("....................................................................................")

"""print("b*b::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}"\
.format('b',b,type(b),'b',b,type(b),(b*b)))"""
# str ghabel zarb nist
print("....................................................................................")

print("b+\'9\'::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}\twith type {7}"\
.format('b',b,type(b),'9','9',type('9'),(b+'9'),type(b+'9')))
print("....................................................................................")

print("int(a+c)::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6} \t with type {7}"\
.format('a',a,type(a),'c',c,type(c),(int(a+c)),type(int(a+c)))) 
print("....................................................................................")

print("float(b)*a::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}\twith type {7}"\
.format('b',b,type(b),'a',a,type(a),(float(b)*a),type(float(b)*a)))
print("....................................................................................")

print("str(a)+b::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}\twith type {7}"\
.format('a',a,type(a),'9',b,type(b),(str(a)+b),type(str(a)+b))) 
print("....................................................................................")

print("int(b)+c::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}\twith type {7}"\
.format('b',b,type(b),'c',c,type(c),(int(b)+c),type(int(b)+c))) 
print("....................................................................................")

print("len(b)+a::>> \t {0} = {1} with type {2} \t and {3} = {4} with type {5}\nAns = {6}\twith type {7}"\
.format('b',b,type(b),'a',a,type(a),(len(b)+a),type(len(b)+a))) 
print("....................................................................................")
