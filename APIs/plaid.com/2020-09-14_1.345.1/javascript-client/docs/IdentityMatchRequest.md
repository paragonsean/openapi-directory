# ThePlaidApi.IdentityMatchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The access token associated with the Item data is being requested for. | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**identityVerificationId** | **String** | ID of the associated Identity Verification attempt. This field can be used instead of &#x60;user&#x60; to perform fuzzy match against the data collected during identity verification. | [optional] 
**options** | [**IdentityMatchRequestOptions**](IdentityMatchRequestOptions.md) |  | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**user** | [**IdentityMatchUser**](IdentityMatchUser.md) |  | [optional] 


