# ThePlaidApi.TransferRecurringListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**count** | **Number** | The maximum number of recurring transfers to return. | [optional] [default to 25]
**endTime** | **Date** | The end datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 
**fundingAccountId** | **String** | Filter recurring transfers to only those with the specified &#x60;funding_account_id&#x60;. | [optional] 
**offset** | **Number** | The number of recurring transfers to skip before returning results. | [optional] [default to 0]
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**startTime** | **Date** | The start datetime of recurring transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 


