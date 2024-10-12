

# AccountLineItemEntity

List Payments

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | Line item amount |  [optional] |
|**balance** | **Double** | Line item balance |  [optional] |
|**createdAt** | **OffsetDateTime** | Line item created at |  [optional] |
|**currency** | **String** | Line item currency |  [optional] |
|**downloadUri** | **String** | Line item download uri |  [optional] |
|**id** | **Integer** | Line item Id |  [optional] |
|**invoiceLineItems** | [**List&lt;InvoiceLineItemEntity&gt;**](InvoiceLineItemEntity.md) | Associated invoice line items |  [optional] |
|**method** | **String** | Line item payment method |  [optional] |
|**paymentLineItems** | [**List&lt;PaymentLineItemEntity&gt;**](PaymentLineItemEntity.md) | Associated payment line items |  [optional] |
|**paymentReversedAt** | **OffsetDateTime** | Date/time payment was reversed if applicable |  [optional] |
|**paymentType** | **String** | Type of payment if applicable |  [optional] |
|**siteName** | **String** | Site name this line item is for |  [optional] |
|**type** | **String** | Type of line item, either payment or invoice |  [optional] |
|**updatedAt** | **OffsetDateTime** | Line item updated at |  [optional] |



