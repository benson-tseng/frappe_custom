// Copyright (c) 2021, aaa and contributors
// For license information, please see license.txt

frappe.ui.form.on('Patient Appointment', {
	refresh: function (frm) {
		frm.add_custom_button(__("Do Something"), function () {
			// When this button is clicked, do this
			console.log(123)
		});
	}
});
