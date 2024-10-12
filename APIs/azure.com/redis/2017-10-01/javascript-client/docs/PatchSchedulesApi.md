# RedisManagementClient.PatchSchedulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patchSchedulesCreateOrUpdate_0**](PatchSchedulesApi.md#patchSchedulesCreateOrUpdate_0) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/patchSchedules/{default} | 
[**patchSchedulesDelete_0**](PatchSchedulesApi.md#patchSchedulesDelete_0) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/patchSchedules/{default} | 
[**patchSchedulesGet_0**](PatchSchedulesApi.md#patchSchedulesGet_0) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/patchSchedules/{default} | 
[**patchSchedulesListByRedisResource_0**](PatchSchedulesApi.md#patchSchedulesListByRedisResource_0) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/patchSchedules | 



## patchSchedulesCreateOrUpdate_0

> RedisPatchSchedule patchSchedulesCreateOrUpdate_0(resourceGroupName, name, _default, apiVersion, subscriptionId, parameters)



Create or replace the patching schedule for Redis cache (requires Premium SKU).

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.PatchSchedulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the Redis cache.
let _default = "_default_example"; // String | Default string modeled as parameter for auto generation to work correctly.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisPatchSchedule(); // RedisPatchSchedule | Parameters to set the patching schedule for Redis cache.
apiInstance.patchSchedulesCreateOrUpdate_0(resourceGroupName, name, _default, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **name** | **String**| The name of the Redis cache. | 
 **_default** | **String**| Default string modeled as parameter for auto generation to work correctly. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RedisPatchSchedule**](RedisPatchSchedule.md)| Parameters to set the patching schedule for Redis cache. | 

### Return type

[**RedisPatchSchedule**](RedisPatchSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchSchedulesDelete_0

> patchSchedulesDelete_0(resourceGroupName, name, _default, apiVersion, subscriptionId)



Deletes the patching schedule of a redis cache (requires Premium SKU).

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.PatchSchedulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the redis cache.
let _default = "_default_example"; // String | Default string modeled as parameter for auto generation to work correctly.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.patchSchedulesDelete_0(resourceGroupName, name, _default, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **name** | **String**| The name of the redis cache. | 
 **_default** | **String**| Default string modeled as parameter for auto generation to work correctly. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## patchSchedulesGet_0

> RedisPatchSchedule patchSchedulesGet_0(resourceGroupName, name, _default, apiVersion, subscriptionId)



Gets the patching schedule of a redis cache (requires Premium SKU).

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.PatchSchedulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the redis cache.
let _default = "_default_example"; // String | Default string modeled as parameter for auto generation to work correctly.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.patchSchedulesGet_0(resourceGroupName, name, _default, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **name** | **String**| The name of the redis cache. | 
 **_default** | **String**| Default string modeled as parameter for auto generation to work correctly. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RedisPatchSchedule**](RedisPatchSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchSchedulesListByRedisResource_0

> RedisPatchScheduleListResult patchSchedulesListByRedisResource_0(apiVersion, subscriptionId, resourceGroupName, cacheName)



Gets all patch schedules in the specified redis cache (there is only one).

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.PatchSchedulesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let cacheName = "cacheName_example"; // String | The name of the Redis cache.
apiInstance.patchSchedulesListByRedisResource_0(apiVersion, subscriptionId, resourceGroupName, cacheName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **cacheName** | **String**| The name of the Redis cache. | 

### Return type

[**RedisPatchScheduleListResult**](RedisPatchScheduleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

