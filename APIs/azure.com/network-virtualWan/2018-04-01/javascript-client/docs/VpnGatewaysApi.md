# VirtualWanasAServiceManagementClient.VpnGatewaysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vpnGatewaysUpdateTags**](VpnGatewaysApi.md#vpnGatewaysUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnGateways/{gatewayName} | 



## vpnGatewaysUpdateTags

> VpnGateway vpnGatewaysUpdateTags(subscriptionId, resourceGroupName, gatewayName, apiVersion, vpnGatewayParameters)



Updates virtual wan vpn gateway tags.

### Example

```javascript
import VirtualWanasAServiceManagementClient from 'virtual_wanas_a_service_management_client';
let defaultClient = VirtualWanasAServiceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualWanasAServiceManagementClient.VpnGatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnGateway.
let gatewayName = "gatewayName_example"; // String | The name of the gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let vpnGatewayParameters = new VirtualWanasAServiceManagementClient.VirtualHubsUpdateTagsRequest(); // VirtualHubsUpdateTagsRequest | Parameters supplied to update a virtual wan vpn gateway tags.
apiInstance.vpnGatewaysUpdateTags(subscriptionId, resourceGroupName, gatewayName, apiVersion, vpnGatewayParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name of the VpnGateway. | 
 **gatewayName** | **String**| The name of the gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **vpnGatewayParameters** | [**VirtualHubsUpdateTagsRequest**](VirtualHubsUpdateTagsRequest.md)| Parameters supplied to update a virtual wan vpn gateway tags. | 

### Return type

[**VpnGateway**](VpnGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

