# SwaggerApi2Cart.CartCouponAdd

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionAmount** | **Number** | Defines the discount amount value. | 
**actionApplyTo** | **String** | Defines where discount should be applied | 
**actionConditionEntity** | **String** | Defines entity for action condition. | [optional] 
**actionConditionKey** | **String** | Defines entity attribute code for action condition. | [optional] 
**actionConditionOperator** | **String** | Defines condition operator. | [optional] 
**actionConditionValue** | **String** | Defines condition attribute value/s. Can be comma separated string. | [optional] 
**actionScope** | **String** | Specify how discount should be applied. If scope&#x3D;matching_items, then discount will be applied to each of the items that match action conditions. Scope order means that discount will be applied once. | 
**actionType** | **String** | Coupon discount type | 
**code** | **String** | Coupon code | 
**codes** | **[String]** | Entity codes | [optional] 
**dateEnd** | **String** | Defines when discount code will be expired. | [optional] 
**dateStart** | **String** | Defines when discount code will be available. | [optional] [default to &#39;now&#39;]
**name** | **String** | Coupon name | [optional] 
**storeId** | **String** | Store Id | [optional] 
**usageLimit** | **Number** | Usage limit for coupon. | [optional] 
**usageLimitPerCustomer** | **Number** | Usage limit per customer. | [optional] 



## Enum: ActionApplyToEnum


* `order_total` (value: `"order_total"`)

* `item_price` (value: `"item_price"`)

* `shipping` (value: `"shipping"`)





## Enum: ActionScopeEnum


* `order` (value: `"order"`)

* `matching_items` (value: `"matching_items"`)





## Enum: ActionTypeEnum


* `percent` (value: `"percent"`)

* `fixed` (value: `"fixed"`)




