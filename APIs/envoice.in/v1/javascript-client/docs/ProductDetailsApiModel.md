# ApiV100.ProductDetailsApiModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | Product short link | [optional] 
**afterPaymentDescription** | **String** | After payment description | [optional] 
**buttonCallToAction** | **String** | Default button call to action  Ex: Buy now, subscribe, ... | [optional] 
**currency** | [**CurrencyDetailsApiModel**](CurrencyDetailsApiModel.md) |  | [optional] 
**currencyId** | **Number** | Foreign key Currency | [optional] 
**description** | **String** | Product description | [optional] 
**id** | **Number** | Product id | [optional] 
**isFeatured** | **Boolean** | Indicate that the product is set as featured | [optional] 
**name** | **String** | Product alias | [optional] 
**shippingAmount** | **Number** | Cost for shipping the product | [optional] 
**shippingDescription** | **String** | Client instructions for shipping | [optional] 
**status** | **String** | Product availability status | [optional] 
**subTotalAmount** | **Number** | Subtotal amount of product | [optional] 
**totalAmount** | **Number** | Total amount of product | [optional] 
**totalWithShipping** | **Number** | Total amount of product with shipping | [optional] 
**whatHappensNextDescription** | **String** | What happens next description | [optional] 



## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `NotAvailable` (value: `"NotAvailable"`)

* `Inactive` (value: `"Inactive"`)




