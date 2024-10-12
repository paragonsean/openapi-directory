# NetworkManagementClient.PeerExpressRouteCircuitConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peerExpressRouteCircuitConnectionsGet**](PeerExpressRouteCircuitConnectionsApi.md#peerExpressRouteCircuitConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/peerConnections/{connectionName} | 
[**peerExpressRouteCircuitConnectionsList**](PeerExpressRouteCircuitConnectionsApi.md#peerExpressRouteCircuitConnectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/peerConnections | 



## peerExpressRouteCircuitConnectionsGet

> PeerExpressRouteCircuitConnection peerExpressRouteCircuitConnectionsGet(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId)



Gets the specified Peer Express Route Circuit Connection from the specified express route circuit.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PeerExpressRouteCircuitConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the express route circuit.
let peeringName = "peeringName_example"; // String | The name of the peering.
let connectionName = "connectionName_example"; // String | The name of the peer express route circuit connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.peerExpressRouteCircuitConnectionsGet(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **circuitName** | **String**| The name of the express route circuit. | 
 **peeringName** | **String**| The name of the peering. | 
 **connectionName** | **String**| The name of the peer express route circuit connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PeerExpressRouteCircuitConnection**](PeerExpressRouteCircuitConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peerExpressRouteCircuitConnectionsList

> PeerExpressRouteCircuitConnectionListResult peerExpressRouteCircuitConnectionsList(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId)



Gets all global reach peer connections associated with a private peering in an express route circuit.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PeerExpressRouteCircuitConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the circuit.
let peeringName = "peeringName_example"; // String | The name of the peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.peerExpressRouteCircuitConnectionsList(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId, (error, data, response) => {
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
 **circuitName** | **String**| The name of the circuit. | 
 **peeringName** | **String**| The name of the peering. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PeerExpressRouteCircuitConnectionListResult**](PeerExpressRouteCircuitConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

