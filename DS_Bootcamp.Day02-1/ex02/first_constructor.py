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

    def file_reader(self):
        with open(f"{self.path}", "r") as input:
            lines=input.readlines()
            self.file_struct(lines) 
            return lines

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Error")
    else:
        path=sys.argv[1]
        research=Research(path)
        lines=research.file_reader()   
        for line in lines:
            print(line.strip())