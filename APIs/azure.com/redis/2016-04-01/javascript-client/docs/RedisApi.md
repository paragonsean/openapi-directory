# RedisManagementClient.RedisApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firewallRulesList**](RedisApi.md#firewallRulesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules | 
[**patchSchedulesCreateOrUpdate**](RedisApi.md#patchSchedulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/patchSchedules/default | 
[**patchSchedulesDelete**](RedisApi.md#patchSchedulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/patchSchedules/default | 
[**patchSchedulesGet**](RedisApi.md#patchSchedulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/patchSchedules/default | 
[**redisCreate**](RedisApi.md#redisCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name} | 
[**redisDelete**](RedisApi.md#redisDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name} | 
[**redisExportData**](RedisApi.md#redisExportData) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/export | 
[**redisFirewallRuleCreateOrUpdate**](RedisApi.md#redisFirewallRuleCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules/{ruleName} | 
[**redisFirewallRuleDelete**](RedisApi.md#redisFirewallRuleDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules/{ruleName} | 
[**redisFirewallRuleGet**](RedisApi.md#redisFirewallRuleGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules/{ruleName} | 
[**redisForceReboot**](RedisApi.md#redisForceReboot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/forceReboot | 
[**redisGet**](RedisApi.md#redisGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name} | 
[**redisImportData**](RedisApi.md#redisImportData) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/import | 
[**redisList**](RedisApi.md#redisList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Cache/Redis/ | 
[**redisListByResourceGroup**](RedisApi.md#redisListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/ | 
[**redisListKeys**](RedisApi.md#redisListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/listKeys | 
[**redisRegenerateKey**](RedisApi.md#redisRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name}/regenerateKey | 
[**redisUpdate**](RedisApi.md#redisUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{name} | 



## firewallRulesList

> RedisFirewallRuleListResult firewallRulesList(apiVersion, subscriptionId, resourceGroupName, cacheName)



Gets all firewall rules in the specified redis cache.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let cacheName = "cacheName_example"; // String | The name of the Redis cache.
apiInstance.firewallRulesList(apiVersion, subscriptionId, resourceGroupName, cacheName, (error, data, response) => {
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

[**RedisFirewallRuleListResult**](RedisFirewallRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchSchedulesCreateOrUpdate

> RedisPatchSchedule patchSchedulesCreateOrUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Create or replace the patching schedule for Redis cache (requires Premium SKU).

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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisPatchSchedule(); // RedisPatchSchedule | Parameters to set the patching schedule for Redis cache.
apiInstance.patchSchedulesCreateOrUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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


## patchSchedulesDelete

> patchSchedulesDelete(resourceGroupName, name, apiVersion, subscriptionId)



Deletes the patching schedule of a redis cache (requires Premium SKU).

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the redis cache.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.patchSchedulesDelete(resourceGroupName, name, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## patchSchedulesGet

> RedisPatchSchedule patchSchedulesGet(resourceGroupName, name, apiVersion, subscriptionId)



Gets the patching schedule of a redis cache (requires Premium SKU).

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let name = "name_example"; // String | The name of the redis cache.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.patchSchedulesGet(resourceGroupName, name, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RedisPatchSchedule**](RedisPatchSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redisCreate

> RedisResource redisCreate(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Create or replace (overwrite/recreate, with potential downtime) an existing Redis cache.

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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisCreateParameters(); // RedisCreateParameters | Parameters supplied to the Create Redis operation.
apiInstance.redisCreate(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RedisCreateParameters**](RedisCreateParameters.md)| Parameters supplied to the Create Redis operation. | 

### Return type

[**RedisResource**](RedisResource.md)

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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## redisExportData

> redisExportData(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Export data from the redis cache to blobs in a container.

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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.ExportRDBParameters(); // ExportRDBParameters | Parameters for Redis export operation.
apiInstance.redisExportData(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ExportRDBParameters**](ExportRDBParameters.md)| Parameters for Redis export operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## redisFirewallRuleCreateOrUpdate

> RedisFirewallRule redisFirewallRuleCreateOrUpdate(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId, parameters)



Create or update a redis cache firewall rule

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let cacheName = "cacheName_example"; // String | The name of the Redis cache.
let ruleName = "ruleName_example"; // String | The name of the firewall rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisFirewallRule(); // RedisFirewallRule | Parameters supplied to the create or update redis firewall rule operation.
apiInstance.redisFirewallRuleCreateOrUpdate(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **cacheName** | **String**| The name of the Redis cache. | 
 **ruleName** | **String**| The name of the firewall rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RedisFirewallRule**](RedisFirewallRule.md)| Parameters supplied to the create or update redis firewall rule operation. | 

### Return type

[**RedisFirewallRule**](RedisFirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## redisFirewallRuleDelete

> redisFirewallRuleDelete(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId)



Deletes a single firewall rule in a specified redis cache.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let cacheName = "cacheName_example"; // String | The name of the Redis cache.
let ruleName = "ruleName_example"; // String | The name of the firewall rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.redisFirewallRuleDelete(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **cacheName** | **String**| The name of the Redis cache. | 
 **ruleName** | **String**| The name of the firewall rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## redisFirewallRuleGet

> RedisFirewallRule redisFirewallRuleGet(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId)



Gets a single firewall rule in a specified redis cache.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let cacheName = "cacheName_example"; // String | The name of the Redis cache.
let ruleName = "ruleName_example"; // String | The name of the firewall rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.redisFirewallRuleGet(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **cacheName** | **String**| The name of the Redis cache. | 
 **ruleName** | **String**| The name of the firewall rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RedisFirewallRule**](RedisFirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redisForceReboot

> RedisForceRebootResponse redisForceReboot(resourceGroupName, name, apiVersion, subscriptionId, parameters)



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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisRebootParameters(); // RedisRebootParameters | Specifies which Redis node(s) to reboot.
apiInstance.redisForceReboot(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RedisRebootParameters**](RedisRebootParameters.md)| Specifies which Redis node(s) to reboot. | 

### Return type

[**RedisForceRebootResponse**](RedisForceRebootResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RedisResource**](RedisResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redisImportData

> redisImportData(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Import data into Redis cache.

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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.ImportRDBParameters(); // ImportRDBParameters | Parameters for Redis import operation.
apiInstance.redisImportData(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ImportRDBParameters**](ImportRDBParameters.md)| Parameters for Redis import operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | 
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



Lists all Redis caches in a resource group.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.RedisApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RedisListResult**](RedisListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redisListKeys

> RedisAccessKeys redisListKeys(resourceGroupName, name, apiVersion, subscriptionId)



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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**RedisAccessKeys**](RedisAccessKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redisRegenerateKey

> RedisAccessKeys redisRegenerateKey(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Regenerate Redis cache&#39;s access keys. This operation requires write permission to the cache resource.

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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisRegenerateKeyParameters(); // RedisRegenerateKeyParameters | Specifies which key to regenerate.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RedisRegenerateKeyParameters**](RedisRegenerateKeyParameters.md)| Specifies which key to regenerate. | 

### Return type

[**RedisAccessKeys**](RedisAccessKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## redisUpdate

> RedisResource redisUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Update an existing Redis cache.

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
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisUpdateParameters(); // RedisUpdateParameters | Parameters supplied to the Update Redis operation.
apiInstance.redisUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RedisUpdateParameters**](RedisUpdateParameters.md)| Parameters supplied to the Update Redis operation. | 

### Return type

[**RedisResource**](RedisResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

