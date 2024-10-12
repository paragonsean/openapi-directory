

# OrderinvoicesCreateRefundInvoiceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**invoiceId** | **String** | [required] The ID of the invoice. |  [optional] |
|**operationId** | **String** | [required] The ID of the operation, unique across all operations for a given order. |  [optional] |
|**refundOnlyOption** | [**OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOption**](OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceRefundOption.md) |  |  [optional] |
|**returnOption** | [**OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOption**](OrderinvoicesCustomBatchRequestEntryCreateRefundInvoiceReturnOption.md) |  |  [optional] |
|**shipmentInvoices** | [**List&lt;ShipmentInvoice&gt;**](ShipmentInvoice.md) | Invoice details for different shipment groups. |  [optional] |



