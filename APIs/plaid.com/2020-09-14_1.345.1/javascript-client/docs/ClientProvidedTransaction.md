# ThePlaidApi.ClientProvidedTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The absolute value of the transaction (&gt;&#x3D; 0). When testing Enrich, note that &#x60;amount&#x60; data should be realistic. Unrealistic or inaccurate &#x60;amount&#x60; data may result in reduced quality output. | 
**datePosted** | **Date** | The date the transaction posted, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. | [optional] 
**description** | **String** | The raw description of the transaction. If you have location data in available an unstructured format, it may be appended to the &#x60;description&#x60; field. | 
**direction** | [**EnrichTransactionDirection**](EnrichTransactionDirection.md) |  | 
**id** | **String** | A unique ID for the transaction used to help you tie data back to your systems. | 
**isoCurrencyCode** | **String** | The ISO-4217 currency code of the transaction e.g. USD. | 
**location** | [**ClientProvidedTransactionLocation**](ClientProvidedTransactionLocation.md) |  | [optional] 
**mcc** | **String** | Merchant category codes (MCCs) are four-digit numbers that describe a merchant&#39;s primary business activities. | [optional] 


