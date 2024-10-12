

# GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig

The reCAPTCHA Enterprise integration config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**emailPasswordEnforcementState** | [**EmailPasswordEnforcementStateEnum**](#EmailPasswordEnforcementStateEnum) | The reCAPTCHA config for email/password provider, containing the enforcement status. The email/password provider contains all related user flows protected by reCAPTCHA. |  [optional] |
|**managedRules** | [**List&lt;GoogleCloudIdentitytoolkitAdminV2RecaptchaManagedRule&gt;**](GoogleCloudIdentitytoolkitAdminV2RecaptchaManagedRule.md) | The managed rules for authentication action based on reCAPTCHA scores. The rules are shared across providers for a given tenant project. |  [optional] |
|**recaptchaKeys** | [**List&lt;GoogleCloudIdentitytoolkitAdminV2RecaptchaKey&gt;**](GoogleCloudIdentitytoolkitAdminV2RecaptchaKey.md) | Output only. The reCAPTCHA keys. |  [optional] [readonly] |
|**useAccountDefender** | **Boolean** | Whether to use the account defender for reCAPTCHA assessment. Defaults to &#x60;false&#x60;. |  [optional] |



## Enum: EmailPasswordEnforcementStateEnum

| Name | Value |
|---- | -----|
| RECAPTCHA_PROVIDER_ENFORCEMENT_STATE_UNSPECIFIED | &quot;RECAPTCHA_PROVIDER_ENFORCEMENT_STATE_UNSPECIFIED&quot; |
| FALSE | &quot;false&quot; |
| AUDIT | &quot;AUDIT&quot; |
| ENFORCE | &quot;ENFORCE&quot; |



