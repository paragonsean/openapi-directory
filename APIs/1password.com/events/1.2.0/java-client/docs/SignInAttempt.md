

# SignInAttempt

A single sign-in attempt object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) |  |  [optional] |
|**client** | [**Client**](Client.md) |  |  [optional] |
|**country** | **String** | Country ISO Code |  [optional] |
|**details** | [**Details**](Details.md) |  |  [optional] |
|**location** | [**Location**](Location.md) |  |  [optional] |
|**sessionUuid** | **String** |  |  [optional] |
|**targetUser** | [**User**](User.md) |  |  [optional] |
|**timestamp** | **OffsetDateTime** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**uuid** | **String** |  |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| CREDENTIALS_FAILED | &quot;credentials_failed&quot; |
| MFA_FAILED | &quot;mfa_failed&quot; |
| SSO_FAILED | &quot;sso_failed&quot; |
| MODERN_VERSION_FAILED | &quot;modern_version_failed&quot; |
| FIREWALL_FAILED | &quot;firewall_failed&quot; |
| FIREWALL_REPORTED_SUCCESS | &quot;firewall_reported_success&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CREDENTIALS_OK | &quot;credentials_ok&quot; |
| MFA_OK | &quot;mfa_ok&quot; |
| PASSWORD_SECRET_BAD | &quot;password_secret_bad&quot; |
| MFA_MISSING | &quot;mfa_missing&quot; |
| TOTP_DISABLED | &quot;totp_disabled&quot; |
| TOTP_BAD | &quot;totp_bad&quot; |
| TOTP_TIMEOUT | &quot;totp_timeout&quot; |
| U2F_DISABLED | &quot;u2f_disabled&quot; |
| U2F_BAD | &quot;u2f_bad&quot; |
| U2F_TIMOUT | &quot;u2f_timout&quot; |
| DUO_DISABLED | &quot;duo_disabled&quot; |
| DUO_BAD | &quot;duo_bad&quot; |
| DUO_TIMEOUT | &quot;duo_timeout&quot; |
| DUO_NATIVE_BAD | &quot;duo_native_bad&quot; |
| SERVICE_ACCOUNT_SSO_DENIED | &quot;service_account_sso_denied&quot; |
| NON_SSO_USER | &quot;non_sso_user&quot; |
| SSO_USER_MISMATCH | &quot;sso_user_mismatch&quot; |
| PLATFORM_SECRET_DISABLED | &quot;platform_secret_disabled&quot; |
| PLATFORM_SECRET_BAD | &quot;platform_secret_bad&quot; |
| PLATFORM_SECRET_PROXY | &quot;platform_secret_proxy&quot; |
| CODE_DISABLED | &quot;code_disabled&quot; |
| CODE_BAD | &quot;code_bad&quot; |
| CODE_TIMEOUT | &quot;code_timeout&quot; |
| IP_BLOCKED | &quot;ip_blocked&quot; |
| CONTINENT_BLOCKED | &quot;continent_blocked&quot; |
| COUNTRY_BLOCKED | &quot;country_blocked&quot; |
| ANONYMOUS_BLOCKED | &quot;anonymous_blocked&quot; |
| ALL_BLOCKED | &quot;all_blocked&quot; |
| MODERN_VERSION_MISSING | &quot;modern_version_missing&quot; |
| MODERN_VERSION_OLD | &quot;modern_version_old&quot; |



