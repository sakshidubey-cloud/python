class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi, {self.name} your average score is {sum/3}")

s1 = Student("Tommy",[91, 44, 83])
s1.avg()

s1.name = "Shampoo"
s1.avg()