import frappe

# Create Reverse of JV
def create_reverse_je():
    curr_date = frappe.utils.nowdate()

    # Check JV of current date
    je_list = frappe.db.sql("""select je.name 
                            from `tabJournal Entry` je
                            where je.provision = 1
                            and je.reversal_provision_date = %(curr_date)s
                            and je.inter_company_journal_entry_reference is null
                            and je.reversal_of is null
                            and je.docstatus = 1
                """,{'curr_date':curr_date},as_dict=True)

    if je_list:
        for i in je_list:
            # Check if already reverse JV is created
            rev_jv = frappe.db.get_value('Journal Entry', {'reversal_of': i.name})

            if rev_jv:
                continue
            else:
                doc = frappe.get_doc("Journal Entry",i.name)
                reverse_doc = frappe.new_doc("Journal Entry")

                reverse_doc.voucher_type = doc.voucher_type
                reverse_doc.naming_series = doc.naming_series
                reverse_doc.company = doc.company
                reverse_doc.posting_date = curr_date
                reverse_doc.provision = 1
                reverse_doc.reversal_provision_date = doc.reversal_provision_date
                reverse_doc.inter_company_journal_entry_reference = i.name
                reverse_doc.reversal_of = i.name

                for j in doc.accounts:             
                    if j.debit_in_account_currency:
                        row = reverse_doc.append("accounts", {
                            "account": j.account,
                            "credit_in_account_currency" : j.debit_in_account_currency,
                        })
                    else:
                        row = reverse_doc.append("accounts", {
                            "account": j.account,
                            "debit_in_account_currency" : j.credit_in_account_currency,
                        })
                reverse_doc.save(ignore_permissions = True)
                reverse_doc.submit()