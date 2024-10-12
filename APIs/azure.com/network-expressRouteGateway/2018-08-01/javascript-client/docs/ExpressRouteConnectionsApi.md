# NetworkManagementClient.ExpressRouteConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRouteConnectionsCreateOrUpdate**](ExpressRouteConnectionsApi.md#expressRouteConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName} | 
[**expressRouteConnectionsDelete**](ExpressRouteConnectionsApi.md#expressRouteConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName} | 
[**expressRouteConnectionsGet**](ExpressRouteConnectionsApi.md#expressRouteConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections/{connectionName} | 
[**expressRouteConnectionsList**](ExpressRouteConnectionsApi.md#expressRouteConnectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}/expressRouteConnections | 



## expressRouteConnectionsCreateOrUpdate

> ExpressRouteConnection expressRouteConnectionsCreateOrUpdate(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId, putExpressRouteConnectionParameters)



Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let expressRouteGatewayName = "expressRouteGatewayName_example"; // String | The name of the ExpressRoute gateway.
let connectionName = "connectionName_example"; // String | The name of the connection subresource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let putExpressRouteConnectionParameters = new NetworkManagementClient.ExpressRouteConnection(); // ExpressRouteConnection | Parameters required in an ExpressRouteConnection PUT operation.
apiInstance.expressRouteConnectionsCreateOrUpdate(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId, putExpressRouteConnectionParameters, (error, data, response) => {
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
 **expressRouteGatewayName** | **String**| The name of the ExpressRoute gateway. | 
 **connectionName** | **String**| The name of the connection subresource. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **putExpressRouteConnectionParameters** | [**ExpressRouteConnection**](ExpressRouteConnection.md)| Parameters required in an ExpressRouteConnection PUT operation. | 

### Return type

[**ExpressRouteConnection**](ExpressRouteConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## expressRouteConnectionsDelete

> expressRouteConnectionsDelete(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId)



Deletes a connection to a ExpressRoute circuit.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let expressRouteGatewayName = "expressRouteGatewayName_example"; // String | The name of the ExpressRoute gateway.
let connectionName = "connectionName_example"; // String | The name of the connection subresource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteConnectionsDelete(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **expressRouteGatewayName** | **String**| The name of the ExpressRoute gateway. | 
 **connectionName** | **String**| The name of the connection subresource. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## expressRouteConnectionsGet

> ExpressRouteConnection expressRouteConnectionsGet(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId)



Gets the specified ExpressRouteConnection.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let expressRouteGatewayName = "expressRouteGatewayName_example"; // String | The name of the ExpressRoute gateway.
let connectionName = "connectionName_example"; // String | The name of the ExpressRoute connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteConnectionsGet(resourceGroupName, expressRouteGatewayName, connectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **expressRouteGatewayName** | **String**| The name of the ExpressRoute gateway. | 
 **connectionName** | **String**| The name of the ExpressRoute connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteConnection**](ExpressRouteConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRouteConnectionsList

> ExpressRouteConnectionList expressRouteConnectionsList(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId)



Lists ExpressRouteConnections.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let expressRouteGatewayName = "expressRouteGatewayName_example"; // String | The name of the ExpressRoute gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteConnectionsList(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **expressRouteGatewayName** | **String**| The name of the ExpressRoute gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteConnectionList**](ExpressRouteConnectionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

