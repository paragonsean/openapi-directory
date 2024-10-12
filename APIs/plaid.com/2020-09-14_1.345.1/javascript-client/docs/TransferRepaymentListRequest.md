# ThePlaidApi.TransferRepaymentListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**count** | **Number** | The maximum number of repayments to return. | [optional] [default to 25]
**endDate** | **Date** | The end datetime of repayments to return (RFC 3339 format). | [optional] 
**offset** | **Number** | The number of repayments to skip before returning results. | [optional] [default to 0]
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**startDate** | **Date** | The start datetime of repayments to return (RFC 3339 format). | [optional] 


