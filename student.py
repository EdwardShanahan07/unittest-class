import requests
from datetime import date, timedelta

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    @property
    def email_address(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@email.com"


    def alert_santa(self):
        self.naughty_list = True


    def apply_extensions(self, days):
        self.end_date = self.end_date + timedelta(days=days)

    
    def course_schedule(self):
        response = requests.get(f"https://company.com/course-schedule/{self.first_name}/{self.last_name}")

        if response.ok: 
            return response.text
        else:
            return "Something went wrong"
