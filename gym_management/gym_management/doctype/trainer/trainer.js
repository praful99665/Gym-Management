// Copyright (c) 2025, Praful_D and contributors
// For license information, please see license.txt

frappe.ui.form.on("Trainer", {
    refresh: function(frm) {
        frm.set_query('specialization', function() {
            return {
                filters: {
                    enable: 1
                }
            };
        });
    },
    onload: function(frm) {
        frm.set_query('specialization', function() {
            return {
                filters: {
                    enable: 1
                }
            };
        });

        frm.fields_dict['assigned_members'].grid.get_field('members').get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    active: 1
                }
            };
        };

    },

});
