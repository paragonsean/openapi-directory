

# ProductUpdateApiModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afterPaymentDescription** | **String** | After payment description |  [optional] |
|**attachments** | [**List&lt;ProductAttachmentApiModel&gt;**](ProductAttachmentApiModel.md) | List of product attachments |  [optional] |
|**buttonCallToAction** | **String** | Default button call to action  Ex: Buy now, subscribe, ... |  [optional] |
|**coupons** | [**List&lt;ProductCouponApiModel&gt;**](ProductCouponApiModel.md) | List of product coupons |  [optional] |
|**currencyId** | **Integer** | Foreign key Currency |  [optional] |
|**description** | **String** | Product description |  [optional] |
|**discounts** | [**List&lt;ProductDiscountApiModel&gt;**](ProductDiscountApiModel.md) | List of product discounts |  [optional] |
|**id** | **Integer** | Product id |  [optional] |
|**isFeatured** | **Boolean** | Indicate that the product is set as featured |  [optional] |
|**items** | [**List&lt;ProductItemApiModel&gt;**](ProductItemApiModel.md) | List of product items |  [optional] |
|**name** | **String** | Product alias |  [optional] |
|**paymentGateways** | [**List&lt;ProductGatewayApiModel&gt;**](ProductGatewayApiModel.md) | List of enabled payment gateways for this product |  [optional] |
|**shippingAmount** | **Double** | Cost for shipping the product |  [optional] |
|**shippingDescription** | **String** | Client instructions for shipping |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Product availability status |  [optional] |
|**whatHappensNextDescription** | **String** | What happens next description |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| NOT_AVAILABLE | &quot;NotAvailable&quot; |
| INACTIVE | &quot;Inactive&quot; |



