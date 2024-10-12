

# PlaceOrderRequestPaymentData

Payment infomation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**giftCardMessages** | **List&lt;Object&gt;** | Array of gift card messages. |  [optional] |
|**giftCards** | [**List&lt;PlaceOrderRequestPaymentDataGiftCardsInner&gt;**](PlaceOrderRequestPaymentDataGiftCardsInner.md) | Gift card information, if it applies to the order. |  [optional] |
|**paymentSystems** | [**List&lt;PlaceOrderRequestPaymentDataPaymentSystemsInner&gt;**](PlaceOrderRequestPaymentDataPaymentSystemsInner.md) | Information on payment systems. |  [optional] |
|**payments** | [**List&lt;PlaceOrderRequestPaymentDataPaymentsInner&gt;**](PlaceOrderRequestPaymentDataPaymentsInner.md) | Payment information. |  |
|**updateStatus** | **String** | Indicates whether this object&#39;s information is up to date according to the order&#39;s items. An order can not be placed if &#x60;\&quot;outdated\&quot;&#x60; |  [optional] |



