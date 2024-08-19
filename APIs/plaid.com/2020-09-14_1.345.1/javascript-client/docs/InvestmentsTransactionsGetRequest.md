# ThePlaidApi.InvestmentsTransactionsGetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The access token associated with the Item data is being requested for. | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**endDate** | **Date** | The most recent date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD. | 
**options** | [**InvestmentsTransactionsGetRequestOptions**](InvestmentsTransactionsGetRequestOptions.md) |  | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**startDate** | **Date** | The earliest date for which to fetch transaction history. Dates should be formatted as YYYY-MM-DD. | 


