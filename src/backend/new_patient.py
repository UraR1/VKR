from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from database.database import connect
class NewPatientScreen(Screen):
    def save_patient(self, name, birth_date, sex):
        with connect() as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO patient (name, birth_date, sex) VALUES (?, ?, ?)", (name, birth_date, sex))
            connection.commit()
