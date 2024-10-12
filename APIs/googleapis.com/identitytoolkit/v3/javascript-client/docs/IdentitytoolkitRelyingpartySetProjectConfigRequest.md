# GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartySetProjectConfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowPasswordUser** | **Boolean** | Whether to allow password user sign in or sign up. | [optional] 
**apiKey** | **String** | Browser API key, needed when making http request to Apiary. | [optional] 
**authorizedDomains** | **[String]** | Authorized domains for widget redirect. | [optional] 
**changeEmailTemplate** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 
**delegatedProjectNumber** | **String** | GCP project number of the requesting delegated app. Currently only intended for Firebase V1 migration. | [optional] 
**enableAnonymousUser** | **Boolean** | Whether to enable anonymous user. | [optional] 
**idpConfig** | [**[IdpConfig]**](IdpConfig.md) | Oauth2 provider configuration. | [optional] 
**legacyResetPasswordTemplate** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 
**resetPasswordTemplate** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 
**useEmailSending** | **Boolean** | Whether to use email sending provided by Firebear. | [optional] 
**verifyEmailTemplate** | [**EmailTemplate**](EmailTemplate.md) |  | [optional] 


