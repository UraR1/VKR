from kivy.uix.screenmanager import Screen
from database.database import connect

class SeizureInfoScreen(Screen):
    def get_patient_names(self):
        with connect() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT name FROM patient")
            result = cursor.fetchall()
            patient_name = [row[0] for row in result]
        return patient_name

    def save_seizure_info(self, patient_name, seizure_start, seizure_duration, seizure_type):
        with connect() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO seizure (patient_name, seizure_start, seizure_duration, seizure_type) VALUES (?, ?, ?, ?)", (patient_name, seizure_start, seizure_duration, seizure_type))
            connection.commit()