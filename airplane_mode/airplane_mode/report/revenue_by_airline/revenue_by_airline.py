# Copyright (c) 2024, beshoy.atef@dynamiceg.com and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):


	columns, data = get_columns(), get_data()

	chart = {
		"type" :"donut" ,
		"data" :{
			"labels" : [i.get("airline") for i in data ] ,
			"datasets" : [{
				"values" : [ i.get("revenue")  or 0 for i in data]}
				
				]
			
		}
	}

	print([ i for i in data])
	total_revenue =sum(float(i.get("revenue") or 0) for i in data)
	report_summry = [
		{
			"value":total_revenue,
			"datatype" : "Currency" ,
			"indicator":"green" if total_revenue > 0 else 0 ,
			"label":"Total Revenue"
		}
	]
	return columns, data ,None , chart ,report_summry


def get_data(filters=None) :
	airline_flight = """select line.name  as airline  ,
	COALESCE(SUM(ticket.total_amount) , 0) AS revenue
	FROM `tabAirline`  line
	LEFT JOIN `tabAirplane` airplane
	ON line.name=  airplane.airline 
	LEFT JOIN `tabAirplane Flight`  flight 
	ON flight.airplane = airplane.name
	LEFT JOIN `tabAirplane Ticket`  ticket 
	ON flight.name = ticket.flight
	GROUP BY airline ;
						
						  """
	data = frappe.db.sql(airline_flight,as_dict=True)
	
	return data


def get_columns(filters=None) :
	return [
			{
				"fieldtype" : "Link" ,
				"fieldname" : "airline" ,
				"label" :"Aitline" ,
				"options" :"Airline" ,
				"width" : 500
			} ,
			{
				"fieldtype" : "Currency" ,
				"fieldname" : "revenue" ,
				"label" :"Revenue" ,
				"width" : 300
				
			}

		]