# Copyright (c) 2024, beshoy.atef@dynamiceg.com and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

from frappe.website.website_generator import WebsiteGenerator
class AirplaneFlight(WebsiteGenerator):
	def on_submit(self) :
		#set status to copleted 
		self.status = "Completed"
	def before_submit(self):
		self.status = "Completed"