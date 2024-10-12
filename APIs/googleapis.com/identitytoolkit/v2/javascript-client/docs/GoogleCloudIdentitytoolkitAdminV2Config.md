# IdentityToolkitApi.GoogleCloudIdentitytoolkitAdminV2Config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizedDomains** | **[String]** | List of domains authorized for OAuth redirects | [optional] 
**autodeleteAnonymousUsers** | **Boolean** | Whether anonymous users will be auto-deleted after a period of 30 days. | [optional] 
**blockingFunctions** | [**GoogleCloudIdentitytoolkitAdminV2BlockingFunctionsConfig**](GoogleCloudIdentitytoolkitAdminV2BlockingFunctionsConfig.md) |  | [optional] 
**client** | [**GoogleCloudIdentitytoolkitAdminV2ClientConfig**](GoogleCloudIdentitytoolkitAdminV2ClientConfig.md) |  | [optional] 
**emailPrivacyConfig** | [**GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfig**](GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfig.md) |  | [optional] 
**mfa** | [**GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig**](GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig.md) |  | [optional] 
**monitoring** | [**GoogleCloudIdentitytoolkitAdminV2MonitoringConfig**](GoogleCloudIdentitytoolkitAdminV2MonitoringConfig.md) |  | [optional] 
**multiTenant** | [**GoogleCloudIdentitytoolkitAdminV2MultiTenantConfig**](GoogleCloudIdentitytoolkitAdminV2MultiTenantConfig.md) |  | [optional] 
**name** | **String** | Output only. The name of the Config resource. Example: \&quot;projects/my-awesome-project/config\&quot; | [optional] [readonly] 
**notification** | [**GoogleCloudIdentitytoolkitAdminV2NotificationConfig**](GoogleCloudIdentitytoolkitAdminV2NotificationConfig.md) |  | [optional] 
**passwordPolicyConfig** | [**GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig**](GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig.md) |  | [optional] 
**quota** | [**GoogleCloudIdentitytoolkitAdminV2QuotaConfig**](GoogleCloudIdentitytoolkitAdminV2QuotaConfig.md) |  | [optional] 
**recaptchaConfig** | [**GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig**](GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig.md) |  | [optional] 
**signIn** | [**GoogleCloudIdentitytoolkitAdminV2SignInConfig**](GoogleCloudIdentitytoolkitAdminV2SignInConfig.md) |  | [optional] 
**smsRegionConfig** | [**GoogleCloudIdentitytoolkitAdminV2SmsRegionConfig**](GoogleCloudIdentitytoolkitAdminV2SmsRegionConfig.md) |  | [optional] 
**subtype** | **String** | Output only. The subtype of this config. | [optional] [readonly] 



## Enum: SubtypeEnum


* `SUBTYPE_UNSPECIFIED` (value: `"SUBTYPE_UNSPECIFIED"`)

* `IDENTITY_PLATFORM` (value: `"IDENTITY_PLATFORM"`)

* `FIREBASE_AUTH` (value: `"FIREBASE_AUTH"`)




