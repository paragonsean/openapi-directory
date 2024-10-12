

# GoogleCloudIdentitytoolkitV2RecaptchaEnforcementState

Enforcement states for reCAPTCHA protection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enforcementState** | [**EnforcementStateEnum**](#EnforcementStateEnum) | The reCAPTCHA enforcement state for the provider. |  [optional] |
|**provider** | [**ProviderEnum**](#ProviderEnum) | The provider that has reCAPTCHA protection. |  [optional] |



## Enum: EnforcementStateEnum

| Name | Value |
|---- | -----|
| ENFORCEMENT_STATE_UNSPECIFIED | &quot;ENFORCEMENT_STATE_UNSPECIFIED&quot; |
| FALSE | &quot;false&quot; |
| AUDIT | &quot;AUDIT&quot; |
| ENFORCE | &quot;ENFORCE&quot; |



## Enum: ProviderEnum

| Name | Value |
|---- | -----|
| RECAPTCHA_PROVIDER_UNSPECIFIED | &quot;RECAPTCHA_PROVIDER_UNSPECIFIED&quot; |
| EMAIL_PASSWORD_PROVIDER | &quot;EMAIL_PASSWORD_PROVIDER&quot; |



