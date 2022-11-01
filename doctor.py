import medicine 

class Doctor:
    def __init__(self, name):
        self.name = name
        print(name)
    


    def test_patient(self, patient):
        
        if patient.is_sick():
            print(f"Dr. {self.name} tested patient {patient.name} positive for {patient.disease}.")
        else:
            print(f"Dr. {self.name} tested patient {patient.name}. Patient is healthy.")
        
        # Note: disease can have a value or be "None"
        return patient.disease
    
    def treat_patient(self, patient, med):
        
        print(f"Dr. {self.name} is treating patient {patient.name}.")
        print(f"  - Giving patient medicine for {med.treating_disease}.")
        
        # Give medicine to patient
        patient.take_medication(med)
        
        if patient.is_sick():
            print(f"  - {patient.name} is still sick.")
        else:
            print(f"  - {patient.name} is cured!")
    
    def fetch_medicine(self, disease):
        """Fetch medicine for disease.
        Args:
        - Disease: String, name of disease"""
        med = medicine.Medicine(disease)
        print(f"Dr. {self.name} fetched medication for disease {med.treating_disease}.")
        
        return med
