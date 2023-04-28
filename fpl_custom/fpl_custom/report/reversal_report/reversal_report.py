# Copyright (c) 2023, Indictranstech and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	if not filters:
		filters = {}

	provision_jv_list = get_provision_data()
	columns = get_columns()

	data = []
	for jv in provision_jv_list:
		row = [
			jv.provision_jv,
			jv.name,
			jv.full_name,
			jv.posting_date,
			jv.reversal_of,
			jv.supplier,
			jv.debit_in_account_currency,
			jv.user_remark,
			jv.from_date,
			jv.to_date,
			jv.account,
			jv.modified_by,
			jv.remark,
			jv.workflow_state,
		]
		data.append(row)

	return columns, data

def get_columns():
	return [
		{
			"label": _("Provision"),
			"fieldname": "provision_jv",
			"fieldtype": "Link",
			"options": "Provision",
			"width": 150,
		},
		{
			"label": _("Name"),
			"fieldname": "name",
			"fieldtype": "Link",
			"options": "Journal Entry",
			"width": 150,
		},
		{
			"label": _("Employee Name/User Name"),
			"fieldname": "full_name",
			"fieldtype": "data",
			"width": 150,
		},
		{
			"label": _("Date of Provision Entry"),
			"fieldname": "posting_date",
			"fieldtype": "date",
			"width": 150,
		},
		{
			"label": _("Reversal Of"),
			"fieldname": "reversal_of",
			"fieldtype": "Link",
			"options": "Journal Entry",
			"width": 150,
		},
		{
			"label": _("Vendor Name"),
			"fieldname": "supplier",
			"fieldtype": "Link",
			"options": "Supplier",
			"width": 150,
		},
		{
			"label": _("Debit"),
			"fieldname": "debit_in_account_currency",
			"fieldtype": "Data",
			"width": 120,
		},
		{
			"label": _("Activity Description"),
			"fieldname": "user_remark",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"label": _("From"),
			"fieldname": "from_date",
			"fieldtype": "Date",
			"width": 100,
		},
		{
			"label": _("To"),
			"fieldname": "to_date",
			"fieldtype": "Date",
			"width": 100,
		},
		{
			"label": _("Expense Head"),
			"fieldname": "account",
			"fieldtype": "Link",
			"options":"Account",
			"width": 150,
		},
		{
			"label": _("Approved by"),
			"fieldname": "modified_by",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"label": _("Remark"),
			"fieldname": "remark",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"label": _("State"),
			"fieldname": "workflow_state",
			"fieldtype": "Data",
			"width": 120,
		},
	]

# def get_conditions(filters):
# 	conditions = ""

# 	if filters.get("supplier"):
# 		conditions += "and jva.supplier = %(supplier)s"

# 	return conditions

def get_provision_data():
	# conditions = get_conditions(filters)
	data = frappe.db.sql(
		"""select jv.provision_jv 
			, jv.name 
			, u.full_name
			, jv.posting_date
			, jva.supplier
			, jva.debit_in_account_currency
			, jva.credit_in_account_currency
			, jv.user_remark
			, jv.from_date
			, jv.to_date
			, jva.account
			, jv.modified_by
			, jva.remark
			, jv.workflow_state
			, jv.reversal_of
		from `tabJournal Entry` jv
		inner join `tabJournal Entry Account` jva
		on jva.parent = jv.name
		inner join `tabUser` u
		on jv.owner = u.name
		where jv.docstatus = 1
		and jv.provision = 1
		and jva.debit_in_account_currency > 0
		and jv.reversal_of is not null
		order by jv.creation desc"""
		, as_dict=1,
	)
	return data