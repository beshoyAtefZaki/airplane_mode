import frappe 
from frappe import throw , _ 



def valiadate_airplane_capacity(airplane , flight ) :
    """
    params 
    airplane : string airplane name 
    flighr : string flight name 
    
    function 
    check all flight ticket on this airplane and valide the capacity 
    """

    capacity = frappe.get_value("Airplane" , airplane , 'capacity')
    ticket_count = frappe.db.get_list("Airplane Flight" , filters={"airplane" : '010'} , 
                    fields=['count(name) as count'] )[0].get("count")
    return True