

# OrderFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalFields** | [**List&lt;OrderAdditionalFields&gt;**](OrderAdditionalFields.md) | Array of additional fields for the given Order |  [optional] |
|**additionalInformation** | **String** | Additional information for the given Order |  [optional] |
|**billingAddress** | [**OrderBillingAddress**](OrderBillingAddress.md) |  |  [optional] |
|**checkoutUrl** | **String** | Store Checkout Order URL for the given Order |  [optional] |
|**coupons** | **String** | Promotion Coupons used on the given Order |  [optional] |
|**createdAt** | **String** | Order date |  [optional] |
|**currency** | **String** | Currency of the Order |  [optional] |
|**customer** | [**Customer**](Customer.md) |  |  [optional] |
|**discount** | **Float** | Discount value for the given Order |  [optional] |
|**duplicateUrl** | **String** | Duplicate Order URL for the given Order |  [optional] |
|**externalShippingRateId** | **String** | Rate id for selected External Shipping Method rate |  [optional] |
|**id** | **Integer** | Unique identifier of the Order |  [optional] |
|**paymentInformation** | **String** | Payment information for the given Order |  [optional] |
|**paymentMethodName** | **String** | Payment Method name used e.g. PayPal |  [optional] |
|**paymentMethodType** | **String** | Payment Method type used e.g. paypal |  [optional] |
|**products** | [**List&lt;OrderProduct&gt;**](OrderProduct.md) |  |  [optional] |
|**recoveryUrl** | **String** | Recovery Order URL for the given Order |  [optional] |
|**shipmentStatus** | [**ShipmentStatusEnum**](#ShipmentStatusEnum) | Shipment Status for Order Fulfillment. |  [optional] |
|**shipping** | **Float** | Shipping value for the given Order |  [optional] |
|**shippingAddress** | [**OrderShippingAddress**](OrderShippingAddress.md) |  |  [optional] |
|**shippingDiscount** | **Float** | Shipping Discount value for the given order |  [optional] |
|**shippingMethodId** | **Integer** | Shipping method e.g. Royal Mail |  [optional] |
|**shippingMethodName** | **String** | Shipping method e.g. Royal Mail |  [optional] |
|**shippingOption** | [**ShippingOptionEnum**](#ShippingOptionEnum) | Shipping option for this order. |  [optional] |
|**shippingRequired** | **Boolean** | False if the order is digital. |  [optional] |
|**shippingTax** | **Float** | Shipping Tax value for the given order |  [optional] |
|**shippingTaxes** | [**List&lt;OrderShippingTax&gt;**](OrderShippingTax.md) |  |  [optional] |
|**source** | [**TrafficSource**](TrafficSource.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the Order |  [optional] |
|**subtotal** | **Float** | Subtotal value for the given Order. Excluding taxes, shipping and discounts |  [optional] |
|**tax** | **Float** | Tax value for the given order |  [optional] |
|**total** | **Float** | Total value for the given Order. Including taxes, shipping and discounts |  [optional] |
|**trackingCompany** | **String** | Company Used for Order Fulfillment. |  [optional] |
|**trackingNumber** | **String** | Tracking Number for Order Fulfillment. |  [optional] |
|**trackingUrl** | **String** | Tracking URL for Order Fulfillment. |  [optional] |



## Enum: ShipmentStatusEnum

| Name | Value |
|---- | -----|
| DELIVERED | &quot;delivered&quot; |
| REQUESTED | &quot;requested&quot; |
| IN_TRANSIT | &quot;in_transit&quot; |
| FAILED | &quot;failed&quot; |
| PICKUP_AVAILABLE | &quot;pickup_available&quot; |



## Enum: ShippingOptionEnum

| Name | Value |
|---- | -----|
| DELIVERY | &quot;delivery&quot; |
| STORE_PICKUP | &quot;store_pickup&quot; |
| NO_SHIPPING | &quot;no_shipping&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ABANDONED | &quot;Abandoned&quot; |
| CANCELED | &quot;Canceled&quot; |
| PENDING_PAYMENT | &quot;Pending Payment&quot; |
| PAID | &quot;Paid&quot; |



