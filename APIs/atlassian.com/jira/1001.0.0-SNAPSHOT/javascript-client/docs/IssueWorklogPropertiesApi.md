# TheJiraCloudPlatformRestApi.IssueWorklogPropertiesApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteWorklogProperty**](IssueWorklogPropertiesApi.md#deleteWorklogProperty) | **DELETE** /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey} | Delete worklog property
[**getWorklogProperty**](IssueWorklogPropertiesApi.md#getWorklogProperty) | **GET** /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey} | Get worklog property
[**getWorklogPropertyKeys**](IssueWorklogPropertiesApi.md#getWorklogPropertyKeys) | **GET** /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties | Get worklog property keys
[**setWorklogProperty**](IssueWorklogPropertiesApi.md#setWorklogProperty) | **PUT** /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey} | Set worklog property



## deleteWorklogProperty

> deleteWorklogProperty(issueIdOrKey, worklogId, propertyKey)

Delete worklog property

Deletes a worklog property.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueWorklogPropertiesApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | The ID or key of the issue.
let worklogId = "worklogId_example"; // String | The ID of the worklog.
let propertyKey = "propertyKey_example"; // String | The key of the property.
apiInstance.deleteWorklogProperty(issueIdOrKey, worklogId, propertyKey, (error, data, response) => {
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
 **issueIdOrKey** | **String**| The ID or key of the issue. | 
 **worklogId** | **String**| The ID of the worklog. | 
 **propertyKey** | **String**| The key of the property. | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getWorklogProperty

> EntityProperty getWorklogProperty(issueIdOrKey, worklogId, propertyKey)

Get worklog property

Returns the value of a worklog property.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueWorklogPropertiesApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | The ID or key of the issue.
let worklogId = "worklogId_example"; // String | The ID of the worklog.
let propertyKey = "propertyKey_example"; // String | The key of the property.
apiInstance.getWorklogProperty(issueIdOrKey, worklogId, propertyKey, (error, data, response) => {
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
 **issueIdOrKey** | **String**| The ID or key of the issue. | 
 **worklogId** | **String**| The ID of the worklog. | 
 **propertyKey** | **String**| The key of the property. | 

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWorklogPropertyKeys

> PropertyKeys getWorklogPropertyKeys(issueIdOrKey, worklogId)

Get worklog property keys

Returns the keys of all properties for a worklog.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueWorklogPropertiesApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | The ID or key of the issue.
let worklogId = "worklogId_example"; // String | The ID of the worklog.
apiInstance.getWorklogPropertyKeys(issueIdOrKey, worklogId, (error, data, response) => {
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
 **issueIdOrKey** | **String**| The ID or key of the issue. | 
 **worklogId** | **String**| The ID of the worklog. | 

### Return type

[**PropertyKeys**](PropertyKeys.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setWorklogProperty

> Object setWorklogProperty(issueIdOrKey, worklogId, propertyKey, body)

Set worklog property

Sets the value of a worklog property. Use this operation to store custom data against the worklog.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  *Edit all worklogs*[ project permission](https://confluence.atlassian.com/x/yodKLg) to update any worklog or *Edit own worklogs* to update worklogs created by the user.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueWorklogPropertiesApi();
let issueIdOrKey = "issueIdOrKey_example"; // String | The ID or key of the issue.
let worklogId = "worklogId_example"; // String | The ID of the worklog.
let propertyKey = "propertyKey_example"; // String | The key of the issue property. The maximum length is 255 characters.
let body = null; // Object | 
apiInstance.setWorklogProperty(issueIdOrKey, worklogId, propertyKey, body, (error, data, response) => {
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
 **issueIdOrKey** | **String**| The ID or key of the issue. | 
 **worklogId** | **String**| The ID of the worklog. | 
 **propertyKey** | **String**| The key of the issue property. The maximum length is 255 characters. | 
 **body** | **Object**|  | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

