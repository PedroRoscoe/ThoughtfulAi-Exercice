class package:
    def __init__(self,width,height,length,weight):
        self.width = width
        self.height = height
        self.length = length
        self.weight = weight
        self.is_bulky = False
        self.is_heavy = False
        if (self.width*self.height*self.length)>=1000000:
            self.is_bulky = True
        if self.width >=150 or self.height >= 150 or self.length >= 150:
            self.is_bulky = True
        if self.weight >= 20:
            self.is_heavy = True

    def sort(self):
        if self.is_bulky and self.is_heavy:
            return "REJECTED"
        if self.is_bulky or self.is_heavy:
            return "SPECIAL"
        return "STANDARD"

