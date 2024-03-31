// Copyright (c) 2023, beshoy.atef@dynamiceg.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {

    setup_button(frm) {
        frm.add_custom_button("assign Seat", ()=>{
            frappe.prompt({
                fieldname :"seat" ,
                fieldtype:"Data" ,
                label:"Seat" ,
                reqd :1
            },(data)=> {
                frm.set_value("seat" , data.seat)
            frm.save()           })
        },"Actions")
    },
	refresh(frm) {
        if (frm.doc.docstatus === 0 ) {
            frm.events.setup_button(frm)
        }
           
	},
});
