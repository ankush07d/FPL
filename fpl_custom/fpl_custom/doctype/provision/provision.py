# Copyright (c) 2023, Indictranstech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class Provision(Document):
	pass

@frappe.whitelist()
def redirect_jv(source_name, target_doc=None):
    target_doc = get_mapped_doc("Provision",source_name, {
            "Provision": {
                "doctype": "Journal Entry",
                "field_map": {
                    "provision": 1,
                    "provision_jv" : source_name,
                },
            }
        })
    return target_doc

