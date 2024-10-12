# EcommerceApi.EcommerceOrder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAddress** | [**EcommerceAddress**](EcommerceAddress.md) |  | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**customer** | [**LinkedEcommerceCustomer**](LinkedEcommerceCustomer.md) |  | [optional] 
**discounts** | [**[EcommerceDiscount]**](EcommerceDiscount.md) |  | [optional] 
**fulfillmentStatus** | **String** | Current fulfillment status of the order. | [optional] 
**id** | **String** | A unique identifier for an object. | [readonly] 
**lineItems** | [**[EcommerceOrderLineItem]**](EcommerceOrderLineItem.md) |  | [optional] 
**note** | **String** | Note for the order. | [optional] 
**orderNumber** | **String** | Order number, if any. | [optional] 
**paymentMethod** | **String** | Payment method used for this order. | [optional] 
**paymentStatus** | **String** | Current payment status of the order. | [optional] 
**shippingAddress** | [**EcommerceAddress**](EcommerceAddress.md) |  | [optional] 
**shippingCost** | **String** | Shipping cost, if any. | [optional] 
**status** | [**EcommerceOrderStatus**](EcommerceOrderStatus.md) |  | [optional] 
**subTotal** | **String** | Sub-total amount, normally before tax. | [optional] 
**totalAmount** | **String** | Total amount due. | [optional] 
**totalDiscount** | **String** | Total discount, if any. | [optional] 
**totalTax** | **String** | Total tax, if any. | [optional] 
**tracking** | [**[TrackingItem]**](TrackingItem.md) |  | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 



## Enum: FulfillmentStatusEnum


* `pending` (value: `"pending"`)

* `shipped` (value: `"shipped"`)

* `partial` (value: `"partial"`)

* `delivered` (value: `"delivered"`)

* `cancelled` (value: `"cancelled"`)

* `returned` (value: `"returned"`)

* `unknown` (value: `"unknown"`)





## Enum: PaymentStatusEnum


* `pending` (value: `"pending"`)

* `authorized` (value: `"authorized"`)

* `paid` (value: `"paid"`)

* `partial` (value: `"partial"`)

* `refunded` (value: `"refunded"`)

* `voided` (value: `"voided"`)

* `unknown` (value: `"unknown"`)




