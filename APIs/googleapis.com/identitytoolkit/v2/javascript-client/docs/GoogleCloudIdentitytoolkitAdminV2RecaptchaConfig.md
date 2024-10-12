# IdentityToolkitApi.GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emailPasswordEnforcementState** | **String** | The reCAPTCHA config for email/password provider, containing the enforcement status. The email/password provider contains all related user flows protected by reCAPTCHA. | [optional] 
**managedRules** | [**[GoogleCloudIdentitytoolkitAdminV2RecaptchaManagedRule]**](GoogleCloudIdentitytoolkitAdminV2RecaptchaManagedRule.md) | The managed rules for authentication action based on reCAPTCHA scores. The rules are shared across providers for a given tenant project. | [optional] 
**recaptchaKeys** | [**[GoogleCloudIdentitytoolkitAdminV2RecaptchaKey]**](GoogleCloudIdentitytoolkitAdminV2RecaptchaKey.md) | Output only. The reCAPTCHA keys. | [optional] [readonly] 
**useAccountDefender** | **Boolean** | Whether to use the account defender for reCAPTCHA assessment. Defaults to &#x60;false&#x60;. | [optional] 



## Enum: EmailPasswordEnforcementStateEnum


* `RECAPTCHA_PROVIDER_ENFORCEMENT_STATE_UNSPECIFIED` (value: `"RECAPTCHA_PROVIDER_ENFORCEMENT_STATE_UNSPECIFIED"`)

* `false` (value: `"false"`)

* `AUDIT` (value: `"AUDIT"`)

* `ENFORCE` (value: `"ENFORCE"`)




