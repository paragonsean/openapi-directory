# TelegramBotApi.Invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **String** | Three-letter ISO 4217 [currency](/bots/payments#supported-currencies) code | 
**description** | **String** | Product description | 
**startParameter** | **String** | Unique bot deep-linking parameter that can be used to generate this invoice | 
**title** | **String** | Product name | 
**totalAmount** | **Number** | Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of &#x60;US$ 1.45&#x60; pass &#x60;amount &#x3D; 145&#x60;. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). | 


