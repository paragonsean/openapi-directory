# ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionPeeringsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRouteCrossConnectionPeeringsCreateOrUpdate**](ExpressRouteCrossConnectionPeeringsApi.md#expressRouteCrossConnectionPeeringsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName} | 
[**expressRouteCrossConnectionPeeringsDelete**](ExpressRouteCrossConnectionPeeringsApi.md#expressRouteCrossConnectionPeeringsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName} | 
[**expressRouteCrossConnectionPeeringsGet**](ExpressRouteCrossConnectionPeeringsApi.md#expressRouteCrossConnectionPeeringsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings/{peeringName} | 
[**expressRouteCrossConnectionPeeringsList**](ExpressRouteCrossConnectionPeeringsApi.md#expressRouteCrossConnectionPeeringsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName}/peerings | 



## expressRouteCrossConnectionPeeringsCreateOrUpdate

> ExpressRouteCrossConnectionPeering expressRouteCrossConnectionPeeringsCreateOrUpdate(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId, peeringParameters)



Creates or updates a peering in the specified ExpressRouteCrossConnection.

### Example

```javascript
import ExpressRouteCrossConnectionRestApis from 'express_route_cross_connection_rest_apis';
let defaultClient = ExpressRouteCrossConnectionRestApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
let peeringName = "peeringName_example"; // String | The name of the peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let peeringParameters = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionPeering(); // ExpressRouteCrossConnectionPeering | Parameters supplied to the create or update ExpressRouteCrossConnection peering operation.
apiInstance.expressRouteCrossConnectionPeeringsCreateOrUpdate(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId, peeringParameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **peeringParameters** | [**ExpressRouteCrossConnectionPeering**](ExpressRouteCrossConnectionPeering.md)| Parameters supplied to the create or update ExpressRouteCrossConnection peering operation. | 

### Return type

[**ExpressRouteCrossConnectionPeering**](ExpressRouteCrossConnectionPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## expressRouteCrossConnectionPeeringsDelete

> expressRouteCrossConnectionPeeringsDelete(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId)



Deletes the specified peering from the ExpressRouteCrossConnection.

### Example

```javascript
import ExpressRouteCrossConnectionRestApis from 'express_route_cross_connection_rest_apis';
let defaultClient = ExpressRouteCrossConnectionRestApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
let peeringName = "peeringName_example"; // String | The name of the peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCrossConnectionPeeringsDelete(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId, (error, data, response) => {
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
 **crossConnectionName** | **String**| The name of the ExpressRouteCrossConnection. | 
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


## expressRouteCrossConnectionPeeringsGet

> ExpressRouteCrossConnectionPeering expressRouteCrossConnectionPeeringsGet(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId)



Gets the specified peering for the ExpressRouteCrossConnection.

### Example

```javascript
import ExpressRouteCrossConnectionRestApis from 'express_route_cross_connection_rest_apis';
let defaultClient = ExpressRouteCrossConnectionRestApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
let peeringName = "peeringName_example"; // String | The name of the peering.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCrossConnectionPeeringsGet(resourceGroupName, crossConnectionName, peeringName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCrossConnectionPeering**](ExpressRouteCrossConnectionPeering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRouteCrossConnectionPeeringsList

> ExpressRouteCrossConnectionPeeringList expressRouteCrossConnectionPeeringsList(resourceGroupName, crossConnectionName, apiVersion, subscriptionId)



Gets all peerings in a specified ExpressRouteCrossConnection.

### Example

```javascript
import ExpressRouteCrossConnectionRestApis from 'express_route_cross_connection_rest_apis';
let defaultClient = ExpressRouteCrossConnectionRestApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionPeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCrossConnectionPeeringsList(resourceGroupName, crossConnectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCrossConnectionPeeringList**](ExpressRouteCrossConnectionPeeringList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

