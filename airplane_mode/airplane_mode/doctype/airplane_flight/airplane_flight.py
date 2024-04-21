# Copyright (c) 2024, beshoy.atef@dynamiceg.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from frappe.website.website_generator import WebsiteGenerator
class AirplaneFlight(WebsiteGenerator):
	def on_submit(self) :
		#set status to copleted 
		self.status = "Completed"
	def before_submit(self):
		self.status = "Completed"
	def on_update(self):
		"""Update gate_number in related Airplane Tickets."""
		if self.gate_number:
			tickets = frappe.get_all("Airplane Ticket", filters={"flight": self.name})
			for ticket in tickets:
				frappe.db.set_value("Airplane Ticket", ticket.name, "gate_number", self.gate_number)
	


# @frappe.whitelist()
# def get_gate_number(doc_name):
#     """Retrieve the gate number for the specified document."""
#     if not frappe.db.exists("Airplane Flight", doc_name):
#         frappe.throw("Airplane Flight '{}' does not exist.".format(doc_name))

#     flight = frappe.get_doc("Airplane Flight", doc_name)
#     gate_number = flight.gate_number
#     tickets = frappe.get_all("Airplane Ticket", filters={"flight": doc_name}, fields=["name"])
#     for ticket in tickets:
#         frappe.db.set_value("Airplane Ticket", ticket.name, "gate_number", gate_number)

#     return gate_number

