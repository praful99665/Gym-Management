import frappe
from frappe.utils import today

def expire_memberships():
    # Get all active memberships that have passed the end date
    memberships = frappe.get_all("Membership",
        filters={
            "status": "Active",
            "end_date": ("<", today())
        },
        fields=["name"]
    )

    for membership in memberships:
        frappe.db.set_value("Membership", membership.name, "status", "Expired")
