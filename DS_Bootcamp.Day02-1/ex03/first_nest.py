import sys
import os

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
        @staticmethod
        def counts(data):
            heads=sum(row[0] for row in data)
            tails=sum(row[1] for row in data)
            return heads, tails

        @staticmethod
        def fractions(heads, tails):
            total=heads+tails
            if total==0:
                return 0,0
            
            fr_heads=(heads/total)*100
            fr_tails=(tails/total)*100
            return fr_heads, fr_tails

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Error")
    else:
        path=sys.argv[1]
        research=Research(path)
        lines=research.file_reader() 
        print(lines)
        count=research.Calculations.counts(lines)
        print(count[0], count[1])

        fract=research.Calculations.fractions(count[0], count[1])
        print(fract[0], fract[1])