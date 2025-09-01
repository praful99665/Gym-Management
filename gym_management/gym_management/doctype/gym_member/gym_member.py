# Copyright (c) 2025, Praful_D and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMember(Document):
	def before_insert(self):
		if self.member_name:
			customer = frappe.get_doc({
				"doctype": "Customer",
				"customer_name": self.member_name,
				"customer_type": "Individual",
				"territory": "All Territories",
				"customer_group": "Individual"
			})
			customer.insert(ignore_permissions=True)
			self.customer = customer.name
   
	def on_update(self):
		# frappe.msgprint("after_save triggered", "Gym Member Debug")
		if self.customer:
			customer_obj = frappe.get_doc("Customer", self.customer)
			if customer_obj.customer_name != self.member_name:
				customer_obj.customer_name = self.member_name
				customer_obj.save(ignore_permissions=True)
    
			
      
