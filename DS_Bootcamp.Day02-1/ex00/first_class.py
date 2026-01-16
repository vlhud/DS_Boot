class Must_read:
    with open("data.csv", "r") as input:
        lines=input.readlines()
    for line in lines:
        print(line.strip())

if __name__=="__main__":
    Must_read()