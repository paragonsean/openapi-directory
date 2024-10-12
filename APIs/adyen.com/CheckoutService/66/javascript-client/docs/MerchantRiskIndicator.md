# AdyenCheckoutApi.MerchantRiskIndicator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressMatch** | **Boolean** | Whether the chosen delivery address is identical to the billing address. | [optional] 
**deliveryAddressIndicator** | **String** | Indicator regarding the delivery address. Allowed values: * &#x60;shipToBillingAddress&#x60; * &#x60;shipToVerifiedAddress&#x60; * &#x60;shipToNewAddress&#x60; * &#x60;shipToStore&#x60; * &#x60;digitalGoods&#x60; * &#x60;goodsNotShipped&#x60; * &#x60;other&#x60; | [optional] 
**deliveryEmail** | **String** | The delivery email address (for digital goods). | [optional] 
**deliveryTimeframe** | **String** | The estimated delivery time for the shopper to receive the goods. Allowed values: * &#x60;electronicDelivery&#x60; * &#x60;sameDayShipping&#x60; * &#x60;overnightShipping&#x60; * &#x60;twoOrMoreDaysShipping&#x60; | [optional] 
**giftCardAmount** | [**Amount**](Amount.md) | For prepaid or gift card purchase, the purchase amount total of prepaid or gift card(s). | [optional] 
**giftCardCount** | **Number** | For prepaid or gift card purchase, total count of individual prepaid or gift cards/codes purchased. | [optional] 
**preOrderDate** | **Date** | For pre-order purchases, the expected date this product will be available to the shopper. | [optional] 
**preOrderPurchase** | **Boolean** | Indicator for whether this transaction is for pre-ordering a product. | [optional] 
**reorderItems** | **Boolean** | Indicator for whether the shopper has already purchased the same items in the past. | [optional] 



## Enum: DeliveryAddressIndicatorEnum


* `shipToBillingAddress` (value: `"shipToBillingAddress"`)

* `shipToVerifiedAddress` (value: `"shipToVerifiedAddress"`)

* `shipToNewAddress` (value: `"shipToNewAddress"`)

* `shipToStore` (value: `"shipToStore"`)

* `digitalGoods` (value: `"digitalGoods"`)

* `goodsNotShipped` (value: `"goodsNotShipped"`)

* `other` (value: `"other"`)





## Enum: DeliveryTimeframeEnum


* `electronicDelivery` (value: `"electronicDelivery"`)

* `sameDayShipping` (value: `"sameDayShipping"`)

* `overnightShipping` (value: `"overnightShipping"`)

* `twoOrMoreDaysShipping` (value: `"twoOrMoreDaysShipping"`)




