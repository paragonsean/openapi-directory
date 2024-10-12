

# OrderinvoicesCreateChargeInvoiceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**invoiceId** | **String** | [required] The ID of the invoice. |  [optional] |
|**invoiceSummary** | [**InvoiceSummary**](InvoiceSummary.md) |  |  [optional] |
|**lineItemInvoices** | [**List&lt;ShipmentInvoiceLineItemInvoice&gt;**](ShipmentInvoiceLineItemInvoice.md) | [required] Invoice details per line item. |  [optional] |
|**operationId** | **String** | [required] The ID of the operation, unique across all operations for a given order. |  [optional] |
|**shipmentGroupId** | **String** | [required] ID of the shipment group. It is assigned by the merchant in the &#x60;shipLineItems&#x60; method and is used to group multiple line items that have the same kind of shipping charges. |  [optional] |



