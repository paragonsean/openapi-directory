# RebillyRestApi.UpcomingInvoiceItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTime** | **Date** | Date-time when the item was added to the subscription. | [optional] [readonly] 
**description** | **String** | Description of line item. | [optional] 
**periodEndTime** | **Date** | Date-time when the period ends for this item. | [optional] 
**periodStartTime** | **Date** | Date-time when the period begins for this item. | [optional] 
**quantity** | **Number** | Quantity of line item. | 
**type** | **String** | Type of line item. | 
**unitPriceAmount** | **Number** | Unit price of the line item. | 
**unitPriceCurrency** | **String** | ISO 4217 alphabetic currency code. | 



## Enum: TypeEnum


* `debit` (value: `"debit"`)

* `credit` (value: `"credit"`)




