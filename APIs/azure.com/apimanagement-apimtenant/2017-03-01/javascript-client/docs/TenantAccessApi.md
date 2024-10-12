# ApiManagementClient.TenantAccessApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenantAccessGet**](TenantAccessApi.md#tenantAccessGet) | **GET** /tenant/{accessName} | 
[**tenantAccessRegeneratePrimaryKey**](TenantAccessApi.md#tenantAccessRegeneratePrimaryKey) | **POST** /tenant/{accessName}/regeneratePrimaryKey | 
[**tenantAccessRegenerateSecondaryKey**](TenantAccessApi.md#tenantAccessRegenerateSecondaryKey) | **POST** /tenant/{accessName}/regenerateSecondaryKey | 
[**tenantAccessUpdate**](TenantAccessApi.md#tenantAccessUpdate) | **PATCH** /tenant/{accessName} | 



## tenantAccessGet

> AccessInformationContract tenantAccessGet(apiVersion, accessName)



Get tenant access information details.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantAccessApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let accessName = "accessName_example"; // String | The identifier of the Access configuration.
apiInstance.tenantAccessGet(apiVersion, accessName, (error, data, response) => {
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


## tenantAccessRegeneratePrimaryKey

> tenantAccessRegeneratePrimaryKey(apiVersion, accessName)



Regenerate primary access key.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantAccessApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let accessName = "accessName_example"; // String | The identifier of the Access configuration.
apiInstance.tenantAccessRegeneratePrimaryKey(apiVersion, accessName, (error, data, response) => {
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


## tenantAccessRegenerateSecondaryKey

> tenantAccessRegenerateSecondaryKey(apiVersion, accessName)



Regenerate secondary access key.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantAccessApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let accessName = "accessName_example"; // String | The identifier of the Access configuration.
apiInstance.tenantAccessRegenerateSecondaryKey(apiVersion, accessName, (error, data, response) => {
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


## tenantAccessUpdate

> tenantAccessUpdate(accessName, ifMatch, apiVersion, parameters)



Update tenant access information details.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.TenantAccessApi();
let accessName = "accessName_example"; // String | The identifier of the Access configuration.
let ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the property to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new ApiManagementClient.AccessInformationUpdateParameters(); // AccessInformationUpdateParameters | Parameters supplied to retrieve the Tenant Access Information.
apiInstance.tenantAccessUpdate(accessName, ifMatch, apiVersion, parameters, (error, data, response) => {
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
 **accessName** | **String**| The identifier of the Access configuration. | 
 **ifMatch** | **String**| The entity state (Etag) version of the property to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**AccessInformationUpdateParameters**](AccessInformationUpdateParameters.md)| Parameters supplied to retrieve the Tenant Access Information. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

