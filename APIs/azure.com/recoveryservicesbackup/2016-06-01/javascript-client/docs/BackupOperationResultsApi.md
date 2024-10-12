# RecoveryServicesBackupClient.BackupOperationResultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupOperationResultsGet**](BackupOperationResultsApi.md#backupOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupOperationResults/{operationId} | 



## backupOperationResultsGet

> backupOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, operationId)



Provides the status of the delete operations, for example, deleting a backup item. Once the operation starts, the response status code is Accepted. The response status code remains in this state until the operation reaches completion. On successful completion, the status code changes to OK. This method expects OperationID as an argument. OperationID is part of the Location header of the operation response.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.BackupOperationResultsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let operationId = "operationId_example"; // String | The ID of the operation.
apiInstance.backupOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, operationId, (error, data, response) => {
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
 **operationId** | **String**| The ID of the operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

