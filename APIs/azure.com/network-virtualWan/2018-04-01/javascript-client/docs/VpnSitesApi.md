# VirtualWanasAServiceManagementClient.VpnSitesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vpnSitesUpdateTags**](VpnSitesApi.md#vpnSitesUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/vpnSites/{vpnSiteName} | 



## vpnSitesUpdateTags

> VpnSite vpnSitesUpdateTags(subscriptionId, resourceGroupName, vpnSiteName, apiVersion, vpnSiteParameters)



Updates VpnSite tags.

### Example

```javascript
import VirtualWanasAServiceManagementClient from 'virtual_wanas_a_service_management_client';
let defaultClient = VirtualWanasAServiceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VirtualWanasAServiceManagementClient.VpnSitesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the VpnSite.
let vpnSiteName = "vpnSiteName_example"; // String | The name of the VpnSite being updated.
let apiVersion = "apiVersion_example"; // String | Client API version.
let vpnSiteParameters = new VirtualWanasAServiceManagementClient.VirtualHubsUpdateTagsRequest(); // VirtualHubsUpdateTagsRequest | Parameters supplied to update VpnSite tags.
apiInstance.vpnSitesUpdateTags(subscriptionId, resourceGroupName, vpnSiteName, apiVersion, vpnSiteParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name of the VpnSite. | 
 **vpnSiteName** | **String**| The name of the VpnSite being updated. | 
 **apiVersion** | **String**| Client API version. | 
 **vpnSiteParameters** | [**VirtualHubsUpdateTagsRequest**](VirtualHubsUpdateTagsRequest.md)| Parameters supplied to update VpnSite tags. | 

### Return type

[**VpnSite**](VpnSite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

