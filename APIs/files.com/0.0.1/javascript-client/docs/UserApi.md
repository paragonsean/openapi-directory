# FilesComApi.UserApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getUserApiKeys**](UserApi.md#getUserApiKeys) | **GET** /user/api_keys | List Api Keys
[**getUserGroups**](UserApi.md#getUserGroups) | **GET** /user/groups | List Group Users
[**getUserPublicKeys**](UserApi.md#getUserPublicKeys) | **GET** /user/public_keys | List Public Keys
[**patchUser**](UserApi.md#patchUser) | **PATCH** /user | Update User
[**postUserApiKeys**](UserApi.md#postUserApiKeys) | **POST** /user/api_keys | Create Api Key
[**postUserPublicKeys**](UserApi.md#postUserPublicKeys) | **POST** /user/public_keys | Create Public Key



## getUserApiKeys

> [ApiKeyEntity] getUserApiKeys(opts)

List Api Keys

List Api Keys

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UserApi();
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
apiInstance.getUserApiKeys(opts, (error, data, response) => {
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


## getUserGroups

> [GroupUserEntity] getUserGroups(opts)

List Group Users

List Group Users

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UserApi();
let opts = {
  'userId': 56, // Number | User ID.  If provided, will return group_users of this user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'groupId': 56 // Number | Group ID.  If provided, will return group_users of this group.
};
apiInstance.getUserGroups(opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  If provided, will return group_users of this user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **groupId** | **Number**| Group ID.  If provided, will return group_users of this group. | [optional] 

### Return type

[**[GroupUserEntity]**](GroupUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserPublicKeys

> [PublicKeyEntity] getUserPublicKeys(opts)

List Public Keys

List Public Keys

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UserApi();
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getUserPublicKeys(opts, (error, data, response) => {
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

### Return type

[**[PublicKeyEntity]**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchUser

> UserEntity patchUser(opts)

Update User

Update User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UserApi();
let opts = {
  'allowedIps': "allowedIps_example", // String | A list of allowed IPs if applicable.  Newline delimited
  'announcementsRead': true, // Boolean | Signifies that the user has read all the announcements in the UI.
  'attachmentsPermission': true, // Boolean | DEPRECATED: Can the user create Bundles (aka Share Links)? Use the bundle permission instead.
  'authenticateUntil': new Date("2013-10-20T19:20:30+01:00"), // Date | Scheduled Date/Time at which user will be deactivated
  'authenticationMethod': "authenticationMethod_example", // String | How is this user authenticated?
  'avatarDelete': true, // Boolean | If true, the avatar will be deleted.
  'avatarFile': "/path/to/file", // File | An image file for your user avatar.
  'billingPermission': true, // Boolean | Allow this user to perform operations on the account, payments, and invoices?
  'bypassInactiveDisable': true, // Boolean | Exempt this user from being disabled based on inactivity?
  'bypassSiteAllowedIps': true, // Boolean | Allow this user to skip site-wide IP blacklists?
  'changePassword': "changePassword_example", // String | Used for changing a password on an existing user.
  'changePasswordConfirmation': "changePasswordConfirmation_example", // String | Optional, but if provided, we will ensure that it matches the value sent in `change_password`.
  'company': "company_example", // String | User's company
  'davPermission': true, // Boolean | Can the user connect with WebDAV?
  'disabled': true, // Boolean | Is user disabled? Disabled users cannot log in, and do not count for billing purposes.  Users can be automatically disabled after an inactivity period via a Site setting.
  'email': "email_example", // String | User's email.
  'ftpPermission': true, // Boolean | Can the user access with FTP/FTPS?
  'grantPermission': "grantPermission_example", // String | Permission to grant on the user root.  Can be blank or `full`, `read`, `write`, `list`, `read+write`, or `list+write`
  'groupId': 56, // Number | Group ID to associate this user with.
  'groupIds': "groupIds_example", // String | A list of group ids to associate this user with.  Comma delimited.
  'headerText': "headerText_example", // String | Text to display to the user in the header of the UI
  'importedPasswordHash': "importedPasswordHash_example", // String | Pre-calculated hash of the user's password. If supplied, this will be used to authenticate the user on first login. Supported hash menthods are MD5, SHA1, and SHA256.
  'language': "language_example", // String | Preferred language
  'name': "name_example", // String | User's full name
  'notes': "notes_example", // String | Any internal notes on the user
  'notificationDailySendTime': 56, // Number | Hour of the day at which daily notifications should be sent. Can be in range 0 to 23
  'officeIntegrationEnabled': true, // Boolean | Enable integration with Office for the web?
  'password': "password_example", // String | User password.
  'passwordConfirmation': "passwordConfirmation_example", // String | Optional, but if provided, we will ensure that it matches the value sent in `password`.
  'passwordValidityDays': 56, // Number | Number of days to allow user to use the same password
  'receiveAdminAlerts': true, // Boolean | Should the user receive admin alerts such a certificate expiration notifications and overages?
  'require2fa': "require2fa_example", // String | 2FA required setting
  'requirePasswordChange': true, // Boolean | Is a password change required upon next user login?
  'restapiPermission': true, // Boolean | Can this user access the REST API?
  'selfManaged': true, // Boolean | Does this user manage it's own credentials or is it a shared/bot user?
  'sftpPermission': true, // Boolean | Can the user access with SFTP?
  'siteAdmin': true, // Boolean | Is the user an administrator for this site?
  'skipWelcomeScreen': true, // Boolean | Skip Welcome page in the UI?
  'sslRequired': "sslRequired_example", // String | SSL required setting
  'ssoStrategyId': 56, // Number | SSO (Single Sign On) strategy ID for the user, if applicable.
  'subscribeToNewsletter': true, // Boolean | Is the user subscribed to the newsletter?
  'timeZone': "timeZone_example", // String | User time zone
  'userRoot': "userRoot_example", // String | Root folder for FTP (and optionally SFTP if the appropriate site-wide setting is set.)  Note that this is not used for API, Desktop, or Web interface.
  'username': "username_example" // String | User's username
};
apiInstance.patchUser(opts, (error, data, response) => {
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
 **allowedIps** | **String**| A list of allowed IPs if applicable.  Newline delimited | [optional] 
 **announcementsRead** | **Boolean**| Signifies that the user has read all the announcements in the UI. | [optional] 
 **attachmentsPermission** | **Boolean**| DEPRECATED: Can the user create Bundles (aka Share Links)? Use the bundle permission instead. | [optional] 
 **authenticateUntil** | **Date**| Scheduled Date/Time at which user will be deactivated | [optional] 
 **authenticationMethod** | **String**| How is this user authenticated? | [optional] 
 **avatarDelete** | **Boolean**| If true, the avatar will be deleted. | [optional] 
 **avatarFile** | **File**| An image file for your user avatar. | [optional] 
 **billingPermission** | **Boolean**| Allow this user to perform operations on the account, payments, and invoices? | [optional] 
 **bypassInactiveDisable** | **Boolean**| Exempt this user from being disabled based on inactivity? | [optional] 
 **bypassSiteAllowedIps** | **Boolean**| Allow this user to skip site-wide IP blacklists? | [optional] 
 **changePassword** | **String**| Used for changing a password on an existing user. | [optional] 
 **changePasswordConfirmation** | **String**| Optional, but if provided, we will ensure that it matches the value sent in &#x60;change_password&#x60;. | [optional] 
 **company** | **String**| User&#39;s company | [optional] 
 **davPermission** | **Boolean**| Can the user connect with WebDAV? | [optional] 
 **disabled** | **Boolean**| Is user disabled? Disabled users cannot log in, and do not count for billing purposes.  Users can be automatically disabled after an inactivity period via a Site setting. | [optional] 
 **email** | **String**| User&#39;s email. | [optional] 
 **ftpPermission** | **Boolean**| Can the user access with FTP/FTPS? | [optional] 
 **grantPermission** | **String**| Permission to grant on the user root.  Can be blank or &#x60;full&#x60;, &#x60;read&#x60;, &#x60;write&#x60;, &#x60;list&#x60;, &#x60;read+write&#x60;, or &#x60;list+write&#x60; | [optional] 
 **groupId** | **Number**| Group ID to associate this user with. | [optional] 
 **groupIds** | **String**| A list of group ids to associate this user with.  Comma delimited. | [optional] 
 **headerText** | **String**| Text to display to the user in the header of the UI | [optional] 
 **importedPasswordHash** | **String**| Pre-calculated hash of the user&#39;s password. If supplied, this will be used to authenticate the user on first login. Supported hash menthods are MD5, SHA1, and SHA256. | [optional] 
 **language** | **String**| Preferred language | [optional] 
 **name** | **String**| User&#39;s full name | [optional] 
 **notes** | **String**| Any internal notes on the user | [optional] 
 **notificationDailySendTime** | **Number**| Hour of the day at which daily notifications should be sent. Can be in range 0 to 23 | [optional] 
 **officeIntegrationEnabled** | **Boolean**| Enable integration with Office for the web? | [optional] 
 **password** | **String**| User password. | [optional] 
 **passwordConfirmation** | **String**| Optional, but if provided, we will ensure that it matches the value sent in &#x60;password&#x60;. | [optional] 
 **passwordValidityDays** | **Number**| Number of days to allow user to use the same password | [optional] 
 **receiveAdminAlerts** | **Boolean**| Should the user receive admin alerts such a certificate expiration notifications and overages? | [optional] 
 **require2fa** | **String**| 2FA required setting | [optional] 
 **requirePasswordChange** | **Boolean**| Is a password change required upon next user login? | [optional] 
 **restapiPermission** | **Boolean**| Can this user access the REST API? | [optional] 
 **selfManaged** | **Boolean**| Does this user manage it&#39;s own credentials or is it a shared/bot user? | [optional] 
 **sftpPermission** | **Boolean**| Can the user access with SFTP? | [optional] 
 **siteAdmin** | **Boolean**| Is the user an administrator for this site? | [optional] 
 **skipWelcomeScreen** | **Boolean**| Skip Welcome page in the UI? | [optional] 
 **sslRequired** | **String**| SSL required setting | [optional] 
 **ssoStrategyId** | **Number**| SSO (Single Sign On) strategy ID for the user, if applicable. | [optional] 
 **subscribeToNewsletter** | **Boolean**| Is the user subscribed to the newsletter? | [optional] 
 **timeZone** | **String**| User time zone | [optional] 
 **userRoot** | **String**| Root folder for FTP (and optionally SFTP if the appropriate site-wide setting is set.)  Note that this is not used for API, Desktop, or Web interface. | [optional] 
 **username** | **String**| User&#39;s username | [optional] 

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postUserApiKeys

> ApiKeyEntity postUserApiKeys(opts)

Create Api Key

Create Api Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UserApi();
let opts = {
  'description': "description_example", // String | User-supplied description of API key.
  'expiresAt': new Date("2013-10-20T19:20:30+01:00"), // Date | API Key expiration date
  'name': "name_example", // String | Internal name for the API Key.  For your use.
  'path': "path_example", // String | Folder path restriction for this api key.
  'permissionSet': "'full'", // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postUserApiKeys(opts, (error, data, response) => {
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


## postUserPublicKeys

> PublicKeyEntity postUserPublicKeys(publicKey, title, opts)

Create Public Key

Create Public Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UserApi();
let publicKey = "publicKey_example"; // String | Actual contents of SSH key.
let title = "title_example"; // String | Internal reference for key.
let opts = {
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postUserPublicKeys(publicKey, title, opts, (error, data, response) => {
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
 **publicKey** | **String**| Actual contents of SSH key. | 
 **title** | **String**| Internal reference for key. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 

### Return type

[**PublicKeyEntity**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

