# FabricAdminClient.StoragePoolsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storagePoolsGet**](StoragePoolsApi.md#storagePoolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/storageSubSystems/{storageSubSystem}/storagePools/{storagePool} | 
[**storagePoolsList**](StoragePoolsApi.md#storagePoolsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/storageSubSystems/{storageSubSystem}/storagePools | 



## storagePoolsGet

> StoragePool storagePoolsGet(subscriptionId, resourceGroupName, location, storageSubSystem, storagePool, apiVersion)



Return the requested a storage pool.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.StoragePoolsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let storageSubSystem = "storageSubSystem_example"; // String | Name of the storage system.
let storagePool = "storagePool_example"; // String | Storage pool name.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
apiInstance.storagePoolsGet(subscriptionId, resourceGroupName, location, storageSubSystem, storagePool, apiVersion, (error, data, response) => {
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
 **storageSubSystem** | **String**| Name of the storage system. | 
 **storagePool** | **String**| Storage pool name. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**StoragePool**](StoragePool.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storagePoolsList

> StoragePoolList storagePoolsList(subscriptionId, resourceGroupName, location, storageSubSystem, apiVersion, opts)



Returns a list of all storage pools for a location.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.StoragePoolsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Location of the resource.
let storageSubSystem = "storageSubSystem_example"; // String | Name of the storage system.
let apiVersion = "'2016-05-01'"; // String | Client API Version.
let opts = {
  'filter': "filter_example" // String | OData filter parameter.
};
apiInstance.storagePoolsList(subscriptionId, resourceGroupName, location, storageSubSystem, apiVersion, opts, (error, data, response) => {
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
 **storageSubSystem** | **String**| Name of the storage system. | 
 **apiVersion** | **String**| Client API Version. | [default to &#39;2016-05-01&#39;]
 **filter** | **String**| OData filter parameter. | [optional] 

### Return type

[**StoragePoolList**](StoragePoolList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

