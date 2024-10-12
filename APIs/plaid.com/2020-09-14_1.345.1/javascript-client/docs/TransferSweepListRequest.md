# ThePlaidApi.TransferSweepListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**count** | **Number** | The maximum number of sweeps to return. | [optional] [default to 25]
**endDate** | **Date** | The end datetime of sweeps to return (RFC 3339 format). | [optional] 
**fundingAccountId** | **String** | Filter sweeps to only those with the specified &#x60;funding_account_id&#x60;. | [optional] 
**offset** | **Number** | The number of sweeps to skip before returning results. | [optional] [default to 0]
**originatorClientId** | **String** | Filter sweeps to only those with the specified originator client. | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**startDate** | **Date** | The start datetime of sweeps to return (RFC 3339 format). | [optional] 


