# RebillyRestApi.Invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandonedTime** | **Date** | Invoice abandoned time. | [optional] [readonly] 
**amount** | **Number** | The invoice&#39;s amount. | [optional] [readonly] 
**amountDue** | **Number** | The invoice&#39;s due amount. | [optional] [readonly] 
**autopayRetryNumber** | **Number** | Invoice autopay retry number. | [optional] [readonly] [default to 0]
**autopayScheduledTime** | **Date** | Invoice autopay scheduled time. | [optional] 
**billingAddress** | [**ContactObject**](ContactObject.md) | Invoice&#39;s billing address. | [optional] 
**collectionPeriod** | **Number** | Collection period - difference between paidTime and issuedTime in days. | [optional] [readonly] 
**createdTime** | **Date** | Invoice created time. | [optional] [readonly] 
**currency** | **String** | ISO 4217 alphabetic currency code. | 
**delinquentCollectionPeriod** | **Number** | Delinquent collection period - difference between paidTime and dueTime in days. | [optional] [readonly] 
**deliveryAddress** | [**ContactObject**](ContactObject.md) | Invoice&#39;s delivery address. | [optional] 
**discountAmount** | **Number** | The invoice&#39;s discounts amount. | [optional] [readonly] 
**discounts** | [**[InvoiceDiscount]**](InvoiceDiscount.md) | Discounts applied. | [optional] [readonly] 
**dueTime** | **Date** | Invoice due time. | [optional] [readonly] 
**id** | **String** | The invoice ID. | [optional] [readonly] 
**invoiceNumber** | **Number** | An auto-incrementing number based on the sequence of invoices for any particular customer. | [optional] [readonly] 
**issuedTime** | **Date** | Invoice issued time. | [optional] [readonly] 
**items** | [**[InvoiceItem]**](InvoiceItem.md) | Invoice items array. | [optional] [readonly] 
**notes** | **String** | Notes for the customer which will be displayed on the invoice. | [optional] 
**paidTime** | **Date** | Invoice paid time. | [optional] [readonly] 
**paymentFormUrl** | **String** | URL where the customer can be redirected to pay for the invoice with one of the methods which are available for this customer. It&#39;s an alternative to creating a new transaction with empty &#x60;methods&#x60;.  | [optional] [readonly] 
**poNumber** | **String** | Purchase order number which will be displayed on the invoice. | [optional] 
**shipping** | [**InvoiceShipping**](InvoiceShipping.md) |  | [optional] 
**status** | **String** | Invoice status. | [optional] [readonly] 
**subscriptionId** | **String** | The related order&#39;s ID if available, otherwise null. | [optional] [readonly] 
**subtotalAmount** | **Number** | The invoice&#39;s subtotal amount. | [optional] [readonly] 
**tax** | [**InvoiceTax**](InvoiceTax.md) |  | [optional] 
**updatedTime** | **Date** | Invoice updated time. | [optional] [readonly] 
**voidedTime** | **Date** | Invoice voided time. | [optional] [readonly] 
**websiteId** | **String** | The website ID. | 
**embedded** | [**[InvoiceAllOfEmbedded]**](InvoiceAllOfEmbedded.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[InvoiceAllOfLinks]**](InvoiceAllOfLinks.md) | The links related to resource. | [optional] [readonly] 
**customerId** | **String** | The сustomer&#39;s ID. | 
**dueReminderNumber** | **Number** | Number of past due reminder events triggered. | [optional] [readonly] 
**dueReminderTime** | **Date** | Time past due reminder event will be triggered. | [optional] [readonly] 
**retryInstruction** | [**InvoiceAllOfRetryInstruction**](InvoiceAllOfRetryInstruction.md) |  | [optional] 
**revision** | **Number** | The number of times the invoice data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation.  | [optional] [readonly] 
**transactions** | [**[Transaction]**](Transaction.md) | Invoice transactions array. | [optional] [readonly] 
**type** | **String** | Invoice type. | [optional] [readonly] 



## Enum: StatusEnum


* `draft` (value: `"draft"`)

* `unpaid` (value: `"unpaid"`)

* `paid` (value: `"paid"`)

* `past-due` (value: `"past-due"`)

* `delinquent` (value: `"delinquent"`)

* `abandoned` (value: `"abandoned"`)

* `voided` (value: `"voided"`)

* `partially-refunded` (value: `"partially-refunded"`)

* `refunded` (value: `"refunded"`)

* `disputed` (value: `"disputed"`)





## Enum: TypeEnum


* `initial` (value: `"initial"`)

* `renewal` (value: `"renewal"`)

* `interim` (value: `"interim"`)

* `cancellation` (value: `"cancellation"`)

* `one-time` (value: `"one-time"`)

* `refund` (value: `"refund"`)

* `charge` (value: `"charge"`)




