

# OrderDetailsApiModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | Product short link |  [optional] |
|**afterPaymentDescription** | **String** | After payment description |  [optional] |
|**couponCode** | **String** | Coupon to apply in order to get the discount |  [optional] |
|**currency** | [**CurrencyDetailsApiModel**](CurrencyDetailsApiModel.md) |  |  [optional] |
|**currencyId** | **Integer** | Foreign key Currency |  [optional] |
|**description** | **String** | Product description |  [optional] |
|**discountAmount** | **Double** | Discount amount |  [optional] |
|**id** | **Integer** | Order id |  [optional] |
|**name** | **String** | Product alias |  [optional] |
|**note** | **String** | Customer note to seller |  [optional] |
|**orderBillingDetails** | [**OrderBillingDetailsApiModel**](OrderBillingDetailsApiModel.md) |  |  [optional] |
|**orderShippingDetails** | [**OrderShippingDetailsApiModel**](OrderShippingDetailsApiModel.md) |  |  [optional] |
|**productId** | **Integer** | Product id |  [optional] |
|**referral** | **String** | Represent the referral for this order |  [optional] |
|**shippingAmount** | **Double** | Cost for shipping the product |  [optional] |
|**shippingDescription** | **String** | Client instructions for shipping |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Order status |  [optional] |
|**subTotalAmount** | **Double** | Sub total amount |  [optional] |
|**taxAmount** | **Double** | Tax amount |  [optional] |
|**totalAmount** | **Double** | Total amount |  [optional] |
|**totalWithShipping** | **Double** | Total amount with shipping |  [optional] |
|**whatHappensNextDescription** | **String** | What happens next description |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING_PAYMENT | &quot;PendingPayment&quot; |
| PROCESSING | &quot;Processing&quot; |
| SHIPPED | &quot;Shipped&quot; |
| COMPLETED | &quot;Completed&quot; |
| ON_HOLD | &quot;OnHold&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| REFUNDED | &quot;Refunded&quot; |
| FAILED | &quot;Failed&quot; |



