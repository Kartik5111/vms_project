# vms_project
Develop a Vendor Management System using Django and Django REST Framework.

1. Vendor Model.
Fields:
name: Vendor's name (CharField).
contact_details: Contact information of the vendor (TextField).
address: Physical address of the vendor (TextField).
vendor_code: A unique identifier for the vendor (CharField).
on_time_delivery_rate: Tracks the percentage of on-time deliveries (FloatField).
quality_rating_avg: Average rating of quality based on purchase orders (FloatField).
average_response_time: Average time taken to acknowledge purchase orders (FloatField).
fulfillment_rate: Percentage of purchase orders fulfilled successfully (FloatField).

2. Purchase Order (PO) Model
Fields:
po_number: Unique number identifying the PO (CharField).
vendor: Link to the Vendor model (ForeignKey).
order_date: Date when the order was placed (DateTimeField).
delivery_date: Expected or actual delivery date of the order (DateTimeField).
items: Details of items ordered (JSONField).
quantity: Total quantity of items in the PO (IntegerField).
status: Current status of the PO (e.g., pending, completed, canceled) (CharField).
quality_rating: Rating given to the vendor for this PO (nullable) (FloatField).
issue_date: Timestamp when the PO was issued to the vendor (DateTimeField).
acknowledgment_date: Timestamp when the vendor acknowledged the PO

3. Historical Performance Model
Fields:
vendor: Link to the Vendor model (ForeignKey).
date: Date of the performance record (DateTimeField).
on_time_delivery_rate: Historical record of the on-time delivery rate (FloatField).
quality_rating_avg: Historical record of the quality rating average (FloatField).
average_response_time: Historical record of the average response time (FloatField).
fulfillment_rate: Historical record of the fulfilment rate (FloatField).
-----------------------------------------------------------------------------------------------------------
some Information
1.This project is built using Django and Django REST Framework.
2.Ensure you have Python and Django installed to run the project locally.
3.Adjust the database settings and configurations according to your environment.


