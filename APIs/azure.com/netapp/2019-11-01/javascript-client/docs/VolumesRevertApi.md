# MicrosoftNetApp.VolumesRevertApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**volumesRevert**](VolumesRevertApi.md#volumesRevert) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/revert | Revert a volume to one of its snapshots



## volumesRevert

> volumesRevert(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body)

Revert a volume to one of its snapshots

Revert a volume to the snapshot specified in the body

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.VolumesRevertApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-11-01'"; // String | Version of the API to be used with the client request.
let body = new MicrosoftNetApp.VolumeRevert(); // VolumeRevert | Object for snapshot to revert supplied in the body of the operation.
apiInstance.volumesRevert(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-11-01&#39;]
 **body** | [**VolumeRevert**](VolumeRevert.md)| Object for snapshot to revert supplied in the body of the operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

