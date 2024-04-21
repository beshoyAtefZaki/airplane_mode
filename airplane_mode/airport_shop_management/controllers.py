import frappe 

from frappe.utils import today

@frappe.whitelist()
def check_contract_monthly_payments(*args , **kwargs) :
    """
    this function will serach for all shop pyment schedual with due date 
    """

    rent_payment_list = frappe.get_list("Shop monthly rent scheduel" ,
                filters = {"due_date" :["<" ,today()]  , "marked" : 0}  ,
                fields = ["name" , "shop" ,"contract", "tenant","due_date"] )


    #create payment document Tenant Rent Payment

    for schduel in rent_payment_list :
        #create payment document Tenant Rent Payment
        pay_doc= frappe.new_doc("Tenant Rent Payment")
        pay_doc.shop = schduel.shop
        pay_doc.due_date = schduel.due_date
        pay_doc.contract = schduel.contract
        pay_doc.tenant =schduel.tenant
        pay_doc.save()
        frappe.db.commit()
        print("Document created" , pay_doc.name)
   
    