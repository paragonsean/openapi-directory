# FilesComApi.UsersApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUsersId**](UsersApi.md#deleteUsersId) | **DELETE** /users/{id} | Delete User
[**getUsers**](UsersApi.md#getUsers) | **GET** /users | List Users
[**getUsersId**](UsersApi.md#getUsersId) | **GET** /users/{id} | Show User
[**getUsersUserIdApiKeys**](UsersApi.md#getUsersUserIdApiKeys) | **GET** /users/{user_id}/api_keys | List Api Keys
[**getUsersUserIdCipherUses**](UsersApi.md#getUsersUserIdCipherUses) | **GET** /users/{user_id}/cipher_uses | List User Cipher Uses
[**getUsersUserIdGroups**](UsersApi.md#getUsersUserIdGroups) | **GET** /users/{user_id}/groups | List Group Users
[**getUsersUserIdPermissions**](UsersApi.md#getUsersUserIdPermissions) | **GET** /users/{user_id}/permissions | List Permissions
[**getUsersUserIdPublicKeys**](UsersApi.md#getUsersUserIdPublicKeys) | **GET** /users/{user_id}/public_keys | List Public Keys
[**patchUsersId**](UsersApi.md#patchUsersId) | **PATCH** /users/{id} | Update User
[**postUsers**](UsersApi.md#postUsers) | **POST** /users | Create User
[**postUsersId2faReset**](UsersApi.md#postUsersId2faReset) | **POST** /users/{id}/2fa/reset | Trigger 2FA Reset process for user who has lost access to their existing 2FA methods.
[**postUsersIdResendWelcomeEmail**](UsersApi.md#postUsersIdResendWelcomeEmail) | **POST** /users/{id}/resend_welcome_email | Resend user welcome email
[**postUsersIdUnlock**](UsersApi.md#postUsersIdUnlock) | **POST** /users/{id}/unlock | Unlock user who has been locked out due to failed logins.
[**postUsersUserIdApiKeys**](UsersApi.md#postUsersUserIdApiKeys) | **POST** /users/{user_id}/api_keys | Create Api Key
[**postUsersUserIdPublicKeys**](UsersApi.md#postUsersUserIdPublicKeys) | **POST** /users/{user_id}/public_keys | Create Public Key



## deleteUsersId

> deleteUsersId(id)

Delete User

Delete User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let id = 56; // Number | User ID.
apiInstance.deleteUsersId(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| User ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getUsers

> [UserEntity] getUsers(opts)

List Users

List Users

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[authenticate_until]=desc`). Valid fields are `authenticate_until`, `active`, `email`, `last_desktop_login_at`, `last_login_at`, `username`, `company`, `name`, `site_admin`, `receive_admin_alerts`, `password_validity_days`, `ssl_required` or `not_site_admin`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `username`, `email`, `company`, `site_admin`, `password_validity_days`, `ssl_required`, `last_login_at`, `authenticate_until` or `not_site_admin`. Valid field combinations are `[ not_site_admin, username ]`.
  'filterGt': {key: null}, // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `password_validity_days`, `last_login_at` or `authenticate_until`.
  'filterGteq': {key: null}, // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `password_validity_days`, `last_login_at` or `authenticate_until`.
  'filterPrefix': {key: null}, // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `username`, `email` or `company`.
  'filterLt': {key: null}, // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `password_validity_days`, `last_login_at` or `authenticate_until`.
  'filterLteq': {key: null}, // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `password_validity_days`, `last_login_at` or `authenticate_until`.
  'ids': "ids_example", // String | comma-separated list of User IDs
  'qUsername': "qUsername_example", // String | List users matching username.
  'qEmail': "qEmail_example", // String | List users matching email.
  'qNotes': "qNotes_example", // String | List users matching notes field.
  'qAdmin': "qAdmin_example", // String | If `true`, list only admin users.
  'qAllowedIps': "qAllowedIps_example", // String | If set, list only users with overridden allowed IP setting.
  'qPasswordValidityDays': "qPasswordValidityDays_example", // String | If set, list only users with overridden password validity days setting.
  'qSslRequired': "qSslRequired_example", // String | If set, list only users with overridden SSL required setting.
  'search': "search_example" // String | Searches for partial matches of name, username, or email.
};
apiInstance.getUsers(opts, (error, data, response) => {
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
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[authenticate_until]&#x3D;desc&#x60;). Valid fields are &#x60;authenticate_until&#x60;, &#x60;active&#x60;, &#x60;email&#x60;, &#x60;last_desktop_login_at&#x60;, &#x60;last_login_at&#x60;, &#x60;username&#x60;, &#x60;company&#x60;, &#x60;name&#x60;, &#x60;site_admin&#x60;, &#x60;receive_admin_alerts&#x60;, &#x60;password_validity_days&#x60;, &#x60;ssl_required&#x60; or &#x60;not_site_admin&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;username&#x60;, &#x60;email&#x60;, &#x60;company&#x60;, &#x60;site_admin&#x60;, &#x60;password_validity_days&#x60;, &#x60;ssl_required&#x60;, &#x60;last_login_at&#x60;, &#x60;authenticate_until&#x60; or &#x60;not_site_admin&#x60;. Valid field combinations are &#x60;[ not_site_admin, username ]&#x60;. | [optional] 
 **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;. | [optional] 
 **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;. | [optional] 
 **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;username&#x60;, &#x60;email&#x60; or &#x60;company&#x60;. | [optional] 
 **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;. | [optional] 
 **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;. | [optional] 
 **ids** | **String**| comma-separated list of User IDs | [optional] 
 **qUsername** | **String**| List users matching username. | [optional] 
 **qEmail** | **String**| List users matching email. | [optional] 
 **qNotes** | **String**| List users matching notes field. | [optional] 
 **qAdmin** | **String**| If &#x60;true&#x60;, list only admin users. | [optional] 
 **qAllowedIps** | **String**| If set, list only users with overridden allowed IP setting. | [optional] 
 **qPasswordValidityDays** | **String**| If set, list only users with overridden password validity days setting. | [optional] 
 **qSslRequired** | **String**| If set, list only users with overridden SSL required setting. | [optional] 
 **search** | **String**| Searches for partial matches of name, username, or email. | [optional] 

### Return type

[**[UserEntity]**](UserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersId

> UserEntity getUsersId(id)

Show User

Show User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let id = 56; // Number | User ID.
apiInstance.getUsersId(id, (error, data, response) => {
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
 **id** | **Number**| User ID. | 

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersUserIdApiKeys

> [ApiKeyEntity] getUsersUserIdApiKeys(userId, opts)

List Api Keys

List Api Keys

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let userId = 56; // Number | User ID.  Provide a value of `0` to operate the current session's user.
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[expires_at]=desc`). Valid fields are `expires_at`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `expires_at`.
  'filterGt': {key: null}, // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `expires_at`.
  'filterGteq': {key: null}, // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `expires_at`.
  'filterLt': {key: null}, // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `expires_at`.
  'filterLteq': {key: null} // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `expires_at`.
};
apiInstance.getUsersUserIdApiKeys(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | 
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


## getUsersUserIdCipherUses

> [UserCipherUseEntity] getUsersUserIdCipherUses(userId, opts)

List User Cipher Uses

List User Cipher Uses

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let userId = 56; // Number | User ID.  Provide a value of `0` to operate the current session's user.
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getUsersUserIdCipherUses(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[UserCipherUseEntity]**](UserCipherUseEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersUserIdGroups

> [GroupUserEntity] getUsersUserIdGroups(userId, opts)

List Group Users

List Group Users

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let userId = 56; // Number | User ID.  If provided, will return group_users of this user.
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'groupId': 56 // Number | Group ID.  If provided, will return group_users of this group.
};
apiInstance.getUsersUserIdGroups(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  If provided, will return group_users of this user. | 
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


## getUsersUserIdPermissions

> [PermissionEntity] getUsersUserIdPermissions(userId, opts)

List Permissions

List Permissions

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let userId = "userId_example"; // String | DEPRECATED: User ID.  If provided, will scope permissions to this user. Use `filter[user_id]` instead.`
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[group_id]=desc`). Valid fields are `group_id`, `path`, `user_id` or `permission`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `group_id`, `user_id` or `path`. Valid field combinations are `[ group_id, path ]` and `[ user_id, path ]`.
  'filterPrefix': {key: null}, // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `path`.
  'path': "path_example", // String | DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use `filter[path]` instead.
  'groupId': "groupId_example", // String | DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use `filter[group_id]` instead.`
  'includeGroups': true // Boolean | If searching by user or group, also include user's permissions that are inherited from its groups?
};
apiInstance.getUsersUserIdPermissions(userId, opts, (error, data, response) => {
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
 **userId** | **String**| DEPRECATED: User ID.  If provided, will scope permissions to this user. Use &#x60;filter[user_id]&#x60; instead.&#x60; | 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[group_id]&#x3D;desc&#x60;). Valid fields are &#x60;group_id&#x60;, &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;permission&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;group_id&#x60;, &#x60;user_id&#x60; or &#x60;path&#x60;. Valid field combinations are &#x60;[ group_id, path ]&#x60; and &#x60;[ user_id, path ]&#x60;. | [optional] 
 **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;. | [optional] 
 **path** | **String**| DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use &#x60;filter[path]&#x60; instead. | [optional] 
 **groupId** | **String**| DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use &#x60;filter[group_id]&#x60; instead.&#x60; | [optional] 
 **includeGroups** | **Boolean**| If searching by user or group, also include user&#39;s permissions that are inherited from its groups? | [optional] 

### Return type

[**[PermissionEntity]**](PermissionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersUserIdPublicKeys

> [PublicKeyEntity] getUsersUserIdPublicKeys(userId, opts)

List Public Keys

List Public Keys

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let userId = 56; // Number | User ID.  Provide a value of `0` to operate the current session's user.
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getUsersUserIdPublicKeys(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[PublicKeyEntity]**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchUsersId

> UserEntity patchUsersId(id, opts)

Update User

Update User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let id = 56; // Number | User ID.
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
apiInstance.patchUsersId(id, opts, (error, data, response) => {
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
 **id** | **Number**| User ID. | 
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


## postUsers

> UserEntity postUsers(opts)

Create User

Create User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
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
apiInstance.postUsers(opts, (error, data, response) => {
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


## postUsersId2faReset

> postUsersId2faReset(id)

Trigger 2FA Reset process for user who has lost access to their existing 2FA methods.

Trigger 2FA Reset process for user who has lost access to their existing 2FA methods.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let id = 56; // Number | User ID.
apiInstance.postUsersId2faReset(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| User ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postUsersIdResendWelcomeEmail

> postUsersIdResendWelcomeEmail(id)

Resend user welcome email

Resend user welcome email

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let id = 56; // Number | User ID.
apiInstance.postUsersIdResendWelcomeEmail(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| User ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postUsersIdUnlock

> postUsersIdUnlock(id)

Unlock user who has been locked out due to failed logins.

Unlock user who has been locked out due to failed logins.

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let id = 56; // Number | User ID.
apiInstance.postUsersIdUnlock(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| User ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postUsersUserIdApiKeys

> ApiKeyEntity postUsersUserIdApiKeys(userId, opts)

Create Api Key

Create Api Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let userId = 56; // Number | User ID.  Provide a value of `0` to operate the current session's user.
let opts = {
  'description': "description_example", // String | User-supplied description of API key.
  'expiresAt': new Date("2013-10-20T19:20:30+01:00"), // Date | API Key expiration date
  'name': "name_example", // String | Internal name for the API Key.  For your use.
  'path': "path_example", // String | Folder path restriction for this api key.
  'permissionSet': "'full'" // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
};
apiInstance.postUsersUserIdApiKeys(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | 
 **description** | **String**| User-supplied description of API key. | [optional] 
 **expiresAt** | **Date**| API Key expiration date | [optional] 
 **name** | **String**| Internal name for the API Key.  For your use. | [optional] 
 **path** | **String**| Folder path restriction for this api key. | [optional] 
 **permissionSet** | **String**| Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] [default to &#39;full&#39;]

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postUsersUserIdPublicKeys

> PublicKeyEntity postUsersUserIdPublicKeys(userId, publicKey, title)

Create Public Key

Create Public Key

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.UsersApi();
let userId = 56; // Number | User ID.  Provide a value of `0` to operate the current session's user.
let publicKey = "publicKey_example"; // String | Actual contents of SSH key.
let title = "title_example"; // String | Internal reference for key.
apiInstance.postUsersUserIdPublicKeys(userId, publicKey, title, (error, data, response) => {
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
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | 
 **publicKey** | **String**| Actual contents of SSH key. | 
 **title** | **String**| Internal reference for key. | 

### Return type

[**PublicKeyEntity**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

