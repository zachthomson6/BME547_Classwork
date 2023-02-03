def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age, []]
    return new_patient

def main_drive():
    db = []
    db.append(create_patient_entry('Ann Ables', 1, 34))
    db.append(create_patient_entry('Bob Boyles', 2, 45))
    db.append(create_patient_entry('Chris Chou', 3, 52))
    print(db)
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, 'LDL', 100)
    room_numbers = ['103','232','333']
    print(db)
    print_directory(db, room_numbers)

def print_directory(db, room_numbers):
    for patient in enumerate(db):
        print('Patient {} is in room {}'.format(patient[0],room_numbers[i]))
    for patient, rn  in zip(db, room_numbers):
        print('Patient {} is in room {}'.format(patient[0],rn))

def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False

def add_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient == False:
        print('Bad Entry')
    else:    
        patient[3].append([test_name, test_value])

def patient_result(db, mrn_to_find, test_name):
    for patient in db:
        if patient[1] == mrn_to_find:
            if patient[2] == test_value:
                print patient[3]
	    else:
                print('No Test Available')
        else:
	    print('No Patient Available')

if __name__ == "__main__":
    main_driver()
