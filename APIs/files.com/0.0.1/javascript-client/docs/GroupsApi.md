# FilesComApi.GroupsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteGroupsGroupIdMembershipsUserId**](GroupsApi.md#deleteGroupsGroupIdMembershipsUserId) | **DELETE** /groups/{group_id}/memberships/{user_id} | Delete Group User
[**deleteGroupsId**](GroupsApi.md#deleteGroupsId) | **DELETE** /groups/{id} | Delete Group
[**getGroups**](GroupsApi.md#getGroups) | **GET** /groups | List Groups
[**getGroupsGroupIdPermissions**](GroupsApi.md#getGroupsGroupIdPermissions) | **GET** /groups/{group_id}/permissions | List Permissions
[**getGroupsGroupIdUsers**](GroupsApi.md#getGroupsGroupIdUsers) | **GET** /groups/{group_id}/users | List Group Users
[**getGroupsId**](GroupsApi.md#getGroupsId) | **GET** /groups/{id} | Show Group
[**patchGroupsGroupIdMembershipsUserId**](GroupsApi.md#patchGroupsGroupIdMembershipsUserId) | **PATCH** /groups/{group_id}/memberships/{user_id} | Update Group User
[**patchGroupsId**](GroupsApi.md#patchGroupsId) | **PATCH** /groups/{id} | Update Group
[**postGroups**](GroupsApi.md#postGroups) | **POST** /groups | Create Group
[**postGroupsGroupIdUsers**](GroupsApi.md#postGroupsGroupIdUsers) | **POST** /groups/{group_id}/users | Create User



## deleteGroupsGroupIdMembershipsUserId

> deleteGroupsGroupIdMembershipsUserId(groupId, userId)

Delete Group User

Delete Group User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupsApi();
let groupId = 56; // Number | Group ID from which to remove user.
let userId = 56; // Number | User ID to remove from group.
apiInstance.deleteGroupsGroupIdMembershipsUserId(groupId, userId, (error, data, response) => {
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
 **groupId** | **Number**| Group ID from which to remove user. | 
 **userId** | **Number**| User ID to remove from group. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteGroupsId

> deleteGroupsId(id)

Delete Group

Delete Group

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupsApi();
let id = 56; // Number | Group ID.
apiInstance.deleteGroupsId(id, (error, data, response) => {
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
 **id** | **Number**| Group ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGroups

> [GroupEntity] getGroups(opts)

List Groups

List Groups

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[name]=desc`). Valid fields are `name`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `name`.
  'filterPrefix': {key: null}, // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `name`.
  'ids': "ids_example" // String | Comma-separated list of group ids to include in results.
};
apiInstance.getGroups(opts, (error, data, response) => {
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
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[name]&#x3D;desc&#x60;). Valid fields are &#x60;name&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;name&#x60;. | [optional] 
 **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;name&#x60;. | [optional] 
 **ids** | **String**| Comma-separated list of group ids to include in results. | [optional] 

### Return type

[**[GroupEntity]**](GroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupsGroupIdPermissions

> [PermissionEntity] getGroupsGroupIdPermissions(groupId, opts)

List Permissions

List Permissions

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupsApi();
let groupId = "groupId_example"; // String | DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use `filter[group_id]` instead.`
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[group_id]=desc`). Valid fields are `group_id`, `path`, `user_id` or `permission`.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `group_id`, `user_id` or `path`. Valid field combinations are `[ group_id, path ]` and `[ user_id, path ]`.
  'filterPrefix': {key: null}, // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `path`.
  'path': "path_example", // String | DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use `filter[path]` instead.
  'userId': "userId_example", // String | DEPRECATED: User ID.  If provided, will scope permissions to this user. Use `filter[user_id]` instead.`
  'includeGroups': true // Boolean | If searching by user or group, also include user's permissions that are inherited from its groups?
};
apiInstance.getGroupsGroupIdPermissions(groupId, opts, (error, data, response) => {
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
 **groupId** | **String**| DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use &#x60;filter[group_id]&#x60; instead.&#x60; | 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[group_id]&#x3D;desc&#x60;). Valid fields are &#x60;group_id&#x60;, &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;permission&#x60;. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;group_id&#x60;, &#x60;user_id&#x60; or &#x60;path&#x60;. Valid field combinations are &#x60;[ group_id, path ]&#x60; and &#x60;[ user_id, path ]&#x60;. | [optional] 
 **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;. | [optional] 
 **path** | **String**| DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use &#x60;filter[path]&#x60; instead. | [optional] 
 **userId** | **String**| DEPRECATED: User ID.  If provided, will scope permissions to this user. Use &#x60;filter[user_id]&#x60; instead.&#x60; | [optional] 
 **includeGroups** | **Boolean**| If searching by user or group, also include user&#39;s permissions that are inherited from its groups? | [optional] 

### Return type

[**[PermissionEntity]**](PermissionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupsGroupIdUsers

> [GroupUserEntity] getGroupsGroupIdUsers(groupId, opts)

List Group Users

List Group Users

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupsApi();
let groupId = 56; // Number | Group ID.  If provided, will return group_users of this group.
let opts = {
  'userId': 56, // Number | User ID.  If provided, will return group_users of this user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getGroupsGroupIdUsers(groupId, opts, (error, data, response) => {
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
 **groupId** | **Number**| Group ID.  If provided, will return group_users of this group. | 
 **userId** | **Number**| User ID.  If provided, will return group_users of this user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[GroupUserEntity]**](GroupUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGroupsId

> GroupEntity getGroupsId(id)

Show Group

Show Group

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupsApi();
let id = 56; // Number | Group ID.
apiInstance.getGroupsId(id, (error, data, response) => {
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
 **id** | **Number**| Group ID. | 

### Return type

[**GroupEntity**](GroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchGroupsGroupIdMembershipsUserId

> GroupUserEntity patchGroupsGroupIdMembershipsUserId(groupId, userId, opts)

Update Group User

Update Group User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupsApi();
let groupId = 56; // Number | Group ID to add user to.
let userId = 56; // Number | User ID to add to group.
let opts = {
  'admin': true // Boolean | Is the user a group administrator?
};
apiInstance.patchGroupsGroupIdMembershipsUserId(groupId, userId, opts, (error, data, response) => {
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
 **groupId** | **Number**| Group ID to add user to. | 
 **userId** | **Number**| User ID to add to group. | 
 **admin** | **Boolean**| Is the user a group administrator? | [optional] 

### Return type

[**GroupUserEntity**](GroupUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## patchGroupsId

> GroupEntity patchGroupsId(id, opts)

Update Group

Update Group

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupsApi();
let id = 56; // Number | Group ID.
let opts = {
  'adminIds': "adminIds_example", // String | A list of group admin user ids. If sent as a string, should be comma-delimited.
  'name': "name_example", // String | Group name.
  'notes': "notes_example", // String | Group notes.
  'userIds': "userIds_example" // String | A list of user ids. If sent as a string, should be comma-delimited.
};
apiInstance.patchGroupsId(id, opts, (error, data, response) => {
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
 **id** | **Number**| Group ID. | 
 **adminIds** | **String**| A list of group admin user ids. If sent as a string, should be comma-delimited. | [optional] 
 **name** | **String**| Group name. | [optional] 
 **notes** | **String**| Group notes. | [optional] 
 **userIds** | **String**| A list of user ids. If sent as a string, should be comma-delimited. | [optional] 

### Return type

[**GroupEntity**](GroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postGroups

> GroupEntity postGroups(opts)

Create Group

Create Group

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupsApi();
let opts = {
  'adminIds': "adminIds_example", // String | A list of group admin user ids. If sent as a string, should be comma-delimited.
  'name': "name_example", // String | Group name.
  'notes': "notes_example", // String | Group notes.
  'userIds': "userIds_example" // String | A list of user ids. If sent as a string, should be comma-delimited.
};
apiInstance.postGroups(opts, (error, data, response) => {
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
 **adminIds** | **String**| A list of group admin user ids. If sent as a string, should be comma-delimited. | [optional] 
 **name** | **String**| Group name. | [optional] 
 **notes** | **String**| Group notes. | [optional] 
 **userIds** | **String**| A list of user ids. If sent as a string, should be comma-delimited. | [optional] 

### Return type

[**GroupEntity**](GroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postGroupsGroupIdUsers

> UserEntity postGroupsGroupIdUsers(groupId, opts)

Create User

Create User

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.GroupsApi();
let groupId = 56; // Number | Group ID to associate this user with.
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
apiInstance.postGroupsGroupIdUsers(groupId, opts, (error, data, response) => {
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
 **groupId** | **Number**| Group ID to associate this user with. | 
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

