# ThePlaidApi.BankTransferSweepListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**count** | **Number** | The maximum number of sweeps to return. | [optional] [default to 25]
**endTime** | **Date** | The end datetime of sweeps to return (RFC 3339 format). | [optional] 
**originationAccountId** | **String** | If multiple origination accounts are available, &#x60;origination_account_id&#x60; must be used to specify the account that the sweeps belong to. | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**startTime** | **Date** | The start datetime of sweeps to return (RFC 3339 format). | [optional] 


