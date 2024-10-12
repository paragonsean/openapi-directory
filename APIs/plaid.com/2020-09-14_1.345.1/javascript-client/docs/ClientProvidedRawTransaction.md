# ThePlaidApi.ClientProvidedRawTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The value of the transaction with direction. (NOTE: this will affect enrichment results, so directions are important):.   Negative (-) for credits (e.g., incoming transfers, refunds)   Positive (+) for debits (e.g., purchases, fees, outgoing transfers) | 
**description** | **String** | The raw description of the transaction. | 
**id** | **String** | A unique ID for the transaction used to help you tie data back to your systems. | 
**isoCurrencyCode** | **String** | The ISO-4217 currency code of the transaction e.g. USD. | 


