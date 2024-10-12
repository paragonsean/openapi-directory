# RecoveryServicesBackupClient.RestoresApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**restoresTrigger**](RestoresApi.md#restoresTrigger) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/restore | 



## restoresTrigger

> restoresTrigger(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, parameters)



Restores the specified backed up data. This is an asynchronous operation. To know the status of this API call, use  GetProtectedItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.RestoresApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the backed up items.
let containerName = "containerName_example"; // String | Container name associated with the backed up items.
let protectedItemName = "protectedItemName_example"; // String | Backed up item to be restored.
let recoveryPointId = "recoveryPointId_example"; // String | Recovery point ID which represents the backed up data to be restored.
let parameters = new RecoveryServicesBackupClient.RestoreRequestResource(); // RestoreRequestResource | resource restore request
apiInstance.restoresTrigger(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, parameters, (error, data, response) => {
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
 **protectedItemName** | **String**| Backed up item to be restored. | 
 **recoveryPointId** | **String**| Recovery point ID which represents the backed up data to be restored. | 
 **parameters** | [**RestoreRequestResource**](RestoreRequestResource.md)| resource restore request | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

