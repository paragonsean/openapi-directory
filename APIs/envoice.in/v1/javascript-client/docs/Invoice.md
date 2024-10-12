# ApiV100.Invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** |  | [optional] 
**activities** | [**[Activity]**](Activity.md) |  | [optional] 
**attachments** | [**[InvoiceAttachment]**](InvoiceAttachment.md) |  | [optional] 
**clientId** | **Number** |  | [optional] 
**clonedFromId** | **Number** |  | [optional] 
**currencyId** | **Number** |  | [optional] 
**discountAmount** | **Number** |  | [optional] 
**duedate** | **Date** |  | [optional] 
**enablePartialPayments** | **Boolean** |  | [optional] 
**estimationId** | **Number** |  | [optional] 
**id** | **Number** |  | [optional] 
**invoiceCategoryId** | **Number** |  | [optional] 
**isDigitallySigned** | **Boolean** |  | [optional] 
**issuedOn** | **Date** |  | [optional] 
**items** | [**[InvoiceItem]**](InvoiceItem.md) |  | [optional] 
**notes** | **String** |  | [optional] 
**number** | **String** |  | [optional] 
**orderId** | **Number** |  | [optional] 
**paymentGateways** | [**[PaymentGatewayForInvoice]**](PaymentGatewayForInvoice.md) |  | [optional] 
**paymentLinkId** | **Number** |  | [optional] 
**payments** | [**[Payment]**](Payment.md) |  | [optional] 
**poNumber** | **String** |  | [optional] 
**recurringProfileId** | **Number** |  | [optional] 
**shouldSendReminders** | **Boolean** |  | [optional] 
**status** | **String** |  | [optional] 
**subTotalAmount** | **Number** |  | [optional] 
**taxAmount** | **Number** |  | [optional] 
**terms** | **String** |  | [optional] 
**totalAmount** | **Number** |  | [optional] 
**userId** | **Number** |  | [optional] 



## Enum: StatusEnum


* `Draft` (value: `"Draft"`)

* `Paid` (value: `"Paid"`)

* `Unpaid` (value: `"Unpaid"`)

* `Overdue` (value: `"Overdue"`)

* `Void` (value: `"Void"`)




