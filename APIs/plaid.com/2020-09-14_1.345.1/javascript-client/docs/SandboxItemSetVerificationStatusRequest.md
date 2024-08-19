# ThePlaidApi.SandboxItemSetVerificationStatusRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The access token associated with the Item data is being requested for. | 
**accountId** | **String** | The &#x60;account_id&#x60; of the account whose verification status is to be modified | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**verificationStatus** | **String** | The verification status to set the account to. | 



## Enum: VerificationStatusEnum


* `automatically_verified` (value: `"automatically_verified"`)

* `verification_expired` (value: `"verification_expired"`)




