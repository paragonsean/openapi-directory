# GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyGetProjectConfigResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowPasswordUser** | **Boolean** | Whether to allow password user sign in or sign up. | [optional] 
**apiKey** | **String** | Browser API key, needed when making http request to Apiary. | [optional] 
**authorizedDomains** | **[String]** | Authorized domains. | [optional] 
**changeEmailTemplate** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 
**dynamicLinksDomain** | **String** |  | [optional] 
**enableAnonymousUser** | **Boolean** | Whether anonymous user is enabled. | [optional] 
**idpConfig** | [**[IdpConfig]**](IdpConfig.md) | OAuth2 provider configuration. | [optional] 
**legacyResetPasswordTemplate** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 
**projectId** | **String** | Project ID of the relying party. | [optional] 
**resetPasswordTemplate** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 
**useEmailSending** | **Boolean** | Whether to use email sending provided by Firebear. | [optional] 
**verifyEmailTemplate** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 


