# NetworkManagementClient.FirewallPolicyRuleGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firewallPolicyRuleGroupsCreateOrUpdate**](FirewallPolicyRuleGroupsApi.md#firewallPolicyRuleGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}/ruleGroups/{ruleGroupName} | 
[**firewallPolicyRuleGroupsDelete**](FirewallPolicyRuleGroupsApi.md#firewallPolicyRuleGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}/ruleGroups/{ruleGroupName} | 
[**firewallPolicyRuleGroupsGet**](FirewallPolicyRuleGroupsApi.md#firewallPolicyRuleGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}/ruleGroups/{ruleGroupName} | 
[**firewallPolicyRuleGroupsList**](FirewallPolicyRuleGroupsApi.md#firewallPolicyRuleGroupsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}/ruleGroups | 



## firewallPolicyRuleGroupsCreateOrUpdate

> FirewallPolicyRuleGroup firewallPolicyRuleGroupsCreateOrUpdate(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId, parameters)



Creates or updates the specified FirewallPolicyRuleGroup.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FirewallPolicyRuleGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
let ruleGroupName = "ruleGroupName_example"; // String | The name of the FirewallPolicyRuleGroup.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.FirewallPolicyRuleGroup(); // FirewallPolicyRuleGroup | Parameters supplied to the create or update FirewallPolicyRuleGroup operation.
apiInstance.firewallPolicyRuleGroupsCreateOrUpdate(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **firewallPolicyName** | **String**| The name of the Firewall Policy. | 
 **ruleGroupName** | **String**| The name of the FirewallPolicyRuleGroup. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**FirewallPolicyRuleGroup**](FirewallPolicyRuleGroup.md)| Parameters supplied to the create or update FirewallPolicyRuleGroup operation. | 

### Return type

[**FirewallPolicyRuleGroup**](FirewallPolicyRuleGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firewallPolicyRuleGroupsDelete

> firewallPolicyRuleGroupsDelete(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId)



Deletes the specified FirewallPolicyRuleGroup.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FirewallPolicyRuleGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
let ruleGroupName = "ruleGroupName_example"; // String | The name of the FirewallPolicyRuleGroup.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.firewallPolicyRuleGroupsDelete(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **firewallPolicyName** | **String**| The name of the Firewall Policy. | 
 **ruleGroupName** | **String**| The name of the FirewallPolicyRuleGroup. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## firewallPolicyRuleGroupsGet

> FirewallPolicyRuleGroup firewallPolicyRuleGroupsGet(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId)



Gets the specified FirewallPolicyRuleGroup.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FirewallPolicyRuleGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
let ruleGroupName = "ruleGroupName_example"; // String | The name of the FirewallPolicyRuleGroup.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.firewallPolicyRuleGroupsGet(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **firewallPolicyName** | **String**| The name of the Firewall Policy. | 
 **ruleGroupName** | **String**| The name of the FirewallPolicyRuleGroup. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**FirewallPolicyRuleGroup**](FirewallPolicyRuleGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallPolicyRuleGroupsList

> FirewallPolicyRuleGroupListResult firewallPolicyRuleGroupsList(resourceGroupName, firewallPolicyName, apiVersion, subscriptionId)



Lists all FirewallPolicyRuleGroups in a FirewallPolicy resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FirewallPolicyRuleGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.firewallPolicyRuleGroupsList(resourceGroupName, firewallPolicyName, apiVersion, subscriptionId, (error, data, response) => {
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
 **firewallPolicyName** | **String**| The name of the Firewall Policy. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**FirewallPolicyRuleGroupListResult**](FirewallPolicyRuleGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

