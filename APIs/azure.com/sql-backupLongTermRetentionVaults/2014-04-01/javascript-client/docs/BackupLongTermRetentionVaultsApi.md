# AzureSqlServerBackupLongTermRetentionVault.BackupLongTermRetentionVaultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupLongTermRetentionVaultsCreateOrUpdate**](BackupLongTermRetentionVaultsApi.md#backupLongTermRetentionVaultsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/backupLongTermRetentionVaults/{backupLongTermRetentionVaultName} | 
[**backupLongTermRetentionVaultsGet**](BackupLongTermRetentionVaultsApi.md#backupLongTermRetentionVaultsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/backupLongTermRetentionVaults/{backupLongTermRetentionVaultName} | 
[**backupLongTermRetentionVaultsListByServer**](BackupLongTermRetentionVaultsApi.md#backupLongTermRetentionVaultsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/backupLongTermRetentionVaults | 



## backupLongTermRetentionVaultsCreateOrUpdate

> BackupLongTermRetentionVault backupLongTermRetentionVaultsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, parameters)



Updates a server backup long term retention vault

### Example

```javascript
import AzureSqlServerBackupLongTermRetentionVault from 'azure_sql_server_backup_long_term_retention_vault';

let apiInstance = new AzureSqlServerBackupLongTermRetentionVault.BackupLongTermRetentionVaultsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let backupLongTermRetentionVaultName = "backupLongTermRetentionVaultName_example"; // String | The name of the backup long term retention vault
let parameters = new AzureSqlServerBackupLongTermRetentionVault.BackupLongTermRetentionVault(); // BackupLongTermRetentionVault | The required parameters to update a backup long term retention vault
apiInstance.backupLongTermRetentionVaultsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, parameters, (error, data, response) => {
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
 **backupLongTermRetentionVaultName** | **String**| The name of the backup long term retention vault | 
 **parameters** | [**BackupLongTermRetentionVault**](BackupLongTermRetentionVault.md)| The required parameters to update a backup long term retention vault | 

### Return type

[**BackupLongTermRetentionVault**](BackupLongTermRetentionVault.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## backupLongTermRetentionVaultsGet

> BackupLongTermRetentionVault backupLongTermRetentionVaultsGet(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName)



Gets a server backup long term retention vault

### Example

```javascript
import AzureSqlServerBackupLongTermRetentionVault from 'azure_sql_server_backup_long_term_retention_vault';

let apiInstance = new AzureSqlServerBackupLongTermRetentionVault.BackupLongTermRetentionVaultsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let backupLongTermRetentionVaultName = "backupLongTermRetentionVaultName_example"; // String | The name of the Azure SQL Server backup LongTermRetention vault
apiInstance.backupLongTermRetentionVaultsGet(apiVersion, subscriptionId, resourceGroupName, serverName, backupLongTermRetentionVaultName, (error, data, response) => {
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
 **backupLongTermRetentionVaultName** | **String**| The name of the Azure SQL Server backup LongTermRetention vault | 

### Return type

[**BackupLongTermRetentionVault**](BackupLongTermRetentionVault.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## backupLongTermRetentionVaultsListByServer

> BackupLongTermRetentionVaultListResult backupLongTermRetentionVaultsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



Gets server backup long term retention vaults in a server

### Example

```javascript
import AzureSqlServerBackupLongTermRetentionVault from 'azure_sql_server_backup_long_term_retention_vault';

let apiInstance = new AzureSqlServerBackupLongTermRetentionVault.BackupLongTermRetentionVaultsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
apiInstance.backupLongTermRetentionVaultsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, (error, data, response) => {
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

[**BackupLongTermRetentionVaultListResult**](BackupLongTermRetentionVaultListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

