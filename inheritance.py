class parent():
    def Dispalyd(self):
        print("i am the parent")
class child(parent):
    def Display(self):
        print("i am the child")

c= child()
c.Display()
c.Dispalyd()