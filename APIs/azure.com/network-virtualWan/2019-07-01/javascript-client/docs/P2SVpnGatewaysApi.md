# VirtualWanasAServiceManagementClient.P2SVpnGatewaysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**p2sVpnGatewaysGenerateVpnProfile**](P2SVpnGatewaysApi.md#p2sVpnGatewaysGenerateVpnProfile) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}/generatevpnprofile | 
[**p2sVpnGatewaysGetP2sVpnConnectionHealth**](P2SVpnGatewaysApi.md#p2sVpnGatewaysGetP2sVpnConnectionHealth) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName}/getP2sVpnConnectionHealth | 
[**p2sVpnGatewaysUpdateTags**](P2SVpnGatewaysApi.md#p2sVpnGatewaysUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/p2svpnGateways/{gatewayName} | 



## p2sVpnGatewaysGenerateVpnProfile

> VpnProfileResponse p2sVpnGatewaysGenerateVpnProfile(resourceGroupName, gatewayName, apiVersion, subscriptionId, parameters)



Generates VPN profile for P2S client of the P2SVpnGateway in the specified resource group.

### Example

```javascript
import VirtualWanasAServiceManagementClient from 'virtual_wanas_a_service_management_client';
let defaultClient = VirtualWanasAServiceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualWanasAServiceManagementClient.P2SVpnGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let gatewayName = "gatewayName_example"; // String | The name of the P2SVpnGateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new VirtualWanasAServiceManagementClient.P2SVpnProfileParameters(); // P2SVpnProfileParameters | Parameters supplied to the generate P2SVpnGateway VPN client package operation.
apiInstance.p2sVpnGatewaysGenerateVpnProfile(resourceGroupName, gatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **gatewayName** | **String**| The name of the P2SVpnGateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**P2SVpnProfileParameters**](P2SVpnProfileParameters.md)| Parameters supplied to the generate P2SVpnGateway VPN client package operation. | 

### Return type

[**VpnProfileResponse**](VpnProfileResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## p2sVpnGatewaysGetP2sVpnConnectionHealth

> P2SVpnGateway p2sVpnGatewaysGetP2sVpnConnectionHealth(resourceGroupName, gatewayName, apiVersion, subscriptionId)



Gets the connection health of P2S clients of the virtual wan P2SVpnGateway in the specified resource group.

### Example

```javascript
import VirtualWanasAServiceManagementClient from 'virtual_wanas_a_service_management_client';
let defaultClient = VirtualWanasAServiceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualWanasAServiceManagementClient.P2SVpnGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let gatewayName = "gatewayName_example"; // String | The name of the P2SVpnGateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.p2sVpnGatewaysGetP2sVpnConnectionHealth(resourceGroupName, gatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **gatewayName** | **String**| The name of the P2SVpnGateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**P2SVpnGateway**](P2SVpnGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## p2sVpnGatewaysUpdateTags

> P2SVpnGateway p2sVpnGatewaysUpdateTags(subscriptionId, resourceGroupName, gatewayName, apiVersion, p2SVpnGatewayParameters)



Updates virtual wan p2s vpn gateway tags.

### Example

```javascript
import VirtualWanasAServiceManagementClient from 'virtual_wanas_a_service_management_client';
let defaultClient = VirtualWanasAServiceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualWanasAServiceManagementClient.P2SVpnGatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the P2SVpnGateway.
let gatewayName = "gatewayName_example"; // String | The name of the gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let p2SVpnGatewayParameters = new VirtualWanasAServiceManagementClient.P2sVpnGatewaysUpdateTagsRequest(); // P2sVpnGatewaysUpdateTagsRequest | Parameters supplied to update a virtual wan p2s vpn gateway tags.
apiInstance.p2sVpnGatewaysUpdateTags(subscriptionId, resourceGroupName, gatewayName, apiVersion, p2SVpnGatewayParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The resource group name of the P2SVpnGateway. | 
 **gatewayName** | **String**| The name of the gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **p2SVpnGatewayParameters** | [**P2sVpnGatewaysUpdateTagsRequest**](P2sVpnGatewaysUpdateTagsRequest.md)| Parameters supplied to update a virtual wan p2s vpn gateway tags. | 

### Return type

[**P2SVpnGateway**](P2SVpnGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

