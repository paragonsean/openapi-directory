# TelegramBotApi.PreCheckoutQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **String** | Three-letter ISO 4217 [currency](/bots/payments#supported-currencies) code | 
**from** | [**User**](User.md) |  | 
**id** | **String** | Unique query identifier | 
**invoicePayload** | **String** | Bot specified invoice payload | 
**orderInfo** | [**OrderInfo**](OrderInfo.md) |  | [optional] 
**shippingOptionId** | **String** | *Optional*. Identifier of the shipping option chosen by the user | [optional] 
**totalAmount** | **Number** | Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of &#x60;US$ 1.45&#x60; pass &#x60;amount &#x3D; 145&#x60;. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). | 


