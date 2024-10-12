# RecoveryServicesBackupClient.BackupOperationStatusesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupOperationStatusesGet**](BackupOperationStatusesApi.md#backupOperationStatusesGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupOperations/{operationId} | 



## backupOperationStatusesGet

> OperationStatus backupOperationStatusesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, operationId)



Fetches the status of an operation such as triggering a backup, restore. The status can be in progress, completed  or failed. You can refer to the OperationStatus enum for all the possible states of an operation. Some operations  create jobs. This method returns the list of jobs when the operation is complete.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.BackupOperationStatusesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let operationId = "operationId_example"; // String | OperationID which represents the operation.
apiInstance.backupOperationStatusesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, operationId, (error, data, response) => {
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
 **vaultName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **operationId** | **String**| OperationID which represents the operation. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

