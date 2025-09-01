# Copyright (c) 2025, Praful_D and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Trainer(Document):
    def before_insert(self):
        if self.trainer_name:
            employee = frappe.get_doc({
                "doctype": "Employee",
                "first_name": self.trainer_name,
                "gender": self.gender,
                "date_of_birth": self.date_of_birth,
                "date_of_joining": self.date_of_joining,
                "custom_email": self.email,
                "cell_number": self.contact_number
            })
            employee.insert(ignore_permissions=True)
            self.employee = employee.name

    def on_update(self):
        if self.trainer_name and self.employee:
            employee_obj = frappe.get_doc("Employee", self.employee)

            if self.trainer_name and employee_obj.first_name != self.trainer_name:
                employee_obj.first_name = self.trainer_name

            if self.gender and employee_obj.gender != self.gender:
                employee_obj.gender = self.gender

            if self.date_of_birth and employee_obj.date_of_birth != self.date_of_birth:
                employee_obj.date_of_birth = self.date_of_birth

            if self.date_of_joining and employee_obj.date_of_joining != self.date_of_joining:
                employee_obj.date_of_joining = self.date_of_joining

            if self.email and employee_obj.custom_email != self.email:
                employee_obj.custom_email = self.email

            if self.contact_number and employee_obj.cell_number != self.contact_number:
                employee_obj.cell_number = self.contact_number

            employee_obj.save(ignore_permissions=True)
