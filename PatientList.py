from PatientNode import PatientNode


class PatientList:
    def __init__(self, max_beds):
        self.max_beds = max_beds
        self.bed_count = 0
        self.head = None

    def addPatient(self, name, age):
        if self.bed_count >= self.max_beds:
            raise Exception("No hay camas disponibles")

        self.bed_count += 1
        new_patient = PatientNode(name, age, self.bed_count)

        if not self.head:
            self.head = new_patient
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_patient

    def removePatient(self, name):
        if not self.head:
            raise Exception("Paciente no encontrado")

        if self.head.name == name:
            self.head = self.head.next
            self.bed_count -= 1
            return

        current = self.head
        prev = None
        while current:
            if current.name == name:
                prev.next = current.next
                self.bed_count -= 1
                return
            prev = current
            current = current.next

        raise Exception("Paciente no encontrado")

    def getPatient(self, name):
        current = self.head
        while current:
            if current.name == name:
                return {
                    'name': current.name,
                    'age': current.age,
                    'bedNumber': current.bed_number
                }
            current = current.next

        raise Exception("Paciente no encontrado")

    def getPatientList(self):
        patient_list = []
        current = self.head
        while current:
            patient_list.append({
                'name': current.name,
                'age': current.age,
                'bedNumber': current.bed_number
            })
            current = current.next
        return patient_list

    def getAvailableBeds(self):
        return self.max_beds - self.bed_count
