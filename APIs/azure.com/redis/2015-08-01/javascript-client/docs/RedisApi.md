# RedisManagementClient.RedisApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redisCreateOrUpdate**](RedisApi.md#redisCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name} | 
[**redisDelete**](RedisApi.md#redisDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name} | 
[**redisForceReboot**](RedisApi.md#redisForceReboot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/forceReboot | 
[**redisGet**](RedisApi.md#redisGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name} | 
[**redisList**](RedisApi.md#redisList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Cache/Redis/ | 
[**redisListByResourceGroup**](RedisApi.md#redisListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/ | 
[**redisListKeys**](RedisApi.md#redisListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/listKeys | 
[**redisRegenerateKey**](RedisApi.md#redisRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/regenerateKey | 



## redisCreateOrUpdate

> RedisResourceWithAccessKey redisCreateOrUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Create a Redis cache, or replace (overwrite/recreate, with potential downtime) an existing cache.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the Redis cache.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisCreateOrUpdateParameters(); // RedisCreateOrUpdateParameters | Parameters supplied to the CreateOrUpdate Redis operation.
apiInstance.redisCreateOrUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RedisCreateOrUpdateParameters**](RedisCreateOrUpdateParameters.md)| Parameters supplied to the CreateOrUpdate Redis operation. | 

### Return type

[**RedisResourceWithAccessKey**](RedisResourceWithAccessKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## redisDelete

> redisDelete(resourceGroupName, name, apiVersion, subscriptionId)



Deletes a Redis cache.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the Redis cache.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.redisDelete(resourceGroupName, name, apiVersion, subscriptionId, (error, data, response) => {
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
 **name** | **String**| The name of the Redis cache. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## redisForceReboot

> redisForceReboot(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Reboot specified Redis node(s). This operation requires write permission to the cache resource. There can be potential data loss.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the Redis cache.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisRebootParameters(); // RedisRebootParameters | Specifies which Redis node(s) to reboot.
apiInstance.redisForceReboot(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **name** | **String**| The name of the Redis cache. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RedisRebootParameters**](RedisRebootParameters.md)| Specifies which Redis node(s) to reboot. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## redisGet

> RedisResource redisGet(resourceGroupName, name, apiVersion, subscriptionId)



Gets a Redis cache (resource description).

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the Redis cache.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.redisGet(resourceGroupName, name, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RedisResource**](RedisResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redisList

> RedisListResult redisList(apiVersion, subscriptionId)



Gets all Redis caches in the specified subscription.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.redisList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RedisListResult**](RedisListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redisListByResourceGroup

> RedisListResult redisListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all Redis caches in a resource group.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.redisListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RedisListResult**](RedisListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redisListKeys

> RedisListKeysResult redisListKeys(resourceGroupName, name, apiVersion, subscriptionId)



Retrieve a Redis cache&#39;s access keys. This operation requires write permission to the cache resource.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the Redis cache.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.redisListKeys(resourceGroupName, name, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RedisListKeysResult**](RedisListKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redisRegenerateKey

> RedisListKeysResult redisRegenerateKey(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Regenerate the access keys for a Redis cache. This operation requires write permission to the cache resource.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the Redis cache.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisRegenerateKeyParameters(); // RedisRegenerateKeyParameters | Specifies which key to reset.
apiInstance.redisRegenerateKey(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RedisRegenerateKeyParameters**](RedisRegenerateKeyParameters.md)| Specifies which key to reset. | 

### Return type

[**RedisListKeysResult**](RedisListKeysResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

