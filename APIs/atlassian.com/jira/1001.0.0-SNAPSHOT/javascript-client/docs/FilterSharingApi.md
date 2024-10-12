# TheJiraCloudPlatformRestApi.FilterSharingApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSharePermission**](FilterSharingApi.md#addSharePermission) | **POST** /rest/api/3/filter/{id}/permission | Add share permission
[**deleteSharePermission**](FilterSharingApi.md#deleteSharePermission) | **DELETE** /rest/api/3/filter/{id}/permission/{permissionId} | Delete share permission
[**getDefaultShareScope**](FilterSharingApi.md#getDefaultShareScope) | **GET** /rest/api/3/filter/defaultShareScope | Get default share scope
[**getSharePermission**](FilterSharingApi.md#getSharePermission) | **GET** /rest/api/3/filter/{id}/permission/{permissionId} | Get share permission
[**getSharePermissions**](FilterSharingApi.md#getSharePermissions) | **GET** /rest/api/3/filter/{id}/permission | Get share permissions
[**setDefaultShareScope**](FilterSharingApi.md#setDefaultShareScope) | **PUT** /rest/api/3/filter/defaultShareScope | Set default share scope



## addSharePermission

> [SharePermission] addSharePermission(id, sharePermissionInputBean)

Add share permission

Add a share permissions to a filter. If you add a global share permission (one for all logged-in users or the public) it will overwrite all share permissions for the filter.  Be aware that this operation uses different objects for updating share permissions compared to [Update filter](#api-rest-api-3-filter-id-put).  **[Permissions](#permissions) required:** *Share dashboards and filters* [global permission](https://confluence.atlassian.com/x/x4dKLg) and the user must own the filter.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.FilterSharingApi();
let id = 789; // Number | The ID of the filter.
let sharePermissionInputBean = {"groupname":"jira-administrators","rights":1,"type":"group"}; // SharePermissionInputBean | 
apiInstance.addSharePermission(id, sharePermissionInputBean, (error, data, response) => {
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
 **id** | **Number**| The ID of the filter. | 
 **sharePermissionInputBean** | [**SharePermissionInputBean**](SharePermissionInputBean.md)|  | 

### Return type

[**[SharePermission]**](SharePermission.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSharePermission

> deleteSharePermission(id, permissionId)

Delete share permission

Deletes a share permission from a filter.  **[Permissions](#permissions) required:** Permission to access Jira and the user must own the filter.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.FilterSharingApi();
let id = 789; // Number | The ID of the filter.
let permissionId = 789; // Number | The ID of the share permission.
apiInstance.deleteSharePermission(id, permissionId, (error, data, response) => {
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
 **id** | **Number**| The ID of the filter. | 
 **permissionId** | **Number**| The ID of the share permission. | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDefaultShareScope

> DefaultShareScope getDefaultShareScope()

Get default share scope

Returns the default sharing settings for new filters and dashboards for a user.  **[Permissions](#permissions) required:** Permission to access Jira.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.FilterSharingApi();
apiInstance.getDefaultShareScope((error, data, response) => {
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

[**DefaultShareScope**](DefaultShareScope.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSharePermission

> SharePermission getSharePermission(id, permissionId)

Get share permission

Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, a share permission is only returned for:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.FilterSharingApi();
let id = 789; // Number | The ID of the filter.
let permissionId = 789; // Number | The ID of the share permission.
apiInstance.getSharePermission(id, permissionId, (error, data, response) => {
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
 **id** | **Number**| The ID of the filter. | 
 **permissionId** | **Number**| The ID of the share permission. | 

### Return type

[**SharePermission**](SharePermission.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSharePermissions

> [SharePermission] getSharePermissions(id)

Get share permissions

Returns the share permissions for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, share permissions are only returned for:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.FilterSharingApi();
let id = 789; // Number | The ID of the filter.
apiInstance.getSharePermissions(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the filter. | 

### Return type

[**[SharePermission]**](SharePermission.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setDefaultShareScope

> DefaultShareScope setDefaultShareScope(defaultShareScope)

Set default share scope

Sets the default sharing for new filters and dashboards for a user.  **[Permissions](#permissions) required:** Permission to access Jira.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.FilterSharingApi();
let defaultShareScope = {"scope":"GLOBAL"}; // DefaultShareScope | 
apiInstance.setDefaultShareScope(defaultShareScope, (error, data, response) => {
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
 **defaultShareScope** | [**DefaultShareScope**](DefaultShareScope.md)|  | 

### Return type

[**DefaultShareScope**](DefaultShareScope.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

