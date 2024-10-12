# TheJiraCloudPlatformRestApi.DynamicModulesApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dynamicModulesResourceGetModulesGet**](DynamicModulesApi.md#dynamicModulesResourceGetModulesGet) | **GET** /rest/atlassian-connect/1/app/module/dynamic | Get modules
[**dynamicModulesResourceRegisterModulesPost**](DynamicModulesApi.md#dynamicModulesResourceRegisterModulesPost) | **POST** /rest/atlassian-connect/1/app/module/dynamic | Register modules
[**dynamicModulesResourceRemoveModulesDelete**](DynamicModulesApi.md#dynamicModulesResourceRemoveModulesDelete) | **DELETE** /rest/atlassian-connect/1/app/module/dynamic | Remove modules



## dynamicModulesResourceGetModulesGet

> ConnectModules dynamicModulesResourceGetModulesGet()

Get modules

Returns all modules registered dynamically by the calling app.  **[Permissions](#permissions) required:** Only Connect apps can make this request.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';

let apiInstance = new TheJiraCloudPlatformRestApi.DynamicModulesApi();
apiInstance.dynamicModulesResourceGetModulesGet((error, data, response) => {
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

[**ConnectModules**](ConnectModules.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dynamicModulesResourceRegisterModulesPost

> dynamicModulesResourceRegisterModulesPost(connectModules)

Register modules

Registers a list of modules.  **[Permissions](#permissions) required:** Only Connect apps can make this request.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';

let apiInstance = new TheJiraCloudPlatformRestApi.DynamicModulesApi();
let connectModules = new TheJiraCloudPlatformRestApi.ConnectModules(); // ConnectModules | 
apiInstance.dynamicModulesResourceRegisterModulesPost(connectModules, (error, data, response) => {
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
 **connectModules** | [**ConnectModules**](ConnectModules.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dynamicModulesResourceRemoveModulesDelete

> dynamicModulesResourceRemoveModulesDelete(opts)

Remove modules

Remove all or a list of modules registered by the calling app.  **[Permissions](#permissions) required:** Only Connect apps can make this request.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';

let apiInstance = new TheJiraCloudPlatformRestApi.DynamicModulesApi();
let opts = {
  'moduleKey': ["null"] // [String] | The key of the module to remove. To include multiple module keys, provide multiple copies of this parameter. For example, `moduleKey=dynamic-attachment-entity-property&moduleKey=dynamic-select-field`. Nonexistent keys are ignored.
};
apiInstance.dynamicModulesResourceRemoveModulesDelete(opts, (error, data, response) => {
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
 **moduleKey** | [**[String]**](String.md)| The key of the module to remove. To include multiple module keys, provide multiple copies of this parameter. For example, &#x60;moduleKey&#x3D;dynamic-attachment-entity-property&amp;moduleKey&#x3D;dynamic-select-field&#x60;. Nonexistent keys are ignored. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

