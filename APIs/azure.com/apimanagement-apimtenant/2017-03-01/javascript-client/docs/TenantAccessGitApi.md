# ApiManagementClient.TenantAccessGitApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenantAccessGitGet**](TenantAccessGitApi.md#tenantAccessGitGet) | **GET** /tenant/{accessName}/git | 
[**tenantAccessGitRegeneratePrimaryKey**](TenantAccessGitApi.md#tenantAccessGitRegeneratePrimaryKey) | **POST** /tenant/{accessName}/git/regeneratePrimaryKey | 
[**tenantAccessGitRegenerateSecondaryKey**](TenantAccessGitApi.md#tenantAccessGitRegenerateSecondaryKey) | **POST** /tenant/{accessName}/git/regenerateSecondaryKey | 



## tenantAccessGitGet

> AccessInformationContract tenantAccessGitGet(apiVersion, accessName)



Gets the Git access configuration for the tenant.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantAccessGitApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let accessName = "accessName_example"; // String | The identifier of the Access configuration.
apiInstance.tenantAccessGitGet(apiVersion, accessName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **accessName** | **String**| The identifier of the Access configuration. | 

### Return type

[**AccessInformationContract**](AccessInformationContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tenantAccessGitRegeneratePrimaryKey

> tenantAccessGitRegeneratePrimaryKey(apiVersion, accessName)



Regenerate primary access key for GIT.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantAccessGitApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let accessName = "accessName_example"; // String | The identifier of the Access configuration.
apiInstance.tenantAccessGitRegeneratePrimaryKey(apiVersion, accessName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **accessName** | **String**| The identifier of the Access configuration. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tenantAccessGitRegenerateSecondaryKey

> tenantAccessGitRegenerateSecondaryKey(apiVersion, accessName)



Regenerate secondary access key for GIT.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantAccessGitApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let accessName = "accessName_example"; // String | The identifier of the Access configuration.
apiInstance.tenantAccessGitRegenerateSecondaryKey(apiVersion, accessName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **accessName** | **String**| The identifier of the Access configuration. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

