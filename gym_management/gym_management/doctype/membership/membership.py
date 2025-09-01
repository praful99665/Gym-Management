# Copyright (c) 2025, Praful_D and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime


class Membership(Document):
	def on_submit(self):
		if self.gym_member:
			gym_member_obj = frappe.get_doc("Gym Member", self.gym_member)

			if self.membership_plan:
				membership_plan_obj = frappe.get_doc("Membership Plan", self.membership_plan)

				invoice = frappe.get_doc({
					"doctype": "Sales Invoice",
					"customer": gym_member_obj.customer,
					"posting_date": frappe.utils.nowdate(),
					"due_date": frappe.utils.nowdate(),
					"items": [
						{
							"item_code": membership_plan_obj.item,
							"qty": 1,
							"rate": membership_plan_obj.price,
						}
					]
				})

				invoice.insert(ignore_permissions=True)
				invoice.submit()

				self.db_set("invoice", invoice.name)



       
    