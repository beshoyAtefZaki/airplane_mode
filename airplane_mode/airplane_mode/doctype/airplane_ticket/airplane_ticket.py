# Copyright (c) 2023, beshoy.atef@dynamiceg.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import throw , _
import string
import random

class AirplaneTicket(Document):
	def before_save(self) :
		#check if not seat name  
		if not self.seat  :
			self.seat = self.seat_random_create()
	def validate(self):
		self.validate_add_ons()
		self.caculate_totals()
		self.validate_airplane_capacity()
		# remove it afetr test 
		# if not self.seat :
		# 	self.seat = self.seat_random_create()
	def seat_random_create(self) :
		# this function will create 3 length straing first 2 letters will be numbers and end the end will add on cap letter
		seat_name = ''.join(random.choice( string.digits) for _ in range(2)) +\
		 			''.join(random.choice( string.ascii_uppercase) for _ in range(1))
		return seat_name

	def caculate_totals(self):
		total_add_ons = 0 
		for add_on in self.add_ons :
			total_add_ons+= float(add_on.amount )
		self.total_amount = float(self.flight_price) + float(total_add_ons)
	def validate_add_ons(self):
		"""
		remove duplicated entry 
		# case one : remove any duplicated entry without sum 
		# case tow  : sum entry amount and remove duplicate 
		our soulation case one 
		"""
		add_ons_list = []
		for add_on in self.add_ons :
			if add_on.item in add_ons_list :
				self.remove(add_on)
			else :
				add_ons_list.append(add_on.item)


	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw(frappe._(f"{self.status}  Not valide status \n  Please set status Boarded " ))	

	def validate_airplane_capacity(self) :
		airplane = frappe.get_value("Airplane Flight" , self.flight , "airplane")
		capacity = frappe.get_value("Airplane" , airplane , 'capacity')
		ticket_count = frappe.db.get_list("Airplane Ticket" , filters={"flight" : self.flight} , 
					fields=['count(name) as count'] )[0].get("count")

		
		if float(ticket_count or 0) > float(capacity or 0) :
			frappe.throw(_(f"airplane capacity : {capacity} is full "))

