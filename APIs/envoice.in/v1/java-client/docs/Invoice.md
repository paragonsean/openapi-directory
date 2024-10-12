

# Invoice


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** |  |  [optional] |
|**activities** | [**List&lt;Activity&gt;**](Activity.md) |  |  [optional] |
|**attachments** | [**List&lt;InvoiceAttachment&gt;**](InvoiceAttachment.md) |  |  [optional] |
|**clientId** | **Integer** |  |  [optional] |
|**clonedFromId** | **Integer** |  |  [optional] |
|**currencyId** | **Integer** |  |  [optional] |
|**discountAmount** | **Double** |  |  [optional] |
|**duedate** | **OffsetDateTime** |  |  [optional] |
|**enablePartialPayments** | **Boolean** |  |  [optional] |
|**estimationId** | **Integer** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**invoiceCategoryId** | **Integer** |  |  [optional] |
|**isDigitallySigned** | **Boolean** |  |  [optional] |
|**issuedOn** | **OffsetDateTime** |  |  [optional] |
|**items** | [**List&lt;InvoiceItem&gt;**](InvoiceItem.md) |  |  [optional] |
|**notes** | **String** |  |  [optional] |
|**number** | **String** |  |  [optional] |
|**orderId** | **Integer** |  |  [optional] |
|**paymentGateways** | [**List&lt;PaymentGatewayForInvoice&gt;**](PaymentGatewayForInvoice.md) |  |  [optional] |
|**paymentLinkId** | **Integer** |  |  [optional] |
|**payments** | [**List&lt;Payment&gt;**](Payment.md) |  |  [optional] |
|**poNumber** | **String** |  |  [optional] |
|**recurringProfileId** | **Integer** |  |  [optional] |
|**shouldSendReminders** | **Boolean** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**subTotalAmount** | **Double** |  |  [optional] |
|**taxAmount** | **Double** |  |  [optional] |
|**terms** | **String** |  |  [optional] |
|**totalAmount** | **Double** |  |  [optional] |
|**userId** | **Integer** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;Draft&quot; |
| PAID | &quot;Paid&quot; |
| UNPAID | &quot;Unpaid&quot; |
| OVERDUE | &quot;Overdue&quot; |
| VOID | &quot;Void&quot; |



