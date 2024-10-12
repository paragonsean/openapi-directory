# NetworkManagementClient.VirtualRouterPeeringsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualRouterPeeringsCreateOrUpdate**](VirtualRouterPeeringsApi.md#virtualRouterPeeringsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName}/peerings/{peeringName} | 
[**virtualRouterPeeringsDelete**](VirtualRouterPeeringsApi.md#virtualRouterPeeringsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName}/peerings/{peeringName} | 
[**virtualRouterPeeringsGet**](VirtualRouterPeeringsApi.md#virtualRouterPeeringsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName}/peerings/{peeringName} | 
[**virtualRouterPeeringsList**](VirtualRouterPeeringsApi.md#virtualRouterPeeringsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualRouters/{virtualRouterName}/peerings | 



## virtualRouterPeeringsCreateOrUpdate

> VirtualRouterPeering virtualRouterPeeringsCreateOrUpdate(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId, parameters)



Creates or updates the specified Virtual Router Peering.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualRouterPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
let peeringName = "peeringName_example"; // String | The name of the Virtual Router Peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VirtualRouterPeering(); // VirtualRouterPeering | Parameters supplied to the create or update Virtual Router Peering operation.
apiInstance.virtualRouterPeeringsCreateOrUpdate(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **peeringName** | **String**| The name of the Virtual Router Peering. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualRouterPeering**](VirtualRouterPeering.md)| Parameters supplied to the create or update Virtual Router Peering operation. | 

### Return type

[**VirtualRouterPeering**](VirtualRouterPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualRouterPeeringsDelete

> virtualRouterPeeringsDelete(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId)



Deletes the specified peering from a Virtual Router.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualRouterPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
let peeringName = "peeringName_example"; // String | The name of the peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualRouterPeeringsDelete(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId, (error, data, response) => {
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
 **peeringName** | **String**| The name of the peering. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualRouterPeeringsGet

> VirtualRouterPeering virtualRouterPeeringsGet(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId)



Gets the specified Virtual Router Peering.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualRouterPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
let peeringName = "peeringName_example"; // String | The name of the Virtual Router Peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualRouterPeeringsGet(resourceGroupName, virtualRouterName, peeringName, apiVersion, subscriptionId, (error, data, response) => {
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
 **peeringName** | **String**| The name of the Virtual Router Peering. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualRouterPeering**](VirtualRouterPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualRouterPeeringsList

> VirtualRouterPeeringListResult virtualRouterPeeringsList(resourceGroupName, virtualRouterName, apiVersion, subscriptionId)



Lists all Virtual Router Peerings in a Virtual Router resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualRouterPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualRouterName = "virtualRouterName_example"; // String | The name of the Virtual Router.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualRouterPeeringsList(resourceGroupName, virtualRouterName, apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**VirtualRouterPeeringListResult**](VirtualRouterPeeringListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

