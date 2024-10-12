# RecoveryServicesBackupClient.ProtectionContainerOperationResultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectionContainerOperationResultsGet**](ProtectionContainerOperationResultsApi.md#protectionContainerOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/operationResults/{operationId} | 



## protectionContainerOperationResultsGet

> ProtectionContainerResource protectionContainerOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, operationId)



Gets the result of any operation on the container.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionContainerOperationResultsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let fabricName = "fabricName_example"; // String | The fabric name associated with the container.
let containerName = "containerName_example"; // String | The container name used for this GET operation.
let operationId = "operationId_example"; // String | The operation ID used for this GET operation.
apiInstance.protectionContainerOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, operationId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **vaultName** | **String**| The name of the Recovery Services vault. | 
 **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **fabricName** | **String**| The fabric name associated with the container. | 
 **containerName** | **String**| The container name used for this GET operation. | 
 **operationId** | **String**| The operation ID used for this GET operation. | 

### Return type

[**ProtectionContainerResource**](ProtectionContainerResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

