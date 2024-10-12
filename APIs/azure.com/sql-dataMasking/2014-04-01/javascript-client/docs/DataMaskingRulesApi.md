# AzureSqlDatabaseDatamaskingPoliciesAndRules.DataMaskingRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataMaskingRulesCreateOrUpdate**](DataMaskingRulesApi.md#dataMaskingRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName}/rules/{dataMaskingRuleName} | 
[**dataMaskingRulesListByDatabase**](DataMaskingRulesApi.md#dataMaskingRulesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName}/rules | 



## dataMaskingRulesCreateOrUpdate

> DataMaskingRule dataMaskingRulesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName, dataMaskingRuleName, parameters)



Creates or updates a database data masking rule.

### Example

```javascript
import AzureSqlDatabaseDatamaskingPoliciesAndRules from 'azure_sql_database_datamasking_policies_and_rules';

let apiInstance = new AzureSqlDatabaseDatamaskingPoliciesAndRules.DataMaskingRulesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let dataMaskingPolicyName = "dataMaskingPolicyName_example"; // String | The name of the database for which the data masking rule applies.
let dataMaskingRuleName = "dataMaskingRuleName_example"; // String | The name of the data masking rule.
let parameters = new AzureSqlDatabaseDatamaskingPoliciesAndRules.DataMaskingRule(); // DataMaskingRule | The required parameters for creating or updating a data masking rule.
apiInstance.dataMaskingRulesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName, dataMaskingRuleName, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **dataMaskingPolicyName** | **String**| The name of the database for which the data masking rule applies. | 
 **dataMaskingRuleName** | **String**| The name of the data masking rule. | 
 **parameters** | [**DataMaskingRule**](DataMaskingRule.md)| The required parameters for creating or updating a data masking rule. | 

### Return type

[**DataMaskingRule**](DataMaskingRule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataMaskingRulesListByDatabase

> DataMaskingRuleListResult dataMaskingRulesListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName)



Gets a list of database data masking rules.

### Example

```javascript
import AzureSqlDatabaseDatamaskingPoliciesAndRules from 'azure_sql_database_datamasking_policies_and_rules';

let apiInstance = new AzureSqlDatabaseDatamaskingPoliciesAndRules.DataMaskingRulesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let dataMaskingPolicyName = "dataMaskingPolicyName_example"; // String | The name of the database for which the data masking rule applies.
apiInstance.dataMaskingRulesListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **dataMaskingPolicyName** | **String**| The name of the database for which the data masking rule applies. | 

### Return type

[**DataMaskingRuleListResult**](DataMaskingRuleListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

