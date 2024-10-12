

# EcommerceOrder


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**EcommerceAddress**](EcommerceAddress.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**customer** | [**LinkedEcommerceCustomer**](LinkedEcommerceCustomer.md) |  |  [optional] |
|**discounts** | [**List&lt;EcommerceDiscount&gt;**](EcommerceDiscount.md) |  |  [optional] |
|**fulfillmentStatus** | [**FulfillmentStatusEnum**](#FulfillmentStatusEnum) | Current fulfillment status of the order. |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [readonly] |
|**lineItems** | [**List&lt;EcommerceOrderLineItem&gt;**](EcommerceOrderLineItem.md) |  |  [optional] |
|**note** | **String** | Note for the order. |  [optional] |
|**orderNumber** | **String** | Order number, if any. |  [optional] |
|**paymentMethod** | **String** | Payment method used for this order. |  [optional] |
|**paymentStatus** | [**PaymentStatusEnum**](#PaymentStatusEnum) | Current payment status of the order. |  [optional] |
|**shippingAddress** | [**EcommerceAddress**](EcommerceAddress.md) |  |  [optional] |
|**shippingCost** | **String** | Shipping cost, if any. |  [optional] |
|**status** | **EcommerceOrderStatus** |  |  [optional] |
|**subTotal** | **String** | Sub-total amount, normally before tax. |  [optional] |
|**totalAmount** | **String** | Total amount due. |  [optional] |
|**totalDiscount** | **String** | Total discount, if any. |  [optional] |
|**totalTax** | **String** | Total tax, if any. |  [optional] |
|**tracking** | [**List&lt;TrackingItem&gt;**](TrackingItem.md) |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |



## Enum: FulfillmentStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| SHIPPED | &quot;shipped&quot; |
| PARTIAL | &quot;partial&quot; |
| DELIVERED | &quot;delivered&quot; |
| CANCELLED | &quot;cancelled&quot; |
| RETURNED | &quot;returned&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: PaymentStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| AUTHORIZED | &quot;authorized&quot; |
| PAID | &quot;paid&quot; |
| PARTIAL | &quot;partial&quot; |
| REFUNDED | &quot;refunded&quot; |
| VOIDED | &quot;voided&quot; |
| UNKNOWN | &quot;unknown&quot; |



