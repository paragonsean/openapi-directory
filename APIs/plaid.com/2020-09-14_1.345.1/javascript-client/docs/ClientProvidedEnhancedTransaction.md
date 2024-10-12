# ThePlaidApi.ClientProvidedEnhancedTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The value of the transaction, denominated in the account&#39;s currency, as stated in &#x60;iso_currency_code&#x60;. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative. | 
**description** | **String** | The raw description of the transaction. | 
**enhancements** | [**Enhancements**](Enhancements.md) |  | 
**id** | **String** | Unique transaction identifier to tie transactions back to clients&#39; systems. | 
**isoCurrencyCode** | **String** | The ISO-4217 currency code of the transaction. | 


