import frappe 

def get_context(context):
    context.flights = frappe.get_list("Airplane Flight" , fields=["name" ,"airplane" ,"source_airport_code" ,
                "destination_airport_code" ,"date_of_departure" , "time_of_departure" , "duration"   ])
    return context