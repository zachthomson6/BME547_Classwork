def interface():
    print("Blood calculator")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Total Cholesterol")
        print("9 - Quit")
        choice = input("Select an option:")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            total_driver()
    print("Program ending")
    
    
def HDL_driver():
    HDL_in = generic_input("HDL")
    HDL_analy = HDL_analysis(HDL_in)
    generic_output("HDL", HDL_in, HDL_analy)
    

def generic_input(test_name):
    value = input ("Enter the {} value: ".format(test_name))
    value = int(value)
    return value
    
    
def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer
    
    
def generic_output(test_name, test_value, test_analy):
    print("The {} result of {} is considered {}"
        .format(test_name, test_value, test_analy))
    return


def LDL_driver():
    LDL_in = generic_input("LDL")
    LDL_analy = LDL_analysis(LDL_in)
    generic_output("LDL", LDL_in, LDL_analy)
    
def LDL_analysis(LDL_int):
    if LDL_int >= 190:
        answer = "Very High"
    elif 160 <= LDL_int < 190:
        answer = "High"
    elif 130 <= LDL_int < 160:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer

def total_driver():
    total_in = generic_input("Total Cholesterol")
    total_analy = total_analysis(total_in)
    generic_output("Total Cholesterol", total_in, total_analy)

def total_analysis(total_int):
    if total_int >= 240:
        answer = "High"
    elif 200 <= total_int < 240:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer

if __name__ == "__main__":
    interface()
