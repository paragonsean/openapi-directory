# SqlManagementClient.VirtualNetworkRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualNetworkRulesCreateOrUpdate**](VirtualNetworkRulesApi.md#virtualNetworkRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/virtualNetworkRules/{virtualNetworkRuleName} | 
[**virtualNetworkRulesDelete**](VirtualNetworkRulesApi.md#virtualNetworkRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/virtualNetworkRules/{virtualNetworkRuleName} | 
[**virtualNetworkRulesGet**](VirtualNetworkRulesApi.md#virtualNetworkRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/virtualNetworkRules/{virtualNetworkRuleName} | 
[**virtualNetworkRulesListByServer**](VirtualNetworkRulesApi.md#virtualNetworkRulesListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/virtualNetworkRules | 



## virtualNetworkRulesCreateOrUpdate

> VirtualNetworkRule virtualNetworkRulesCreateOrUpdate(resourceGroupName, serverName, virtualNetworkRuleName, subscriptionId, apiVersion, parameters)



Creates or updates an existing virtual network rule.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.VirtualNetworkRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.VirtualNetworkRule(); // VirtualNetworkRule | The requested virtual Network Rule Resource state.
apiInstance.virtualNetworkRulesCreateOrUpdate(resourceGroupName, serverName, virtualNetworkRuleName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **virtualNetworkRuleName** | **String**| The name of the virtual network rule. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**VirtualNetworkRule**](VirtualNetworkRule.md)| The requested virtual Network Rule Resource state. | 

### Return type

[**VirtualNetworkRule**](VirtualNetworkRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkRulesDelete

> virtualNetworkRulesDelete(resourceGroupName, serverName, virtualNetworkRuleName, subscriptionId, apiVersion)



Deletes the virtual network rule with the given name.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.VirtualNetworkRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.virtualNetworkRulesDelete(resourceGroupName, serverName, virtualNetworkRuleName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **virtualNetworkRuleName** | **String**| The name of the virtual network rule. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualNetworkRulesGet

> VirtualNetworkRule virtualNetworkRulesGet(resourceGroupName, serverName, virtualNetworkRuleName, subscriptionId, apiVersion)



Gets a virtual network rule.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.VirtualNetworkRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.virtualNetworkRulesGet(resourceGroupName, serverName, virtualNetworkRuleName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **virtualNetworkRuleName** | **String**| The name of the virtual network rule. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**VirtualNetworkRule**](VirtualNetworkRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkRulesListByServer

> VirtualNetworkRuleListResult virtualNetworkRulesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Gets a list of virtual network rules in a server.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.VirtualNetworkRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.virtualNetworkRulesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**VirtualNetworkRuleListResult**](VirtualNetworkRuleListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

