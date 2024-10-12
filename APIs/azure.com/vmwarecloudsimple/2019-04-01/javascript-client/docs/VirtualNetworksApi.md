# VMwareCloudSimple.VirtualNetworksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualNetworksGet**](VirtualNetworksApi.md#virtualNetworksGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/virtualNetworks/{virtualNetworkName} | Implements virtual network GET method
[**virtualNetworksList**](VirtualNetworksApi.md#virtualNetworksList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.VMwareCloudSimple/locations/{regionId}/privateClouds/{pcName}/virtualNetworks | Implements list available virtual networks within a subscription method



## virtualNetworksGet

> VirtualNetwork virtualNetworksGet(subscriptionId, regionId, pcName, virtualNetworkName, apiVersion)

Implements virtual network GET method

Return virtual network by its name

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualNetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let pcName = "pcName_example"; // String | The private cloud name
let virtualNetworkName = "virtualNetworkName_example"; // String | virtual network id (vsphereId)
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.virtualNetworksGet(subscriptionId, regionId, pcName, virtualNetworkName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **pcName** | **String**| The private cloud name | 
 **virtualNetworkName** | **String**| virtual network id (vsphereId) | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworksList

> VirtualNetworkListResponse virtualNetworksList(subscriptionId, regionId, pcName, apiVersion, resourcePoolName)

Implements list available virtual networks within a subscription method

Return list of virtual networks in location for private cloud

### Example

```javascript
import VMwareCloudSimple from 'v_mware_cloud_simple';
let defaultClient = VMwareCloudSimple.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VMwareCloudSimple.VirtualNetworksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let regionId = "regionId_example"; // String | The region Id (westus, eastus)
let pcName = "pcName_example"; // String | The private cloud name
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourcePoolName = "resourcePoolName_example"; // String | Resource pool used to derive vSphere cluster which contains virtual networks
apiInstance.virtualNetworksList(subscriptionId, regionId, pcName, apiVersion, resourcePoolName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **regionId** | **String**| The region Id (westus, eastus) | 
 **pcName** | **String**| The private cloud name | 
 **apiVersion** | **String**| Client API version. | 
 **resourcePoolName** | **String**| Resource pool used to derive vSphere cluster which contains virtual networks | 

### Return type

[**VirtualNetworkListResponse**](VirtualNetworkListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

