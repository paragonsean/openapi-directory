# ThePlaidApi.TransactionsEnhanceGetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountType** | **String** | The type of account for the requested transactions (&#x60;depository&#x60; or &#x60;credit&#x60;). | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**transactions** | [**[ClientProvidedRawTransaction]**](ClientProvidedRawTransaction.md) | An array of raw transactions to be enhanced. | 


