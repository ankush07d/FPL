from . import __version__ as app_version

app_name = "fpl_custom"
app_title = "Fpl Custom"
app_publisher = "Indictranstech"
app_description = "Custom Developments for FPL"
app_email = "ankush.d@indictranstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/fpl_custom/css/fpl_custom.css"
# app_include_js = "/assets/fpl_custom/js/fpl_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/fpl_custom/css/fpl_custom.css"
# web_include_js = "/assets/fpl_custom/js/fpl_custom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "fpl_custom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
#   "doctype" : "public/js/doctype.js"
    "Journal Entry" : "public/js/journal_entry.js",
	"File" : "public/js/file.js",
	"Purchase Order" : "public/js/purchase_order.js",
    "Purchase Invoice" : "public/js/purchase_invoice.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Fixtures
# fixtures = [{"dt":'Report',"filters":[["name", "in", ("Purchase Order or Provision List","Accounts Payable - FPL","Purchase Register - FPL","PI Condensed","Audit System Hooks","TDS Payable Monthly - FPL","Reversal Report","Provision Report - JV","Purchase Register - GST")]]}]
fixtures = ["Mode of Payment"]
# "Account",
# "Fiscal Year",
# "Accounting Dimension",
# "Payment Term",
# "Payment Terms Template",
# "Journal Entry Template",
# "Customer Group",
# "Customer",
# "Supplier Group",
# "Supplier",
# "Bank",
# "Bank Account",
# "Cost Center",
# "Budget",
# "Tax Category",
# "Tax Withholding Category",
# "Asset Category",
# "Item",
# "Price List",
# "Item Price",
# "Item Group",
# "Purchase Taxes and Charges Template",
# "Contact",
# "Address",
# "Warehouse"]


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "fpl_custom.utils.jinja_methods",
#	"filters": "fpl_custom.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "fpl_custom.install.before_install"
# after_install = "fpl_custom.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "fpl_custom.uninstall.before_uninstall"
# after_uninstall = "fpl_custom.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "fpl_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
#	"all": [
#		"fpl_custom.tasks.all"
#	],
	"daily": [
		"fpl_custom.docevents.journal_entry.create_reverse_je",
	],
#	"hourly": [
#		"fpl_custom.tasks.hourly"
#	],
#	"weekly": [
#		"fpl_custom.tasks.weekly"
#	],
#	"monthly": [
#		"fpl_custom.tasks.monthly"
#	],
}

# Testing
# -------

# before_tests = "fpl_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "fpl_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "fpl_custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"fpl_custom.auth.validate"
# ]
