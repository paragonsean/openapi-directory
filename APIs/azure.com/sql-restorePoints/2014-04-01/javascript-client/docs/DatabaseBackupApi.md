# AzureSqlDatabaseBackup.DatabaseBackupApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**restorePointsListByDatabase**](DatabaseBackupApi.md#restorePointsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/restorePoints | 



## restorePointsListByDatabase

> RestorePointListResult restorePointsListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName)



Gets a list of database restore points.

### Example

```javascript
import AzureSqlDatabaseBackup from 'azure_sql_database_backup';

let apiInstance = new AzureSqlDatabaseBackup.DatabaseBackupApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database to get available restore points.
apiInstance.restorePointsListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database to get available restore points. | 

### Return type

[**RestorePointListResult**](RestorePointListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

