# NetworkManagementClient.SecurityRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**securityRulesCreateOrUpdate**](SecurityRulesApi.md#securityRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}/securityRules/{securityRuleName} | 
[**securityRulesDelete**](SecurityRulesApi.md#securityRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}/securityRules/{securityRuleName} | 
[**securityRulesGet**](SecurityRulesApi.md#securityRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}/securityRules/{securityRuleName} | 
[**securityRulesList**](SecurityRulesApi.md#securityRulesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkSecurityGroups/{networkSecurityGroupName}/securityRules | 



## securityRulesCreateOrUpdate

> SecurityRule securityRulesCreateOrUpdate(resourceGroupName, networkSecurityGroupName, securityRuleName, apiVersion, subscriptionId, securityRuleParameters)



The Put network security rule operation creates/updates a security rule in the specified network security group

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.SecurityRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkSecurityGroupName = "networkSecurityGroupName_example"; // String | The name of the network security group.
let securityRuleName = "securityRuleName_example"; // String | The name of the security rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let securityRuleParameters = new NetworkManagementClient.SecurityRule(); // SecurityRule | Parameters supplied to the create/update network security rule operation
apiInstance.securityRulesCreateOrUpdate(resourceGroupName, networkSecurityGroupName, securityRuleName, apiVersion, subscriptionId, securityRuleParameters, (error, data, response) => {
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
 **networkSecurityGroupName** | **String**| The name of the network security group. | 
 **securityRuleName** | **String**| The name of the security rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **securityRuleParameters** | [**SecurityRule**](SecurityRule.md)| Parameters supplied to the create/update network security rule operation | 

### Return type

[**SecurityRule**](SecurityRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## securityRulesDelete

> securityRulesDelete(resourceGroupName, networkSecurityGroupName, securityRuleName, apiVersion, subscriptionId)



The delete network security rule operation deletes the specified network security rule.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.SecurityRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkSecurityGroupName = "networkSecurityGroupName_example"; // String | The name of the network security group.
let securityRuleName = "securityRuleName_example"; // String | The name of the security rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.securityRulesDelete(resourceGroupName, networkSecurityGroupName, securityRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **networkSecurityGroupName** | **String**| The name of the network security group. | 
 **securityRuleName** | **String**| The name of the security rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## securityRulesGet

> SecurityRule securityRulesGet(resourceGroupName, networkSecurityGroupName, securityRuleName, apiVersion, subscriptionId)



The Get NetworkSecurityRule operation retrieves information about the specified network security rule.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.SecurityRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkSecurityGroupName = "networkSecurityGroupName_example"; // String | The name of the network security group.
let securityRuleName = "securityRuleName_example"; // String | The name of the security rule.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.securityRulesGet(resourceGroupName, networkSecurityGroupName, securityRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **networkSecurityGroupName** | **String**| The name of the network security group. | 
 **securityRuleName** | **String**| The name of the security rule. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SecurityRule**](SecurityRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## securityRulesList

> SecurityRuleListResult securityRulesList(resourceGroupName, networkSecurityGroupName, apiVersion, subscriptionId)



The List network security rule operation retrieves all the security rules in a network security group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.SecurityRulesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkSecurityGroupName = "networkSecurityGroupName_example"; // String | The name of the network security group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.securityRulesList(resourceGroupName, networkSecurityGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **networkSecurityGroupName** | **String**| The name of the network security group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SecurityRuleListResult**](SecurityRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

