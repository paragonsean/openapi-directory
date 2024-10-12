# StorageCacheMgmtClient.CachesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cachesCreateOrUpdate**](CachesApi.md#cachesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName} | 
[**cachesDelete**](CachesApi.md#cachesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName} | 
[**cachesFlush**](CachesApi.md#cachesFlush) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/flush | 
[**cachesGet**](CachesApi.md#cachesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName} | 
[**cachesList**](CachesApi.md#cachesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.StorageCache/caches | 
[**cachesListByResourceGroup**](CachesApi.md#cachesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches | 
[**cachesStart**](CachesApi.md#cachesStart) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/start | 
[**cachesStop**](CachesApi.md#cachesStop) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/stop | 
[**cachesUpdate**](CachesApi.md#cachesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName} | 
[**cachesUpgradeFirmware**](CachesApi.md#cachesUpgradeFirmware) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/upgrade | 



## cachesCreateOrUpdate

> Cache cachesCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, opts)



Create or update a Cache.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.CachesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of Cache.
let opts = {
  'cache': new StorageCacheMgmtClient.Cache() // Cache | Object containing the user-selectable properties of the new Cache. If read-only properties are included, they must match the existing values of those properties.
};
apiInstance.cachesCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, opts, (error, data, response) => {
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
 **cache** | [**Cache**](Cache.md)| Object containing the user-selectable properties of the new Cache. If read-only properties are included, they must match the existing values of those properties. | [optional] 

### Return type

[**Cache**](Cache.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cachesDelete

> Object cachesDelete(resourceGroupName, cacheName, apiVersion, subscriptionId)



Schedules a Cache for deletion.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.CachesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let cacheName = "cacheName_example"; // String | Name of Cache.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.cachesDelete(resourceGroupName, cacheName, apiVersion, subscriptionId, (error, data, response) => {
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
 **cacheName** | **String**| Name of Cache. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cachesFlush

> Object cachesFlush(resourceGroupName, apiVersion, subscriptionId, cacheName)



Tells a Cache to write all dirty data to the Storage Target(s). During the flush, clients will see errors returned until the flush is complete.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.CachesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of Cache.
apiInstance.cachesFlush(resourceGroupName, apiVersion, subscriptionId, cacheName, (error, data, response) => {
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

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cachesGet

> Cache cachesGet(resourceGroupName, cacheName, apiVersion, subscriptionId)



Returns a Cache.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.CachesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let cacheName = "cacheName_example"; // String | Name of Cache.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.cachesGet(resourceGroupName, cacheName, apiVersion, subscriptionId, (error, data, response) => {
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
 **cacheName** | **String**| Name of Cache. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Cache**](Cache.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cachesList

> CachesListResult cachesList(apiVersion, subscriptionId)



Returns all Caches the user has access to under a subscription.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.CachesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.cachesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**CachesListResult**](CachesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cachesListByResourceGroup

> CachesListResult cachesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Returns all Caches the user has access to under a resource group.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.CachesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.cachesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**CachesListResult**](CachesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cachesStart

> Object cachesStart(resourceGroupName, apiVersion, subscriptionId, cacheName)



Tells a Stopped state Cache to transition to Active state.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.CachesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of Cache.
apiInstance.cachesStart(resourceGroupName, apiVersion, subscriptionId, cacheName, (error, data, response) => {
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

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cachesStop

> Object cachesStop(resourceGroupName, apiVersion, subscriptionId, cacheName)



Tells an Active Cache to transition to Stopped state.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.CachesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of Cache.
apiInstance.cachesStop(resourceGroupName, apiVersion, subscriptionId, cacheName, (error, data, response) => {
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

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cachesUpdate

> Cache cachesUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, opts)



Update a Cache instance.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.CachesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of Cache.
let opts = {
  'cache': new StorageCacheMgmtClient.Cache() // Cache | Object containing the user-selectable properties of the Cache. If read-only properties are included, they must match the existing values of those properties.
};
apiInstance.cachesUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, opts, (error, data, response) => {
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
 **cache** | [**Cache**](Cache.md)| Object containing the user-selectable properties of the Cache. If read-only properties are included, they must match the existing values of those properties. | [optional] 

### Return type

[**Cache**](Cache.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cachesUpgradeFirmware

> Object cachesUpgradeFirmware(resourceGroupName, apiVersion, subscriptionId, cacheName)



Upgrade a Cache&#39;s firmware if a new version is available. Otherwise, this operation has no effect.

### Example

```javascript
import StorageCacheMgmtClient from 'storage_cache_mgmt_client';
let defaultClient = StorageCacheMgmtClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageCacheMgmtClient.CachesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Target resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let cacheName = "cacheName_example"; // String | Name of Cache.
apiInstance.cachesUpgradeFirmware(resourceGroupName, apiVersion, subscriptionId, cacheName, (error, data, response) => {
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

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

