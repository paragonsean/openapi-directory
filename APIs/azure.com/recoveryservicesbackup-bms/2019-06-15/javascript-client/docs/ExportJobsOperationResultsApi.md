# RecoveryServicesBackupClient.ExportJobsOperationResultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exportJobsOperationResultsGet**](ExportJobsOperationResultsApi.md#exportJobsOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupJobs/operationResults/{operationId} | 



## exportJobsOperationResultsGet

> OperationResultInfoBaseResource exportJobsOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, operationId)



Gets the operation result of operation triggered by Export Jobs API. If the operation is successful, then it also  contains URL of a Blob and a SAS key to access the same. The blob contains exported jobs in JSON serialized format.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ExportJobsOperationResultsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let operationId = "operationId_example"; // String | OperationID which represents the export job.
apiInstance.exportJobsOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, operationId, (error, data, response) => {
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
 **operationId** | **String**| OperationID which represents the export job. | 

### Return type

[**OperationResultInfoBaseResource**](OperationResultInfoBaseResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

