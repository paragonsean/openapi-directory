# ThePlaidApi.IdentityVerificationCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**gaveConsent** | **Boolean** | A flag specifying whether the end user has already agreed to a privacy policy specifying that their data will be shared with Plaid for verification purposes.  If &#x60;gave_consent&#x60; is set to &#x60;true&#x60;, the &#x60;accept_tos&#x60; step will be marked as &#x60;skipped&#x60; and the end user&#39;s session will start at the next step requirement. | [default to false]
**isIdempotent** | **Boolean** | An optional flag specifying how you would like Plaid to handle attempts to create an Identity Verification when an Identity Verification already exists for the provided &#x60;client_user_id&#x60; and &#x60;template_id&#x60;. If idempotency is enabled, Plaid will return the existing Identity Verification. If idempotency is disabled, Plaid will reject the request with a &#x60;400 Bad Request&#x60; status code if an Identity Verification already exists for the supplied &#x60;client_user_id&#x60; and &#x60;template_id&#x60;. | [optional] 
**isShareable** | **Boolean** | A flag specifying whether you would like Plaid to expose a shareable URL for the verification being created. | 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**templateId** | **String** | ID of the associated Identity Verification template. | 
**user** | [**IdentityVerificationRequestUser**](IdentityVerificationRequestUser.md) |  | 


