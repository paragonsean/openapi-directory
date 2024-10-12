# VirtualWanasAServiceManagementClient.VirtualWANsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualHubsUpdateTags**](VirtualWANsApi.md#virtualHubsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName} | 
[**virtualWansUpdateTags**](VirtualWANsApi.md#virtualWansUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualWans/{VirtualWANName} | 



## virtualHubsUpdateTags

> VirtualHub virtualHubsUpdateTags(subscriptionId, resourceGroupName, virtualHubName, apiVersion, virtualHubParameters)



Updates VirtualHub tags.

### Example

```javascript
import VirtualWanasAServiceManagementClient from 'virtual_wanas_a_service_management_client';
let defaultClient = VirtualWanasAServiceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualWanasAServiceManagementClient.VirtualWANsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualHub.
let virtualHubName = "virtualHubName_example"; // String | The name of the VirtualHub.
let apiVersion = "apiVersion_example"; // String | Client API version.
let virtualHubParameters = new VirtualWanasAServiceManagementClient.P2sVpnGatewaysUpdateTagsRequest(); // P2sVpnGatewaysUpdateTagsRequest | Parameters supplied to update VirtualHub tags.
apiInstance.virtualHubsUpdateTags(subscriptionId, resourceGroupName, virtualHubName, apiVersion, virtualHubParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name of the VirtualHub. | 
 **virtualHubName** | **String**| The name of the VirtualHub. | 
 **apiVersion** | **String**| Client API version. | 
 **virtualHubParameters** | [**P2sVpnGatewaysUpdateTagsRequest**](P2sVpnGatewaysUpdateTagsRequest.md)| Parameters supplied to update VirtualHub tags. | 

### Return type

[**VirtualHub**](VirtualHub.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualWansUpdateTags

> VirtualWAN virtualWansUpdateTags(subscriptionId, resourceGroupName, virtualWANName, apiVersion, wANParameters)



Updates a VirtualWAN tags.

### Example

```javascript
import VirtualWanasAServiceManagementClient from 'virtual_wanas_a_service_management_client';
let defaultClient = VirtualWanasAServiceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualWanasAServiceManagementClient.VirtualWANsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VirtualWan.
let virtualWANName = "virtualWANName_example"; // String | The name of the VirtualWAN being updated.
let apiVersion = "apiVersion_example"; // String | Client API version.
let wANParameters = new VirtualWanasAServiceManagementClient.P2sVpnGatewaysUpdateTagsRequest(); // P2sVpnGatewaysUpdateTagsRequest | Parameters supplied to Update VirtualWAN tags.
apiInstance.virtualWansUpdateTags(subscriptionId, resourceGroupName, virtualWANName, apiVersion, wANParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name of the VirtualWan. | 
 **virtualWANName** | **String**| The name of the VirtualWAN being updated. | 
 **apiVersion** | **String**| Client API version. | 
 **wANParameters** | [**P2sVpnGatewaysUpdateTagsRequest**](P2sVpnGatewaysUpdateTagsRequest.md)| Parameters supplied to Update VirtualWAN tags. | 

### Return type

[**VirtualWAN**](VirtualWAN.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

