# RecoveryServicesBackupClient.ItemLevelRecoveryConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**itemLevelRecoveryConnectionsProvision**](ItemLevelRecoveryConnectionsApi.md#itemLevelRecoveryConnectionsProvision) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/provisionInstantItemRecovery | 
[**itemLevelRecoveryConnectionsRevoke**](ItemLevelRecoveryConnectionsApi.md#itemLevelRecoveryConnectionsRevoke) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/revokeInstantItemRecovery | 



## itemLevelRecoveryConnectionsProvision

> itemLevelRecoveryConnectionsProvision(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, resourceILRRequest)



Provisions a script which invokes an iSCSI connection to the backup data. Executing this script opens File Explorer which displays the recoverable files and folders. This is an asynchronous operation. To get the provisioning status, call GetProtectedItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ItemLevelRecoveryConnectionsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let fabricName = "fabricName_example"; // String | The fabric name associated with the backup items.
let containerName = "containerName_example"; // String | The container name associated with the backup items.
let protectedItemName = "protectedItemName_example"; // String | The name of the backup item whose files or folders are to be restored.
let recoveryPointId = "recoveryPointId_example"; // String | The recovery point ID for backup data. The iSCSI connection will be provisioned for this backup data.
let resourceILRRequest = new RecoveryServicesBackupClient.ILRRequestResource(); // ILRRequestResource | The resource Item Level Recovery (ILR) request.
apiInstance.itemLevelRecoveryConnectionsProvision(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, resourceILRRequest, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **vaultName** | **String**| The name of the Recovery Services vault. | 
 **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **fabricName** | **String**| The fabric name associated with the backup items. | 
 **containerName** | **String**| The container name associated with the backup items. | 
 **protectedItemName** | **String**| The name of the backup item whose files or folders are to be restored. | 
 **recoveryPointId** | **String**| The recovery point ID for backup data. The iSCSI connection will be provisioned for this backup data. | 
 **resourceILRRequest** | [**ILRRequestResource**](ILRRequestResource.md)| The resource Item Level Recovery (ILR) request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## itemLevelRecoveryConnectionsRevoke

> itemLevelRecoveryConnectionsRevoke(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId)



Revokes an iSCSI connection which can be used to download a script. Executing this script opens a file explorer displaying all recoverable files and folders. This is an asynchronous operation.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ItemLevelRecoveryConnectionsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let fabricName = "fabricName_example"; // String | The fabric name associated with the backup items. The value allowed is Azure.
let containerName = "containerName_example"; // String | The container name associated with the backup items.
let protectedItemName = "protectedItemName_example"; // String | The name of the backup items whose files or folders will be restored.
let recoveryPointId = "recoveryPointId_example"; // String | The string that identifies the recovery point. The iSCSI connection will be revoked for this protected data.
apiInstance.itemLevelRecoveryConnectionsRevoke(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **vaultName** | **String**| The name of the Recovery Services vault. | 
 **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **fabricName** | **String**| The fabric name associated with the backup items. The value allowed is Azure. | 
 **containerName** | **String**| The container name associated with the backup items. | 
 **protectedItemName** | **String**| The name of the backup items whose files or folders will be restored. | 
 **recoveryPointId** | **String**| The string that identifies the recovery point. The iSCSI connection will be revoked for this protected data. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

