

# MerchantRiskIndicator


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressMatch** | **Boolean** | Whether the chosen delivery address is identical to the billing address. |  [optional] |
|**deliveryAddressIndicator** | [**DeliveryAddressIndicatorEnum**](#DeliveryAddressIndicatorEnum) | Indicator regarding the delivery address. Allowed values: * &#x60;shipToBillingAddress&#x60; * &#x60;shipToVerifiedAddress&#x60; * &#x60;shipToNewAddress&#x60; * &#x60;shipToStore&#x60; * &#x60;digitalGoods&#x60; * &#x60;goodsNotShipped&#x60; * &#x60;other&#x60; |  [optional] |
|**deliveryEmail** | **String** | The delivery email address (for digital goods). |  [optional] |
|**deliveryTimeframe** | [**DeliveryTimeframeEnum**](#DeliveryTimeframeEnum) | The estimated delivery time for the shopper to receive the goods. Allowed values: * &#x60;electronicDelivery&#x60; * &#x60;sameDayShipping&#x60; * &#x60;overnightShipping&#x60; * &#x60;twoOrMoreDaysShipping&#x60; |  [optional] |
|**giftCardAmount** | [**Amount**](Amount.md) | For prepaid or gift card purchase, the purchase amount total of prepaid or gift card(s). |  [optional] |
|**giftCardCount** | **Integer** | For prepaid or gift card purchase, total count of individual prepaid or gift cards/codes purchased. |  [optional] |
|**preOrderDate** | **OffsetDateTime** | For pre-order purchases, the expected date this product will be available to the shopper. |  [optional] |
|**preOrderPurchase** | **Boolean** | Indicator for whether this transaction is for pre-ordering a product. |  [optional] |
|**reorderItems** | **Boolean** | Indicator for whether the shopper has already purchased the same items in the past. |  [optional] |



## Enum: DeliveryAddressIndicatorEnum

| Name | Value |
|---- | -----|
| SHIP_TO_BILLING_ADDRESS | &quot;shipToBillingAddress&quot; |
| SHIP_TO_VERIFIED_ADDRESS | &quot;shipToVerifiedAddress&quot; |
| SHIP_TO_NEW_ADDRESS | &quot;shipToNewAddress&quot; |
| SHIP_TO_STORE | &quot;shipToStore&quot; |
| DIGITAL_GOODS | &quot;digitalGoods&quot; |
| GOODS_NOT_SHIPPED | &quot;goodsNotShipped&quot; |
| OTHER | &quot;other&quot; |



## Enum: DeliveryTimeframeEnum

| Name | Value |
|---- | -----|
| ELECTRONIC_DELIVERY | &quot;electronicDelivery&quot; |
| SAME_DAY_SHIPPING | &quot;sameDayShipping&quot; |
| OVERNIGHT_SHIPPING | &quot;overnightShipping&quot; |
| TWO_OR_MORE_DAYS_SHIPPING | &quot;twoOrMoreDaysShipping&quot; |



