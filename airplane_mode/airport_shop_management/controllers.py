import frappe 

from frappe.utils import add_to_date ,today


def check_contract_monthly_payments(doc) :
    """
    param :doc -- > string Contract name
    """
    contract = frappe.get_doc("Contract" , doc )
    contract.validate_status()
    if contract.active == 1 :
        start_date = contract.contract_start_date
        due_date = add_to_date(start_date , )