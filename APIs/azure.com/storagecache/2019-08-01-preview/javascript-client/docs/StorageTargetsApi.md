# StorageCacheMgmtClient.StorageTargetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageTargetsCreate**](StorageTargetsApi.md#storageTargetsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} | 
[**storageTargetsDelete**](StorageTargetsApi.md#storageTargetsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} | 
[**storageTargetsGet**](StorageTargetsApi.md#storageTargetsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} | 
[**storageTargetsListByCache**](StorageTargetsApi.md#storageTargetsListByCache) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets | 
[**storageTargetsUpdate**](StorageTargetsApi.md#storageTargetsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/storageTargets/{storageTargetName} | 



## storageTargetsCreate

> StorageTarget storageTargetsCreate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, opts)



Create/update a storage target.  This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the storage target may be delayed until the cache is healthy again.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.StorageTargetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of cache.
let storageTargetName = "storageTargetName_example"; // String | Name of storage target.
let opts = {
  'storagetarget': new StorageCacheMgmtClient.StorageTarget() // StorageTarget | Object containing the definition of a storage target.
};
apiInstance.storageTargetsCreate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **cacheName** | **String**| Name of cache. | 
 **storageTargetName** | **String**| Name of storage target. | 
 **storagetarget** | [**StorageTarget**](StorageTarget.md)| Object containing the definition of a storage target. | [optional] 

### Return type

[**StorageTarget**](StorageTarget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageTargetsDelete

> Object storageTargetsDelete(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName)



Removes a storage target from a cache.  This operation is allowed at any time, but if the cache is down or unhealthy, the actual removal of the storage target may be delayed until the cache is healthy again.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.StorageTargetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of cache.
let storageTargetName = "storageTargetName_example"; // String | Name of storage target.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **cacheName** | **String**| Name of cache. | 
 **storageTargetName** | **String**| Name of storage target. | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageTargetsGet

> StorageTarget storageTargetsGet(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName)



Returns a storage target from a cache.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.StorageTargetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of cache.
let storageTargetName = "storageTargetName_example"; // String | Name of storage target.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **cacheName** | **String**| Name of cache. | 
 **storageTargetName** | **String**| Name of storage target. | 

### Return type

[**StorageTarget**](StorageTarget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageTargetsListByCache

> StorageTargetsResult storageTargetsListByCache(resourceGroupName, apiVersion, subscriptionId, cacheName)



Returns the StorageTargets for this cache in the subscription and resource group.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.StorageTargetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of cache.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **cacheName** | **String**| Name of cache. | 

### Return type

[**StorageTargetsResult**](StorageTargetsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageTargetsUpdate

> StorageTarget storageTargetsUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, opts)



Update a storage target.  This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the storage target may be delayed until the cache is healthy again.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.StorageTargetsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of cache.
let storageTargetName = "storageTargetName_example"; // String | Name of storage target.
let opts = {
  'storagetarget': new StorageCacheMgmtClient.StorageTarget() // StorageTarget | Object containing the definition of a storage target.
};
apiInstance.storageTargetsUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, storageTargetName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **cacheName** | **String**| Name of cache. | 
 **storageTargetName** | **String**| Name of storage target. | 
 **storagetarget** | [**StorageTarget**](StorageTarget.md)| Object containing the definition of a storage target. | [optional] 

### Return type

[**StorageTarget**](StorageTarget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

