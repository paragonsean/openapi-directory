# FilesComApi.AccountLineItemEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | Line item amount | [optional] 
**balance** | **Number** | Line item balance | [optional] 
**createdAt** | **Date** | Line item created at | [optional] 
**currency** | **String** | Line item currency | [optional] 
**downloadUri** | **String** | Line item download uri | [optional] 
**id** | **Number** | Line item Id | [optional] 
**invoiceLineItems** | [**[InvoiceLineItemEntity]**](InvoiceLineItemEntity.md) | Associated invoice line items | [optional] 
**method** | **String** | Line item payment method | [optional] 
**paymentLineItems** | [**[PaymentLineItemEntity]**](PaymentLineItemEntity.md) | Associated payment line items | [optional] 
**paymentReversedAt** | **Date** | Date/time payment was reversed if applicable | [optional] 
**paymentType** | **String** | Type of payment if applicable | [optional] 
**siteName** | **String** | Site name this line item is for | [optional] 
**type** | **String** | Type of line item, either payment or invoice | [optional] 
**updatedAt** | **Date** | Line item updated at | [optional] 


