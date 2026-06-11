# src/superstore/constants.py

RAW_DATA_FILENAME = "superstore.csv"
PROCESSED_DATA_FILENAME = "superstore_clean.csv"

DATE_COLUMNS = [
    "order_date",
    "ship_date",
]

REQUIRED_COLUMNS = [
    "Order.Date",
    "Ship.Date",
    "Ship.Mode",
    "Customer.ID",
    "Customer.Name",
    "Segment",
    "Country",
    "City",
    "State",
    "Region",
    "Market",
    "Category",
    "Sub.Category",
    "Product.Name",
    "Sales",
    "Quantity",
    "Discount",
    "Profit",
    "Shipping.Cost",
    "Order.Priority",
]

UNUSED_COLUMNS = [
    "Row.ID",
    "Postal.Code",
    "记录数",
]

COLUMN_RENAME_MAP = {
    "Row.ID": "row_id",
    "Order.ID": "order_id",
    "Order.Date": "order_date",
    "Ship.Date": "ship_date",
    "Ship.Mode": "ship_mode",
    "Customer.ID": "customer_id",
    "Customer.Name": "customer_name",
    "Segment": "segment",
    "Country": "country",
    "City": "city",
    "State": "state",
    "Postal.Code": "postal_code",
    "Market": "market",
    "Market2": "market_group",
    "Region": "region",
    "Product.ID": "product_id",
    "Category": "category",
    "Sub.Category": "sub_category",
    "Product.Name": "product_name",
    "Sales": "sales",
    "Quantity": "quantity",
    "Discount": "discount",
    "Profit": "profit",
    "Shipping.Cost": "shipping_cost",
    "Order.Priority": "order_priority",
    "Year": "year",
    "weeknum": "week_number",
    "记录数": "record_count",
}
