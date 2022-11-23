import medicine 

class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease

        print(name + " : " + disease)

    def is_sick(self):
        if self.disease == None:
            return False
        else:
            return True

    def take_medication(self, med):
        
        if self.disease == med.treating_disease:
            self.disease = None

    def greet(self):
        print("Hello! " + self.name)
