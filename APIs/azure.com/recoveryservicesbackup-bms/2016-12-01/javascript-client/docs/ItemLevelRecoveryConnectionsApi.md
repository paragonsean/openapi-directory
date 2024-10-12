# RecoveryServicesBackupClient.ItemLevelRecoveryConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**itemLevelRecoveryConnectionsProvision**](ItemLevelRecoveryConnectionsApi.md#itemLevelRecoveryConnectionsProvision) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/provisionInstantItemRecovery | 
[**itemLevelRecoveryConnectionsRevoke**](ItemLevelRecoveryConnectionsApi.md#itemLevelRecoveryConnectionsRevoke) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/revokeInstantItemRecovery | 



## itemLevelRecoveryConnectionsProvision

> itemLevelRecoveryConnectionsProvision(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, parameters)



Provisions a script which invokes an iSCSI connection to the backup data. Executing this script opens a file  explorer displaying all the recoverable files and folders. This is an asynchronous operation. To know the status of  provisioning, call GetProtectedItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ItemLevelRecoveryConnectionsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the backed up items.
let containerName = "containerName_example"; // String | Container name associated with the backed up items.
let protectedItemName = "protectedItemName_example"; // String | Backed up item name whose files/folders are to be restored.
let recoveryPointId = "recoveryPointId_example"; // String | Recovery point ID which represents backed up data. iSCSI connection will be provisioned  for this backed up data.
let parameters = new RecoveryServicesBackupClient.ILRRequestResource(); // ILRRequestResource | resource ILR request
apiInstance.itemLevelRecoveryConnectionsProvision(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **vaultName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric name associated with the backed up items. | 
 **containerName** | **String**| Container name associated with the backed up items. | 
 **protectedItemName** | **String**| Backed up item name whose files/folders are to be restored. | 
 **recoveryPointId** | **String**| Recovery point ID which represents backed up data. iSCSI connection will be provisioned  for this backed up data. | 
 **parameters** | [**ILRRequestResource**](ILRRequestResource.md)| resource ILR request | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## itemLevelRecoveryConnectionsRevoke

> itemLevelRecoveryConnectionsRevoke(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId)



Revokes an iSCSI connection which can be used to download a script. Executing this script opens a file explorer  displaying all recoverable files and folders. This is an asynchronous operation.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ItemLevelRecoveryConnectionsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the backed up items.
let containerName = "containerName_example"; // String | Container name associated with the backed up items.
let protectedItemName = "protectedItemName_example"; // String | Backed up item name whose files/folders are to be restored.
let recoveryPointId = "recoveryPointId_example"; // String | Recovery point ID which represents backed up data. iSCSI connection will be revoked for  this backed up data.
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
 **apiVersion** | **String**| Client Api Version. | 
 **vaultName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric name associated with the backed up items. | 
 **containerName** | **String**| Container name associated with the backed up items. | 
 **protectedItemName** | **String**| Backed up item name whose files/folders are to be restored. | 
 **recoveryPointId** | **String**| Recovery point ID which represents backed up data. iSCSI connection will be revoked for  this backed up data. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

