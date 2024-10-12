# ApiV100.OrderCreateApiModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterPaymentDescription** | **String** | After payment description | [optional] 
**attachments** | [**[OrderAttachmentApiModel]**](OrderAttachmentApiModel.md) | List of Order attachments | [optional] 
**couponCode** | **String** | Coupon to apply in order to get the discount | [optional] 
**currencyId** | **Number** | Foreign key Currency | [optional] 
**description** | **String** | Product description | [optional] 
**discountAmount** | **Number** | Discount amount | [optional] 
**items** | [**[OrderItemApiModel]**](OrderItemApiModel.md) | List of Order items | [optional] 
**name** | **String** | Product alias | [optional] 
**note** | **String** | Customer note to seller | [optional] 
**orderBillingDetails** | [**OrderBillingDetailsApiModel**](OrderBillingDetailsApiModel.md) |  | [optional] 
**orderShippingDetails** | [**OrderShippingDetailsApiModel**](OrderShippingDetailsApiModel.md) |  | [optional] 
**productId** | **Number** | Product id | [optional] 
**referral** | **String** | Represent the referral for this order | [optional] 
**shippingAmount** | **Number** | Cost for shipping the product | [optional] 
**shippingDescription** | **String** | Client instructions for shipping | [optional] 
**status** | **String** | Order status | [optional] 
**subTotalAmount** | **Number** | Sub total amount | [optional] 
**taxAmount** | **Number** | Tax amount | [optional] 
**totalAmount** | **Number** | Total amount | [optional] 
**whatHappensNextDescription** | **String** | What happens next description | [optional] 



## Enum: StatusEnum


* `PendingPayment` (value: `"PendingPayment"`)

* `Processing` (value: `"Processing"`)

* `Shipped` (value: `"Shipped"`)

* `Completed` (value: `"Completed"`)

* `OnHold` (value: `"OnHold"`)

* `Cancelled` (value: `"Cancelled"`)

* `Refunded` (value: `"Refunded"`)

* `Failed` (value: `"Failed"`)




