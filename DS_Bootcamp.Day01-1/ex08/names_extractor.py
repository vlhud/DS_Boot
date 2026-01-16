import sys

def read_csv(path):
    with open(rf'{path}', "r", encoding='utf-8') as input:
        emails= input.read().strip().split('\n')
    
    employees=[]
    
    for email in emails:
        if "@corp.com" in email:
            body=email.split("@")[0]
            name, surname=body.split(".")
            name=name.capitalize()
            surname=surname.capitalize()
            employees.append(f"{name}/t,{surname}/t,{email}")
    return employees
         
def write_tsv(lines):
    with open("employees.tsv", "w", encoding='utf-8') as output:
        output.write("Name\tSurname\tE-mail\n")
        return output.writelines(lines)
    
def main():
    if len(sys.argv) !=2:
        return
    path=sys.argv[1]

    lines=read_csv(path)
    write_tsv(lines)

if __name__ == "__main__":
    main()