# Medical Expert System using Knowledge Representation
class Patient:
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms

class KnowledgeBase:

    def __init__(self):

        self.rules = {
            ("Fever", "Headache", "Fatigue"): "Malaria",
            ("Cough", "Chest Pain", "Fatigue"): "Pneumonia",
            ("Sneezing", "Runny Nose", "Sore Throat"): "Flu",
            ("Vomiting", "Diarrhea", "Fatigue"): "Food Poisoning"
        }


    def diagnose(self, patient):

        for symptoms, disease in self.rules.items():

           
            if all(symptom in patient.symptoms for symptom in symptoms):
                return disease

        return "No matching disease found."



print("=== Medical Expert System ===")

name = input("Enter patient name: ")

print("\n Enter symptoms separated by commas")
user_input = input("Symptoms: ")

# Convert input into list
symptoms = [s.strip() for s in user_input.split(",")]

patient = Patient(name, symptoms)

system = KnowledgeBase()

result = system.diagnose(patient)

# Display result
print(f"\n Patient: {patient.name}")
print(f"Possible illness: {result}")
