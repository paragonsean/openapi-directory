# NetworkManagementClient.ExpressRouteCircuitStatsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRouteCircuitsListStats**](ExpressRouteCircuitStatsApi.md#expressRouteCircuitsListStats) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCircuits/{circuitName}/stats | 



## expressRouteCircuitsListStats

> ExpressRouteCircuitsStatsListResult expressRouteCircuitsListStats(resourceGroupName, circuitName, apiVersion, subscriptionId)



The ListStats ExpressRouteCircuit operation retrieves all the stats from a ExpressRouteCircuits in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteCircuitStatsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let circuitName = "circuitName_example"; // String | The name of the loadBalancer.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCircuitsListStats(resourceGroupName, circuitName, apiVersion, subscriptionId, (error, data, response) => {
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
 **circuitName** | **String**| The name of the loadBalancer. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCircuitsStatsListResult**](ExpressRouteCircuitsStatsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

