class A:
    varA="welcome to class a "
class B:
    varB="welcome to class b"
class C(A,B):
    varc="welcome to class c"
c1=C()
print(c1.varc)
print(c1.varB)
print(c1.varA)