import frappe


def execute(filters=None):
    columns = [
        {
            "fieldname": "name",
            "label": "Airport Name",
            "fieldtype": "Link",
            "options": "Airport",
            "width": 150
        },
        {
            "fieldname": "shop_count",
            "label": "Number of Shops",
            "fieldtype": "Int",
            "width": 150
        },
        {
            "fieldname": "available_airport",
            "label": "Available Airport",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "unavailable_airport",
            "label": "Unavailable Airport",
            "fieldtype": "Data",
            "width": 150
        }
    ]
    base_query = """
        SELECT
            a.name AS 'name',
            COUNT(s.name) AS 'shop_count',
            SUM(CASE WHEN s.available = 1 THEN 1 ELSE 0 END) AS 'available_airport',
            SUM(CASE WHEN s.available = 0 THEN 1 ELSE 0 END) AS 'unavailable_airport'
        FROM
            `tabAirport` a
        LEFT JOIN
            `tabShop` s ON s.airport = a.name
    """
    where_condition = ""
    if filters and filters.get("name"):
        where_condition = "WHERE a.name = '{0}'".format(filters.get("name").replace("'", "\\'"))
    final_query = base_query + where_condition + " GROUP BY a.name"
    data = frappe.db.sql(final_query, as_dict=True)

    return columns, data




