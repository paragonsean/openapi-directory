

# ProductDetailsApiModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | Product short link |  [optional] |
|**afterPaymentDescription** | **String** | After payment description |  [optional] |
|**buttonCallToAction** | **String** | Default button call to action  Ex: Buy now, subscribe, ... |  [optional] |
|**currency** | [**CurrencyDetailsApiModel**](CurrencyDetailsApiModel.md) |  |  [optional] |
|**currencyId** | **Integer** | Foreign key Currency |  [optional] |
|**description** | **String** | Product description |  [optional] |
|**id** | **Integer** | Product id |  [optional] |
|**isFeatured** | **Boolean** | Indicate that the product is set as featured |  [optional] |
|**name** | **String** | Product alias |  [optional] |
|**shippingAmount** | **Double** | Cost for shipping the product |  [optional] |
|**shippingDescription** | **String** | Client instructions for shipping |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Product availability status |  [optional] |
|**subTotalAmount** | **Double** | Subtotal amount of product |  [optional] |
|**totalAmount** | **Double** | Total amount of product |  [optional] |
|**totalWithShipping** | **Double** | Total amount of product with shipping |  [optional] |
|**whatHappensNextDescription** | **String** | What happens next description |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| NOT_AVAILABLE | &quot;NotAvailable&quot; |
| INACTIVE | &quot;Inactive&quot; |



