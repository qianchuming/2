class BMI:
    def __init__(self,name,age,weight,height):
        self.name= name
        self.age= age
        self.weight= weight
        self.height= height
        
    def get_name(self):
        return self.name
    
    def get_BMI(self):
        self.BMI=self.weight/(self.height*self.height)
        return round(self.BMI,1)
    def get_status(self):
        if self.BMI < 18.5:
            BMI_status='偏瘦'
        elif self.BMI > 18.5 and self.BMI<24:
            BMI_status='正常'
        elif self.BMI > 24 and self.BMI<30:
            BMI_status='偏胖'
        else:
            BMI_status='肥胖'
        return BMI_status
    
bmi1 = BMI("zhangsan",18,60,1.75)
print(bmi1.get_name(),"的BMI是",bmi1.get_BMI(),bmi1.get_status())
