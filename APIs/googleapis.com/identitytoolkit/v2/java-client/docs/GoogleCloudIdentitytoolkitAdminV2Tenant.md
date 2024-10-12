

# GoogleCloudIdentitytoolkitAdminV2Tenant

A Tenant contains configuration for the tenant in a multi-tenant project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowPasswordSignup** | **Boolean** | Whether to allow email/password user authentication. |  [optional] |
|**autodeleteAnonymousUsers** | **Boolean** | Whether anonymous users will be auto-deleted after a period of 30 days. |  [optional] |
|**client** | [**GoogleCloudIdentitytoolkitAdminV2ClientPermissionConfig**](GoogleCloudIdentitytoolkitAdminV2ClientPermissionConfig.md) |  |  [optional] |
|**disableAuth** | **Boolean** | Whether authentication is disabled for the tenant. If true, the users under the disabled tenant are not allowed to sign-in. Admins of the disabled tenant are not able to manage its users. |  [optional] |
|**displayName** | **String** | Display name of the tenant. |  [optional] |
|**emailPrivacyConfig** | [**GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfig**](GoogleCloudIdentitytoolkitAdminV2EmailPrivacyConfig.md) |  |  [optional] |
|**enableAnonymousUser** | **Boolean** | Whether to enable anonymous user authentication. |  [optional] |
|**enableEmailLinkSignin** | **Boolean** | Whether to enable email link user authentication. |  [optional] |
|**hashConfig** | [**GoogleCloudIdentitytoolkitAdminV2HashConfig**](GoogleCloudIdentitytoolkitAdminV2HashConfig.md) |  |  [optional] |
|**inheritance** | [**GoogleCloudIdentitytoolkitAdminV2Inheritance**](GoogleCloudIdentitytoolkitAdminV2Inheritance.md) |  |  [optional] |
|**mfaConfig** | [**GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig**](GoogleCloudIdentitytoolkitAdminV2MultiFactorAuthConfig.md) |  |  [optional] |
|**monitoring** | [**GoogleCloudIdentitytoolkitAdminV2MonitoringConfig**](GoogleCloudIdentitytoolkitAdminV2MonitoringConfig.md) |  |  [optional] |
|**name** | **String** | Output only. Resource name of a tenant. For example: \&quot;projects/{project-id}/tenants/{tenant-id}\&quot; |  [optional] [readonly] |
|**passwordPolicyConfig** | [**GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig**](GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig.md) |  |  [optional] |
|**recaptchaConfig** | [**GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig**](GoogleCloudIdentitytoolkitAdminV2RecaptchaConfig.md) |  |  [optional] |
|**smsRegionConfig** | [**GoogleCloudIdentitytoolkitAdminV2SmsRegionConfig**](GoogleCloudIdentitytoolkitAdminV2SmsRegionConfig.md) |  |  [optional] |
|**testPhoneNumbers** | **Map&lt;String, String&gt;** | A map of pairs that can be used for MFA. The phone number should be in E.164 format (https://www.itu.int/rec/T-REC-E.164/) and a maximum of 10 pairs can be added (error will be thrown once exceeded). |  [optional] |



