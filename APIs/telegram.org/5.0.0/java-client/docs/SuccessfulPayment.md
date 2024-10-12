

# SuccessfulPayment

This object contains basic information about a successful payment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currency** | **String** | Three-letter ISO 4217 [currency](/bots/payments#supported-currencies) code |  |
|**invoicePayload** | **String** | Bot specified invoice payload |  |
|**orderInfo** | [**OrderInfo**](OrderInfo.md) |  |  [optional] |
|**providerPaymentChargeId** | **String** | Provider payment identifier |  |
|**shippingOptionId** | **String** | *Optional*. Identifier of the shipping option chosen by the user |  [optional] |
|**telegramPaymentChargeId** | **String** | Telegram payment identifier |  |
|**totalAmount** | **Integer** | Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of &#x60;US$ 1.45&#x60; pass &#x60;amount &#x3D; 145&#x60;. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). |  |



