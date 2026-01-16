def read_csv():
    with open(r'ds.csv', 'r', encoding='utf-8') as output:
        return output.readlines()
    
def replace_commas(lines):
    return [line.replace(',', '\t') for line in lines]
    
def write_tsv(lines):
    with open(r"ds.tsv", 'w', encoding='utf-8') as output:
        return output.writelines(lines)
    
def main():
    lines=read_csv()
    write_tsv(replace_commas(lines))

if __name__ == "__main__":
    main()