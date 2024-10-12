# FabricAdminClient.FileSharesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileSharesGet**](FileSharesApi.md#fileSharesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/fileShares/{fileShare} | 
[**fileSharesList**](FileSharesApi.md#fileSharesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/fileShares | 



## fileSharesGet

> FileShare fileSharesGet(subscriptionId, resourceGroupName, location, fileShare, apiVersion)



Returns the requested fabric file share.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.FileSharesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let fileShare = "fileShare_example"; // String | Fabric file share name.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.fileSharesGet(subscriptionId, resourceGroupName, location, fileShare, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Location of the resource. | 
 **fileShare** | **String**| Fabric file share name. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**FileShare**](FileShare.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileSharesList

> FileShareList fileSharesList(subscriptionId, resourceGroupName, location, apiVersion, opts)



Returns a list of all fabric file shares at a certain location.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.FileSharesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
let opts = {
  'filter': "filter_example" // String | OData filter parameter.
};
apiInstance.fileSharesList(subscriptionId, resourceGroupName, location, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Location of the resource. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]
 **filter** | **String**| OData filter parameter. | [optional] 

### Return type

[**FileShareList**](FileShareList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

