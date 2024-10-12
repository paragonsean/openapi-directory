# UserApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUserApiKeys**](UserApi.md#getUserApiKeys) | **GET** /user/api_keys | List Api Keys |
| [**getUserGroups**](UserApi.md#getUserGroups) | **GET** /user/groups | List Group Users |
| [**getUserPublicKeys**](UserApi.md#getUserPublicKeys) | **GET** /user/public_keys | List Public Keys |
| [**patchUser**](UserApi.md#patchUser) | **PATCH** /user | Update User |
| [**postUserApiKeys**](UserApi.md#postUserApiKeys) | **POST** /user/api_keys | Create Api Key |
| [**postUserPublicKeys**](UserApi.md#postUserPublicKeys) | **POST** /user/public_keys | Create Public Key |


<a id="getUserApiKeys"></a>
# **getUserApiKeys**
> List&lt;ApiKeyEntity&gt; getUserApiKeys(userId, cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq)

List Api Keys

List Api Keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UserApi apiInstance = new UserApi(defaultClient);
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
      List<ApiKeyEntity> result = apiInstance.getUserApiKeys(userId, cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserApiKeys");
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

<a id="getUserGroups"></a>
# **getUserGroups**
> List&lt;GroupUserEntity&gt; getUserGroups(userId, cursor, perPage, groupId)

List Group Users

List Group Users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UserApi apiInstance = new UserApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  If provided, will return group_users of this user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Integer groupId = 56; // Integer | Group ID.  If provided, will return group_users of this group.
    try {
      List<GroupUserEntity> result = apiInstance.getUserGroups(userId, cursor, perPage, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserGroups");
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
| **userId** | **Integer**| User ID.  If provided, will return group_users of this user. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **groupId** | **Integer**| Group ID.  If provided, will return group_users of this group. | [optional] |

### Return type

[**List&lt;GroupUserEntity&gt;**](GroupUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of GroupUsers objects. |  -  |
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

<a id="getUserPublicKeys"></a>
# **getUserPublicKeys**
> List&lt;PublicKeyEntity&gt; getUserPublicKeys(userId, cursor, perPage)

List Public Keys

List Public Keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UserApi apiInstance = new UserApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<PublicKeyEntity> result = apiInstance.getUserPublicKeys(userId, cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserPublicKeys");
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

### Return type

[**List&lt;PublicKeyEntity&gt;**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of PublicKeys objects. |  -  |
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

<a id="patchUser"></a>
# **patchUser**
> UserEntity patchUser(allowedIps, announcementsRead, attachmentsPermission, authenticateUntil, authenticationMethod, avatarDelete, avatarFile, billingPermission, bypassInactiveDisable, bypassSiteAllowedIps, changePassword, changePasswordConfirmation, company, davPermission, disabled, email, ftpPermission, grantPermission, groupId, groupIds, headerText, importedPasswordHash, language, name, notes, notificationDailySendTime, officeIntegrationEnabled, password, passwordConfirmation, passwordValidityDays, receiveAdminAlerts, require2fa, requirePasswordChange, restapiPermission, selfManaged, sftpPermission, siteAdmin, skipWelcomeScreen, sslRequired, ssoStrategyId, subscribeToNewsletter, timeZone, userRoot, username)

Update User

Update User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UserApi apiInstance = new UserApi(defaultClient);
    String allowedIps = "allowedIps_example"; // String | A list of allowed IPs if applicable.  Newline delimited
    Boolean announcementsRead = true; // Boolean | Signifies that the user has read all the announcements in the UI.
    Boolean attachmentsPermission = true; // Boolean | DEPRECATED: Can the user create Bundles (aka Share Links)? Use the bundle permission instead.
    OffsetDateTime authenticateUntil = OffsetDateTime.now(); // OffsetDateTime | Scheduled Date/Time at which user will be deactivated
    String authenticationMethod = "password"; // String | How is this user authenticated?
    Boolean avatarDelete = true; // Boolean | If true, the avatar will be deleted.
    File avatarFile = new File("/path/to/file"); // File | An image file for your user avatar.
    Boolean billingPermission = true; // Boolean | Allow this user to perform operations on the account, payments, and invoices?
    Boolean bypassInactiveDisable = true; // Boolean | Exempt this user from being disabled based on inactivity?
    Boolean bypassSiteAllowedIps = true; // Boolean | Allow this user to skip site-wide IP blacklists?
    String changePassword = "changePassword_example"; // String | Used for changing a password on an existing user.
    String changePasswordConfirmation = "changePasswordConfirmation_example"; // String | Optional, but if provided, we will ensure that it matches the value sent in `change_password`.
    String company = "company_example"; // String | User's company
    Boolean davPermission = true; // Boolean | Can the user connect with WebDAV?
    Boolean disabled = true; // Boolean | Is user disabled? Disabled users cannot log in, and do not count for billing purposes.  Users can be automatically disabled after an inactivity period via a Site setting.
    String email = "email_example"; // String | User's email.
    Boolean ftpPermission = true; // Boolean | Can the user access with FTP/FTPS?
    String grantPermission = "grantPermission_example"; // String | Permission to grant on the user root.  Can be blank or `full`, `read`, `write`, `list`, `read+write`, or `list+write`
    Integer groupId = 56; // Integer | Group ID to associate this user with.
    String groupIds = "groupIds_example"; // String | A list of group ids to associate this user with.  Comma delimited.
    String headerText = "headerText_example"; // String | Text to display to the user in the header of the UI
    String importedPasswordHash = "importedPasswordHash_example"; // String | Pre-calculated hash of the user's password. If supplied, this will be used to authenticate the user on first login. Supported hash menthods are MD5, SHA1, and SHA256.
    String language = "language_example"; // String | Preferred language
    String name = "name_example"; // String | User's full name
    String notes = "notes_example"; // String | Any internal notes on the user
    Integer notificationDailySendTime = 56; // Integer | Hour of the day at which daily notifications should be sent. Can be in range 0 to 23
    Boolean officeIntegrationEnabled = true; // Boolean | Enable integration with Office for the web?
    String password = "password_example"; // String | User password.
    String passwordConfirmation = "passwordConfirmation_example"; // String | Optional, but if provided, we will ensure that it matches the value sent in `password`.
    Integer passwordValidityDays = 56; // Integer | Number of days to allow user to use the same password
    Boolean receiveAdminAlerts = true; // Boolean | Should the user receive admin alerts such a certificate expiration notifications and overages?
    String require2fa = "use_system_setting"; // String | 2FA required setting
    Boolean requirePasswordChange = true; // Boolean | Is a password change required upon next user login?
    Boolean restapiPermission = true; // Boolean | Can this user access the REST API?
    Boolean selfManaged = true; // Boolean | Does this user manage it's own credentials or is it a shared/bot user?
    Boolean sftpPermission = true; // Boolean | Can the user access with SFTP?
    Boolean siteAdmin = true; // Boolean | Is the user an administrator for this site?
    Boolean skipWelcomeScreen = true; // Boolean | Skip Welcome page in the UI?
    String sslRequired = "use_system_setting"; // String | SSL required setting
    Integer ssoStrategyId = 56; // Integer | SSO (Single Sign On) strategy ID for the user, if applicable.
    Boolean subscribeToNewsletter = true; // Boolean | Is the user subscribed to the newsletter?
    String timeZone = "timeZone_example"; // String | User time zone
    String userRoot = "userRoot_example"; // String | Root folder for FTP (and optionally SFTP if the appropriate site-wide setting is set.)  Note that this is not used for API, Desktop, or Web interface.
    String username = "username_example"; // String | User's username
    try {
      UserEntity result = apiInstance.patchUser(allowedIps, announcementsRead, attachmentsPermission, authenticateUntil, authenticationMethod, avatarDelete, avatarFile, billingPermission, bypassInactiveDisable, bypassSiteAllowedIps, changePassword, changePasswordConfirmation, company, davPermission, disabled, email, ftpPermission, grantPermission, groupId, groupIds, headerText, importedPasswordHash, language, name, notes, notificationDailySendTime, officeIntegrationEnabled, password, passwordConfirmation, passwordValidityDays, receiveAdminAlerts, require2fa, requirePasswordChange, restapiPermission, selfManaged, sftpPermission, siteAdmin, skipWelcomeScreen, sslRequired, ssoStrategyId, subscribeToNewsletter, timeZone, userRoot, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#patchUser");
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
| **allowedIps** | **String**| A list of allowed IPs if applicable.  Newline delimited | [optional] |
| **announcementsRead** | **Boolean**| Signifies that the user has read all the announcements in the UI. | [optional] |
| **attachmentsPermission** | **Boolean**| DEPRECATED: Can the user create Bundles (aka Share Links)? Use the bundle permission instead. | [optional] |
| **authenticateUntil** | **OffsetDateTime**| Scheduled Date/Time at which user will be deactivated | [optional] |
| **authenticationMethod** | **String**| How is this user authenticated? | [optional] [enum: password, unused_former_ldap, sso, none, email_signup, password_with_imported_hash] |
| **avatarDelete** | **Boolean**| If true, the avatar will be deleted. | [optional] |
| **avatarFile** | **File**| An image file for your user avatar. | [optional] |
| **billingPermission** | **Boolean**| Allow this user to perform operations on the account, payments, and invoices? | [optional] |
| **bypassInactiveDisable** | **Boolean**| Exempt this user from being disabled based on inactivity? | [optional] |
| **bypassSiteAllowedIps** | **Boolean**| Allow this user to skip site-wide IP blacklists? | [optional] |
| **changePassword** | **String**| Used for changing a password on an existing user. | [optional] |
| **changePasswordConfirmation** | **String**| Optional, but if provided, we will ensure that it matches the value sent in &#x60;change_password&#x60;. | [optional] |
| **company** | **String**| User&#39;s company | [optional] |
| **davPermission** | **Boolean**| Can the user connect with WebDAV? | [optional] |
| **disabled** | **Boolean**| Is user disabled? Disabled users cannot log in, and do not count for billing purposes.  Users can be automatically disabled after an inactivity period via a Site setting. | [optional] |
| **email** | **String**| User&#39;s email. | [optional] |
| **ftpPermission** | **Boolean**| Can the user access with FTP/FTPS? | [optional] |
| **grantPermission** | **String**| Permission to grant on the user root.  Can be blank or &#x60;full&#x60;, &#x60;read&#x60;, &#x60;write&#x60;, &#x60;list&#x60;, &#x60;read+write&#x60;, or &#x60;list+write&#x60; | [optional] |
| **groupId** | **Integer**| Group ID to associate this user with. | [optional] |
| **groupIds** | **String**| A list of group ids to associate this user with.  Comma delimited. | [optional] |
| **headerText** | **String**| Text to display to the user in the header of the UI | [optional] |
| **importedPasswordHash** | **String**| Pre-calculated hash of the user&#39;s password. If supplied, this will be used to authenticate the user on first login. Supported hash menthods are MD5, SHA1, and SHA256. | [optional] |
| **language** | **String**| Preferred language | [optional] |
| **name** | **String**| User&#39;s full name | [optional] |
| **notes** | **String**| Any internal notes on the user | [optional] |
| **notificationDailySendTime** | **Integer**| Hour of the day at which daily notifications should be sent. Can be in range 0 to 23 | [optional] |
| **officeIntegrationEnabled** | **Boolean**| Enable integration with Office for the web? | [optional] |
| **password** | **String**| User password. | [optional] |
| **passwordConfirmation** | **String**| Optional, but if provided, we will ensure that it matches the value sent in &#x60;password&#x60;. | [optional] |
| **passwordValidityDays** | **Integer**| Number of days to allow user to use the same password | [optional] |
| **receiveAdminAlerts** | **Boolean**| Should the user receive admin alerts such a certificate expiration notifications and overages? | [optional] |
| **require2fa** | **String**| 2FA required setting | [optional] [enum: use_system_setting, always_require, never_require] |
| **requirePasswordChange** | **Boolean**| Is a password change required upon next user login? | [optional] |
| **restapiPermission** | **Boolean**| Can this user access the REST API? | [optional] |
| **selfManaged** | **Boolean**| Does this user manage it&#39;s own credentials or is it a shared/bot user? | [optional] |
| **sftpPermission** | **Boolean**| Can the user access with SFTP? | [optional] |
| **siteAdmin** | **Boolean**| Is the user an administrator for this site? | [optional] |
| **skipWelcomeScreen** | **Boolean**| Skip Welcome page in the UI? | [optional] |
| **sslRequired** | **String**| SSL required setting | [optional] [enum: use_system_setting, always_require, never_require] |
| **ssoStrategyId** | **Integer**| SSO (Single Sign On) strategy ID for the user, if applicable. | [optional] |
| **subscribeToNewsletter** | **Boolean**| Is the user subscribed to the newsletter? | [optional] |
| **timeZone** | **String**| User time zone | [optional] |
| **userRoot** | **String**| Root folder for FTP (and optionally SFTP if the appropriate site-wide setting is set.)  Note that this is not used for API, Desktop, or Web interface. | [optional] |
| **username** | **String**| User&#39;s username | [optional] |

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Users object. |  -  |
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

<a id="postUserApiKeys"></a>
# **postUserApiKeys**
> ApiKeyEntity postUserApiKeys(description, expiresAt, name, path, permissionSet, userId)

Create Api Key

Create Api Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UserApi apiInstance = new UserApi(defaultClient);
    String description = "description_example"; // String | User-supplied description of API key.
    OffsetDateTime expiresAt = OffsetDateTime.now(); // OffsetDateTime | API Key expiration date
    String name = "name_example"; // String | Internal name for the API Key.  For your use.
    String path = "path_example"; // String | Folder path restriction for this api key.
    String permissionSet = "none"; // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    try {
      ApiKeyEntity result = apiInstance.postUserApiKeys(description, expiresAt, name, path, permissionSet, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#postUserApiKeys");
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

<a id="postUserPublicKeys"></a>
# **postUserPublicKeys**
> PublicKeyEntity postUserPublicKeys(publicKey, title, userId)

Create Public Key

Create Public Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UserApi apiInstance = new UserApi(defaultClient);
    String publicKey = "publicKey_example"; // String | Actual contents of SSH key.
    String title = "title_example"; // String | Internal reference for key.
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    try {
      PublicKeyEntity result = apiInstance.postUserPublicKeys(publicKey, title, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#postUserPublicKeys");
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
| **publicKey** | **String**| Actual contents of SSH key. | |
| **title** | **String**| Internal reference for key. | |
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |

### Return type

[**PublicKeyEntity**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The PublicKeys object. |  -  |
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

