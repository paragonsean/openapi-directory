# GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartySignupNewUserRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captchaChallenge** | **String** | The captcha challenge. | [optional] 
**captchaResponse** | **String** | Response to the captcha. | [optional] 
**disabled** | **Boolean** | Whether to disable the user. Only can be used by service account. | [optional] 
**displayName** | **String** | The name of the user. | [optional] 
**email** | **String** | The email of the user. | [optional] 
**emailVerified** | **Boolean** | Mark the email as verified or not. Only can be used by service account. | [optional] 
**idToken** | **String** | The GITKit token of the authenticated user. | [optional] 
**instanceId** | **String** | Instance id token of the app. | [optional] 
**localId** | **String** | Privileged caller can create user with specified user id. | [optional] 
**password** | **String** | The new password of the user. | [optional] 
**phoneNumber** | **String** | Privileged caller can create user with specified phone number. | [optional] 
**photoUrl** | **String** | The photo url of the user. | [optional] 
**tenantId** | **String** | For multi-tenant use cases, in order to construct sign-in URL with the correct IDP parameters, Firebear needs to know which Tenant to retrieve IDP configs from. | [optional] 
**tenantProjectNumber** | **String** | Tenant project number to be used for idp discovery. | [optional] 


