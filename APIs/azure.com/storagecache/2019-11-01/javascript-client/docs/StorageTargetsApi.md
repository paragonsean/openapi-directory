# StorageCacheMgmtClient.StorageTargetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageTargetsCreateOrUpdate**](StorageTargetsApi.md#storageTargetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} | 
[**storageTargetsDelete**](StorageTargetsApi.md#storageTargetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} | 
[**storageTargetsGet**](StorageTargetsApi.md#storageTargetsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} | 
[**storageTargetsListByCache**](StorageTargetsApi.md#storageTargetsListByCache) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets | 



## storageTargetsCreateOrUpdate

> StorageTarget storageTargetsCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, opts)



Create or update a Storage Target. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the Cache is healthy again.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.StorageTargetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of Cache.
let storageTargetName = "storageTargetName_example"; // String | Name of the Storage Target.
let opts = {
  'storagetarget': new StorageCacheMgmtClient.StorageTarget() // StorageTarget | Object containing the definition of a Storage Target.
};
apiInstance.storageTargetsCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Target resource group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **cacheName** | **String**| Name of Cache. | 
 **storageTargetName** | **String**| Name of the Storage Target. | 
 **storagetarget** | [**StorageTarget**](StorageTarget.md)| Object containing the definition of a Storage Target. | [optional] 

### Return type

[**StorageTarget**](StorageTarget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageTargetsDelete

> Object storageTargetsDelete(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName)



Removes a Storage Target from a Cache. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual removal of the Storage Target may be delayed until the Cache is healthy again. Note that if the Cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.StorageTargetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of Cache.
let storageTargetName = "storageTargetName_example"; // String | Name of Storage Target.
apiInstance.storageTargetsDelete(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, (error, data, response) => {
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
 **resourceGroupName** | **String**| Target resource group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **cacheName** | **String**| Name of Cache. | 
 **storageTargetName** | **String**| Name of Storage Target. | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageTargetsGet

> StorageTarget storageTargetsGet(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName)



Returns a Storage Target from a Cache.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.StorageTargetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of Cache.
let storageTargetName = "storageTargetName_example"; // String | Name of the Storage Target.
apiInstance.storageTargetsGet(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, (error, data, response) => {
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
 **resourceGroupName** | **String**| Target resource group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **cacheName** | **String**| Name of Cache. | 
 **storageTargetName** | **String**| Name of the Storage Target. | 

### Return type

[**StorageTarget**](StorageTarget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageTargetsListByCache

> StorageTargetsResult storageTargetsListByCache(resourceGroupName, apiVersion, subscriptionId, cacheName)



Returns a list of Storage Targets for the specified Cache.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.StorageTargetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of Cache.
apiInstance.storageTargetsListByCache(resourceGroupName, apiVersion, subscriptionId, cacheName, (error, data, response) => {
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
 **resourceGroupName** | **String**| Target resource group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **cacheName** | **String**| Name of Cache. | 

### Return type

[**StorageTargetsResult**](StorageTargetsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

