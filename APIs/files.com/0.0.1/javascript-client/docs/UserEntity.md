# FilesComApi.UserEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active2fa** | **Boolean** | Is 2fa active for the user? | [optional] 
**adminGroupIds** | **[Number]** | List of group IDs of which this user is an administrator | [optional] 
**allowedIps** | **String** | A list of allowed IPs if applicable.  Newline delimited | [optional] 
**apiKeysCount** | **Number** | Number of api keys associated with this user | [optional] 
**attachmentsPermission** | **Boolean** | DEPRECATED: Can the user create Bundles (aka Share Links)? Use the bundle permission instead. | [optional] 
**authenticateUntil** | **Date** | Scheduled Date/Time at which user will be deactivated | [optional] 
**authenticationMethod** | **String** | How is this user authenticated? | [optional] 
**avatarUrl** | **String** | URL holding the user&#39;s avatar | [optional] 
**billingPermission** | **Boolean** | Allow this user to perform operations on the account, payments, and invoices? | [optional] 
**bypassInactiveDisable** | **Boolean** | Exempt this user from being disabled based on inactivity? | [optional] 
**bypassSiteAllowedIps** | **Boolean** | Allow this user to skip site-wide IP blacklists? | [optional] 
**company** | **String** | User&#39;s company | [optional] 
**createdAt** | **Date** | When this user was created | [optional] 
**davPermission** | **Boolean** | Can the user connect with WebDAV? | [optional] 
**daysRemainingUntilPasswordExpire** | **Number** | Number of days remaining until password expires | [optional] 
**disabled** | **Boolean** | Is user disabled? Disabled users cannot log in, and do not count for billing purposes.  Users can be automatically disabled after an inactivity period via a Site setting. | [optional] 
**email** | **String** | User email address | [optional] 
**externallyManaged** | **Boolean** | Is this user managed by a SsoStrategy? | [optional] 
**firstLoginAt** | **Date** | User&#39;s first login time | [optional] 
**ftpPermission** | **Boolean** | Can the user access with FTP/FTPS? | [optional] 
**groupIds** | **String** | Comma-separated list of group IDs of which this user is a member | [optional] 
**headerText** | **String** | Text to display to the user in the header of the UI | [optional] 
**id** | **Number** | User ID | [optional] 
**language** | **String** | Preferred language | [optional] 
**lastActiveAt** | **Date** | User&#39;s most recent activity time, which is the latest of most recent login, most recent API use, enablement, or creation | [optional] 
**lastApiUseAt** | **Date** | User&#39;s most recent API use time | [optional] 
**lastDavLoginAt** | **Date** | User&#39;s most recent login time via WebDAV | [optional] 
**lastDesktopLoginAt** | **Date** | User&#39;s most recent login time via Desktop app | [optional] 
**lastFtpLoginAt** | **Date** | User&#39;s most recent login time via FTP | [optional] 
**lastLoginAt** | **Date** | User&#39;s most recent login time via any protocol | [optional] 
**lastProtocolCipher** | **String** | The most recent protocol and cipher used | [optional] 
**lastRestapiLoginAt** | **Date** | User&#39;s most recent login time via Rest API | [optional] 
**lastSftpLoginAt** | **Date** | User&#39;s most recent login time via SFTP | [optional] 
**lastWebLoginAt** | **Date** | User&#39;s most recent login time via web | [optional] 
**lockoutExpires** | **Date** | Time in the future that the user will no longer be locked out if applicable | [optional] 
**name** | **String** | User&#39;s full name | [optional] 
**notes** | **String** | Any internal notes on the user | [optional] 
**notificationDailySendTime** | **Number** | Hour of the day at which daily notifications should be sent. Can be in range 0 to 23 | [optional] 
**officeIntegrationEnabled** | **Boolean** | Enable integration with Office for the web? | [optional] 
**passwordExpireAt** | **Date** | Password expiration datetime | [optional] 
**passwordExpired** | **Boolean** | Is user&#39;s password expired? | [optional] 
**passwordSetAt** | **Date** | Last time the user&#39;s password was set | [optional] 
**passwordValidityDays** | **Number** | Number of days to allow user to use the same password | [optional] 
**publicKeysCount** | **Number** | Number of public keys associated with this user | [optional] 
**receiveAdminAlerts** | **Boolean** | Should the user receive admin alerts such a certificate expiration notifications and overages? | [optional] 
**require2fa** | **String** | 2FA required setting | [optional] 
**requirePasswordChange** | **Boolean** | Is a password change required upon next user login? | [optional] 
**restapiPermission** | **Boolean** | Can this user access the REST API? | [optional] 
**selfManaged** | **Boolean** | Does this user manage it&#39;s own credentials or is it a shared/bot user? | [optional] 
**sftpPermission** | **Boolean** | Can the user access with SFTP? | [optional] 
**siteAdmin** | **Boolean** | Is the user an administrator for this site? | [optional] 
**skipWelcomeScreen** | **Boolean** | Skip Welcome page in the UI? | [optional] 
**sslRequired** | **String** | SSL required setting | [optional] 
**ssoStrategyId** | **Number** | SSO (Single Sign On) strategy ID for the user, if applicable. | [optional] 
**subscribeToNewsletter** | **Boolean** | Is the user subscribed to the newsletter? | [optional] 
**timeZone** | **String** | User time zone | [optional] 
**typeOf2fa** | **String** | Type(s) of 2FA methods in use.  Will be either &#x60;sms&#x60;, &#x60;totp&#x60;, &#x60;u2f&#x60;, &#x60;yubi&#x60;, or multiple values sorted alphabetically and joined by an underscore. | [optional] 
**userRoot** | **String** | Root folder for FTP (and optionally SFTP if the appropriate site-wide setting is set.)  Note that this is not used for API, Desktop, or Web interface. | [optional] 
**username** | **String** | User&#39;s username | [optional] 



## Enum: AuthenticationMethodEnum


* `password` (value: `"password"`)

* `unused_former_ldap` (value: `"unused_former_ldap"`)

* `sso` (value: `"sso"`)

* `none` (value: `"none"`)

* `email_signup` (value: `"email_signup"`)

* `password_with_imported_hash` (value: `"password_with_imported_hash"`)





## Enum: Require2faEnum


* `use_system_setting` (value: `"use_system_setting"`)

* `always_require` (value: `"always_require"`)

* `never_require` (value: `"never_require"`)





## Enum: SslRequiredEnum


* `use_system_setting` (value: `"use_system_setting"`)

* `always_require` (value: `"always_require"`)

* `never_require` (value: `"never_require"`)




