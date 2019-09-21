#user input
mask = input("Enter code mobile RU operator (example: 90x or 95x or 'all'): ")

#Create dict operators
operators = {'90x' : [900, 901, 902, 903, 904, 905, 906, 908, 909],
             '91x' : [910, 911, 912, 913, 914, 915, 916, 917, 918, 919],
             '92x' : [920, 921, 922, 923, 924, 925, 926, 927, 928, 929],
             '93x' : [930, 931, 932, 933, 934, 936, 937, 938, 939],
             '94x' : [941],
             '95x' : [950, 951, 952, 953, 954, 955, 956, 958],
             '96x' : [960, 961, 962, 963, 964, 965, 966, 967, 968, 969],
             '97x' : [970, 971, 977, 978],
             '98x' : [980, 981, 982, 983, 984, 985, 986, 987, 988, 989],
             '99x' : [991, 992, 993, 994, 995, 996, 997, 999]}

def select_operator():
    if mask in operators:
        return operators[mask]
    elif mask == 'all':
        all_operators = []
        for i in operators:
            all_operators += operators[i]  
        return all_operators
    else:
        print("\n" + "Error input")
        exit()

def create_dict():
    file = open('mobidict.txt', 'w')
    for i in operator:
        for j in range(9999999):
            file.write('{}{}'.format(i, str(j).zfill(7) + '\n'))
    file.close()
            
    
    
if __name__=="__main__":
    operator = select_operator()
    create_dict()