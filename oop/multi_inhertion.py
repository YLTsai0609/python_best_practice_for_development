class A:
    def __init__(self):
        print("A's init")

class B(A):
    def __init__(self):
        print("B's init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C's init")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D's init")
        super().__init__()

class E(D):
# https://stackoverflow.com/questions/62744176/how-to-overwrite-parent-class-init-method-and-use-super-to-call-grandparent-ini
# init grand-parent or specific parent directly without chainning all of them.
    def __init__(self):
        print("E's init")
        A.__init__(self)

print(D.mro())
print('-'*50)
D()
print('-'*50)
print(A.mro())
E()
