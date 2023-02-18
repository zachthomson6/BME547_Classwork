in_file = open("input_data.txt", "r")
fruits = in_file.readlines()
print(fruits)
in_file.close()
print(fruits)


in_file = open("input_data.txt", "r")
    for line in in_file:
        print(line)


# New Data



def read_file(filename):
    in_file = open(filename, "r")
    first_line = in_file.readline()
    id = analyze_ID(first_line)
    
    
def test_read_file():
    from module import read_file
    
