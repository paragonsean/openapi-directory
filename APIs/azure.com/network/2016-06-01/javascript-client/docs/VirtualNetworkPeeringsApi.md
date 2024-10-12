# NetworkManagementClient.VirtualNetworkPeeringsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualNetworkPeeringsCreateOrUpdate**](VirtualNetworkPeeringsApi.md#virtualNetworkPeeringsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/virtualNetworkPeerings/{virtualNetworkPeeringName} | 
[**virtualNetworkPeeringsDelete**](VirtualNetworkPeeringsApi.md#virtualNetworkPeeringsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/virtualNetworkPeerings/{virtualNetworkPeeringName} | 
[**virtualNetworkPeeringsGet**](VirtualNetworkPeeringsApi.md#virtualNetworkPeeringsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/virtualNetworkPeerings/{virtualNetworkPeeringName} | 
[**virtualNetworkPeeringsList**](VirtualNetworkPeeringsApi.md#virtualNetworkPeeringsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}/virtualNetworkPeerings | 



## virtualNetworkPeeringsCreateOrUpdate

> VirtualNetworkPeering virtualNetworkPeeringsCreateOrUpdate(resourceGroupName, virtualNetworkName, virtualNetworkPeeringName, apiVersion, subscriptionId, virtualNetworkPeeringParameters)



The Put virtual network peering operation creates/updates a peering in the specified virtual network

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkName = "virtualNetworkName_example"; // String | The name of the virtual network.
let virtualNetworkPeeringName = "virtualNetworkPeeringName_example"; // String | The name of the peering.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let virtualNetworkPeeringParameters = new NetworkManagementClient.VirtualNetworkPeering(); // VirtualNetworkPeering | Parameters supplied to the create/update virtual network peering operation
apiInstance.virtualNetworkPeeringsCreateOrUpdate(resourceGroupName, virtualNetworkName, virtualNetworkPeeringName, apiVersion, subscriptionId, virtualNetworkPeeringParameters, (error, data, response) => {
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
 **virtualNetworkName** | **String**| The name of the virtual network. | 
 **virtualNetworkPeeringName** | **String**| The name of the peering. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **virtualNetworkPeeringParameters** | [**VirtualNetworkPeering**](VirtualNetworkPeering.md)| Parameters supplied to the create/update virtual network peering operation | 

### Return type

[**VirtualNetworkPeering**](VirtualNetworkPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## virtualNetworkPeeringsDelete

> virtualNetworkPeeringsDelete(resourceGroupName, virtualNetworkName, virtualNetworkPeeringName, apiVersion, subscriptionId)



The delete virtual network peering operation deletes the specified peering.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkName = "virtualNetworkName_example"; // String | The name of the virtual network.
let virtualNetworkPeeringName = "virtualNetworkPeeringName_example"; // String | The name of the virtual network peering.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkPeeringsDelete(resourceGroupName, virtualNetworkName, virtualNetworkPeeringName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkName** | **String**| The name of the virtual network. | 
 **virtualNetworkPeeringName** | **String**| The name of the virtual network peering. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualNetworkPeeringsGet

> VirtualNetworkPeering virtualNetworkPeeringsGet(resourceGroupName, virtualNetworkName, virtualNetworkPeeringName, apiVersion, subscriptionId)



The Get virtual network peering operation retrieves information about the specified virtual network peering.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkName = "virtualNetworkName_example"; // String | The name of the virtual network.
let virtualNetworkPeeringName = "virtualNetworkPeeringName_example"; // String | The name of the virtual network peering.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkPeeringsGet(resourceGroupName, virtualNetworkName, virtualNetworkPeeringName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkName** | **String**| The name of the virtual network. | 
 **virtualNetworkPeeringName** | **String**| The name of the virtual network peering. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualNetworkPeering**](VirtualNetworkPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## virtualNetworkPeeringsList

> VirtualNetworkPeeringListResult virtualNetworkPeeringsList(resourceGroupName, virtualNetworkName, apiVersion, subscriptionId)



The List virtual network peerings operation retrieves all the peerings in a virtual network.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkName = "virtualNetworkName_example"; // String | The name of the virtual network.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkPeeringsList(resourceGroupName, virtualNetworkName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkName** | **String**| The name of the virtual network. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualNetworkPeeringListResult**](VirtualNetworkPeeringListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

