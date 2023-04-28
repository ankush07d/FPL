// Copyright (c) 2023, Indictranstech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Provision', {
	refresh: function(frm) {
		if (frm.doc.entry_type == "Provision Journal Entry"){
			frm.add_custom_button(__("Create JV"), function() {				
				frappe.model.open_mapped_doc({
					method: "fpl_custom.fpl_custom.doctype.provision.provision.redirect_jv",
					frm: cur_frm
				})
			});
		}
	}
});
