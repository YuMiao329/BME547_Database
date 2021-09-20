class Patient:

    def __init__(self, input_name, id, age):
        #self.name = "Ann Ables"
        self.name = input_name
        #self.id = 120
        self.id = id
        #self.age = 36
        self.age = age
        self.tests = []

    def is_adult(self):
        if self.age >= 21:
            return True
        else:
            False

#def class_work():
#    new_patient = Patient("ann",23,4)
#    print(new_patient.id)
#    print(new_patient.name)
#    new_guy = Patient("chii",23,5)
#    new_guy.name = "new name is me"
#    print(new_guy.name)
#    new_new_guy = Patient("Bob", 25,33)
#    print(new_new_guy.name)

def create_database_entry(patients_name, id, age):
#    new_patient = {"patient_names":patients_name,
#                                  "id":id,
#                   "age":age, "test":[]}
#    new_patient = [patients_name, id, age, []]
#    return new_patient

    new_patient = Patient(patients_name, id, age)
    return new_patient


def print_database(db):
    for patient in db:
        print(patient)

def print_datalocation(db):
    locations = ["rm1" ,"rm2", "rm3", "rm4"]
    for i, patient in enumerate(db):
        print("{} - {} - {}".format(i, patient, locations[i]))

def print_zip(db):
    locations = ["rm5","rm6","rm7","rm8"]
    for patient, locations in zip(db, locations):
        print("{} - {}".format(patient, locations))

def get_patient(db, id_no):
    patient = db[id_no]
    #for patient in db:
    #    if patient["id"] == id_no:
    #        return patient
    return patient

def main():
#    class_work()
#    return

    db = {}
    x = create_database_entry("a", 1, 21)
    db[x.id] = x
    x = create_database_entry("b", 2, 23)
    #db.append(x)
    db[x.id] = x
    x = create_database_entry("c", 3, 35)
    #db.append[x.id](x)
    db[x.id] = x
    x = create_database_entry("d", 4, 54)
    #db.append(x)
    db[x.id] = x
    print(db)

    print_database(db)
    print("/d")
    print(get_patient(db, 2))
    print("/d")
    print(print_zip(db))
    print("/d")
    patient_id_tested = 3
    test_done = ["HDL", 24]
    patient = get_patient(db, patient_id_tested)
    patient.tests.append(test_done)
    print(db[3].tests)
    print_database(db)
    
if __name__ == "__main__":
    main()
