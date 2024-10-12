# NetworkManagementClient.ExpressRouteCircuitConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRouteCircuitConnectionsCreateOrUpdate**](ExpressRouteCircuitConnectionsApi.md#expressRouteCircuitConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections/{connectionName} | 
[**expressRouteCircuitConnectionsDelete**](ExpressRouteCircuitConnectionsApi.md#expressRouteCircuitConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections/{connectionName} | 
[**expressRouteCircuitConnectionsGet**](ExpressRouteCircuitConnectionsApi.md#expressRouteCircuitConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections/{connectionName} | 
[**expressRouteCircuitConnectionsList**](ExpressRouteCircuitConnectionsApi.md#expressRouteCircuitConnectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/connections | 



## expressRouteCircuitConnectionsCreateOrUpdate

> ExpressRouteCircuitConnection expressRouteCircuitConnectionsCreateOrUpdate(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId, expressRouteCircuitConnectionParameters)



Creates or updates a Express Route Circuit Connection in the specified express route circuits.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteCircuitConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the express route circuit.
let peeringName = "peeringName_example"; // String | The name of the peering.
let connectionName = "connectionName_example"; // String | The name of the express route circuit connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let expressRouteCircuitConnectionParameters = new NetworkManagementClient.ExpressRouteCircuitConnection(); // ExpressRouteCircuitConnection | Parameters supplied to the create or update express route circuit connection operation.
apiInstance.expressRouteCircuitConnectionsCreateOrUpdate(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId, expressRouteCircuitConnectionParameters, (error, data, response) => {
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
 **connectionName** | **String**| The name of the express route circuit connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expressRouteCircuitConnectionParameters** | [**ExpressRouteCircuitConnection**](ExpressRouteCircuitConnection.md)| Parameters supplied to the create or update express route circuit connection operation. | 

### Return type

[**ExpressRouteCircuitConnection**](ExpressRouteCircuitConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## expressRouteCircuitConnectionsDelete

> expressRouteCircuitConnectionsDelete(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId)



Deletes the specified Express Route Circuit Connection from the specified express route circuit.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteCircuitConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the express route circuit.
let peeringName = "peeringName_example"; // String | The name of the peering.
let connectionName = "connectionName_example"; // String | The name of the express route circuit connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitConnectionsDelete(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **connectionName** | **String**| The name of the express route circuit connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## expressRouteCircuitConnectionsGet

> ExpressRouteCircuitConnection expressRouteCircuitConnectionsGet(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId)



Gets the specified Express Route Circuit Connection from the specified express route circuit.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteCircuitConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the express route circuit.
let peeringName = "peeringName_example"; // String | The name of the peering.
let connectionName = "connectionName_example"; // String | The name of the express route circuit connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitConnectionsGet(resourceGroupName, circuitName, peeringName, connectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **connectionName** | **String**| The name of the express route circuit connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCircuitConnection**](ExpressRouteCircuitConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRouteCircuitConnectionsList

> ExpressRouteCircuitConnectionListResult expressRouteCircuitConnectionsList(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId)



Gets all global reach connections associated with a private peering in an express route circuit.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteCircuitConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the circuit.
let peeringName = "peeringName_example"; // String | The name of the peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitConnectionsList(resourceGroupName, circuitName, peeringName, apiVersion, subscriptionId, (error, data, response) => {
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

[**ExpressRouteCircuitConnectionListResult**](ExpressRouteCircuitConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

