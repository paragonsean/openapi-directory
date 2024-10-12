# ProviderApiClient.ProviderApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providerGetAvailableStacks**](ProviderApi.md#providerGetAvailableStacks) | **GET** /providers/Microsoft.Web/availableStacks | Get available application frameworks and their versions
[**providerGetAvailableStacksOnPrem**](ProviderApi.md#providerGetAvailableStacksOnPrem) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/availableStacks | Get available application frameworks and their versions
[**providerListOperations**](ProviderApi.md#providerListOperations) | **GET** /providers/Microsoft.Web/operations | Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions



## providerGetAvailableStacks

> ApplicationStackCollection providerGetAvailableStacks(apiVersion, opts)

Get available application frameworks and their versions

Description for Get available application frameworks and their versions

### Example

```javascript
import ProviderApiClient from 'provider_api_client';
let defaultClient = ProviderApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProviderApiClient.ProviderApi();
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'osTypeSelected': "osTypeSelected_example" // String | 
};
apiInstance.providerGetAvailableStacks(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API Version | 
 **osTypeSelected** | **String**|  | [optional] 

### Return type

[**ApplicationStackCollection**](ApplicationStackCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providerGetAvailableStacksOnPrem

> ApplicationStackCollection providerGetAvailableStacksOnPrem(subscriptionId, apiVersion, opts)

Get available application frameworks and their versions

Description for Get available application frameworks and their versions

### Example

```javascript
import ProviderApiClient from 'provider_api_client';
let defaultClient = ProviderApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProviderApiClient.ProviderApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'osTypeSelected': "osTypeSelected_example" // String | 
};
apiInstance.providerGetAvailableStacksOnPrem(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **osTypeSelected** | **String**|  | [optional] 

### Return type

[**ApplicationStackCollection**](ApplicationStackCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providerListOperations

> ProviderListOperations200Response providerListOperations(apiVersion)

Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions

Description for Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions

### Example

```javascript
import ProviderApiClient from 'provider_api_client';
let defaultClient = ProviderApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProviderApiClient.ProviderApi();
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.providerListOperations(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| API Version | 

### Return type

[**ProviderListOperations200Response**](ProviderListOperations200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

