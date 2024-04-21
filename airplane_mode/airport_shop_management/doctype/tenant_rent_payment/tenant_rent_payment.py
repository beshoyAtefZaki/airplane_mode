# Copyright (c) 2024, beshoy.atef@dynamiceg.com and contributors
# For license information, please see license.txt

import frappe
from frappe import _ 
from frappe.model.document import Document


class TenantRentPayment(Document):
	def after_insert(self) :
		frappe.sendmail(
					recipients=self.email,
					subject=frappe._('Rent Reminder'),
					#template='rent_reminder',
					args=dict(
						reminder_text=f"you have payment on {self.due_date}",
						
						message="Payment required",
					),
					header=_('Payment Reminder ')
				)


