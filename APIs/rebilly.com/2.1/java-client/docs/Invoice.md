

# Invoice


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**abandonedTime** | **OffsetDateTime** | Invoice abandoned time. |  [optional] [readonly] |
|**amount** | **Double** | The invoice&#39;s amount. |  [optional] [readonly] |
|**amountDue** | **Double** | The invoice&#39;s due amount. |  [optional] [readonly] |
|**autopayRetryNumber** | **Integer** | Invoice autopay retry number. |  [optional] [readonly] |
|**autopayScheduledTime** | **OffsetDateTime** | Invoice autopay scheduled time. |  [optional] |
|**billingAddress** | [**ContactObject**](ContactObject.md) | Invoice&#39;s billing address. |  [optional] |
|**collectionPeriod** | **Integer** | Collection period - difference between paidTime and issuedTime in days. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Invoice created time. |  [optional] [readonly] |
|**currency** | **String** | ISO 4217 alphabetic currency code. |  |
|**delinquentCollectionPeriod** | **Integer** | Delinquent collection period - difference between paidTime and dueTime in days. |  [optional] [readonly] |
|**deliveryAddress** | [**ContactObject**](ContactObject.md) | Invoice&#39;s delivery address. |  [optional] |
|**discountAmount** | **Double** | The invoice&#39;s discounts amount. |  [optional] [readonly] |
|**discounts** | [**List&lt;InvoiceDiscount&gt;**](InvoiceDiscount.md) | Discounts applied. |  [optional] [readonly] |
|**dueTime** | **OffsetDateTime** | Invoice due time. |  [optional] [readonly] |
|**id** | **String** | The invoice ID. |  [optional] [readonly] |
|**invoiceNumber** | **Integer** | An auto-incrementing number based on the sequence of invoices for any particular customer. |  [optional] [readonly] |
|**issuedTime** | **OffsetDateTime** | Invoice issued time. |  [optional] [readonly] |
|**items** | [**List&lt;InvoiceItem&gt;**](InvoiceItem.md) | Invoice items array. |  [optional] [readonly] |
|**notes** | **String** | Notes for the customer which will be displayed on the invoice. |  [optional] |
|**paidTime** | **OffsetDateTime** | Invoice paid time. |  [optional] [readonly] |
|**paymentFormUrl** | **String** | URL where the customer can be redirected to pay for the invoice with one of the methods which are available for this customer. It&#39;s an alternative to creating a new transaction with empty &#x60;methods&#x60;.  |  [optional] [readonly] |
|**poNumber** | **String** | Purchase order number which will be displayed on the invoice. |  [optional] |
|**shipping** | [**InvoiceShipping**](InvoiceShipping.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Invoice status. |  [optional] [readonly] |
|**subscriptionId** | **String** | The related order&#39;s ID if available, otherwise null. |  [optional] [readonly] |
|**subtotalAmount** | **Double** | The invoice&#39;s subtotal amount. |  [optional] [readonly] |
|**tax** | [**InvoiceTax**](InvoiceTax.md) |  |  [optional] |
|**updatedTime** | **OffsetDateTime** | Invoice updated time. |  [optional] [readonly] |
|**voidedTime** | **OffsetDateTime** | Invoice voided time. |  [optional] [readonly] |
|**websiteId** | **String** | The website ID. |  |
|**embedded** | [**List&lt;InvoiceAllOfEmbedded&gt;**](InvoiceAllOfEmbedded.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;InvoiceAllOfLinks&gt;**](InvoiceAllOfLinks.md) | The links related to resource. |  [optional] [readonly] |
|**customerId** | **String** | The сustomer&#39;s ID. |  |
|**dueReminderNumber** | **Integer** | Number of past due reminder events triggered. |  [optional] [readonly] |
|**dueReminderTime** | **OffsetDateTime** | Time past due reminder event will be triggered. |  [optional] [readonly] |
|**retryInstruction** | [**InvoiceAllOfRetryInstruction**](InvoiceAllOfRetryInstruction.md) |  |  [optional] |
|**revision** | **Integer** | The number of times the invoice data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation.  |  [optional] [readonly] |
|**transactions** | [**List&lt;Transaction&gt;**](Transaction.md) | Invoice transactions array. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Invoice type. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| UNPAID | &quot;unpaid&quot; |
| PAID | &quot;paid&quot; |
| PAST_DUE | &quot;past-due&quot; |
| DELINQUENT | &quot;delinquent&quot; |
| ABANDONED | &quot;abandoned&quot; |
| VOIDED | &quot;voided&quot; |
| PARTIALLY_REFUNDED | &quot;partially-refunded&quot; |
| REFUNDED | &quot;refunded&quot; |
| DISPUTED | &quot;disputed&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INITIAL | &quot;initial&quot; |
| RENEWAL | &quot;renewal&quot; |
| INTERIM | &quot;interim&quot; |
| CANCELLATION | &quot;cancellation&quot; |
| ONE_TIME | &quot;one-time&quot; |
| REFUND | &quot;refund&quot; |
| CHARGE | &quot;charge&quot; |



