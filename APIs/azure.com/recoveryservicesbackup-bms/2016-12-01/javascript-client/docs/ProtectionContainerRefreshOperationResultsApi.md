# RecoveryServicesBackupClient.ProtectionContainerRefreshOperationResultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectionContainerRefreshOperationResultsGet**](ProtectionContainerRefreshOperationResultsApi.md#protectionContainerRefreshOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/operationResults/{operationId} | 



## protectionContainerRefreshOperationResultsGet

> protectionContainerRefreshOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, operationId)



Provides the result of the refresh operation triggered by the BeginRefresh operation.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionContainerRefreshOperationResultsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the container.
let operationId = "operationId_example"; // String | Operation ID associated with the operation whose result needs to be fetched.
apiInstance.protectionContainerRefreshOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, operationId, (error, data, response) => {
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
 **fabricName** | **String**| Fabric name associated with the container. | 
 **operationId** | **String**| Operation ID associated with the operation whose result needs to be fetched. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

