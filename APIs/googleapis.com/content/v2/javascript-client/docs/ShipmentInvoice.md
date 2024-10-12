# ContentApiForShopping.ShipmentInvoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoiceSummary** | [**InvoiceSummary**](InvoiceSummary.md) |  | [optional] 
**lineItemInvoices** | [**[ShipmentInvoiceLineItemInvoice]**](ShipmentInvoiceLineItemInvoice.md) | [required] Invoice details per line item. | [optional] 
**shipmentGroupId** | **String** | [required] ID of the shipment group. It is assigned by the merchant in the &#x60;shipLineItems&#x60; method and is used to group multiple line items that have the same kind of shipping charges. | [optional] 


