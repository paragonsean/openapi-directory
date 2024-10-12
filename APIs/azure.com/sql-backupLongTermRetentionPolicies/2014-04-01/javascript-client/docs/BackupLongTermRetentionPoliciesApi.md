# AzureSqlDatabaseBackupLongTermRetentionPolicy.BackupLongTermRetentionPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupLongTermRetentionPoliciesCreateOrUpdate**](BackupLongTermRetentionPoliciesApi.md#backupLongTermRetentionPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupLongTermRetentionPolicies/{backupLongTermRetentionPolicyName} | 
[**backupLongTermRetentionPoliciesGet**](BackupLongTermRetentionPoliciesApi.md#backupLongTermRetentionPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupLongTermRetentionPolicies/{backupLongTermRetentionPolicyName} | 
[**backupLongTermRetentionPoliciesListByDatabase**](BackupLongTermRetentionPoliciesApi.md#backupLongTermRetentionPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/backupLongTermRetentionPolicies | 



## backupLongTermRetentionPoliciesCreateOrUpdate

> BackupLongTermRetentionPolicy backupLongTermRetentionPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, backupLongTermRetentionPolicyName, parameters)



Creates or updates a database backup long term retention policy

### Example

```javascript
import AzureSqlDatabaseBackupLongTermRetentionPolicy from 'azure_sql_database_backup_long_term_retention_policy';

let apiInstance = new AzureSqlDatabaseBackupLongTermRetentionPolicy.BackupLongTermRetentionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database
let backupLongTermRetentionPolicyName = "backupLongTermRetentionPolicyName_example"; // String | The name of the backup long term retention policy
let parameters = new AzureSqlDatabaseBackupLongTermRetentionPolicy.BackupLongTermRetentionPolicy(); // BackupLongTermRetentionPolicy | The required parameters to update a backup long term retention policy
apiInstance.backupLongTermRetentionPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, backupLongTermRetentionPolicyName, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database | 
 **backupLongTermRetentionPolicyName** | **String**| The name of the backup long term retention policy | 
 **parameters** | [**BackupLongTermRetentionPolicy**](BackupLongTermRetentionPolicy.md)| The required parameters to update a backup long term retention policy | 

### Return type

[**BackupLongTermRetentionPolicy**](BackupLongTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## backupLongTermRetentionPoliciesGet

> BackupLongTermRetentionPolicy backupLongTermRetentionPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, backupLongTermRetentionPolicyName)



Returns a database backup long term retention policy

### Example

```javascript
import AzureSqlDatabaseBackupLongTermRetentionPolicy from 'azure_sql_database_backup_long_term_retention_policy';

let apiInstance = new AzureSqlDatabaseBackupLongTermRetentionPolicy.BackupLongTermRetentionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let backupLongTermRetentionPolicyName = "backupLongTermRetentionPolicyName_example"; // String | The name of the backup long term retention policy
apiInstance.backupLongTermRetentionPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, backupLongTermRetentionPolicyName, (error, data, response) => {
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
 **backupLongTermRetentionPolicyName** | **String**| The name of the backup long term retention policy | 

### Return type

[**BackupLongTermRetentionPolicy**](BackupLongTermRetentionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## backupLongTermRetentionPoliciesListByDatabase

> BackupLongTermRetentionPolicyListResult backupLongTermRetentionPoliciesListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName)



Returns a database backup long term retention policy

### Example

```javascript
import AzureSqlDatabaseBackupLongTermRetentionPolicy from 'azure_sql_database_backup_long_term_retention_policy';

let apiInstance = new AzureSqlDatabaseBackupLongTermRetentionPolicy.BackupLongTermRetentionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
apiInstance.backupLongTermRetentionPoliciesListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, (error, data, response) => {
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

### Return type

[**BackupLongTermRetentionPolicyListResult**](BackupLongTermRetentionPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

