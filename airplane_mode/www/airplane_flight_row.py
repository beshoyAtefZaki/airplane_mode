import frappe 

def get_context(context):
    flight= frappe.form_dict.flight
    context.flight = frappe.get_doc("Airplane Flight" , {"name" :flight} ,      ["name" ,"airplane" ,"source_airport_code" ,
                "destination_airport_code" ,"date_of_departure" , "time_of_departure" , "duration"   ])
    return context