# JumpsellerApi.OrderFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalFields** | [**[OrderAdditionalFields]**](OrderAdditionalFields.md) | Array of additional fields for the given Order | [optional] 
**additionalInformation** | **String** | Additional information for the given Order | [optional] 
**billingAddress** | [**OrderBillingAddress**](OrderBillingAddress.md) |  | [optional] 
**checkoutUrl** | **String** | Store Checkout Order URL for the given Order | [optional] 
**coupons** | **String** | Promotion Coupons used on the given Order | [optional] 
**createdAt** | **String** | Order date | [optional] 
**currency** | **String** | Currency of the Order | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**discount** | **Number** | Discount value for the given Order | [optional] 
**duplicateUrl** | **String** | Duplicate Order URL for the given Order | [optional] 
**externalShippingRateId** | **String** | Rate id for selected External Shipping Method rate | [optional] 
**id** | **Number** | Unique identifier of the Order | [optional] 
**paymentInformation** | **String** | Payment information for the given Order | [optional] 
**paymentMethodName** | **String** | Payment Method name used e.g. PayPal | [optional] 
**paymentMethodType** | **String** | Payment Method type used e.g. paypal | [optional] 
**products** | [**[OrderProduct]**](OrderProduct.md) |  | [optional] 
**recoveryUrl** | **String** | Recovery Order URL for the given Order | [optional] 
**shipmentStatus** | **String** | Shipment Status for Order Fulfillment. | [optional] 
**shipping** | **Number** | Shipping value for the given Order | [optional] 
**shippingAddress** | [**OrderShippingAddress**](OrderShippingAddress.md) |  | [optional] 
**shippingDiscount** | **Number** | Shipping Discount value for the given order | [optional] 
**shippingMethodId** | **Number** | Shipping method e.g. Royal Mail | [optional] 
**shippingMethodName** | **String** | Shipping method e.g. Royal Mail | [optional] 
**shippingOption** | **String** | Shipping option for this order. | [optional] 
**shippingRequired** | **Boolean** | False if the order is digital. | [optional] [default to true]
**shippingTax** | **Number** | Shipping Tax value for the given order | [optional] 
**shippingTaxes** | [**[OrderShippingTax]**](OrderShippingTax.md) |  | [optional] 
**source** | [**TrafficSource**](TrafficSource.md) |  | [optional] 
**status** | **String** | Status of the Order | [optional] 
**subtotal** | **Number** | Subtotal value for the given Order. Excluding taxes, shipping and discounts | [optional] 
**tax** | **Number** | Tax value for the given order | [optional] 
**total** | **Number** | Total value for the given Order. Including taxes, shipping and discounts | [optional] 
**trackingCompany** | **String** | Company Used for Order Fulfillment. | [optional] 
**trackingNumber** | **String** | Tracking Number for Order Fulfillment. | [optional] 
**trackingUrl** | **String** | Tracking URL for Order Fulfillment. | [optional] 



## Enum: ShipmentStatusEnum


* `delivered` (value: `"delivered"`)

* `requested` (value: `"requested"`)

* `in_transit` (value: `"in_transit"`)

* `failed` (value: `"failed"`)

* `pickup_available` (value: `"pickup_available"`)





## Enum: ShippingOptionEnum


* `delivery` (value: `"delivery"`)

* `store_pickup` (value: `"store_pickup"`)

* `no_shipping` (value: `"no_shipping"`)





## Enum: StatusEnum


* `Abandoned` (value: `"Abandoned"`)

* `Canceled` (value: `"Canceled"`)

* `Pending Payment` (value: `"Pending Payment"`)

* `Paid` (value: `"Paid"`)




