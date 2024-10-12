

# Profile

A Profile represents your User in our system. This is where you can change information about your User. This information is available to any OAuth Client regardless of requested scopes, and can be used to populate User information in third-party applications. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authenticationType** | [**AuthenticationTypeEnum**](#AuthenticationTypeEnum) | This account&#39;s Cloud Manager authentication type. Authentication types are chosen through Cloud Manager and authorized when logging into your account. These authentication types are either the user&#39;s password (in conjunction with their username), or the name of their indentity provider such as GitHub. For example, if a user:  - Has never used Third-Party Authentication, their authentication type will be &#x60;password&#x60;. - Is using Third-Party Authentication, their authentication type will be the name of their Identity Provider (eg. &#x60;github&#x60;). - Has used Third-Party Authentication and has since revoked it, their authentication type will be &#x60;password&#x60;.   **Note:** This functionality may not yet be available in Cloud Manager. See the [Cloud Manager Changelog](/changelog/cloud-manager/) for the latest updates.  |  [optional] [readonly] |
|**authorizedKeys** | **List&lt;String&gt;** | The list of SSH Keys authorized to use Lish for your User. This value is ignored if &#x60;lish_auth_method&#x60; is \&quot;disabled.\&quot;  |  [optional] |
|**email** | **String** | Your email address.  This address will be used for communication with Linode as necessary.  |  [optional] |
|**emailNotifications** | **Boolean** | If true, you will receive email notifications about account activity.  If false, you may still receive business-critical communications through email.  |  [optional] |
|**ipWhitelistEnabled** | **Boolean** | If true, logins for your User will only be allowed from whitelisted IPs. This setting is currently deprecated, and cannot be enabled.  If you disable this setting, you will not be able to re-enable it.  |  [optional] |
|**lishAuthMethod** | [**LishAuthMethodEnum**](#LishAuthMethodEnum) | The authentication methods that are allowed when connecting to [the Linode Shell (Lish)](/docs/guides/lish/). * &#x60;keys_only&#x60; is the most secure if you intend to use Lish. * &#x60;disabled&#x60; is recommended if you do not intend to use Lish at all. * If this account&#39;s Cloud Manager authentication type is set to a Third-Party Authentication method, &#x60;password_keys&#x60; cannot be used as your Lish authentication method. To view this account&#39;s Cloud Manager &#x60;authentication_type&#x60; field, send a request to the [View Profile](/docs/api/profile/#profile-view) endpoint.  |  [optional] |
|**referrals** | [**ProfileReferrals**](ProfileReferrals.md) |  |  [optional] |
|**restricted** | **Boolean** | If true, your User has restrictions on what can be accessed on your Account. To get details on what entities/actions you can access/perform, see [/profile/grants](/docs/api/profile/#grants-list).  |  [optional] |
|**timezone** | **String** | The timezone you prefer to see times in. This is not used by the API directly. It is provided for the benefit of clients such as the Linode Cloud Manager and other clients built on the API. All times returned by the API are in UTC.  |  [optional] |
|**twoFactorAuth** | **Boolean** | If true, logins from untrusted computers will require Two Factor Authentication.  See [/profile/tfa-enable](/docs/api/profile/#two-factor-secret-create) to enable Two Factor Authentication.  |  [optional] |
|**uid** | **Integer** | Your unique ID in our system. This value will never change, and can safely be used to identify your User.  |  [optional] [readonly] |
|**username** | **String** | Your username, used for logging in to our system.  |  [optional] [readonly] |
|**verifiedPhoneNumber** | **String** | The phone number verified for this Profile with the **Phone Number Verify** ([POST /profile/phone-number/verify](/docs/api/profile/#phone-number-verify)) command.  &#x60;null&#x60; if this Profile has no verified phone number.  |  [optional] [readonly] |



## Enum: AuthenticationTypeEnum

| Name | Value |
|---- | -----|
| PASSWORD | &quot;password&quot; |
| GITHUB | &quot;github&quot; |



## Enum: LishAuthMethodEnum

| Name | Value |
|---- | -----|
| PASSWORD_KEYS | &quot;password_keys&quot; |
| KEYS_ONLY | &quot;keys_only&quot; |
| DISABLED | &quot;disabled&quot; |



