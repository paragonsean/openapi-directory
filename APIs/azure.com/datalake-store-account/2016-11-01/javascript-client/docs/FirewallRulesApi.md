# DataLakeStoreAccountManagementClient.FirewallRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firewallRulesCreateOrUpdate**](FirewallRulesApi.md#firewallRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{firewallRuleName} | 
[**firewallRulesDelete**](FirewallRulesApi.md#firewallRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{firewallRuleName} | 
[**firewallRulesGet**](FirewallRulesApi.md#firewallRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{firewallRuleName} | 
[**firewallRulesListByAccount**](FirewallRulesApi.md#firewallRulesListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules | 
[**firewallRulesUpdate**](FirewallRulesApi.md#firewallRulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{firewallRuleName} | 



## firewallRulesCreateOrUpdate

> FirewallRule firewallRulesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion, parameters)



Creates or updates the specified firewall rule. During update, the firewall rule with the specified name will be replaced with this new firewall rule.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.FirewallRulesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule to create or update.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new DataLakeStoreAccountManagementClient.CreateOrUpdateFirewallRuleParameters(); // CreateOrUpdateFirewallRuleParameters | Parameters supplied to create or update the firewall rule.
apiInstance.firewallRulesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **firewallRuleName** | **String**| The name of the firewall rule to create or update. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**CreateOrUpdateFirewallRuleParameters**](CreateOrUpdateFirewallRuleParameters.md)| Parameters supplied to create or update the firewall rule. | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firewallRulesDelete

> firewallRulesDelete(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion)



Deletes the specified firewall rule from the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.FirewallRulesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule to delete.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.firewallRulesDelete(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **firewallRuleName** | **String**| The name of the firewall rule to delete. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## firewallRulesGet

> FirewallRule firewallRulesGet(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion)



Gets the specified Data Lake Store firewall rule.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.FirewallRulesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule to retrieve.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.firewallRulesGet(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **firewallRuleName** | **String**| The name of the firewall rule to retrieve. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallRulesListByAccount

> FirewallRuleListResult firewallRulesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Data Lake Store firewall rules within the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.FirewallRulesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.firewallRulesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**FirewallRuleListResult**](FirewallRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firewallRulesUpdate

> FirewallRule firewallRulesUpdate(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion, opts)



Updates the specified firewall rule.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.FirewallRulesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule to update.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'parameters': new DataLakeStoreAccountManagementClient.UpdateFirewallRuleParameters() // UpdateFirewallRuleParameters | Parameters supplied to update the firewall rule.
};
apiInstance.firewallRulesUpdate(subscriptionId, resourceGroupName, accountName, firewallRuleName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **firewallRuleName** | **String**| The name of the firewall rule to update. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**UpdateFirewallRuleParameters**](UpdateFirewallRuleParameters.md)| Parameters supplied to update the firewall rule. | [optional] 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

