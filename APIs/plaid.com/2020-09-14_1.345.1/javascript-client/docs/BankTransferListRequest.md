# ThePlaidApi.BankTransferListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**count** | **Number** | The maximum number of bank transfers to return. | [optional] [default to 25]
**direction** | [**BankTransferDirection**](BankTransferDirection.md) |  | [optional] 
**endDate** | **Date** | The end datetime of bank transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 
**offset** | **Number** | The number of bank transfers to skip before returning results. | [optional] [default to 0]
**originationAccountId** | **String** | Filter bank transfers to only those originated through the specified origination account. | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**startDate** | **Date** | The start datetime of bank transfers to list. This should be in RFC 3339 format (i.e. &#x60;2019-12-06T22:35:49Z&#x60;) | [optional] 


