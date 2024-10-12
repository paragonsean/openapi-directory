# NetworkManagementClient.PublicIPPrefixesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publicIPPrefixesCreateOrUpdate**](PublicIPPrefixesApi.md#publicIPPrefixesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName} | 
[**publicIPPrefixesDelete**](PublicIPPrefixesApi.md#publicIPPrefixesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName} | 
[**publicIPPrefixesGet**](PublicIPPrefixesApi.md#publicIPPrefixesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName} | 
[**publicIPPrefixesList**](PublicIPPrefixesApi.md#publicIPPrefixesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes | 
[**publicIPPrefixesListAll**](PublicIPPrefixesApi.md#publicIPPrefixesListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/publicIPPrefixes | 
[**publicIPPrefixesUpdateTags**](PublicIPPrefixesApi.md#publicIPPrefixesUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/publicIPPrefixes/{publicIpPrefixName} | 



## publicIPPrefixesCreateOrUpdate

> PublicIPPrefix publicIPPrefixesCreateOrUpdate(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, parameters)



Creates or updates a static or dynamic public IP prefix.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PublicIPPrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let publicIpPrefixName = "publicIpPrefixName_example"; // String | The name of the public IP prefix.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.PublicIPPrefix(); // PublicIPPrefix | Parameters supplied to the create or update public IP prefix operation.
apiInstance.publicIPPrefixesCreateOrUpdate(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **publicIpPrefixName** | **String**| The name of the public IP prefix. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**PublicIPPrefix**](PublicIPPrefix.md)| Parameters supplied to the create or update public IP prefix operation. | 

### Return type

[**PublicIPPrefix**](PublicIPPrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## publicIPPrefixesDelete

> publicIPPrefixesDelete(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId)



Deletes the specified public IP prefix.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PublicIPPrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let publicIpPrefixName = "publicIpPrefixName_example"; // String | The name of the PublicIpPrefix.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.publicIPPrefixesDelete(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **publicIpPrefixName** | **String**| The name of the PublicIpPrefix. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## publicIPPrefixesGet

> PublicIPPrefix publicIPPrefixesGet(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, opts)



Gets the specified public IP prefix in a specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PublicIPPrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let publicIpPrefixName = "publicIpPrefixName_example"; // String | The name of the Public IP Prefix.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | Expands referenced resources.
};
apiInstance.publicIPPrefixesGet(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **publicIpPrefixName** | **String**| The name of the Public IP Prefix. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| Expands referenced resources. | [optional] 

### Return type

[**PublicIPPrefix**](PublicIPPrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publicIPPrefixesList

> PublicIPPrefixListResult publicIPPrefixesList(resourceGroupName, apiVersion, subscriptionId)



Gets all public IP prefixes in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PublicIPPrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.publicIPPrefixesList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PublicIPPrefixListResult**](PublicIPPrefixListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publicIPPrefixesListAll

> PublicIPPrefixListResult publicIPPrefixesListAll(apiVersion, subscriptionId)



Gets all the public IP prefixes in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PublicIPPrefixesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.publicIPPrefixesListAll(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PublicIPPrefixListResult**](PublicIPPrefixListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publicIPPrefixesUpdateTags

> PublicIPPrefix publicIPPrefixesUpdateTags(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, parameters)



Updates public IP prefix tags.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PublicIPPrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let publicIpPrefixName = "publicIpPrefixName_example"; // String | The name of the public IP prefix.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.PublicIPPrefixesUpdateTagsRequest(); // PublicIPPrefixesUpdateTagsRequest | Parameters supplied to update public IP prefix tags.
apiInstance.publicIPPrefixesUpdateTags(resourceGroupName, publicIpPrefixName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **publicIpPrefixName** | **String**| The name of the public IP prefix. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**PublicIPPrefixesUpdateTagsRequest**](PublicIPPrefixesUpdateTagsRequest.md)| Parameters supplied to update public IP prefix tags. | 

### Return type

[**PublicIPPrefix**](PublicIPPrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

