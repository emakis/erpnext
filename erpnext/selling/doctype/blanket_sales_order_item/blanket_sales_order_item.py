# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

from frappe.model.document import Document
from erpnext.controllers.print_settings import print_settings_for_item_table

class BlanketSalesOrderItem(Document):
	def __setup__(self):
		print_settings_for_item_table(self)

def on_doctype_update():
	frappe.db.add_index("Blanket Sales Order Item", ["item_code", "warehouse"])
