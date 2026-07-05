class Patient:
    def __init__(self, id=None, name=None, age=None, address=None, phone=None, weight=None, height=None, bp=None, allergies=None, symptoms=None, triage_status=None, recommendation=None, created_at=None):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.weight = weight
        self.height = height
        self.bp = bp
        self.allergies = allergies
        self.symptoms = symptoms
        self.triage_status = triage_status
        self.recommendation = recommendation
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "address": self.address,
            "phone": self.phone,
            "weight": self.weight,
            "height": self.height,
            "bp": self.bp,
            "allergies": self.allergies,
            "symptoms": self.symptoms,
            "triage_status": self.triage_status,
            "recommendation": self.recommendation,
            "created_at": self.created_at
        }
