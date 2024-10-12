# AzureSqlDatabaseServerFirewallRules.FirewallRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firewallRulesCreateOrUpdate**](FirewallRulesApi.md#firewallRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules/{firewallRuleName} | 
[**firewallRulesDelete**](FirewallRulesApi.md#firewallRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules/{firewallRuleName} | 
[**firewallRulesGet**](FirewallRulesApi.md#firewallRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules/{firewallRuleName} | 
[**firewallRulesListByServer**](FirewallRulesApi.md#firewallRulesListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/firewallRules | 



## firewallRulesCreateOrUpdate

> FirewallRule firewallRulesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, firewallRuleName, parameters)



Creates or updates a firewall rule.

### Example

```javascript
import AzureSqlDatabaseServerFirewallRules from 'azure_sql_database_server_firewall_rules';

let apiInstance = new AzureSqlDatabaseServerFirewallRules.FirewallRulesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule.
let parameters = new AzureSqlDatabaseServerFirewallRules.FirewallRule(); // FirewallRule | The required parameters for creating or updating a firewall rule.
apiInstance.firewallRulesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, firewallRuleName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **firewallRuleName** | **String**| The name of the firewall rule. | 
 **parameters** | [**FirewallRule**](FirewallRule.md)| The required parameters for creating or updating a firewall rule. | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firewallRulesDelete

> firewallRulesDelete(apiVersion, subscriptionId, resourceGroupName, serverName, firewallRuleName)



Deletes a firewall rule.

### Example

```javascript
import AzureSqlDatabaseServerFirewallRules from 'azure_sql_database_server_firewall_rules';

let apiInstance = new AzureSqlDatabaseServerFirewallRules.FirewallRulesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule.
apiInstance.firewallRulesDelete(apiVersion, subscriptionId, resourceGroupName, serverName, firewallRuleName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **firewallRuleName** | **String**| The name of the firewall rule. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## firewallRulesGet

> FirewallRule firewallRulesGet(apiVersion, subscriptionId, resourceGroupName, serverName, firewallRuleName)



Gets a firewall rule.

### Example

```javascript
import AzureSqlDatabaseServerFirewallRules from 'azure_sql_database_server_firewall_rules';

let apiInstance = new AzureSqlDatabaseServerFirewallRules.FirewallRulesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule.
apiInstance.firewallRulesGet(apiVersion, subscriptionId, resourceGroupName, serverName, firewallRuleName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **firewallRuleName** | **String**| The name of the firewall rule. | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallRulesListByServer

> FirewallRuleListResult firewallRulesListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



Returns a list of firewall rules.

### Example

```javascript
import AzureSqlDatabaseServerFirewallRules from 'azure_sql_database_server_firewall_rules';

let apiInstance = new AzureSqlDatabaseServerFirewallRules.FirewallRulesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
apiInstance.firewallRulesListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 

### Return type

[**FirewallRuleListResult**](FirewallRuleListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

