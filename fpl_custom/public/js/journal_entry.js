frappe.ui.form.on("Journal Entry", {
    provision:function(frm){
        if (frm.doc.provision == 1){
            hide_column(frm);
        }
        refresh_field("accounts");
        reversal_validations(frm);
        check_posting_date(frm);
    },
    before_save:function(frm){
        check_posting_date(frm);
        add_provision_expense(frm);
    },
    onload:function(frm){
        if (frm.doc.provision == 1){
            hide_column(frm);
        }
        refresh_field("accounts");
        reversal_validations(frm);
        check_posting_date(frm);
    }
})

frappe.ui.form.on("Journal Entry Account", {
    debit_in_account_currency:function(frm){
        if (frm.doc.provision == 1){
            frappe.msgprint(__("Enter the amount excluding GST"));
        }
    }
})

// Functions 
function reversal_validations(frm){
    // set reversal_provision_date
    if (frm.doc.provision == 1 && frm.doc.workflow_state == 'DRAFT'){
        const curr_date = new Date();
        var nxt_month_first_date = new Date(curr_date.getFullYear(), curr_date.getMonth() + 1, 1);
        var day = nxt_month_first_date.getDate()
        var month = nxt_month_first_date.getMonth() + 1
        var year = nxt_month_first_date.getFullYear()

        frm.set_value("reversal_provision_date", year+"-"+month+"-"+day);
    }
}
// check posting date is less than or equal to 20th of current month
function check_posting_date(frm){
    // var post_date = new Date(frm.doc.posting_date)
    
    var post_date = moment(new Date(frm.doc.posting_date));
    
    if (frm.doc.provision == 1 && frm.doc.workflow_state == 'DRAFT'){    
        if (post_date._d.getDate() < 20){
            frappe.throw(__("Posting Date is less than 20th of this month"));
            }
    }
}

// Add Provision for Expense - FPL in A/Cs
function add_provision_expense(frm){
    var total_debit_amt = 0;

    if (frm.doc.provision == 1){
        (frm.doc.accounts || []).forEach(function(je_acc){
            if (je_acc.account == 'Provision for Expense - FPL'){
                frappe.model.remove_from_locals(je_acc.doctype, je_acc.name);
            }
            else{
                total_debit_amt += je_acc.debit_in_account_currency;
            }
        })
        refresh_field("accounts");

        let row = frm.add_child('accounts', {							
            account:'Provision for Expense - FPL',
            credit_in_account_currency : total_debit_amt,
        });
        refresh_field("accounts");
    }
}
// hide child table column
function hide_column(frm){
    if (frm.doc.provision == 1){
        frm.fields_dict.accounts.grid.set_column_disp('party_type', false);
        frm.fields_dict.accounts.grid.set_column_disp('party', false);
    }
    else{
        frm.fields_dict.accounts.grid.set_column_disp('party_type', true);
        frm.fields_dict.accounts.grid.set_column_disp('party', true);
    }
}