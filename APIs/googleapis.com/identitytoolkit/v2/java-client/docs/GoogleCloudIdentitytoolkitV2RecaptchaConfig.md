

# GoogleCloudIdentitytoolkitV2RecaptchaConfig

Configuration for reCAPTCHA

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recaptchaEnforcementState** | [**List&lt;GoogleCloudIdentitytoolkitV2RecaptchaEnforcementState&gt;**](GoogleCloudIdentitytoolkitV2RecaptchaEnforcementState.md) | The reCAPTCHA enforcement state for the providers that GCIP supports reCAPTCHA protection. |  [optional] |
|**recaptchaKey** | **String** | The reCAPTCHA Enterprise key resource name, e.g. \&quot;projects/{project}/keys/{key}\&quot;. This will only be returned when the reCAPTCHA enforcement state is AUDIT or ENFORCE on at least one of the reCAPTCHA providers. |  [optional] |



