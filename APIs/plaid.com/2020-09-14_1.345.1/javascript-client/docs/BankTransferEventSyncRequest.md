# ThePlaidApi.BankTransferEventSyncRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**afterId** | **Number** | The latest (largest) &#x60;event_id&#x60; fetched via the sync endpoint, or 0 initially. | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**count** | **Number** | The maximum number of bank transfer events to return. | [optional] [default to 25]
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 


