class Research:
    def file_reader(self):
        with open("data.csv", "r") as input:
            return input.readlines()

research=Research()
lines=research.file_reader()    
for line in lines:
    print(line.strip())

if __name__=="__main__":
    Research()