import sys
from random import randint

class Research:
    def __init__(self, path):
        self.path= path

    def file_struct(self, lines):
        if len(lines)<2:
            raise ValueError("Invalid structure1")
        header=lines[0].strip().split(",")
        if len(header)!=2 or not all(isinstance(head, str) for head in header):
            raise ValueError("Invalid structure2")
        for line in lines[1:]:
            elem=line.strip().split(",")
            if len(elem)!=2 or not all(value in ['0','1'] for value in elem) or elem[0]==elem[1]:
                raise ValueError("Invalid structure3")

    def file_reader(self, has_header=True):
        with open(f"{self.path}", "r") as input:
            lines=input.readlines()
            if all(value in ['0', '1'] for value in lines[0].strip().split(",")):
                has_header=False
            if has_header:
                self.file_struct(lines)
                data=lines[1:]
            else:
                data=lines

            data_dict=[list(map(int, line.strip().split(","))) for line in data]
            return data_dict

class Calculations:

    def __init__(self, data):
        self.data=data

    def counts(self):
        heads=sum(row[0] for row in self.data)
        tails=sum(row[1] for row in self.data)
        return heads, tails

    def fractions(self):
        heads, tails=self.counts()
        total=heads+tails
        if total==0:
            return 0,0  
        fr_heads=(heads/total)*100
        fr_tails=(tails/total)*100
        return fr_heads, fr_tails

class Analytics(Calculations):
    def __init__(self, data):
        super().__init__(data)

    def predict_random(self, numb_pred):
        predictions=[]
        for _ in range(numb_pred):
            predictions.append([0, 1] if randint(0,1)==0 else [1, 0])
        return predictions

    def predict_last(self):
        return self.data[-1] if self.data else []

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Error")
    else:
        path=sys.argv[1]
        research=Research(path)
        lines=research.file_reader() 
        print(lines)
        calc=Calculations(lines)
        count=calc.counts()
        print(count[0], count[1])

        fract=calc.fractions()
        print(fract[0], fract[1])

        analyt=Analytics(lines)
        print(analyt.predict_random(3))
        print(analyt.predict_last())