
import doctor
import patient
import medicine

class Hospital():

    def __init__(self):
        self.doctors = []
        self.patients = []
        
        self.init_doctors()
        self.init_patients()

        #self.test_all_patients()
        #self.test_all_patients(doctor)
        self.treat_patients()
    
    def init_doctors(self):
        print('Employing doctors...\n')
        self.doctors.append(doctor.Doctor(name='Mike'))
        self.doctors.append(doctor.Doctor(name='Anna'))
    
    def init_patients(self):
        print('Receiving patients...\n')
        self.patients.append(patient.Patient(name='Betty', disease='Uncommon Cold'))
        self.patients.append(patient.Patient(name='Rosario', disease='Infectious Laughter'))
        self.patients.append(patient.Patient(name='Anna', disease='Golf Stones'))
        self.patients.append(patient.Patient(name='Bernard', disease='Transparency'))
        self.patients.append(patient.Patient(name='Mark', disease='3rd Degree Sideburns'))
        self.patients.append(patient.Patient(name='Cory', disease='Spare Ribs'))
        self.patients.append(patient.Patient(name='Robin', disease='Broken Wind'))
    
    def test_all_patients(self, doc):
        print('Testing all patients!')
        
        for p in self.patients:
            doc.test_patient(p)
    # 2
    def greet_all_patients(self):
        for p in self.patients:
            p.greet()
    
    def treat_patients(self):
        print('Greeting all patients!')
        # 3
        self.greet_all_patients()
        print('-' * 15)
        print('\nTreating all patients!')
        print('-' * 15)
        self.test_all_patients(self.doctors[0])
        
        print('-' * 15)
        self.doctors[1].treat_patient(self.patients[0], self.doctors[1].fetch_medicine('Uncommon Cold'))
        self.doctors[0].treat_patient(self.patients[1], self.doctors[0].fetch_medicine('Infectious Laughter'))
        self.doctors[1].treat_patient(self.patients[3], self.doctors[1].fetch_medicine('Transparency'))
        self.doctors[0].treat_patient(self.patients[5], self.doctors[0].fetch_medicine('Transparency'))
        self.doctors[1].treat_patient(self.patients[5], self.doctors[1].fetch_medicine('Spare Ribs'))
        
        print('-' * 15)
        self.test_all_patients(self.doctors[1])
        
        print('-' * 15)
        self.doctors[0].treat_patient(self.patients[2], self.doctors[0].fetch_medicine('Golf Stones'))
        self.doctors[1].treat_patient(self.patients[4], self.doctors[1].fetch_medicine('3rd Degree Sideburns'))
        self.doctors[0].treat_patient(self.patients[6], self.doctors[0].fetch_medicine('Broken Wind'))
        
        print('-' * 15)
        self.test_all_patients(self.doctors[0])
        
        print('-' * 15)
        print('\nDone!')
            
if __name__ == '__main__':
    Hospital()