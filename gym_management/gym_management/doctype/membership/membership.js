// Copyright (c) 2025, Praful_D and contributors
// For license information, please see license.txt

frappe.ui.form.on("Membership", {
    start_date(frm) {
        if (frm.doc.start_date && frm.doc.membership_plan) {
            frappe.call({
                method: "frappe.client.get",
                args: {
                    doctype: "Membership Plan",
                    name: frm.doc.membership_plan
                },
                callback: function(response) {
                    if (response.message) {
                        let duration = response.message.duration_in_days;

                        if (duration) {
                            
                            let start = frappe.datetime.str_to_obj(frm.doc.start_date);
                            let end = frappe.datetime.add_days(start, duration);
                            frm.set_value("end_date", frappe.datetime.obj_to_str(end));

                            // frappe.msgprint(frappe.datetime.obj_to_str(end));
                        }
                    }
                }
            });
        }
    },

    refresh: function(frm) {
        if (frm.doc.docstatus === 1) {
            frm.add_custom_button(__('Create Payment Entry'), function() {
                frappe.set_route('Form', 'Payment Entry', 'new-payment-entry');  
            }, __('Create')); 
        }
    },
    onload: function(frm) {
        frm.set_query('gym_member', function() {
            return {
                filters: {
                    active: 1
                }
            };
        });

        frm.set_query('membership_plan', function() {
            return {
                filters: {
                    enable: 1
                }
            };
        });

    }


});

