# FilesComApi.SiteApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSite**](SiteApi.md#getSite) | **GET** /site | Show site settings
[**getSiteApiKeys**](SiteApi.md#getSiteApiKeys) | **GET** /site/api_keys | List Api Keys
[**getSiteDnsRecords**](SiteApi.md#getSiteDnsRecords) | **GET** /site/dns_records | Show site DNS configuration.
[**getSiteIpAddresses**](SiteApi.md#getSiteIpAddresses) | **GET** /site/ip_addresses | List IP Addresses associated with the current site
[**getSiteUsage**](SiteApi.md#getSiteUsage) | **GET** /site/usage | Get the most recent usage snapshot (usage data for billing purposes) for a Site.
[**patchSite**](SiteApi.md#patchSite) | **PATCH** /site | Update site settings.
[**postSiteApiKeys**](SiteApi.md#postSiteApiKeys) | **POST** /site/api_keys | Create Api Key
[**postSiteTestWebhook**](SiteApi.md#postSiteTestWebhook) | **POST** /site/test-webhook | Test webhook.



## getSite

> SiteEntity getSite()

Show site settings

Show site settings

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SiteApi();
apiInstance.getSite((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SiteEntity**](SiteEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSiteApiKeys

> [ApiKeyEntity] getSiteApiKeys(opts)

List Api Keys

List Api Keys

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SiteApi();
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[expires_at]=desc`). Valid fields are `expires_at`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `expires_at`.
  'filterGt': {key: null}, // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `expires_at`.
  'filterGteq': {key: null}, // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `expires_at`.
  'filterLt': {key: null}, // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `expires_at`.
  'filterLteq': {key: null} // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `expires_at`.
};
apiInstance.getSiteApiKeys(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[expires_at]&#x3D;desc&#x60;). Valid fields are &#x60;expires_at&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] 
 **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] 
 **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] 
 **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] 
 **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] 

### Return type

[**[ApiKeyEntity]**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSiteDnsRecords

> [DnsRecordEntity] getSiteDnsRecords(opts)

Show site DNS configuration.

Show site DNS configuration.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SiteApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getSiteDnsRecords(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[DnsRecordEntity]**](DnsRecordEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSiteIpAddresses

> [IpAddressEntity] getSiteIpAddresses(opts)

List IP Addresses associated with the current site

List IP Addresses associated with the current site

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SiteApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getSiteIpAddresses(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[IpAddressEntity]**](IpAddressEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSiteUsage

> UsageSnapshotEntity getSiteUsage()

Get the most recent usage snapshot (usage data for billing purposes) for a Site.

Get the most recent usage snapshot (usage data for billing purposes) for a Site.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SiteApi();
apiInstance.getSiteUsage((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**UsageSnapshotEntity**](UsageSnapshotEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchSite

> SiteEntity patchSite(opts)

Update site settings.

Update site settings.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SiteApi();
let opts = {
  'activeSftpHostKeyId': 56, // Number | Id of the currently selected custom SFTP Host Key
  'allowBundleNames': true, // Boolean | Are manual Bundle names allowed?
  'allowed2faMethodBypassForFtpSftpDav': true, // Boolean | Are users allowed to configure their two factor authentication to be bypassed for FTP/SFTP/WebDAV?
  'allowed2faMethodSms': true, // Boolean | Is SMS two factor authentication allowed?
  'allowed2faMethodTotp': true, // Boolean | Is TOTP two factor authentication allowed?
  'allowed2faMethodU2f': true, // Boolean | Is U2F two factor authentication allowed?
  'allowed2faMethodWebauthn': true, // Boolean | Is WebAuthn two factor authentication allowed?
  'allowed2faMethodYubi': true, // Boolean | Is yubikey two factor authentication allowed?
  'allowedCountries': "allowedCountries_example", // String | Comma seperated list of allowed Country codes
  'allowedIps': "allowedIps_example", // String | List of allowed IP addresses
  'askAboutOverwrites': true, // Boolean | If false, rename conflicting files instead of asking for overwrite confirmation.  Only applies to web interface.
  'bundleActivityNotifications': "bundleActivityNotifications_example", // String | Do Bundle owners receive activity notifications?
  'bundleExpiration': 56, // Number | Site-wide Bundle expiration in days
  'bundlePasswordRequired': true, // Boolean | Do Bundles require password protection?
  'bundleRegistrationNotifications': "bundleRegistrationNotifications_example", // String | Do Bundle owners receive registration notification?
  'bundleRequireShareRecipient': true, // Boolean | Do Bundles require recipients for sharing?
  'bundleUploadReceiptNotifications': "bundleUploadReceiptNotifications_example", // String | Do Bundle uploaders receive upload confirmation notifications?
  'bundleWatermarkAttachmentDelete': true, // Boolean | If true, will delete the file stored in bundle_watermark_attachment
  'bundleWatermarkAttachmentFile': "/path/to/file", // File | 
  'bundleWatermarkValue': {key: null}, // Object | Preview watermark settings applied to all bundle items. Uses the same keys as Behavior.value
  'color2Left': "color2Left_example", // String | Page link and button color
  'color2Link': "color2Link_example", // String | Top bar link color
  'color2Text': "color2Text_example", // String | Page link and button color
  'color2Top': "color2Top_example", // String | Top bar background color
  'color2TopText': "color2TopText_example", // String | Top bar text color
  'customNamespace': true, // Boolean | Is this site using a custom namespace for users?
  'daysToRetainBackups': 56, // Number | Number of days to keep deleted files
  'defaultTimeZone': "defaultTimeZone_example", // String | Site default time zone
  'desktopApp': true, // Boolean | Is the desktop app enabled?
  'desktopAppSessionIpPinning': true, // Boolean | Is desktop app session IP pinning enabled?
  'desktopAppSessionLifetime': 56, // Number | Desktop app session lifetime (in hours)
  'disable2faWithDelay': true, // Boolean | If set to true, we will begin the process of disabling 2FA on this site.
  'disableFilesCertificateGeneration': true, // Boolean | If set, Files.com will not set the CAA records required to generate future SSL certificates for this domain.
  'disablePasswordReset': true, // Boolean | Is password reset disabled?
  'disableUsersFromInactivityPeriodDays': 56, // Number | If greater than zero, users will unable to login if they do not show activity within this number of days.
  'disallowedCountries': "disallowedCountries_example", // String | Comma seperated list of disallowed Country codes
  'domain': "domain_example", // String | Custom domain
  'domainHstsHeader': true, // Boolean | Send HSTS (HTTP Strict Transport Security) header when visitors access the site via a custom domain?
  'domainLetsencryptChain': "domainLetsencryptChain_example", // String | Letsencrypt chain to use when registering SSL Certificate for domain.
  'email': "email_example", // String | Main email for this site
  'folderPermissionsGroupsOnly': true, // Boolean | If true, permissions for this site must be bound to a group (not a user). Otherwise, permissions must be bound to a user.
  'ftpEnabled': true, // Boolean | Is FTP enabled?
  'icon128Delete': true, // Boolean | If true, will delete the file stored in icon128
  'icon128File': "/path/to/file", // File | 
  'icon16Delete': true, // Boolean | If true, will delete the file stored in icon16
  'icon16File': "/path/to/file", // File | 
  'icon32Delete': true, // Boolean | If true, will delete the file stored in icon32
  'icon32File': "/path/to/file", // File | 
  'icon48Delete': true, // Boolean | If true, will delete the file stored in icon48
  'icon48File': "/path/to/file", // File | 
  'immutableFiles': true, // Boolean | Are files protected from modification?
  'includePasswordInWelcomeEmail': true, // Boolean | Include password in emails to new users?
  'language': "language_example", // String | Site default language
  'ldapBaseDn': "ldapBaseDn_example", // String | Base DN for looking up users in LDAP server
  'ldapDomain': "ldapDomain_example", // String | Domain name that will be appended to usernames
  'ldapEnabled': true, // Boolean | Main LDAP setting: is LDAP enabled?
  'ldapGroupAction': "ldapGroupAction_example", // String | Should we sync groups from LDAP server?
  'ldapGroupExclusion': "ldapGroupExclusion_example", // String | Comma or newline separated list of group names (with optional wildcards) to exclude when syncing.
  'ldapGroupInclusion': "ldapGroupInclusion_example", // String | Comma or newline separated list of group names (with optional wildcards) to include when syncing.
  'ldapHost': "ldapHost_example", // String | LDAP host
  'ldapHost2': "ldapHost2_example", // String | LDAP backup host
  'ldapHost3': "ldapHost3_example", // String | LDAP backup host
  'ldapPasswordChange': "ldapPasswordChange_example", // String | New LDAP password.
  'ldapPasswordChangeConfirmation': "ldapPasswordChangeConfirmation_example", // String | Confirm new LDAP password.
  'ldapPort': 56, // Number | LDAP port
  'ldapSecure': true, // Boolean | Use secure LDAP?
  'ldapType': "ldapType_example", // String | LDAP type
  'ldapUserAction': "ldapUserAction_example", // String | Should we sync users from LDAP server?
  'ldapUserIncludeGroups': "ldapUserIncludeGroups_example", // String | Comma or newline separated list of group names (with optional wildcards) - if provided, only users in these groups will be added or synced.
  'ldapUsername': "ldapUsername_example", // String | Username for signing in to LDAP server.
  'ldapUsernameField': "ldapUsernameField_example", // String | LDAP username field
  'loginHelpText': "loginHelpText_example", // String | Login help text
  'logoDelete': true, // Boolean | If true, will delete the file stored in logo
  'logoFile': "/path/to/file", // File | 
  'maxPriorPasswords': 56, // Number | Number of prior passwords to disallow
  'mobileApp': true, // Boolean | Is the mobile app enabled?
  'mobileAppSessionIpPinning': true, // Boolean | Is mobile app session IP pinning enabled?
  'mobileAppSessionLifetime': 56, // Number | Mobile app session lifetime (in hours)
  'motdText': "motdText_example", // String | A message to show users when they connect via FTP or SFTP.
  'motdUseForFtp': true, // Boolean | Show message to users connecting via FTP
  'motdUseForSftp': true, // Boolean | Show message to users connecting via SFTP
  'name': "name_example", // String | Site name
  'nonSsoGroupsAllowed': true, // Boolean | If true, groups can be manually created / modified / deleted by Site Admins. Otherwise, groups can only be managed via your SSO provider.
  'nonSsoUsersAllowed': true, // Boolean | If true, users can be manually created / modified / deleted by Site Admins. Otherwise, users can only be managed via your SSO provider.
  'officeIntegrationAvailable': true, // Boolean | Allow users to use Office for the web?
  'officeIntegrationType': "officeIntegrationType_example", // String | Office integration application used to edit and view the MS Office documents
  'optOutGlobal': true, // Boolean | Use servers in the USA only?
  'passwordMinLength': 56, // Number | Shortest password length for users
  'passwordRequireLetter': true, // Boolean | Require a letter in passwords?
  'passwordRequireMixed': true, // Boolean | Require lower and upper case letters in passwords?
  'passwordRequireNumber': true, // Boolean | Require a number in passwords?
  'passwordRequireSpecial': true, // Boolean | Require special characters in password?
  'passwordRequireUnbreached': true, // Boolean | Require passwords that have not been previously breached? (see https://haveibeenpwned.com/)
  'passwordRequirementsApplyToBundles': true, // Boolean | Require bundles' passwords, and passwords for other items (inboxes, public shares, etc.) to conform to the same requirements as users' passwords?
  'passwordValidityDays': 56, // Number | Number of days password is valid
  'pinAllRemoteServersToSiteRegion': true, // Boolean | If true, we will ensure that all internal communications with any remote server are made through the primary region of the site. This setting overrides individual remote server settings.
  'replyToEmail': "replyToEmail_example", // String | Reply-to email for this site
  'require2fa': true, // Boolean | Require two-factor authentication for all users?
  'require2faUserType': "require2faUserType_example", // String | What type of user is required to use two-factor authentication (when require_2fa is set to `true` for this site)?
  'sessionExpiry': 3.4, // Number | Session expiry in hours
  'sessionExpiryMinutes': 56, // Number | Session expiry in minutes
  'sessionPinnedByIp': true, // Boolean | Are sessions locked to the same IP? (i.e. do users need to log in again if they change IPs?)
  'sftpEnabled': true, // Boolean | Is SFTP enabled?
  'sftpHostKeyType': "sftpHostKeyType_example", // String | Sftp Host Key Type
  'sftpInsecureCiphers': true, // Boolean | Are Insecure Ciphers allowed for SFTP?  Note:  Settting TLS Disabled -> True will always allow insecure ciphers for SFTP as well.  Enabling this is insecure.
  'sftpUserRootEnabled': true, // Boolean | Use user FTP roots also for SFTP?
  'sharingEnabled': true, // Boolean | Allow bundle creation
  'showRequestAccessLink': true, // Boolean | Show request access link for users without access?  Currently unused.
  'siteFooter': "siteFooter_example", // String | Custom site footer text
  'siteHeader': "siteHeader_example", // String | Custom site header text
  'smtpAddress': "smtpAddress_example", // String | SMTP server hostname or IP
  'smtpAuthentication': "smtpAuthentication_example", // String | SMTP server authentication type
  'smtpFrom': "smtpFrom_example", // String | From address to use when mailing through custom SMTP
  'smtpPassword': "smtpPassword_example", // String | Password for SMTP server.
  'smtpPort': 56, // Number | SMTP server port
  'smtpUsername': "smtpUsername_example", // String | SMTP server username
  'sslRequired': true, // Boolean | Is SSL required?  Disabling this is insecure.
  'subdomain': "subdomain_example", // String | Site subdomain
  'tlsDisabled': true, // Boolean | Are Insecure TLS and SFTP Ciphers allowed?  Enabling this is insecure.
  'uploadsViaEmailAuthentication': true, // Boolean | Do incoming emails in the Inboxes require checking for SPF/DKIM/DMARC?
  'useProvidedModifiedAt': true, // Boolean | Allow uploaders to set `provided_modified_at` for uploaded files?
  'userLockout': true, // Boolean | Will users be locked out after incorrect login attempts?
  'userLockoutLockPeriod': 56, // Number | How many hours to lock user out for failed password?
  'userLockoutTries': 56, // Number | Number of login tries within `user_lockout_within` hours before users are locked out
  'userLockoutWithin': 56, // Number | Number of hours for user lockout window
  'userRequestsEnabled': true, // Boolean | Enable User Requests feature
  'userRequestsNotifyAdmins': true, // Boolean | Send email to site admins when a user request is received?
  'welcomeCustomText': "welcomeCustomText_example", // String | Custom text send in user welcome email
  'welcomeEmailCc': "welcomeEmailCc_example", // String | Include this email in welcome emails if enabled
  'welcomeEmailEnabled': true, // Boolean | Will the welcome email be sent to new users?
  'welcomeEmailSubject': "welcomeEmailSubject_example", // String | Include this email subject in welcome emails if enabled
  'welcomeScreen': "welcomeScreen_example", // String | Does the welcome screen appear?
  'windowsModeFtp': true // Boolean | Does FTP user Windows emulation mode?
};
apiInstance.patchSite(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activeSftpHostKeyId** | **Number**| Id of the currently selected custom SFTP Host Key | [optional] 
 **allowBundleNames** | **Boolean**| Are manual Bundle names allowed? | [optional] 
 **allowed2faMethodBypassForFtpSftpDav** | **Boolean**| Are users allowed to configure their two factor authentication to be bypassed for FTP/SFTP/WebDAV? | [optional] 
 **allowed2faMethodSms** | **Boolean**| Is SMS two factor authentication allowed? | [optional] 
 **allowed2faMethodTotp** | **Boolean**| Is TOTP two factor authentication allowed? | [optional] 
 **allowed2faMethodU2f** | **Boolean**| Is U2F two factor authentication allowed? | [optional] 
 **allowed2faMethodWebauthn** | **Boolean**| Is WebAuthn two factor authentication allowed? | [optional] 
 **allowed2faMethodYubi** | **Boolean**| Is yubikey two factor authentication allowed? | [optional] 
 **allowedCountries** | **String**| Comma seperated list of allowed Country codes | [optional] 
 **allowedIps** | **String**| List of allowed IP addresses | [optional] 
 **askAboutOverwrites** | **Boolean**| If false, rename conflicting files instead of asking for overwrite confirmation.  Only applies to web interface. | [optional] 
 **bundleActivityNotifications** | **String**| Do Bundle owners receive activity notifications? | [optional] 
 **bundleExpiration** | **Number**| Site-wide Bundle expiration in days | [optional] 
 **bundlePasswordRequired** | **Boolean**| Do Bundles require password protection? | [optional] 
 **bundleRegistrationNotifications** | **String**| Do Bundle owners receive registration notification? | [optional] 
 **bundleRequireShareRecipient** | **Boolean**| Do Bundles require recipients for sharing? | [optional] 
 **bundleUploadReceiptNotifications** | **String**| Do Bundle uploaders receive upload confirmation notifications? | [optional] 
 **bundleWatermarkAttachmentDelete** | **Boolean**| If true, will delete the file stored in bundle_watermark_attachment | [optional] 
 **bundleWatermarkAttachmentFile** | **File**|  | [optional] 
 **bundleWatermarkValue** | [**Object**](Object.md)| Preview watermark settings applied to all bundle items. Uses the same keys as Behavior.value | [optional] 
 **color2Left** | **String**| Page link and button color | [optional] 
 **color2Link** | **String**| Top bar link color | [optional] 
 **color2Text** | **String**| Page link and button color | [optional] 
 **color2Top** | **String**| Top bar background color | [optional] 
 **color2TopText** | **String**| Top bar text color | [optional] 
 **customNamespace** | **Boolean**| Is this site using a custom namespace for users? | [optional] 
 **daysToRetainBackups** | **Number**| Number of days to keep deleted files | [optional] 
 **defaultTimeZone** | **String**| Site default time zone | [optional] 
 **desktopApp** | **Boolean**| Is the desktop app enabled? | [optional] 
 **desktopAppSessionIpPinning** | **Boolean**| Is desktop app session IP pinning enabled? | [optional] 
 **desktopAppSessionLifetime** | **Number**| Desktop app session lifetime (in hours) | [optional] 
 **disable2faWithDelay** | **Boolean**| If set to true, we will begin the process of disabling 2FA on this site. | [optional] 
 **disableFilesCertificateGeneration** | **Boolean**| If set, Files.com will not set the CAA records required to generate future SSL certificates for this domain. | [optional] 
 **disablePasswordReset** | **Boolean**| Is password reset disabled? | [optional] 
 **disableUsersFromInactivityPeriodDays** | **Number**| If greater than zero, users will unable to login if they do not show activity within this number of days. | [optional] 
 **disallowedCountries** | **String**| Comma seperated list of disallowed Country codes | [optional] 
 **domain** | **String**| Custom domain | [optional] 
 **domainHstsHeader** | **Boolean**| Send HSTS (HTTP Strict Transport Security) header when visitors access the site via a custom domain? | [optional] 
 **domainLetsencryptChain** | **String**| Letsencrypt chain to use when registering SSL Certificate for domain. | [optional] 
 **email** | **String**| Main email for this site | [optional] 
 **folderPermissionsGroupsOnly** | **Boolean**| If true, permissions for this site must be bound to a group (not a user). Otherwise, permissions must be bound to a user. | [optional] 
 **ftpEnabled** | **Boolean**| Is FTP enabled? | [optional] 
 **icon128Delete** | **Boolean**| If true, will delete the file stored in icon128 | [optional] 
 **icon128File** | **File**|  | [optional] 
 **icon16Delete** | **Boolean**| If true, will delete the file stored in icon16 | [optional] 
 **icon16File** | **File**|  | [optional] 
 **icon32Delete** | **Boolean**| If true, will delete the file stored in icon32 | [optional] 
 **icon32File** | **File**|  | [optional] 
 **icon48Delete** | **Boolean**| If true, will delete the file stored in icon48 | [optional] 
 **icon48File** | **File**|  | [optional] 
 **immutableFiles** | **Boolean**| Are files protected from modification? | [optional] 
 **includePasswordInWelcomeEmail** | **Boolean**| Include password in emails to new users? | [optional] 
 **language** | **String**| Site default language | [optional] 
 **ldapBaseDn** | **String**| Base DN for looking up users in LDAP server | [optional] 
 **ldapDomain** | **String**| Domain name that will be appended to usernames | [optional] 
 **ldapEnabled** | **Boolean**| Main LDAP setting: is LDAP enabled? | [optional] 
 **ldapGroupAction** | **String**| Should we sync groups from LDAP server? | [optional] 
 **ldapGroupExclusion** | **String**| Comma or newline separated list of group names (with optional wildcards) to exclude when syncing. | [optional] 
 **ldapGroupInclusion** | **String**| Comma or newline separated list of group names (with optional wildcards) to include when syncing. | [optional] 
 **ldapHost** | **String**| LDAP host | [optional] 
 **ldapHost2** | **String**| LDAP backup host | [optional] 
 **ldapHost3** | **String**| LDAP backup host | [optional] 
 **ldapPasswordChange** | **String**| New LDAP password. | [optional] 
 **ldapPasswordChangeConfirmation** | **String**| Confirm new LDAP password. | [optional] 
 **ldapPort** | **Number**| LDAP port | [optional] 
 **ldapSecure** | **Boolean**| Use secure LDAP? | [optional] 
 **ldapType** | **String**| LDAP type | [optional] 
 **ldapUserAction** | **String**| Should we sync users from LDAP server? | [optional] 
 **ldapUserIncludeGroups** | **String**| Comma or newline separated list of group names (with optional wildcards) - if provided, only users in these groups will be added or synced. | [optional] 
 **ldapUsername** | **String**| Username for signing in to LDAP server. | [optional] 
 **ldapUsernameField** | **String**| LDAP username field | [optional] 
 **loginHelpText** | **String**| Login help text | [optional] 
 **logoDelete** | **Boolean**| If true, will delete the file stored in logo | [optional] 
 **logoFile** | **File**|  | [optional] 
 **maxPriorPasswords** | **Number**| Number of prior passwords to disallow | [optional] 
 **mobileApp** | **Boolean**| Is the mobile app enabled? | [optional] 
 **mobileAppSessionIpPinning** | **Boolean**| Is mobile app session IP pinning enabled? | [optional] 
 **mobileAppSessionLifetime** | **Number**| Mobile app session lifetime (in hours) | [optional] 
 **motdText** | **String**| A message to show users when they connect via FTP or SFTP. | [optional] 
 **motdUseForFtp** | **Boolean**| Show message to users connecting via FTP | [optional] 
 **motdUseForSftp** | **Boolean**| Show message to users connecting via SFTP | [optional] 
 **name** | **String**| Site name | [optional] 
 **nonSsoGroupsAllowed** | **Boolean**| If true, groups can be manually created / modified / deleted by Site Admins. Otherwise, groups can only be managed via your SSO provider. | [optional] 
 **nonSsoUsersAllowed** | **Boolean**| If true, users can be manually created / modified / deleted by Site Admins. Otherwise, users can only be managed via your SSO provider. | [optional] 
 **officeIntegrationAvailable** | **Boolean**| Allow users to use Office for the web? | [optional] 
 **officeIntegrationType** | **String**| Office integration application used to edit and view the MS Office documents | [optional] 
 **optOutGlobal** | **Boolean**| Use servers in the USA only? | [optional] 
 **passwordMinLength** | **Number**| Shortest password length for users | [optional] 
 **passwordRequireLetter** | **Boolean**| Require a letter in passwords? | [optional] 
 **passwordRequireMixed** | **Boolean**| Require lower and upper case letters in passwords? | [optional] 
 **passwordRequireNumber** | **Boolean**| Require a number in passwords? | [optional] 
 **passwordRequireSpecial** | **Boolean**| Require special characters in password? | [optional] 
 **passwordRequireUnbreached** | **Boolean**| Require passwords that have not been previously breached? (see https://haveibeenpwned.com/) | [optional] 
 **passwordRequirementsApplyToBundles** | **Boolean**| Require bundles&#39; passwords, and passwords for other items (inboxes, public shares, etc.) to conform to the same requirements as users&#39; passwords? | [optional] 
 **passwordValidityDays** | **Number**| Number of days password is valid | [optional] 
 **pinAllRemoteServersToSiteRegion** | **Boolean**| If true, we will ensure that all internal communications with any remote server are made through the primary region of the site. This setting overrides individual remote server settings. | [optional] 
 **replyToEmail** | **String**| Reply-to email for this site | [optional] 
 **require2fa** | **Boolean**| Require two-factor authentication for all users? | [optional] 
 **require2faUserType** | **String**| What type of user is required to use two-factor authentication (when require_2fa is set to &#x60;true&#x60; for this site)? | [optional] 
 **sessionExpiry** | **Number**| Session expiry in hours | [optional] 
 **sessionExpiryMinutes** | **Number**| Session expiry in minutes | [optional] 
 **sessionPinnedByIp** | **Boolean**| Are sessions locked to the same IP? (i.e. do users need to log in again if they change IPs?) | [optional] 
 **sftpEnabled** | **Boolean**| Is SFTP enabled? | [optional] 
 **sftpHostKeyType** | **String**| Sftp Host Key Type | [optional] 
 **sftpInsecureCiphers** | **Boolean**| Are Insecure Ciphers allowed for SFTP?  Note:  Settting TLS Disabled -&gt; True will always allow insecure ciphers for SFTP as well.  Enabling this is insecure. | [optional] 
 **sftpUserRootEnabled** | **Boolean**| Use user FTP roots also for SFTP? | [optional] 
 **sharingEnabled** | **Boolean**| Allow bundle creation | [optional] 
 **showRequestAccessLink** | **Boolean**| Show request access link for users without access?  Currently unused. | [optional] 
 **siteFooter** | **String**| Custom site footer text | [optional] 
 **siteHeader** | **String**| Custom site header text | [optional] 
 **smtpAddress** | **String**| SMTP server hostname or IP | [optional] 
 **smtpAuthentication** | **String**| SMTP server authentication type | [optional] 
 **smtpFrom** | **String**| From address to use when mailing through custom SMTP | [optional] 
 **smtpPassword** | **String**| Password for SMTP server. | [optional] 
 **smtpPort** | **Number**| SMTP server port | [optional] 
 **smtpUsername** | **String**| SMTP server username | [optional] 
 **sslRequired** | **Boolean**| Is SSL required?  Disabling this is insecure. | [optional] 
 **subdomain** | **String**| Site subdomain | [optional] 
 **tlsDisabled** | **Boolean**| Are Insecure TLS and SFTP Ciphers allowed?  Enabling this is insecure. | [optional] 
 **uploadsViaEmailAuthentication** | **Boolean**| Do incoming emails in the Inboxes require checking for SPF/DKIM/DMARC? | [optional] 
 **useProvidedModifiedAt** | **Boolean**| Allow uploaders to set &#x60;provided_modified_at&#x60; for uploaded files? | [optional] 
 **userLockout** | **Boolean**| Will users be locked out after incorrect login attempts? | [optional] 
 **userLockoutLockPeriod** | **Number**| How many hours to lock user out for failed password? | [optional] 
 **userLockoutTries** | **Number**| Number of login tries within &#x60;user_lockout_within&#x60; hours before users are locked out | [optional] 
 **userLockoutWithin** | **Number**| Number of hours for user lockout window | [optional] 
 **userRequestsEnabled** | **Boolean**| Enable User Requests feature | [optional] 
 **userRequestsNotifyAdmins** | **Boolean**| Send email to site admins when a user request is received? | [optional] 
 **welcomeCustomText** | **String**| Custom text send in user welcome email | [optional] 
 **welcomeEmailCc** | **String**| Include this email in welcome emails if enabled | [optional] 
 **welcomeEmailEnabled** | **Boolean**| Will the welcome email be sent to new users? | [optional] 
 **welcomeEmailSubject** | **String**| Include this email subject in welcome emails if enabled | [optional] 
 **welcomeScreen** | **String**| Does the welcome screen appear? | [optional] 
 **windowsModeFtp** | **Boolean**| Does FTP user Windows emulation mode? | [optional] 

### Return type

[**SiteEntity**](SiteEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postSiteApiKeys

> ApiKeyEntity postSiteApiKeys(opts)

Create Api Key

Create Api Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SiteApi();
let opts = {
  'description': "description_example", // String | User-supplied description of API key.
  'expiresAt': new Date("2013-10-20T19:20:30+01:00"), // Date | API Key expiration date
  'name': "name_example", // String | Internal name for the API Key.  For your use.
  'path': "path_example", // String | Folder path restriction for this api key.
  'permissionSet': "'full'", // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postSiteApiKeys(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **String**| User-supplied description of API key. | [optional] 
 **expiresAt** | **Date**| API Key expiration date | [optional] 
 **name** | **String**| Internal name for the API Key.  For your use. | [optional] 
 **path** | **String**| Folder path restriction for this api key. | [optional] 
 **permissionSet** | **String**| Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] [default to &#39;full&#39;]
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postSiteTestWebhook

> StatusEntity postSiteTestWebhook(url, opts)

Test webhook.

Test webhook.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.SiteApi();
let url = "url_example"; // String | URL for testing the webhook.
let opts = {
  'action': "action_example", // String | action for test body
  'body': {key: null}, // Object | Additional body parameters.
  'encoding': "encoding_example", // String | HTTP encoding method.  Can be JSON, XML, or RAW (form data).
  'headers': {key: null}, // Object | Additional request headers.
  'method': "method_example" // String | HTTP method(GET or POST).
};
apiInstance.postSiteTestWebhook(url, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **String**| URL for testing the webhook. | 
 **action** | **String**| action for test body | [optional] 
 **body** | [**Object**](Object.md)| Additional body parameters. | [optional] 
 **encoding** | **String**| HTTP encoding method.  Can be JSON, XML, or RAW (form data). | [optional] 
 **headers** | [**Object**](Object.md)| Additional request headers. | [optional] 
 **method** | **String**| HTTP method(GET or POST). | [optional] 

### Return type

[**StatusEntity**](StatusEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

