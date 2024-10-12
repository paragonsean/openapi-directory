# RedisManagementClient.FirewallRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firewallRulesList_0**](FirewallRulesApi.md#firewallRulesList_0) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules | 
[**redisFirewallRuleCreateOrUpdate_0**](FirewallRulesApi.md#redisFirewallRuleCreateOrUpdate_0) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules/{ruleName} | 
[**redisFirewallRuleDelete_0**](FirewallRulesApi.md#redisFirewallRuleDelete_0) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules/{ruleName} | 
[**redisFirewallRuleGet_0**](FirewallRulesApi.md#redisFirewallRuleGet_0) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/Redis/{cacheName}/firewallRules/{ruleName} | 



## firewallRulesList_0

> RedisFirewallRuleListResult firewallRulesList_0(apiVersion, subscriptionId, resourceGroupName, cacheName)



Gets all firewall rules in the specified redis cache.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.FirewallRulesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let cacheName = "cacheName_example"; // String | The name of the Redis cache.
apiInstance.firewallRulesList_0(apiVersion, subscriptionId, resourceGroupName, cacheName, (error, data, response) => {
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


## redisFirewallRuleCreateOrUpdate_0

> RedisFirewallRule redisFirewallRuleCreateOrUpdate_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId, parameters)



Create or update a redis cache firewall rule

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.FirewallRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let cacheName = "cacheName_example"; // String | The name of the Redis cache.
let ruleName = "ruleName_example"; // String | The name of the firewall rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new RedisManagementClient.RedisFirewallRule(); // RedisFirewallRule | Parameters supplied to the create or update redis firewall rule operation.
apiInstance.redisFirewallRuleCreateOrUpdate_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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


## redisFirewallRuleDelete_0

> redisFirewallRuleDelete_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId)



Deletes a single firewall rule in a specified redis cache.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.FirewallRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let cacheName = "cacheName_example"; // String | The name of the Redis cache.
let ruleName = "ruleName_example"; // String | The name of the firewall rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.redisFirewallRuleDelete_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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


## redisFirewallRuleGet_0

> RedisFirewallRule redisFirewallRuleGet_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId)



Gets a single firewall rule in a specified redis cache.

### Example

```javascript
import RedisManagementClient from 'redis_management_client';
let defaultClient = RedisManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RedisManagementClient.FirewallRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let cacheName = "cacheName_example"; // String | The name of the Redis cache.
let ruleName = "ruleName_example"; // String | The name of the firewall rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.redisFirewallRuleGet_0(resourceGroupName, cacheName, ruleName, apiVersion, subscriptionId, (error, data, response) => {
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

