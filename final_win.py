# write the code for the third screen of the application here
res1 = "Low"
res2 = 'Satisfactory'
res3 = "Average"
res4 = "Above Average"
res5 = "High"
class Screen3(QWidget):
    def __init__(self,exp):
        self.exp = exp

    def evaluation(self):
        self.formula = (4 * (int(self.exp.pulse) + int(self.exp.test1) + int(self.exp.test3)) -200) /10
        if self.exp.age >= 15 :
            level = res1

        elif self.exp.age >= 15 :
            if self.formula >11 :
                level = res2

        elif self.exp.age >= 15 :
            if self.formula >= 6:
                level = res3
        elif self.exp.age >= 15 :
            if self.formula >= 0.5:
                level = res4
        elif self.exp.age >= 15 :
            if self.formula <= 0.4:
                level = res4