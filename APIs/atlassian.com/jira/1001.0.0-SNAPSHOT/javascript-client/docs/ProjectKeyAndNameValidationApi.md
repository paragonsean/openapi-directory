# TheJiraCloudPlatformRestApi.ProjectKeyAndNameValidationApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getValidProjectKey**](ProjectKeyAndNameValidationApi.md#getValidProjectKey) | **GET** /rest/api/3/projectvalidate/validProjectKey | Get valid project key
[**getValidProjectName**](ProjectKeyAndNameValidationApi.md#getValidProjectName) | **GET** /rest/api/3/projectvalidate/validProjectName | Get valid project name
[**validateProjectKey**](ProjectKeyAndNameValidationApi.md#validateProjectKey) | **GET** /rest/api/3/projectvalidate/key | Validate project key



## getValidProjectKey

> String getValidProjectKey(opts)

Get valid project key

Validates a project key and, if the key is invalid or in use, generates a valid random string for the project key.  **[Permissions](#permissions) required:** None.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.ProjectKeyAndNameValidationApi();
let opts = {
  'key': "HSP" // String | The project key.
};
apiInstance.getValidProjectKey(opts, (error, data, response) => {
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
 **key** | **String**| The project key. | [optional] 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getValidProjectName

> String getValidProjectName(name)

Get valid project name

Checks that a project name isn&#39;t in use. If the name isn&#39;t in use, the passed string is returned. If the name is in use, this operation attempts to generate a valid project name based on the one supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404 response is returned.  **[Permissions](#permissions) required:** None.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.ProjectKeyAndNameValidationApi();
let name = "name_example"; // String | The project name.
apiInstance.getValidProjectName(name, (error, data, response) => {
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
 **name** | **String**| The project name. | 

### Return type

**String**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## validateProjectKey

> ErrorCollection validateProjectKey(opts)

Validate project key

Validates a project key by confirming the key is a valid string and not in use.  **[Permissions](#permissions) required:** None.

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

let apiInstance = new TheJiraCloudPlatformRestApi.ProjectKeyAndNameValidationApi();
let opts = {
  'key': "HSP" // String | The project key.
};
apiInstance.validateProjectKey(opts, (error, data, response) => {
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
 **key** | **String**| The project key. | [optional] 

### Return type

[**ErrorCollection**](ErrorCollection.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

