# NetworkManagementClient.ExpressRouteCircuitPeeringsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRouteCircuitPeeringsCreateOrUpdate**](ExpressRouteCircuitPeeringsApi.md#expressRouteCircuitPeeringsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName} | 
[**expressRouteCircuitPeeringsDelete**](ExpressRouteCircuitPeeringsApi.md#expressRouteCircuitPeeringsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName} | 
[**expressRouteCircuitPeeringsGet**](ExpressRouteCircuitPeeringsApi.md#expressRouteCircuitPeeringsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName} | 
[**expressRouteCircuitPeeringsList**](ExpressRouteCircuitPeeringsApi.md#expressRouteCircuitPeeringsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings | 



## expressRouteCircuitPeeringsCreateOrUpdate

> ExpressRouteCircuitPeering expressRouteCircuitPeeringsCreateOrUpdate(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId, peeringParameters)



Creates or updates a peering in the specified express route circuits.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteCircuitPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the express route circuit.
let peeringName = "peeringName_example"; // String | The name of the peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let peeringParameters = new NetworkManagementClient.ExpressRouteCircuitPeering(); // ExpressRouteCircuitPeering | Parameters supplied to the create or update express route circuit peering operation.
apiInstance.expressRouteCircuitPeeringsCreateOrUpdate(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId, peeringParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **peeringParameters** | [**ExpressRouteCircuitPeering**](ExpressRouteCircuitPeering.md)| Parameters supplied to the create or update express route circuit peering operation. | 

### Return type

[**ExpressRouteCircuitPeering**](ExpressRouteCircuitPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## expressRouteCircuitPeeringsDelete

> expressRouteCircuitPeeringsDelete(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId)



Deletes the specified peering from the specified express route circuit.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteCircuitPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the express route circuit.
let peeringName = "peeringName_example"; // String | The name of the peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitPeeringsDelete(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId, (error, data, response) => {
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
 **circuitName** | **String**| The name of the express route circuit. | 
 **peeringName** | **String**| The name of the peering. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## expressRouteCircuitPeeringsGet

> ExpressRouteCircuitPeering expressRouteCircuitPeeringsGet(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId)



Gets the specified peering for the express route circuit.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteCircuitPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the express route circuit.
let peeringName = "peeringName_example"; // String | The name of the peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitPeeringsGet(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCircuitPeering**](ExpressRouteCircuitPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRouteCircuitPeeringsList

> ExpressRouteCircuitPeeringListResult expressRouteCircuitPeeringsList(resourceGroupName, circuitName, apiVersion, subscriptionId)



Gets all peerings in a specified express route circuit.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteCircuitPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the express route circuit.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitPeeringsList(resourceGroupName, circuitName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCircuitPeeringListResult**](ExpressRouteCircuitPeeringListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

