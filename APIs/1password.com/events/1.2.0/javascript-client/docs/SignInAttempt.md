# EventsApi.SignInAttempt

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** |  | [optional] 
**client** | [**Client**](Client.md) |  | [optional] 
**country** | **String** | Country ISO Code | [optional] 
**details** | [**Details**](Details.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**sessionUuid** | **String** |  | [optional] 
**targetUser** | [**User**](User.md) |  | [optional] 
**timestamp** | **Date** |  | [optional] 
**type** | **String** |  | [optional] 
**uuid** | **String** |  | [optional] 



## Enum: CategoryEnum


* `success` (value: `"success"`)

* `credentials_failed` (value: `"credentials_failed"`)

* `mfa_failed` (value: `"mfa_failed"`)

* `sso_failed` (value: `"sso_failed"`)

* `modern_version_failed` (value: `"modern_version_failed"`)

* `firewall_failed` (value: `"firewall_failed"`)

* `firewall_reported_success` (value: `"firewall_reported_success"`)





## Enum: TypeEnum


* `credentials_ok` (value: `"credentials_ok"`)

* `mfa_ok` (value: `"mfa_ok"`)

* `password_secret_bad` (value: `"password_secret_bad"`)

* `mfa_missing` (value: `"mfa_missing"`)

* `totp_disabled` (value: `"totp_disabled"`)

* `totp_bad` (value: `"totp_bad"`)

* `totp_timeout` (value: `"totp_timeout"`)

* `u2f_disabled` (value: `"u2f_disabled"`)

* `u2f_bad` (value: `"u2f_bad"`)

* `u2f_timout` (value: `"u2f_timout"`)

* `duo_disabled` (value: `"duo_disabled"`)

* `duo_bad` (value: `"duo_bad"`)

* `duo_timeout` (value: `"duo_timeout"`)

* `duo_native_bad` (value: `"duo_native_bad"`)

* `service_account_sso_denied` (value: `"service_account_sso_denied"`)

* `non_sso_user` (value: `"non_sso_user"`)

* `sso_user_mismatch` (value: `"sso_user_mismatch"`)

* `platform_secret_disabled` (value: `"platform_secret_disabled"`)

* `platform_secret_bad` (value: `"platform_secret_bad"`)

* `platform_secret_proxy` (value: `"platform_secret_proxy"`)

* `code_disabled` (value: `"code_disabled"`)

* `code_bad` (value: `"code_bad"`)

* `code_timeout` (value: `"code_timeout"`)

* `ip_blocked` (value: `"ip_blocked"`)

* `continent_blocked` (value: `"continent_blocked"`)

* `country_blocked` (value: `"country_blocked"`)

* `anonymous_blocked` (value: `"anonymous_blocked"`)

* `all_blocked` (value: `"all_blocked"`)

* `modern_version_missing` (value: `"modern_version_missing"`)

* `modern_version_old` (value: `"modern_version_old"`)




