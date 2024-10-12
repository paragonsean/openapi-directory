# ResourceManagementClient.ProvidersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providersGet**](ProvidersApi.md#providersGet) | **GET** /subscriptions/{subscriptionId}/providers/{resourceProviderNamespace} | 
[**providersGetAtTenantScope**](ProvidersApi.md#providersGetAtTenantScope) | **GET** /providers/{resourceProviderNamespace} | 
[**providersList**](ProvidersApi.md#providersList) | **GET** /subscriptions/{subscriptionId}/providers | 
[**providersListAtTenantScope**](ProvidersApi.md#providersListAtTenantScope) | **GET** /providers | 
[**providersRegister**](ProvidersApi.md#providersRegister) | **POST** /subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/register | 
[**providersUnregister**](ProvidersApi.md#providersUnregister) | **POST** /subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/unregister | 



## providersGet

> Provider providersGet(resourceProviderNamespace, apiVersion, subscriptionId, opts)



Gets the specified resource provider.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ProvidersApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'expand': "expand_example" // String | The $expand query parameter. For example, to include property aliases in response, use $expand=resourceTypes/aliases.
};
apiInstance.providersGet(resourceProviderNamespace, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **expand** | **String**| The $expand query parameter. For example, to include property aliases in response, use $expand&#x3D;resourceTypes/aliases. | [optional] 

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providersGetAtTenantScope

> Provider providersGetAtTenantScope(resourceProviderNamespace, apiVersion, opts)



Gets the specified resource provider at the tenant level.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ProvidersApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'expand': "expand_example" // String | The $expand query parameter. For example, to include property aliases in response, use $expand=resourceTypes/aliases.
};
apiInstance.providersGetAtTenantScope(resourceProviderNamespace, apiVersion, opts, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **expand** | **String**| The $expand query parameter. For example, to include property aliases in response, use $expand&#x3D;resourceTypes/aliases. | [optional] 

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providersList

> ProviderListResult providersList(apiVersion, subscriptionId, opts)



Gets all resource providers for a subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ProvidersApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'top': 56, // Number | The number of results to return. If null is passed returns all deployments.
  'expand': "expand_example" // String | The properties to include in the results. For example, use &$expand=metadata in the query string to retrieve resource provider metadata. To include property aliases in response, use $expand=resourceTypes/aliases.
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **top** | **Number**| The number of results to return. If null is passed returns all deployments. | [optional] 
 **expand** | **String**| The properties to include in the results. For example, use &amp;$expand&#x3D;metadata in the query string to retrieve resource provider metadata. To include property aliases in response, use $expand&#x3D;resourceTypes/aliases. | [optional] 

### Return type

[**ProviderListResult**](ProviderListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providersListAtTenantScope

> ProviderListResult providersListAtTenantScope(apiVersion, opts)



Gets all resource providers for the tenant.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ProvidersApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'top': 56, // Number | The number of results to return. If null is passed returns all providers.
  'expand': "expand_example" // String | The properties to include in the results. For example, use &$expand=metadata in the query string to retrieve resource provider metadata. To include property aliases in response, use $expand=resourceTypes/aliases.
};
apiInstance.providersListAtTenantScope(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **top** | **Number**| The number of results to return. If null is passed returns all providers. | [optional] 
 **expand** | **String**| The properties to include in the results. For example, use &amp;$expand&#x3D;metadata in the query string to retrieve resource provider metadata. To include property aliases in response, use $expand&#x3D;resourceTypes/aliases. | [optional] 

### Return type

[**ProviderListResult**](ProviderListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providersRegister

> Provider providersRegister(resourceProviderNamespace, apiVersion, subscriptionId)



Registers a subscription with a resource provider.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ProvidersApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider to register.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
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
 **resourceProviderNamespace** | **String**| The namespace of the resource provider to register. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## providersUnregister

> Provider providersUnregister(resourceProviderNamespace, apiVersion, subscriptionId)



Unregisters a subscription from a resource provider.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ProvidersApi();
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider to unregister.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
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
 **resourceProviderNamespace** | **String**| The namespace of the resource provider to unregister. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

