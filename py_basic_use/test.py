class A:
   def foo(self):
      print("A")

class B(A):
   pass

class C:
   def foo(self):
      print("C")

class D(C):
   def foo(self):
      print("D")

class E(B, C, D):
   pass

print(E.mro())
E().foo()
