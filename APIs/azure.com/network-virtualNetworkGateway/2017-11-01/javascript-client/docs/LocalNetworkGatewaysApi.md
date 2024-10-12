# NetworkManagementClient.LocalNetworkGatewaysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**localNetworkGatewaysCreateOrUpdate**](LocalNetworkGatewaysApi.md#localNetworkGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} | 
[**localNetworkGatewaysDelete**](LocalNetworkGatewaysApi.md#localNetworkGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} | 
[**localNetworkGatewaysGet**](LocalNetworkGatewaysApi.md#localNetworkGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} | 
[**localNetworkGatewaysList**](LocalNetworkGatewaysApi.md#localNetworkGatewaysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways | 
[**localNetworkGatewaysUpdateTags**](LocalNetworkGatewaysApi.md#localNetworkGatewaysUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/localNetworkGateways/{localNetworkGatewayName} | 



## localNetworkGatewaysCreateOrUpdate

> LocalNetworkGateway localNetworkGatewaysCreateOrUpdate(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, parameters)



Creates or updates a local network gateway in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.LocalNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.LocalNetworkGateway(); // LocalNetworkGateway | Parameters supplied to the create or update local network gateway operation.
apiInstance.localNetworkGatewaysCreateOrUpdate(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **localNetworkGatewayName** | **String**| The name of the local network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**LocalNetworkGateway**](LocalNetworkGateway.md)| Parameters supplied to the create or update local network gateway operation. | 

### Return type

[**LocalNetworkGateway**](LocalNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## localNetworkGatewaysDelete

> localNetworkGatewaysDelete(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId)



Deletes the specified local network gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.LocalNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.localNetworkGatewaysDelete(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **localNetworkGatewayName** | **String**| The name of the local network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## localNetworkGatewaysGet

> LocalNetworkGateway localNetworkGatewaysGet(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId)



Gets the specified local network gateway in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.LocalNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.localNetworkGatewaysGet(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **localNetworkGatewayName** | **String**| The name of the local network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LocalNetworkGateway**](LocalNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## localNetworkGatewaysList

> LocalNetworkGatewayListResult localNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId)



Gets all the local network gateways in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.LocalNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.localNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**LocalNetworkGatewayListResult**](LocalNetworkGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## localNetworkGatewaysUpdateTags

> LocalNetworkGateway localNetworkGatewaysUpdateTags(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, parameters)



Updates a local network gateway tags.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.LocalNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let localNetworkGatewayName = "localNetworkGatewayName_example"; // String | The name of the local network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VirtualNetworkGatewayConnectionsUpdateTagsRequest(); // VirtualNetworkGatewayConnectionsUpdateTagsRequest | Parameters supplied to update local network gateway tags.
apiInstance.localNetworkGatewaysUpdateTags(resourceGroupName, localNetworkGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **localNetworkGatewayName** | **String**| The name of the local network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualNetworkGatewayConnectionsUpdateTagsRequest**](VirtualNetworkGatewayConnectionsUpdateTagsRequest.md)| Parameters supplied to update local network gateway tags. | 

### Return type

[**LocalNetworkGateway**](LocalNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

