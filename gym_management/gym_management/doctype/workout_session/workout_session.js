// Copyright (c) 2025, Praful_D and contributors
// For license information, please see license.txt

frappe.ui.form.on("Workout Session", {
    refresh(frm) {

        frm.fields_dict['members'].grid.get_field('members').get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    active: 1
                }
            };
        };


        frm.set_query('workout_type', function() {
            return {
                filters: {
                    enable: 1
                }
            };
        });







    }
});
