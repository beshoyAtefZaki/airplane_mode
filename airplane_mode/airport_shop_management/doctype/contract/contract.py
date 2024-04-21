# Copyright (c) 2024, beshoy.atef@dynamiceg.com and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import today , add_to_date

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
		self.create_payemnt_scheduel()
	def validate_dates(self):
		if self.doe < self.contract_start_date :
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
		
	def create_payemnt_scheduel(self) :
		start_date = self.contract_start_date  
		end_date   = self.doe
		month_rent = self.contract_start_date  #add_to_date(self.contract_start_date  ,months=1   , as_string=True)
		validation_date =self.contract_start_date  # add_to_date(self.contract_start_date  ,months=1  ,days=-1 , as_string=True)
		while validation_date < end_date  :
			#create scheduel 
			scheduel = frappe.new_doc("Shop monthly rent scheduel" )
			scheduel.contract = self.name 
			scheduel.shop = self.shop 
			scheduel.amount = self.rent_amount 
			scheduel.due_date = month_rent
			scheduel.save()
			rent = month_rent
			month_rent = add_to_date( rent,months=1  , as_string=True)
			validation_date = add_to_date(rent ,months=1  , as_string=True)