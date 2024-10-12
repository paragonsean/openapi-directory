# MicrosoftNetApp.MountTargetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mountTargetsList**](MountTargetsApi.md#mountTargetsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/mountTargets | Describe all mount targets



## mountTargetsList

> MountTargetList mountTargetsList(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Describe all mount targets

List all mount targets associated with the volume

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.MountTargetsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let accountName = "accountName_example"; // String | The name of the NetApp account
let poolName = "poolName_example"; // String | The name of the capacity pool
let volumeName = "volumeName_example"; // String | The name of the volume
let apiVersion = "'2019-05-01'"; // String | Version of the API to be used with the client request.
apiInstance.mountTargetsList(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **accountName** | **String**| The name of the NetApp account | 
 **poolName** | **String**| The name of the capacity pool | 
 **volumeName** | **String**| The name of the volume | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-05-01&#39;]

### Return type

[**MountTargetList**](MountTargetList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

