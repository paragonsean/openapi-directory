# NetworkManagementClient.VirtualRoutersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualRoutersCreateOrUpdate**](VirtualRoutersApi.md#virtualRoutersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName} | 
[**virtualRoutersDelete**](VirtualRoutersApi.md#virtualRoutersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName} | 
[**virtualRoutersGet**](VirtualRoutersApi.md#virtualRoutersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName} | 
[**virtualRoutersList**](VirtualRoutersApi.md#virtualRoutersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/virtualRouters | 
[**virtualRoutersListByResourceGroup**](VirtualRoutersApi.md#virtualRoutersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters | 
[**virtualRoutersUpdate**](VirtualRoutersApi.md#virtualRoutersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName} | 



## virtualRoutersCreateOrUpdate

> VirtualRouter virtualRoutersCreateOrUpdate(resourceGroupName, virtualRouterName, apiVersion, subscriptionId, parameters)



Creates or updates the specified Virtual Router.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualRoutersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VirtualRouter(); // VirtualRouter | Parameters supplied to the create or update Virtual Router.
apiInstance.virtualRoutersCreateOrUpdate(resourceGroupName, virtualRouterName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualRouterName** | **String**| The name of the Virtual Router. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualRouter**](VirtualRouter.md)| Parameters supplied to the create or update Virtual Router. | 

### Return type

[**VirtualRouter**](VirtualRouter.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualRoutersDelete

> virtualRoutersDelete(resourceGroupName, virtualRouterName, apiVersion, subscriptionId)



Deletes the specified Virtual Router.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualRoutersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualRoutersDelete(resourceGroupName, virtualRouterName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualRouterName** | **String**| The name of the Virtual Router. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualRoutersGet

> VirtualRouter virtualRoutersGet(resourceGroupName, virtualRouterName, apiVersion, subscriptionId, opts)



Gets the specified Virtual Router.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualRoutersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | Expands referenced resources.
};
apiInstance.virtualRoutersGet(resourceGroupName, virtualRouterName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **virtualRouterName** | **String**| The name of the Virtual Router. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| Expands referenced resources. | [optional] 

### Return type

[**VirtualRouter**](VirtualRouter.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualRoutersList

> VirtualRouterListResult virtualRoutersList(apiVersion, subscriptionId)



Gets all the Virtual Routers in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualRoutersApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualRoutersList(apiVersion, subscriptionId, (error, data, response) => {
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

[**VirtualRouterListResult**](VirtualRouterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualRoutersListByResourceGroup

> VirtualRouterListResult virtualRoutersListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists all Virtual Routers in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualRoutersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualRoutersListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**VirtualRouterListResult**](VirtualRouterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualRoutersUpdate

> VirtualRouter virtualRoutersUpdate(subscriptionId, resourceGroupName, virtualRouterName, apiVersion, parameters)



Updates a Virtual Router.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualRoutersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the Virtual Router.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router being updated.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new NetworkManagementClient.VirtualRoutersUpdateRequest(); // VirtualRoutersUpdateRequest | Parameters supplied to Update Virtual Router Tags.
apiInstance.virtualRoutersUpdate(subscriptionId, resourceGroupName, virtualRouterName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group name of the Virtual Router. | 
 **virtualRouterName** | **String**| The name of the Virtual Router being updated. | 
 **apiVersion** | **String**| Client API version. | 
 **parameters** | [**VirtualRoutersUpdateRequest**](VirtualRoutersUpdateRequest.md)| Parameters supplied to Update Virtual Router Tags. | 

### Return type

[**VirtualRouter**](VirtualRouter.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

