# TheJiraCloudPlatformRestApi.ApplicationRolesApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllApplicationRoles**](ApplicationRolesApi.md#getAllApplicationRoles) | **GET** /rest/api/3/applicationrole | Get all application roles
[**getApplicationRole**](ApplicationRolesApi.md#getApplicationRole) | **GET** /rest/api/3/applicationrole/{key} | Get application role



## getAllApplicationRoles

> [ApplicationRole] getAllApplicationRoles()

Get all application roles

Returns all application roles. In Jira, application roles are managed using the [Application access configuration](https://confluence.atlassian.com/x/3YxjL) page.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.ApplicationRolesApi();
apiInstance.getAllApplicationRoles((error, data, response) => {
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

[**[ApplicationRole]**](ApplicationRole.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationRole

> ApplicationRole getApplicationRole(key)

Get application role

Returns an application role.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.ApplicationRolesApi();
let key = "jira-software"; // String | The key of the application role. Use the [Get all application roles](#api-rest-api-3-applicationrole-get) operation to get the key for each application role.
apiInstance.getApplicationRole(key, (error, data, response) => {
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
 **key** | **String**| The key of the application role. Use the [Get all application roles](#api-rest-api-3-applicationrole-get) operation to get the key for each application role. | 

### Return type

[**ApplicationRole**](ApplicationRole.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

