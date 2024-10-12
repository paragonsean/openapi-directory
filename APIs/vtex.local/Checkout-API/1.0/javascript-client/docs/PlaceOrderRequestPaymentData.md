# CheckoutApi.PlaceOrderRequestPaymentData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**giftCardMessages** | **[Object]** | Array of gift card messages. | [optional] 
**giftCards** | [**[PlaceOrderRequestPaymentDataGiftCardsInner]**](PlaceOrderRequestPaymentDataGiftCardsInner.md) | Gift card information, if it applies to the order. | [optional] 
**paymentSystems** | [**[PlaceOrderRequestPaymentDataPaymentSystemsInner]**](PlaceOrderRequestPaymentDataPaymentSystemsInner.md) | Information on payment systems. | [optional] 
**payments** | [**[PlaceOrderRequestPaymentDataPaymentsInner]**](PlaceOrderRequestPaymentDataPaymentsInner.md) | Payment information. | 
**updateStatus** | **String** | Indicates whether this object&#39;s information is up to date according to the order&#39;s items. An order can not be placed if &#x60;\&quot;outdated\&quot;&#x60; | [optional] [default to &#39;updated&#39;]


