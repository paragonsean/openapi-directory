# ThePlaidApi.TransactionsEnrichGetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountType** | **String** | The account type for the requested transactions (either &#x60;depository&#x60; or &#x60;credit&#x60;). | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**options** | [**TransactionsEnrichRequestOptions**](TransactionsEnrichRequestOptions.md) |  | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**transactions** | [**[ClientProvidedTransaction]**](ClientProvidedTransaction.md) | An array of transaction objects to be enriched by Plaid. Maximum of 100 transactions per request. | 


