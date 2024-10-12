# SqlManagementClient.BackupLongTermRetentionPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupLongTermRetentionPoliciesCreateOrUpdate**](BackupLongTermRetentionPoliciesApi.md#backupLongTermRetentionPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupLongTermRetentionPolicies/{policyName} | 
[**backupLongTermRetentionPoliciesGet**](BackupLongTermRetentionPoliciesApi.md#backupLongTermRetentionPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupLongTermRetentionPolicies/{policyName} | 
[**backupLongTermRetentionPoliciesListByDatabase**](BackupLongTermRetentionPoliciesApi.md#backupLongTermRetentionPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupLongTermRetentionPolicies | 



## backupLongTermRetentionPoliciesCreateOrUpdate

> BackupLongTermRetentionPolicy backupLongTermRetentionPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, parameters)



Sets a database&#39;s long term retention policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BackupLongTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let policyName = "policyName_example"; // String | The policy name. Should always be Default.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.BackupLongTermRetentionPolicy(); // BackupLongTermRetentionPolicy | The long term retention policy info.
apiInstance.backupLongTermRetentionPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **policyName** | **String**| The policy name. Should always be Default. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**BackupLongTermRetentionPolicy**](BackupLongTermRetentionPolicy.md)| The long term retention policy info. | 

### Return type

[**BackupLongTermRetentionPolicy**](BackupLongTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## backupLongTermRetentionPoliciesGet

> BackupLongTermRetentionPolicy backupLongTermRetentionPoliciesGet(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion)



Gets a database&#39;s long term retention policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BackupLongTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let policyName = "policyName_example"; // String | The policy name. Should always be Default.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.backupLongTermRetentionPoliciesGet(resourceGroupName, serverName, databaseName, policyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **policyName** | **String**| The policy name. Should always be Default. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**BackupLongTermRetentionPolicy**](BackupLongTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## backupLongTermRetentionPoliciesListByDatabase

> BackupLongTermRetentionPolicy backupLongTermRetentionPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion)



Gets a database&#39;s long term retention policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BackupLongTermRetentionPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.backupLongTermRetentionPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**BackupLongTermRetentionPolicy**](BackupLongTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

