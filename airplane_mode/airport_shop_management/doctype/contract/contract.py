# Copyright (c) 2024, beshoy.atef@dynamiceg.com and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import today

class Contract(Document):
	"""

	TODO 
	Validate dates 
	validate status 
	On submit this document create two things 
	1 - make shop  not available 
	2 - create ledger for Tenant 
	
	"""
	def validate(self):
		self.validate_dates()
		self.validate_status()
		
	def validate_dates(self):
		if self.doe > self.contract_start_date :
			frappe.throw(_("Start date can not be befor expire date "))

	def validate_status(self) :
		if self.doe > today():
			self.active = 1 
		else :
			self.active = 0

	def validate_shop(self) :
		if not frappe.db.get_value("Shop" ,self.shop  , "available" )  :
			frappe.throw("shop is not  Available")

	def update_shop_status(self) :
		frappe.db.set_value('Shop', self.shop , 'available', 0)
	def before_save(self) :
		"""
		Set rent amount if not 

		"""

		if not self.rent_amount   :
			self.rent_amount = frappe.db.get_single_value("Global Configuration"  ,"default_rent_amount")
		self.validate_shop()
	def on_submit(self) :
		self.update_shop_status()
		
