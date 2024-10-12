# NetworkManagementClient.VirtualNetworkGatewaysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualNetworkGatewaysCreateOrUpdate**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} | 
[**virtualNetworkGatewaysDelete**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} | 
[**virtualNetworkGatewaysGeneratevpnclientpackage**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGeneratevpnclientpackage) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/generatevpnclientpackage | 
[**virtualNetworkGatewaysGet**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName} | 
[**virtualNetworkGatewaysList**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways | 
[**virtualNetworkGatewaysReset**](VirtualNetworkGatewaysApi.md#virtualNetworkGatewaysReset) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworkGateways/{virtualNetworkGatewayName}/reset | 



## virtualNetworkGatewaysCreateOrUpdate

> VirtualNetworkGateway virtualNetworkGatewaysCreateOrUpdate(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Creates or updates a virtual network gateway in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VirtualNetworkGateway(); // VirtualNetworkGateway | Parameters supplied to create or update virtual network gateway operation.
apiInstance.virtualNetworkGatewaysCreateOrUpdate(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md)| Parameters supplied to create or update virtual network gateway operation. | 

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## virtualNetworkGatewaysDelete

> virtualNetworkGatewaysDelete(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Deletes the specified virtual network gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysDelete(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualNetworkGatewaysGeneratevpnclientpackage

> String virtualNetworkGatewaysGeneratevpnclientpackage(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Generates VPN client package for P2S client of the virtual network gateway in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VpnClientParameters(); // VpnClientParameters | Parameters supplied to the generate virtual network gateway VPN client package operation.
apiInstance.virtualNetworkGatewaysGeneratevpnclientpackage(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VpnClientParameters**](VpnClientParameters.md)| Parameters supplied to the generate virtual network gateway VPN client package operation. | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## virtualNetworkGatewaysGet

> VirtualNetworkGateway virtualNetworkGatewaysGet(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId)



Gets the specified virtual network gateway by resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysGet(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## virtualNetworkGatewaysList

> VirtualNetworkGatewayListResult virtualNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId)



Gets all virtual network gateways by resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.virtualNetworkGatewaysList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**VirtualNetworkGatewayListResult**](VirtualNetworkGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## virtualNetworkGatewaysReset

> VirtualNetworkGateway virtualNetworkGatewaysReset(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters)



Resets the primary of the virtual network gateway in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.VirtualNetworkGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let virtualNetworkGatewayName = "virtualNetworkGatewayName_example"; // String | The name of the virtual network gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VirtualNetworkGateway(); // VirtualNetworkGateway | Virtual network gateway vip address supplied to the begin reset of the active-active feature enabled gateway.
apiInstance.virtualNetworkGatewaysReset(resourceGroupName, virtualNetworkGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **virtualNetworkGatewayName** | **String**| The name of the virtual network gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VirtualNetworkGateway**](VirtualNetworkGateway.md)| Virtual network gateway vip address supplied to the begin reset of the active-active feature enabled gateway. | 

### Return type

[**VirtualNetworkGateway**](VirtualNetworkGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

