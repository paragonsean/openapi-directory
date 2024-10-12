# ResourceManagementClient.ProvidersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providersGet**](ProvidersApi.md#providersGet) | **GET** /subscriptions/{subscriptionId}/providers/{resourceProviderNamespace} | 
[**providersList**](ProvidersApi.md#providersList) | **GET** /subscriptions/{subscriptionId}/providers | 
[**providersRegister**](ProvidersApi.md#providersRegister) | **POST** /subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/register | 
[**providersUnregister**](ProvidersApi.md#providersUnregister) | **POST** /subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/unregister | 



## providersGet

> Provider providersGet(resourceProviderNamespace, apiVersion, subscriptionId)



Gets a resource provider.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ProvidersApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Namespace of the resource provider.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.providersGet(resourceProviderNamespace, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| Namespace of the resource provider. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providersList

> ProviderListResult providersList(apiVersion, subscriptionId, opts)



Gets a list of resource providers.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ProvidersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56 // Number | Query parameters. If null is passed returns all deployments.
};
apiInstance.providersList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **top** | **Number**| Query parameters. If null is passed returns all deployments. | [optional] 

### Return type

[**ProviderListResult**](ProviderListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providersRegister

> Provider providersRegister(resourceProviderNamespace, apiVersion, subscriptionId)



Registers provider to be used with a subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ProvidersApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Namespace of the resource provider.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.providersRegister(resourceProviderNamespace, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| Namespace of the resource provider. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providersUnregister

> Provider providersUnregister(resourceProviderNamespace, apiVersion, subscriptionId)



Unregisters provider from a subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ProvidersApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Namespace of the resource provider.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.providersUnregister(resourceProviderNamespace, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| Namespace of the resource provider. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

