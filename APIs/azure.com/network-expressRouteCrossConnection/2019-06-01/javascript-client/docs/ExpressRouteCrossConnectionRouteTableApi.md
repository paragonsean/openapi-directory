# ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionRouteTableApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRouteCrossConnectionsListRoutesTable**](ExpressRouteCrossConnectionRouteTableApi.md#expressRouteCrossConnectionsListRoutesTable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName}/routeTables/{devicePath} | 



## expressRouteCrossConnectionsListRoutesTable

> ExpressRouteCrossConnectionsListRoutesTable200Response expressRouteCrossConnectionsListRoutesTable(resourceGroupName, crossConnectionName, peeringName, devicePath, apiVersion, subscriptionId)



Gets the currently advertised routes table associated with the express route cross connection in a resource group.

### Example

```javascript
import ExpressRouteCrossConnectionRestApis from 'express_route_cross_connection_rest_apis';
let defaultClient = ExpressRouteCrossConnectionRestApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionRouteTableApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
let peeringName = "peeringName_example"; // String | The name of the peering.
let devicePath = "devicePath_example"; // String | The path of the device.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCrossConnectionsListRoutesTable(resourceGroupName, crossConnectionName, peeringName, devicePath, apiVersion, subscriptionId, (error, data, response) => {
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
 **crossConnectionName** | **String**| The name of the ExpressRouteCrossConnection. | 
 **peeringName** | **String**| The name of the peering. | 
 **devicePath** | **String**| The path of the device. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCrossConnectionsListRoutesTable200Response**](ExpressRouteCrossConnectionsListRoutesTable200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

