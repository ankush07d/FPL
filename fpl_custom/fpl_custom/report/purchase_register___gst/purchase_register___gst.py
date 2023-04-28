import frappe
from frappe import _


def execute(filters=None):
	if not filters:
		filters = {}

	pi_list = get_pr_gst_data(filters)
	columns = get_columns()

	data = []
	for pi in pi_list:
		row = [
			pi.posting_date, pi.supplier, pi.name, pi.bill_no,
			pi.bill_date, pi.tax_id, pi.rounded_total, pi.fixed_assets, pi.direct, pi.indirect,
			pi.in_state_5, pi.in_state_5, pi.igst5, 
			pi.in_state_12, pi.in_state_12, pi.igst12,
			pi.in_state_18, pi.in_state_18, pi.igst18,
			pi.in_state_28, pi.in_state_28, pi.igst28, ]

		data.append(row)
	return columns, data

def get_columns():
	return [
		{
			"label": _("Date"),
			"fieldname": "posting_date",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"label": _("Particulars"),
			"fieldname": "supplier",
			"fieldtype": "Link",
			"options" : "Supplier",
			"width": 150,
		},
		{
			"label": _("Voucher No."),
			"fieldname": "name",
			"fieldtype": "Link",
			"options" : "Purchase Invoice",
			"width": 150,
		},
		{
			"label": _("Supplier Invoice No"),
			"fieldname": "bill_no",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"label": _("Supplier Invoice Date"),
			"fieldname": "bill_date",
			"fieldtype": "Date",
			"width": 120,
		},
		{
			"label": _("GSTIN/UIN"),
			"fieldname": "tax_id",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"label": _("Gross Total"),
			"fieldname": "rounded_total",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 120,
		},
		{
			"label": _("Fixed Assets"),
			"fieldname": "fixed_assets",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 120,
		},
		{
			"label": _("Direct Expenses"),
			"fieldname": "direct_expenses",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 120,
		},
		{
			"label": _("Indirect Expenses"),
			"fieldname": "indirect_expenses",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 120,
		},
		{
			"label": _("CGST 2.5%"),
			"fieldname": "cgst2_5",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("SGST 2.5%"),
			"fieldname": "sgst2_5",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("IGST 5%"),
			"fieldname": "igst5",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("CGST 6%"),
			"fieldname": "cgst6",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("SGST 6%"),
			"fieldname": "sgst6",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("IGST 12%"),
			"fieldname": "igst12",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("CGST 9%"),
			"fieldname": "cgst9",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("SGST 9%"),
			"fieldname": "sgst9",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("IGST 18%"),
			"fieldname": "igst18",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("CGST 14%"),
			"fieldname": "cgst14",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("SGST 14%"),
			"fieldname": "sgst14",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
		{
			"label": _("IGST 28%"),
			"fieldname": "igst28",
			"fieldtype": "Float",
			"precision" : 2,
			"width": 110,
		},
	]

def get_conditions(filters):
	conditions = ""

	if filters.get("from_date"):
		conditions += " and pi.posting_date>=%(from_date)s"
	if filters.get("to_date"):
		conditions += " and date(pi.posting_date)<=%(to_date)s"

	return conditions

def get_pr_gst_data(filters):
	conditions = get_conditions(filters)
	data = frappe.db.sql(
		"""select pi.posting_date
			, pi.supplier
			, pi.name
			, pi.bill_no
			, pi.bill_date
			, pi.tax_id
			, pi.rounded_total
			, (case when tx.rate = 2.5 then tx.base_tax_amount_after_discount_amount 
				when tx.rate = 2.5 then tx.base_tax_amount_after_discount_amount
				else 0 end) as 'in_state_5'
			, (case when tx.rate = 6 then tx.base_tax_amount_after_discount_amount 
				when tx.rate = 6 then tx.base_tax_amount_after_discount_amount
				else 0 end) as 'in_state_12'
			, (case when tx.rate = 9 then tx.base_tax_amount_after_discount_amount 
				when tx.rate = 9 then tx.base_tax_amount_after_discount_amount
				else 0 end) as 'in_state_18'
			, (case when tx.rate = 14 then tx.base_tax_amount_after_discount_amount 
				when tx.rate = 14 then tx.base_tax_amount_after_discount_amount
				else 0 end) as 'in_state_28'
			, (case when tx.rate = 2.5 then (tx.base_tax_amount_after_discount_amount * 2)
				when tx.rate = 2.5 then (tx.base_tax_amount_after_discount_amount * 2)
				else 0 end) as 'igst5'
			, (case when tx.rate = 6 then (tx.base_tax_amount_after_discount_amount * 2)
				when tx.rate = 6 then (tx.base_tax_amount_after_discount_amount * 2)
				else 0 end) as 'igst12'
			, (case when tx.rate = 9 then (tx.base_tax_amount_after_discount_amount * 2)
				when tx.rate = 9 then (tx.base_tax_amount_after_discount_amount * 2)
				else 0 end) as 'igst18'
			, (case when tx.rate = 14 then (tx.base_tax_amount_after_discount_amount * 2)
				when tx.rate = 14 then (tx.base_tax_amount_after_discount_amount * 2)
				else 0 end) as 'igst28'
			, tx.rate
			, pi.taxes_and_charges_added
			, pi.taxes_and_charges
			, pii.expense_account
			, pii.amount
		from `tabPurchase Invoice` pi
		inner join `tabPurchase Taxes and Charges` tx
		on tx.parent = pi.name
		inner join `tabPurchase Invoice Item` pii 
		on pii.parent = pi.name
		where pi.docstatus = 1 %s order by pi.posting_date desc""" 
		% conditions, filters, as_dict=1)

	for i in data:
		main_parent = get_main_parent(i['expense_account'])

		# add column of indirect if main parent is "Indirect Expenses"
		if main_parent == 'Indirect Expenses - FPL' and i['igst5'] != 0.0:
			i['indirect'] = i['rounded_total'] - i['igst5']
		elif main_parent == 'Indirect Expenses - FPL' and i['igst12'] != 0.0:
			i['indirect'] = i['rounded_total'] - i['igst12']
		elif main_parent == 'Indirect Expenses - FPL' and i['igst18'] != 0.0:
			i['indirect'] = i['rounded_total'] - i['igst18']
		elif main_parent == 'Indirect Expenses - FPL' and i['igst28'] != 0.0:
			i['indirect'] = i['rounded_total'] - i['igst28']

		# add column of direct if main parent is "Direct Expenses"
		if main_parent == 'Direct Expenses - FPL' and i['igst5'] != 0.0:
			i['direct'] = i['rounded_total'] - i['igst5']
		elif main_parent == 'Direct Expenses - FPL' and i['igst12'] != 0.0:
			i['direct'] = i['rounded_total'] - i['igst12']
		elif main_parent == 'Direct Expenses - FPL' and i['igst18'] != 0.0:
			i['direct'] = i['rounded_total'] - i['igst18']
		elif main_parent == 'Direct Expenses - FPL' and i['igst28'] != 0.0:
			i['direct'] = i['rounded_total'] - i['igst28']

		# add column of direct if main parent is "Fixed Assets - FPL"
		if main_parent == 'Fixed Assets - FPL' and i['igst5'] != 0.0:
			i['fixed_assets'] = i['rounded_total'] - i['igst5']
		elif main_parent == 'Fixed Assets - FPL' and i['igst12'] != 0.0:
			i['fixed_assets'] = i['rounded_total'] - i['igst12']
		elif main_parent == 'Fixed Assets - FPL' and i['igst18'] != 0.0:
			i['fixed_assets'] = i['rounded_total'] - i['igst18']
		elif main_parent == 'Fixed Assets - FPL' and i['igst28'] != 0.0:
			i['fixed_assets'] = i['rounded_total'] - i['igst28']


	data1 = []
	used_invoice = []
    
	for i in data:
		if i.name in used_invoice:
			del i['posting_date']
			del i['supplier']
			del i['name']
			del i['bill_no']
			del i['bill_date']
			del i['tax_id']
			del i['rounded_total']
			del i['in_state_5']
			del i['in_state_12']
			del i['in_state_18']
			del i['in_state_28']
			del i['igst5']
			del i['igst12']
			del i['igst18']
			del i['igst28']
			del i['rate']
			del i['taxes_and_charges_added']
			del i['taxes_and_charges']
			del i['expense_account']
			del i['amount']

			if 'indirect' in i:
				del i['indirect']
			elif 'direct' in i:
				del i['direct']
			elif 'fixed_assets' in i:
				del i['fixed_assets']
				
			data1.append(i)
		else:
			used_invoice.append(i.name)
			data1.append(i)
	
	return filter(None,data1)

def get_main_parent(expense_name):
	expense_acc = ['Indirect Expenses - FPL', 'Direct Expenses - FPL', 'Fixed Assets - FPL']

	parent_present = True
	main_parent = ""
	
	parent_name = frappe.db.get_value("Account", expense_name, 'parent_account')
	
	if not parent_name:
		return expense_name
	else:
		main_parent = parent_name

	while parent_present:
		parent_name = frappe.db.get_value("Account", parent_name, 'parent_account')
		
		if not parent_name:
			parent_present = False
			main_parent = main_parent
		
		if parent_name in expense_acc:
			main_parent = parent_name
			parent_present = False

		main_parent = parent_name

	return main_parent