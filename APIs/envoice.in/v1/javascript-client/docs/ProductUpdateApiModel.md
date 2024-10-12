# ApiV100.ProductUpdateApiModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterPaymentDescription** | **String** | After payment description | [optional] 
**attachments** | [**[ProductAttachmentApiModel]**](ProductAttachmentApiModel.md) | List of product attachments | [optional] 
**buttonCallToAction** | **String** | Default button call to action  Ex: Buy now, subscribe, ... | [optional] 
**coupons** | [**[ProductCouponApiModel]**](ProductCouponApiModel.md) | List of product coupons | [optional] 
**currencyId** | **Number** | Foreign key Currency | [optional] 
**description** | **String** | Product description | [optional] 
**discounts** | [**[ProductDiscountApiModel]**](ProductDiscountApiModel.md) | List of product discounts | [optional] 
**id** | **Number** | Product id | [optional] 
**isFeatured** | **Boolean** | Indicate that the product is set as featured | [optional] 
**items** | [**[ProductItemApiModel]**](ProductItemApiModel.md) | List of product items | [optional] 
**name** | **String** | Product alias | [optional] 
**paymentGateways** | [**[ProductGatewayApiModel]**](ProductGatewayApiModel.md) | List of enabled payment gateways for this product | [optional] 
**shippingAmount** | **Number** | Cost for shipping the product | [optional] 
**shippingDescription** | **String** | Client instructions for shipping | [optional] 
**status** | **String** | Product availability status | [optional] 
**whatHappensNextDescription** | **String** | What happens next description | [optional] 



## Enum: StatusEnum


* `Active` (value: `"Active"`)

* `NotAvailable` (value: `"NotAvailable"`)

* `Inactive` (value: `"Inactive"`)




