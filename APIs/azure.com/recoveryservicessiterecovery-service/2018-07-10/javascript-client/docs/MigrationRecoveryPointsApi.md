# SiteRecoveryManagementClient.MigrationRecoveryPointsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migrationRecoveryPointsGet**](MigrationRecoveryPointsApi.md#migrationRecoveryPointsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName}/migrationRecoveryPoints/{migrationRecoveryPointName} | Gets a recovery point for a migration item.
[**migrationRecoveryPointsListByReplicationMigrationItems**](MigrationRecoveryPointsApi.md#migrationRecoveryPointsListByReplicationMigrationItems) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationMigrationItems/{migrationItemName}/migrationRecoveryPoints | Gets the recovery points for a migration item.



## migrationRecoveryPointsGet

> MigrationRecoveryPoint migrationRecoveryPointsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, migrationRecoveryPointName)

Gets a recovery point for a migration item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.MigrationRecoveryPointsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric unique name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let migrationItemName = "migrationItemName_example"; // String | Migration item name.
let migrationRecoveryPointName = "migrationRecoveryPointName_example"; // String | The migration recovery point name.
apiInstance.migrationRecoveryPointsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, migrationRecoveryPointName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric unique name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **migrationItemName** | **String**| Migration item name. | 
 **migrationRecoveryPointName** | **String**| The migration recovery point name. | 

### Return type

[**MigrationRecoveryPoint**](MigrationRecoveryPoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrationRecoveryPointsListByReplicationMigrationItems

> MigrationRecoveryPointCollection migrationRecoveryPointsListByReplicationMigrationItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName)

Gets the recovery points for a migration item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.MigrationRecoveryPointsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric unique name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let migrationItemName = "migrationItemName_example"; // String | Migration item name.
apiInstance.migrationRecoveryPointsListByReplicationMigrationItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, migrationItemName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric unique name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **migrationItemName** | **String**| Migration item name. | 

### Return type

[**MigrationRecoveryPointCollection**](MigrationRecoveryPointCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

