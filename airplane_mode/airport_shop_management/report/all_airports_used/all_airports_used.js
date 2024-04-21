frappe.query_reports["All Airports Used"] = {
    "filters": [
        {
            "fieldname": "name",
            "label": __("Airport Name"),
            "fieldtype": "Link",
            "options": "Airport",
            "reqd": 0
        }
    ]
};
