# AzureSqlDatabaseDatamaskingPoliciesAndRules.DataMaskingPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataMaskingPoliciesCreateOrUpdate**](DataMaskingPoliciesApi.md#dataMaskingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName} | 
[**dataMaskingPoliciesGet**](DataMaskingPoliciesApi.md#dataMaskingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName} | 



## dataMaskingPoliciesCreateOrUpdate

> DataMaskingPolicy dataMaskingPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName, parameters)



Creates or updates a database data masking policy

### Example

```javascript
import AzureSqlDatabaseDatamaskingPoliciesAndRules from 'azure_sql_database_datamasking_policies_and_rules';

let apiInstance = new AzureSqlDatabaseDatamaskingPoliciesAndRules.DataMaskingPoliciesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let dataMaskingPolicyName = "dataMaskingPolicyName_example"; // String | The name of the database for which the data masking rule applies.
let parameters = new AzureSqlDatabaseDatamaskingPoliciesAndRules.DataMaskingPolicy(); // DataMaskingPolicy | Parameters for creating or updating a data masking policy.
apiInstance.dataMaskingPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName, parameters, (error, data, response) => {
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
 **parameters** | [**DataMaskingPolicy**](DataMaskingPolicy.md)| Parameters for creating or updating a data masking policy. | 

### Return type

[**DataMaskingPolicy**](DataMaskingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataMaskingPoliciesGet

> DataMaskingPolicy dataMaskingPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName)



Gets a database data masking policy.

### Example

```javascript
import AzureSqlDatabaseDatamaskingPoliciesAndRules from 'azure_sql_database_datamasking_policies_and_rules';

let apiInstance = new AzureSqlDatabaseDatamaskingPoliciesAndRules.DataMaskingPoliciesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let dataMaskingPolicyName = "dataMaskingPolicyName_example"; // String | The name of the database for which the data masking rule applies.
apiInstance.dataMaskingPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, dataMaskingPolicyName, (error, data, response) => {
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

[**DataMaskingPolicy**](DataMaskingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

