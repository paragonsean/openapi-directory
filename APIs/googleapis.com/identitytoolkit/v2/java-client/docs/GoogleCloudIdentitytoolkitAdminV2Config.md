

# GoogleCloudIdentitytoolkitAdminV2Config

Represents an Identity Toolkit project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizedDomains** | **List&lt;String&gt;** | List of domains authorized for OAuth redirects |  [optional] |
|**autodeleteAnonymousUsers** | **Boolean** | Whether anonymous users will be auto-deleted after a period of 30 days. |  [optional] |
|**blockingFunctions** | [**GoogleCloudIdentitytoolkitAdminV2BlockingFunctionsConfig**](GoogleCloudIdentitytoolkitAdminV2BlockingFunctionsConfig.md) |  |  [optional] |
|**client** | [**GoogleCloudIdentitytoolkitAdminV2ClientConfig**](GoogleCloudIdentitytoolkitAdminV2ClientConfig.md) |  |  [optional] |
|**emailPrivacyConfig** | [**GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfig**](GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfig.md) |  |  [optional] |
|**mfa** | [**GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig**](GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig.md) |  |  [optional] |
|**monitoring** | [**GoogleCloudIdentitytoolkitAdminV2MonitoringConfig**](GoogleCloudIdentitytoolkitAdminV2MonitoringConfig.md) |  |  [optional] |
|**multiTenant** | [**GoogleCloudIdentitytoolkitAdminV2MultiTenantConfig**](GoogleCloudIdentitytoolkitAdminV2MultiTenantConfig.md) |  |  [optional] |
|**name** | **String** | Output only. The name of the Config resource. Example: \&quot;projects/my-awesome-project/config\&quot; |  [optional] [readonly] |
|**notification** | [**GoogleCloudIdentitytoolkitAdminV2NotificationConfig**](GoogleCloudIdentitytoolkitAdminV2NotificationConfig.md) |  |  [optional] |
|**passwordPolicyConfig** | [**GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig**](GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig.md) |  |  [optional] |
|**quota** | [**GoogleCloudIdentitytoolkitAdminV2QuotaConfig**](GoogleCloudIdentitytoolkitAdminV2QuotaConfig.md) |  |  [optional] |
|**recaptchaConfig** | [**GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig**](GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig.md) |  |  [optional] |
|**signIn** | [**GoogleCloudIdentitytoolkitAdminV2SignInConfig**](GoogleCloudIdentitytoolkitAdminV2SignInConfig.md) |  |  [optional] |
|**smsRegionConfig** | [**GoogleCloudIdentitytoolkitAdminV2SmsRegionConfig**](GoogleCloudIdentitytoolkitAdminV2SmsRegionConfig.md) |  |  [optional] |
|**subtype** | [**SubtypeEnum**](#SubtypeEnum) | Output only. The subtype of this config. |  [optional] [readonly] |



## Enum: SubtypeEnum

| Name | Value |
|---- | -----|
| SUBTYPE_UNSPECIFIED | &quot;SUBTYPE_UNSPECIFIED&quot; |
| IDENTITY_PLATFORM | &quot;IDENTITY_PLATFORM&quot; |
| FIREBASE_AUTH | &quot;FIREBASE_AUTH&quot; |



