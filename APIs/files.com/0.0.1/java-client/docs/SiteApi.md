# SiteApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSite**](SiteApi.md#getSite) | **GET** /site | Show site settings |
| [**getSiteApiKeys**](SiteApi.md#getSiteApiKeys) | **GET** /site/api_keys | List Api Keys |
| [**getSiteDnsRecords**](SiteApi.md#getSiteDnsRecords) | **GET** /site/dns_records | Show site DNS configuration. |
| [**getSiteIpAddresses**](SiteApi.md#getSiteIpAddresses) | **GET** /site/ip_addresses | List IP Addresses associated with the current site |
| [**getSiteUsage**](SiteApi.md#getSiteUsage) | **GET** /site/usage | Get the most recent usage snapshot (usage data for billing purposes) for a Site. |
| [**patchSite**](SiteApi.md#patchSite) | **PATCH** /site | Update site settings. |
| [**postSiteApiKeys**](SiteApi.md#postSiteApiKeys) | **POST** /site/api_keys | Create Api Key |
| [**postSiteTestWebhook**](SiteApi.md#postSiteTestWebhook) | **POST** /site/test-webhook | Test webhook. |


<a id="getSite"></a>
# **getSite**
> SiteEntity getSite()

Show site settings

Show site settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SiteApi apiInstance = new SiteApi(defaultClient);
    try {
      SiteEntity result = apiInstance.getSite();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#getSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Site object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getSiteApiKeys"></a>
# **getSiteApiKeys**
> List&lt;ApiKeyEntity&gt; getSiteApiKeys(userId, cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq)

List Api Keys

List Api Keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SiteApi apiInstance = new SiteApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[expires_at]=desc`). Valid fields are `expires_at`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `expires_at`.
    Object filterGt = null; // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `expires_at`.
    Object filterGteq = null; // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `expires_at`.
    Object filterLt = null; // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `expires_at`.
    Object filterLteq = null; // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `expires_at`.
    try {
      List<ApiKeyEntity> result = apiInstance.getSiteApiKeys(userId, cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#getSiteApiKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[expires_at]&#x3D;desc&#x60;). Valid fields are &#x60;expires_at&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] |
| **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] |
| **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] |
| **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] |
| **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] |

### Return type

[**List&lt;ApiKeyEntity&gt;**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of ApiKeys objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getSiteDnsRecords"></a>
# **getSiteDnsRecords**
> List&lt;DnsRecordEntity&gt; getSiteDnsRecords(cursor, perPage)

Show site DNS configuration.

Show site DNS configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<DnsRecordEntity> result = apiInstance.getSiteDnsRecords(cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#getSiteDnsRecords");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |

### Return type

[**List&lt;DnsRecordEntity&gt;**](DnsRecordEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of DnsRecords objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getSiteIpAddresses"></a>
# **getSiteIpAddresses**
> List&lt;IpAddressEntity&gt; getSiteIpAddresses(cursor, perPage)

List IP Addresses associated with the current site

List IP Addresses associated with the current site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<IpAddressEntity> result = apiInstance.getSiteIpAddresses(cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#getSiteIpAddresses");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |

### Return type

[**List&lt;IpAddressEntity&gt;**](IpAddressEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of IpAddresses objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getSiteUsage"></a>
# **getSiteUsage**
> UsageSnapshotEntity getSiteUsage()

Get the most recent usage snapshot (usage data for billing purposes) for a Site.

Get the most recent usage snapshot (usage data for billing purposes) for a Site.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SiteApi apiInstance = new SiteApi(defaultClient);
    try {
      UsageSnapshotEntity result = apiInstance.getSiteUsage();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#getSiteUsage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Site object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="patchSite"></a>
# **patchSite**
> SiteEntity patchSite(activeSftpHostKeyId, allowBundleNames, allowed2faMethodBypassForFtpSftpDav, allowed2faMethodSms, allowed2faMethodTotp, allowed2faMethodU2f, allowed2faMethodWebauthn, allowed2faMethodYubi, allowedCountries, allowedIps, askAboutOverwrites, bundleActivityNotifications, bundleExpiration, bundlePasswordRequired, bundleRegistrationNotifications, bundleRequireShareRecipient, bundleUploadReceiptNotifications, bundleWatermarkAttachmentDelete, bundleWatermarkAttachmentFile, bundleWatermarkValue, color2Left, color2Link, color2Text, color2Top, color2TopText, customNamespace, daysToRetainBackups, defaultTimeZone, desktopApp, desktopAppSessionIpPinning, desktopAppSessionLifetime, disable2faWithDelay, disableFilesCertificateGeneration, disablePasswordReset, disableUsersFromInactivityPeriodDays, disallowedCountries, domain, domainHstsHeader, domainLetsencryptChain, email, folderPermissionsGroupsOnly, ftpEnabled, icon128Delete, icon128File, icon16Delete, icon16File, icon32Delete, icon32File, icon48Delete, icon48File, immutableFiles, includePasswordInWelcomeEmail, language, ldapBaseDn, ldapDomain, ldapEnabled, ldapGroupAction, ldapGroupExclusion, ldapGroupInclusion, ldapHost, ldapHost2, ldapHost3, ldapPasswordChange, ldapPasswordChangeConfirmation, ldapPort, ldapSecure, ldapType, ldapUserAction, ldapUserIncludeGroups, ldapUsername, ldapUsernameField, loginHelpText, logoDelete, logoFile, maxPriorPasswords, mobileApp, mobileAppSessionIpPinning, mobileAppSessionLifetime, motdText, motdUseForFtp, motdUseForSftp, name, nonSsoGroupsAllowed, nonSsoUsersAllowed, officeIntegrationAvailable, officeIntegrationType, optOutGlobal, passwordMinLength, passwordRequireLetter, passwordRequireMixed, passwordRequireNumber, passwordRequireSpecial, passwordRequireUnbreached, passwordRequirementsApplyToBundles, passwordValidityDays, pinAllRemoteServersToSiteRegion, replyToEmail, require2fa, require2faUserType, sessionExpiry, sessionExpiryMinutes, sessionPinnedByIp, sftpEnabled, sftpHostKeyType, sftpInsecureCiphers, sftpUserRootEnabled, sharingEnabled, showRequestAccessLink, siteFooter, siteHeader, smtpAddress, smtpAuthentication, smtpFrom, smtpPassword, smtpPort, smtpUsername, sslRequired, subdomain, tlsDisabled, uploadsViaEmailAuthentication, useProvidedModifiedAt, userLockout, userLockoutLockPeriod, userLockoutTries, userLockoutWithin, userRequestsEnabled, userRequestsNotifyAdmins, welcomeCustomText, welcomeEmailCc, welcomeEmailEnabled, welcomeEmailSubject, welcomeScreen, windowsModeFtp)

Update site settings.

Update site settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SiteApi apiInstance = new SiteApi(defaultClient);
    Integer activeSftpHostKeyId = 56; // Integer | Id of the currently selected custom SFTP Host Key
    Boolean allowBundleNames = true; // Boolean | Are manual Bundle names allowed?
    Boolean allowed2faMethodBypassForFtpSftpDav = true; // Boolean | Are users allowed to configure their two factor authentication to be bypassed for FTP/SFTP/WebDAV?
    Boolean allowed2faMethodSms = true; // Boolean | Is SMS two factor authentication allowed?
    Boolean allowed2faMethodTotp = true; // Boolean | Is TOTP two factor authentication allowed?
    Boolean allowed2faMethodU2f = true; // Boolean | Is U2F two factor authentication allowed?
    Boolean allowed2faMethodWebauthn = true; // Boolean | Is WebAuthn two factor authentication allowed?
    Boolean allowed2faMethodYubi = true; // Boolean | Is yubikey two factor authentication allowed?
    String allowedCountries = "allowedCountries_example"; // String | Comma seperated list of allowed Country codes
    String allowedIps = "allowedIps_example"; // String | List of allowed IP addresses
    Boolean askAboutOverwrites = true; // Boolean | If false, rename conflicting files instead of asking for overwrite confirmation.  Only applies to web interface.
    String bundleActivityNotifications = "bundleActivityNotifications_example"; // String | Do Bundle owners receive activity notifications?
    Integer bundleExpiration = 56; // Integer | Site-wide Bundle expiration in days
    Boolean bundlePasswordRequired = true; // Boolean | Do Bundles require password protection?
    String bundleRegistrationNotifications = "bundleRegistrationNotifications_example"; // String | Do Bundle owners receive registration notification?
    Boolean bundleRequireShareRecipient = true; // Boolean | Do Bundles require recipients for sharing?
    String bundleUploadReceiptNotifications = "bundleUploadReceiptNotifications_example"; // String | Do Bundle uploaders receive upload confirmation notifications?
    Boolean bundleWatermarkAttachmentDelete = true; // Boolean | If true, will delete the file stored in bundle_watermark_attachment
    File bundleWatermarkAttachmentFile = new File("/path/to/file"); // File | 
    Object bundleWatermarkValue = null; // Object | Preview watermark settings applied to all bundle items. Uses the same keys as Behavior.value
    String color2Left = "color2Left_example"; // String | Page link and button color
    String color2Link = "color2Link_example"; // String | Top bar link color
    String color2Text = "color2Text_example"; // String | Page link and button color
    String color2Top = "color2Top_example"; // String | Top bar background color
    String color2TopText = "color2TopText_example"; // String | Top bar text color
    Boolean customNamespace = true; // Boolean | Is this site using a custom namespace for users?
    Integer daysToRetainBackups = 56; // Integer | Number of days to keep deleted files
    String defaultTimeZone = "defaultTimeZone_example"; // String | Site default time zone
    Boolean desktopApp = true; // Boolean | Is the desktop app enabled?
    Boolean desktopAppSessionIpPinning = true; // Boolean | Is desktop app session IP pinning enabled?
    Integer desktopAppSessionLifetime = 56; // Integer | Desktop app session lifetime (in hours)
    Boolean disable2faWithDelay = true; // Boolean | If set to true, we will begin the process of disabling 2FA on this site.
    Boolean disableFilesCertificateGeneration = true; // Boolean | If set, Files.com will not set the CAA records required to generate future SSL certificates for this domain.
    Boolean disablePasswordReset = true; // Boolean | Is password reset disabled?
    Integer disableUsersFromInactivityPeriodDays = 56; // Integer | If greater than zero, users will unable to login if they do not show activity within this number of days.
    String disallowedCountries = "disallowedCountries_example"; // String | Comma seperated list of disallowed Country codes
    String domain = "domain_example"; // String | Custom domain
    Boolean domainHstsHeader = true; // Boolean | Send HSTS (HTTP Strict Transport Security) header when visitors access the site via a custom domain?
    String domainLetsencryptChain = "domainLetsencryptChain_example"; // String | Letsencrypt chain to use when registering SSL Certificate for domain.
    String email = "email_example"; // String | Main email for this site
    Boolean folderPermissionsGroupsOnly = true; // Boolean | If true, permissions for this site must be bound to a group (not a user). Otherwise, permissions must be bound to a user.
    Boolean ftpEnabled = true; // Boolean | Is FTP enabled?
    Boolean icon128Delete = true; // Boolean | If true, will delete the file stored in icon128
    File icon128File = new File("/path/to/file"); // File | 
    Boolean icon16Delete = true; // Boolean | If true, will delete the file stored in icon16
    File icon16File = new File("/path/to/file"); // File | 
    Boolean icon32Delete = true; // Boolean | If true, will delete the file stored in icon32
    File icon32File = new File("/path/to/file"); // File | 
    Boolean icon48Delete = true; // Boolean | If true, will delete the file stored in icon48
    File icon48File = new File("/path/to/file"); // File | 
    Boolean immutableFiles = true; // Boolean | Are files protected from modification?
    Boolean includePasswordInWelcomeEmail = true; // Boolean | Include password in emails to new users?
    String language = "language_example"; // String | Site default language
    String ldapBaseDn = "ldapBaseDn_example"; // String | Base DN for looking up users in LDAP server
    String ldapDomain = "ldapDomain_example"; // String | Domain name that will be appended to usernames
    Boolean ldapEnabled = true; // Boolean | Main LDAP setting: is LDAP enabled?
    String ldapGroupAction = "ldapGroupAction_example"; // String | Should we sync groups from LDAP server?
    String ldapGroupExclusion = "ldapGroupExclusion_example"; // String | Comma or newline separated list of group names (with optional wildcards) to exclude when syncing.
    String ldapGroupInclusion = "ldapGroupInclusion_example"; // String | Comma or newline separated list of group names (with optional wildcards) to include when syncing.
    String ldapHost = "ldapHost_example"; // String | LDAP host
    String ldapHost2 = "ldapHost2_example"; // String | LDAP backup host
    String ldapHost3 = "ldapHost3_example"; // String | LDAP backup host
    String ldapPasswordChange = "ldapPasswordChange_example"; // String | New LDAP password.
    String ldapPasswordChangeConfirmation = "ldapPasswordChangeConfirmation_example"; // String | Confirm new LDAP password.
    Integer ldapPort = 56; // Integer | LDAP port
    Boolean ldapSecure = true; // Boolean | Use secure LDAP?
    String ldapType = "ldapType_example"; // String | LDAP type
    String ldapUserAction = "ldapUserAction_example"; // String | Should we sync users from LDAP server?
    String ldapUserIncludeGroups = "ldapUserIncludeGroups_example"; // String | Comma or newline separated list of group names (with optional wildcards) - if provided, only users in these groups will be added or synced.
    String ldapUsername = "ldapUsername_example"; // String | Username for signing in to LDAP server.
    String ldapUsernameField = "ldapUsernameField_example"; // String | LDAP username field
    String loginHelpText = "loginHelpText_example"; // String | Login help text
    Boolean logoDelete = true; // Boolean | If true, will delete the file stored in logo
    File logoFile = new File("/path/to/file"); // File | 
    Integer maxPriorPasswords = 56; // Integer | Number of prior passwords to disallow
    Boolean mobileApp = true; // Boolean | Is the mobile app enabled?
    Boolean mobileAppSessionIpPinning = true; // Boolean | Is mobile app session IP pinning enabled?
    Integer mobileAppSessionLifetime = 56; // Integer | Mobile app session lifetime (in hours)
    String motdText = "motdText_example"; // String | A message to show users when they connect via FTP or SFTP.
    Boolean motdUseForFtp = true; // Boolean | Show message to users connecting via FTP
    Boolean motdUseForSftp = true; // Boolean | Show message to users connecting via SFTP
    String name = "name_example"; // String | Site name
    Boolean nonSsoGroupsAllowed = true; // Boolean | If true, groups can be manually created / modified / deleted by Site Admins. Otherwise, groups can only be managed via your SSO provider.
    Boolean nonSsoUsersAllowed = true; // Boolean | If true, users can be manually created / modified / deleted by Site Admins. Otherwise, users can only be managed via your SSO provider.
    Boolean officeIntegrationAvailable = true; // Boolean | Allow users to use Office for the web?
    String officeIntegrationType = "officeIntegrationType_example"; // String | Office integration application used to edit and view the MS Office documents
    Boolean optOutGlobal = true; // Boolean | Use servers in the USA only?
    Integer passwordMinLength = 56; // Integer | Shortest password length for users
    Boolean passwordRequireLetter = true; // Boolean | Require a letter in passwords?
    Boolean passwordRequireMixed = true; // Boolean | Require lower and upper case letters in passwords?
    Boolean passwordRequireNumber = true; // Boolean | Require a number in passwords?
    Boolean passwordRequireSpecial = true; // Boolean | Require special characters in password?
    Boolean passwordRequireUnbreached = true; // Boolean | Require passwords that have not been previously breached? (see https://haveibeenpwned.com/)
    Boolean passwordRequirementsApplyToBundles = true; // Boolean | Require bundles' passwords, and passwords for other items (inboxes, public shares, etc.) to conform to the same requirements as users' passwords?
    Integer passwordValidityDays = 56; // Integer | Number of days password is valid
    Boolean pinAllRemoteServersToSiteRegion = true; // Boolean | If true, we will ensure that all internal communications with any remote server are made through the primary region of the site. This setting overrides individual remote server settings.
    String replyToEmail = "replyToEmail_example"; // String | Reply-to email for this site
    Boolean require2fa = true; // Boolean | Require two-factor authentication for all users?
    String require2faUserType = "require2faUserType_example"; // String | What type of user is required to use two-factor authentication (when require_2fa is set to `true` for this site)?
    Double sessionExpiry = 3.4D; // Double | Session expiry in hours
    Integer sessionExpiryMinutes = 56; // Integer | Session expiry in minutes
    Boolean sessionPinnedByIp = true; // Boolean | Are sessions locked to the same IP? (i.e. do users need to log in again if they change IPs?)
    Boolean sftpEnabled = true; // Boolean | Is SFTP enabled?
    String sftpHostKeyType = "sftpHostKeyType_example"; // String | Sftp Host Key Type
    Boolean sftpInsecureCiphers = true; // Boolean | Are Insecure Ciphers allowed for SFTP?  Note:  Settting TLS Disabled -> True will always allow insecure ciphers for SFTP as well.  Enabling this is insecure.
    Boolean sftpUserRootEnabled = true; // Boolean | Use user FTP roots also for SFTP?
    Boolean sharingEnabled = true; // Boolean | Allow bundle creation
    Boolean showRequestAccessLink = true; // Boolean | Show request access link for users without access?  Currently unused.
    String siteFooter = "siteFooter_example"; // String | Custom site footer text
    String siteHeader = "siteHeader_example"; // String | Custom site header text
    String smtpAddress = "smtpAddress_example"; // String | SMTP server hostname or IP
    String smtpAuthentication = "smtpAuthentication_example"; // String | SMTP server authentication type
    String smtpFrom = "smtpFrom_example"; // String | From address to use when mailing through custom SMTP
    String smtpPassword = "smtpPassword_example"; // String | Password for SMTP server.
    Integer smtpPort = 56; // Integer | SMTP server port
    String smtpUsername = "smtpUsername_example"; // String | SMTP server username
    Boolean sslRequired = true; // Boolean | Is SSL required?  Disabling this is insecure.
    String subdomain = "subdomain_example"; // String | Site subdomain
    Boolean tlsDisabled = true; // Boolean | Are Insecure TLS and SFTP Ciphers allowed?  Enabling this is insecure.
    Boolean uploadsViaEmailAuthentication = true; // Boolean | Do incoming emails in the Inboxes require checking for SPF/DKIM/DMARC?
    Boolean useProvidedModifiedAt = true; // Boolean | Allow uploaders to set `provided_modified_at` for uploaded files?
    Boolean userLockout = true; // Boolean | Will users be locked out after incorrect login attempts?
    Integer userLockoutLockPeriod = 56; // Integer | How many hours to lock user out for failed password?
    Integer userLockoutTries = 56; // Integer | Number of login tries within `user_lockout_within` hours before users are locked out
    Integer userLockoutWithin = 56; // Integer | Number of hours for user lockout window
    Boolean userRequestsEnabled = true; // Boolean | Enable User Requests feature
    Boolean userRequestsNotifyAdmins = true; // Boolean | Send email to site admins when a user request is received?
    String welcomeCustomText = "welcomeCustomText_example"; // String | Custom text send in user welcome email
    String welcomeEmailCc = "welcomeEmailCc_example"; // String | Include this email in welcome emails if enabled
    Boolean welcomeEmailEnabled = true; // Boolean | Will the welcome email be sent to new users?
    String welcomeEmailSubject = "welcomeEmailSubject_example"; // String | Include this email subject in welcome emails if enabled
    String welcomeScreen = "welcomeScreen_example"; // String | Does the welcome screen appear?
    Boolean windowsModeFtp = true; // Boolean | Does FTP user Windows emulation mode?
    try {
      SiteEntity result = apiInstance.patchSite(activeSftpHostKeyId, allowBundleNames, allowed2faMethodBypassForFtpSftpDav, allowed2faMethodSms, allowed2faMethodTotp, allowed2faMethodU2f, allowed2faMethodWebauthn, allowed2faMethodYubi, allowedCountries, allowedIps, askAboutOverwrites, bundleActivityNotifications, bundleExpiration, bundlePasswordRequired, bundleRegistrationNotifications, bundleRequireShareRecipient, bundleUploadReceiptNotifications, bundleWatermarkAttachmentDelete, bundleWatermarkAttachmentFile, bundleWatermarkValue, color2Left, color2Link, color2Text, color2Top, color2TopText, customNamespace, daysToRetainBackups, defaultTimeZone, desktopApp, desktopAppSessionIpPinning, desktopAppSessionLifetime, disable2faWithDelay, disableFilesCertificateGeneration, disablePasswordReset, disableUsersFromInactivityPeriodDays, disallowedCountries, domain, domainHstsHeader, domainLetsencryptChain, email, folderPermissionsGroupsOnly, ftpEnabled, icon128Delete, icon128File, icon16Delete, icon16File, icon32Delete, icon32File, icon48Delete, icon48File, immutableFiles, includePasswordInWelcomeEmail, language, ldapBaseDn, ldapDomain, ldapEnabled, ldapGroupAction, ldapGroupExclusion, ldapGroupInclusion, ldapHost, ldapHost2, ldapHost3, ldapPasswordChange, ldapPasswordChangeConfirmation, ldapPort, ldapSecure, ldapType, ldapUserAction, ldapUserIncludeGroups, ldapUsername, ldapUsernameField, loginHelpText, logoDelete, logoFile, maxPriorPasswords, mobileApp, mobileAppSessionIpPinning, mobileAppSessionLifetime, motdText, motdUseForFtp, motdUseForSftp, name, nonSsoGroupsAllowed, nonSsoUsersAllowed, officeIntegrationAvailable, officeIntegrationType, optOutGlobal, passwordMinLength, passwordRequireLetter, passwordRequireMixed, passwordRequireNumber, passwordRequireSpecial, passwordRequireUnbreached, passwordRequirementsApplyToBundles, passwordValidityDays, pinAllRemoteServersToSiteRegion, replyToEmail, require2fa, require2faUserType, sessionExpiry, sessionExpiryMinutes, sessionPinnedByIp, sftpEnabled, sftpHostKeyType, sftpInsecureCiphers, sftpUserRootEnabled, sharingEnabled, showRequestAccessLink, siteFooter, siteHeader, smtpAddress, smtpAuthentication, smtpFrom, smtpPassword, smtpPort, smtpUsername, sslRequired, subdomain, tlsDisabled, uploadsViaEmailAuthentication, useProvidedModifiedAt, userLockout, userLockoutLockPeriod, userLockoutTries, userLockoutWithin, userRequestsEnabled, userRequestsNotifyAdmins, welcomeCustomText, welcomeEmailCc, welcomeEmailEnabled, welcomeEmailSubject, welcomeScreen, windowsModeFtp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#patchSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **activeSftpHostKeyId** | **Integer**| Id of the currently selected custom SFTP Host Key | [optional] |
| **allowBundleNames** | **Boolean**| Are manual Bundle names allowed? | [optional] |
| **allowed2faMethodBypassForFtpSftpDav** | **Boolean**| Are users allowed to configure their two factor authentication to be bypassed for FTP/SFTP/WebDAV? | [optional] |
| **allowed2faMethodSms** | **Boolean**| Is SMS two factor authentication allowed? | [optional] |
| **allowed2faMethodTotp** | **Boolean**| Is TOTP two factor authentication allowed? | [optional] |
| **allowed2faMethodU2f** | **Boolean**| Is U2F two factor authentication allowed? | [optional] |
| **allowed2faMethodWebauthn** | **Boolean**| Is WebAuthn two factor authentication allowed? | [optional] |
| **allowed2faMethodYubi** | **Boolean**| Is yubikey two factor authentication allowed? | [optional] |
| **allowedCountries** | **String**| Comma seperated list of allowed Country codes | [optional] |
| **allowedIps** | **String**| List of allowed IP addresses | [optional] |
| **askAboutOverwrites** | **Boolean**| If false, rename conflicting files instead of asking for overwrite confirmation.  Only applies to web interface. | [optional] |
| **bundleActivityNotifications** | **String**| Do Bundle owners receive activity notifications? | [optional] |
| **bundleExpiration** | **Integer**| Site-wide Bundle expiration in days | [optional] |
| **bundlePasswordRequired** | **Boolean**| Do Bundles require password protection? | [optional] |
| **bundleRegistrationNotifications** | **String**| Do Bundle owners receive registration notification? | [optional] |
| **bundleRequireShareRecipient** | **Boolean**| Do Bundles require recipients for sharing? | [optional] |
| **bundleUploadReceiptNotifications** | **String**| Do Bundle uploaders receive upload confirmation notifications? | [optional] |
| **bundleWatermarkAttachmentDelete** | **Boolean**| If true, will delete the file stored in bundle_watermark_attachment | [optional] |
| **bundleWatermarkAttachmentFile** | **File**|  | [optional] |
| **bundleWatermarkValue** | [**Object**](Object.md)| Preview watermark settings applied to all bundle items. Uses the same keys as Behavior.value | [optional] |
| **color2Left** | **String**| Page link and button color | [optional] |
| **color2Link** | **String**| Top bar link color | [optional] |
| **color2Text** | **String**| Page link and button color | [optional] |
| **color2Top** | **String**| Top bar background color | [optional] |
| **color2TopText** | **String**| Top bar text color | [optional] |
| **customNamespace** | **Boolean**| Is this site using a custom namespace for users? | [optional] |
| **daysToRetainBackups** | **Integer**| Number of days to keep deleted files | [optional] |
| **defaultTimeZone** | **String**| Site default time zone | [optional] |
| **desktopApp** | **Boolean**| Is the desktop app enabled? | [optional] |
| **desktopAppSessionIpPinning** | **Boolean**| Is desktop app session IP pinning enabled? | [optional] |
| **desktopAppSessionLifetime** | **Integer**| Desktop app session lifetime (in hours) | [optional] |
| **disable2faWithDelay** | **Boolean**| If set to true, we will begin the process of disabling 2FA on this site. | [optional] |
| **disableFilesCertificateGeneration** | **Boolean**| If set, Files.com will not set the CAA records required to generate future SSL certificates for this domain. | [optional] |
| **disablePasswordReset** | **Boolean**| Is password reset disabled? | [optional] |
| **disableUsersFromInactivityPeriodDays** | **Integer**| If greater than zero, users will unable to login if they do not show activity within this number of days. | [optional] |
| **disallowedCountries** | **String**| Comma seperated list of disallowed Country codes | [optional] |
| **domain** | **String**| Custom domain | [optional] |
| **domainHstsHeader** | **Boolean**| Send HSTS (HTTP Strict Transport Security) header when visitors access the site via a custom domain? | [optional] |
| **domainLetsencryptChain** | **String**| Letsencrypt chain to use when registering SSL Certificate for domain. | [optional] |
| **email** | **String**| Main email for this site | [optional] |
| **folderPermissionsGroupsOnly** | **Boolean**| If true, permissions for this site must be bound to a group (not a user). Otherwise, permissions must be bound to a user. | [optional] |
| **ftpEnabled** | **Boolean**| Is FTP enabled? | [optional] |
| **icon128Delete** | **Boolean**| If true, will delete the file stored in icon128 | [optional] |
| **icon128File** | **File**|  | [optional] |
| **icon16Delete** | **Boolean**| If true, will delete the file stored in icon16 | [optional] |
| **icon16File** | **File**|  | [optional] |
| **icon32Delete** | **Boolean**| If true, will delete the file stored in icon32 | [optional] |
| **icon32File** | **File**|  | [optional] |
| **icon48Delete** | **Boolean**| If true, will delete the file stored in icon48 | [optional] |
| **icon48File** | **File**|  | [optional] |
| **immutableFiles** | **Boolean**| Are files protected from modification? | [optional] |
| **includePasswordInWelcomeEmail** | **Boolean**| Include password in emails to new users? | [optional] |
| **language** | **String**| Site default language | [optional] |
| **ldapBaseDn** | **String**| Base DN for looking up users in LDAP server | [optional] |
| **ldapDomain** | **String**| Domain name that will be appended to usernames | [optional] |
| **ldapEnabled** | **Boolean**| Main LDAP setting: is LDAP enabled? | [optional] |
| **ldapGroupAction** | **String**| Should we sync groups from LDAP server? | [optional] |
| **ldapGroupExclusion** | **String**| Comma or newline separated list of group names (with optional wildcards) to exclude when syncing. | [optional] |
| **ldapGroupInclusion** | **String**| Comma or newline separated list of group names (with optional wildcards) to include when syncing. | [optional] |
| **ldapHost** | **String**| LDAP host | [optional] |
| **ldapHost2** | **String**| LDAP backup host | [optional] |
| **ldapHost3** | **String**| LDAP backup host | [optional] |
| **ldapPasswordChange** | **String**| New LDAP password. | [optional] |
| **ldapPasswordChangeConfirmation** | **String**| Confirm new LDAP password. | [optional] |
| **ldapPort** | **Integer**| LDAP port | [optional] |
| **ldapSecure** | **Boolean**| Use secure LDAP? | [optional] |
| **ldapType** | **String**| LDAP type | [optional] |
| **ldapUserAction** | **String**| Should we sync users from LDAP server? | [optional] |
| **ldapUserIncludeGroups** | **String**| Comma or newline separated list of group names (with optional wildcards) - if provided, only users in these groups will be added or synced. | [optional] |
| **ldapUsername** | **String**| Username for signing in to LDAP server. | [optional] |
| **ldapUsernameField** | **String**| LDAP username field | [optional] |
| **loginHelpText** | **String**| Login help text | [optional] |
| **logoDelete** | **Boolean**| If true, will delete the file stored in logo | [optional] |
| **logoFile** | **File**|  | [optional] |
| **maxPriorPasswords** | **Integer**| Number of prior passwords to disallow | [optional] |
| **mobileApp** | **Boolean**| Is the mobile app enabled? | [optional] |
| **mobileAppSessionIpPinning** | **Boolean**| Is mobile app session IP pinning enabled? | [optional] |
| **mobileAppSessionLifetime** | **Integer**| Mobile app session lifetime (in hours) | [optional] |
| **motdText** | **String**| A message to show users when they connect via FTP or SFTP. | [optional] |
| **motdUseForFtp** | **Boolean**| Show message to users connecting via FTP | [optional] |
| **motdUseForSftp** | **Boolean**| Show message to users connecting via SFTP | [optional] |
| **name** | **String**| Site name | [optional] |
| **nonSsoGroupsAllowed** | **Boolean**| If true, groups can be manually created / modified / deleted by Site Admins. Otherwise, groups can only be managed via your SSO provider. | [optional] |
| **nonSsoUsersAllowed** | **Boolean**| If true, users can be manually created / modified / deleted by Site Admins. Otherwise, users can only be managed via your SSO provider. | [optional] |
| **officeIntegrationAvailable** | **Boolean**| Allow users to use Office for the web? | [optional] |
| **officeIntegrationType** | **String**| Office integration application used to edit and view the MS Office documents | [optional] |
| **optOutGlobal** | **Boolean**| Use servers in the USA only? | [optional] |
| **passwordMinLength** | **Integer**| Shortest password length for users | [optional] |
| **passwordRequireLetter** | **Boolean**| Require a letter in passwords? | [optional] |
| **passwordRequireMixed** | **Boolean**| Require lower and upper case letters in passwords? | [optional] |
| **passwordRequireNumber** | **Boolean**| Require a number in passwords? | [optional] |
| **passwordRequireSpecial** | **Boolean**| Require special characters in password? | [optional] |
| **passwordRequireUnbreached** | **Boolean**| Require passwords that have not been previously breached? (see https://haveibeenpwned.com/) | [optional] |
| **passwordRequirementsApplyToBundles** | **Boolean**| Require bundles&#39; passwords, and passwords for other items (inboxes, public shares, etc.) to conform to the same requirements as users&#39; passwords? | [optional] |
| **passwordValidityDays** | **Integer**| Number of days password is valid | [optional] |
| **pinAllRemoteServersToSiteRegion** | **Boolean**| If true, we will ensure that all internal communications with any remote server are made through the primary region of the site. This setting overrides individual remote server settings. | [optional] |
| **replyToEmail** | **String**| Reply-to email for this site | [optional] |
| **require2fa** | **Boolean**| Require two-factor authentication for all users? | [optional] |
| **require2faUserType** | **String**| What type of user is required to use two-factor authentication (when require_2fa is set to &#x60;true&#x60; for this site)? | [optional] |
| **sessionExpiry** | **Double**| Session expiry in hours | [optional] |
| **sessionExpiryMinutes** | **Integer**| Session expiry in minutes | [optional] |
| **sessionPinnedByIp** | **Boolean**| Are sessions locked to the same IP? (i.e. do users need to log in again if they change IPs?) | [optional] |
| **sftpEnabled** | **Boolean**| Is SFTP enabled? | [optional] |
| **sftpHostKeyType** | **String**| Sftp Host Key Type | [optional] |
| **sftpInsecureCiphers** | **Boolean**| Are Insecure Ciphers allowed for SFTP?  Note:  Settting TLS Disabled -&gt; True will always allow insecure ciphers for SFTP as well.  Enabling this is insecure. | [optional] |
| **sftpUserRootEnabled** | **Boolean**| Use user FTP roots also for SFTP? | [optional] |
| **sharingEnabled** | **Boolean**| Allow bundle creation | [optional] |
| **showRequestAccessLink** | **Boolean**| Show request access link for users without access?  Currently unused. | [optional] |
| **siteFooter** | **String**| Custom site footer text | [optional] |
| **siteHeader** | **String**| Custom site header text | [optional] |
| **smtpAddress** | **String**| SMTP server hostname or IP | [optional] |
| **smtpAuthentication** | **String**| SMTP server authentication type | [optional] |
| **smtpFrom** | **String**| From address to use when mailing through custom SMTP | [optional] |
| **smtpPassword** | **String**| Password for SMTP server. | [optional] |
| **smtpPort** | **Integer**| SMTP server port | [optional] |
| **smtpUsername** | **String**| SMTP server username | [optional] |
| **sslRequired** | **Boolean**| Is SSL required?  Disabling this is insecure. | [optional] |
| **subdomain** | **String**| Site subdomain | [optional] |
| **tlsDisabled** | **Boolean**| Are Insecure TLS and SFTP Ciphers allowed?  Enabling this is insecure. | [optional] |
| **uploadsViaEmailAuthentication** | **Boolean**| Do incoming emails in the Inboxes require checking for SPF/DKIM/DMARC? | [optional] |
| **useProvidedModifiedAt** | **Boolean**| Allow uploaders to set &#x60;provided_modified_at&#x60; for uploaded files? | [optional] |
| **userLockout** | **Boolean**| Will users be locked out after incorrect login attempts? | [optional] |
| **userLockoutLockPeriod** | **Integer**| How many hours to lock user out for failed password? | [optional] |
| **userLockoutTries** | **Integer**| Number of login tries within &#x60;user_lockout_within&#x60; hours before users are locked out | [optional] |
| **userLockoutWithin** | **Integer**| Number of hours for user lockout window | [optional] |
| **userRequestsEnabled** | **Boolean**| Enable User Requests feature | [optional] |
| **userRequestsNotifyAdmins** | **Boolean**| Send email to site admins when a user request is received? | [optional] |
| **welcomeCustomText** | **String**| Custom text send in user welcome email | [optional] |
| **welcomeEmailCc** | **String**| Include this email in welcome emails if enabled | [optional] |
| **welcomeEmailEnabled** | **Boolean**| Will the welcome email be sent to new users? | [optional] |
| **welcomeEmailSubject** | **String**| Include this email subject in welcome emails if enabled | [optional] |
| **welcomeScreen** | **String**| Does the welcome screen appear? | [optional] |
| **windowsModeFtp** | **Boolean**| Does FTP user Windows emulation mode? | [optional] |

### Return type

[**SiteEntity**](SiteEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Site object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postSiteApiKeys"></a>
# **postSiteApiKeys**
> ApiKeyEntity postSiteApiKeys(description, expiresAt, name, path, permissionSet, userId)

Create Api Key

Create Api Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String description = "description_example"; // String | User-supplied description of API key.
    OffsetDateTime expiresAt = OffsetDateTime.now(); // OffsetDateTime | API Key expiration date
    String name = "name_example"; // String | Internal name for the API Key.  For your use.
    String path = "path_example"; // String | Folder path restriction for this api key.
    String permissionSet = "none"; // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    try {
      ApiKeyEntity result = apiInstance.postSiteApiKeys(description, expiresAt, name, path, permissionSet, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#postSiteApiKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **description** | **String**| User-supplied description of API key. | [optional] |
| **expiresAt** | **OffsetDateTime**| API Key expiration date | [optional] |
| **name** | **String**| Internal name for the API Key.  For your use. | [optional] |
| **path** | **String**| Folder path restriction for this api key. | [optional] |
| **permissionSet** | **String**| Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] [default to full] [enum: none, full, desktop_app, sync_app, office_integration, mobile_app] |
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ApiKeys object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postSiteTestWebhook"></a>
# **postSiteTestWebhook**
> StatusEntity postSiteTestWebhook(url, action, body, encoding, headers, method)

Test webhook.

Test webhook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    SiteApi apiInstance = new SiteApi(defaultClient);
    String url = "url_example"; // String | URL for testing the webhook.
    String action = "action_example"; // String | action for test body
    Object body = null; // Object | Additional body parameters.
    String encoding = "encoding_example"; // String | HTTP encoding method.  Can be JSON, XML, or RAW (form data).
    Object headers = null; // Object | Additional request headers.
    String method = "method_example"; // String | HTTP method(GET or POST).
    try {
      StatusEntity result = apiInstance.postSiteTestWebhook(url, action, body, encoding, headers, method);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteApi#postSiteTestWebhook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **url** | **String**| URL for testing the webhook. | |
| **action** | **String**| action for test body | [optional] |
| **body** | [**Object**](Object.md)| Additional body parameters. | [optional] |
| **encoding** | **String**| HTTP encoding method.  Can be JSON, XML, or RAW (form data). | [optional] |
| **headers** | [**Object**](Object.md)| Additional request headers. | [optional] |
| **method** | **String**| HTTP method(GET or POST). | [optional] |

### Return type

[**StatusEntity**](StatusEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Behaviors object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

