// Copyright (c) 2023, Indictranstech and contributors
// For license information, please see license.txt

frappe.ui.form.on("Purchase Order", {
    is_provision:function(frm) {
        reset_naming_series(frm);
        hide_tax_details(frm);
    },
    onload:function(frm){
        reset_naming_series(frm);
        hide_tax_details(frm);
    },
    refresh:function(frm){
        hide_show(frm);
    },
    customized_document_status:function(frm){
        frm.set_value("manger_approval","");
    }
})

frappe.ui.form.on("Purchase Order Item", {
    rate:function(frm){
        if (frm.doc.is_provision == 1){
            frappe.msgprint(__("Enter rate excluding GST"))
        }
    }
})


// Reset naming series for provision
function reset_naming_series(frm){
    if (frm.doc.is_provision == 1){
        frm.set_value("naming_series","PROV-ORD-.YY.-");
        frm.refresh_field("naming_series");
    }
    else{
        frm.set_value("naming_series","PUR-ORD-.YYYY.-");
        frm.refresh_field("naming_series");
    }
}

// Hide and show fields
function hide_show(frm){
    if (frm.doc.workflow_state == 'Approved'){
        frm.set_df_property("customized_document_status", "hidden", 0);
        frm.set_df_property("manger_approval", "hidden", 0);
    }
    else{
        frm.set_df_property("customized_document_status", "hidden", 1);
        frm.set_df_property("manger_approval", "hidden", 1);
    }
}

// Hide tax section
function hide_tax_details(frm){
    if (frm.doc.is_provision == 1){
        frm.set_df_property("total_taxes_and_charges", "hidden", 1);
        frm.set_df_property("taxes", "hidden", 1);
    }
    else{
        frm.set_df_property("total_taxes_and_charges", "hidden", 0);
        frm.set_df_property("taxes", "hidden", 0);
    }
}