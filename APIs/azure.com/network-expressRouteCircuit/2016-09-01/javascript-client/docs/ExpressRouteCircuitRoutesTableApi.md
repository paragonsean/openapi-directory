# NetworkManagementClient.ExpressRouteCircuitRoutesTableApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRouteCircuitsListRoutesTable**](ExpressRouteCircuitRoutesTableApi.md#expressRouteCircuitsListRoutesTable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/peerings/{peeringName}/routeTables/{devicePath} | 



## expressRouteCircuitsListRoutesTable

> ExpressRouteCircuitsRoutesTableListResult expressRouteCircuitsListRoutesTable(resourceGroupName, circuitName, peeringName, devicePath, apiVersion, subscriptionId)



Gets the currently advertised routes table associated with the express route circuit in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteCircuitRoutesTableApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the express route circuit.
let peeringName = "peeringName_example"; // String | The name of the peering.
let devicePath = "devicePath_example"; // String | The path of the device.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitsListRoutesTable(resourceGroupName, circuitName, peeringName, devicePath, apiVersion, subscriptionId, (error, data, response) => {
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
 **devicePath** | **String**| The path of the device. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCircuitsRoutesTableListResult**](ExpressRouteCircuitsRoutesTableListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

