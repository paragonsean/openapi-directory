# RecoveryServicesBackupClient.RecoveryPointsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recoveryPointsGet**](RecoveryPointsApi.md#recoveryPointsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId} | 
[**recoveryPointsList**](RecoveryPointsApi.md#recoveryPointsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints | 



## recoveryPointsGet

> RecoveryPointResource recoveryPointsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId)



Provides the backup data for the RecoveryPointID. This is an asynchronous operation. To learn the status of the operation, call the GetProtectedItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.RecoveryPointsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let fabricName = "fabricName_example"; // String | The fabric name associated with backup item.
let containerName = "containerName_example"; // String | The container name associated with backup item.
let protectedItemName = "protectedItemName_example"; // String | The name of the backup item used in this GET operation.
let recoveryPointId = "recoveryPointId_example"; // String | The RecoveryPointID associated with this GET operation.
apiInstance.recoveryPointsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, (error, data, response) => {
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
 **fabricName** | **String**| The fabric name associated with backup item. | 
 **containerName** | **String**| The container name associated with backup item. | 
 **protectedItemName** | **String**| The name of the backup item used in this GET operation. | 
 **recoveryPointId** | **String**| The RecoveryPointID associated with this GET operation. | 

### Return type

[**RecoveryPointResource**](RecoveryPointResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoveryPointsList

> RecoveryPointResourceList recoveryPointsList(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, opts)



Lists the recovery points, or backup copies, for the specified backup item.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.RecoveryPointsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let fabricName = "fabricName_example"; // String | The fabric name associated with the backup item.
let containerName = "containerName_example"; // String | The container name associated with the backup item.
let protectedItemName = "protectedItemName_example"; // String | The name of backup item used in this GET operation.
let opts = {
  'filter': "filter_example" // String | startDate eq {yyyy-mm-dd hh:mm:ss PM} and endDate { yyyy-mm-dd hh:mm:ss PM}.
};
apiInstance.recoveryPointsList(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, opts, (error, data, response) => {
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
 **fabricName** | **String**| The fabric name associated with the backup item. | 
 **containerName** | **String**| The container name associated with the backup item. | 
 **protectedItemName** | **String**| The name of backup item used in this GET operation. | 
 **filter** | **String**| startDate eq {yyyy-mm-dd hh:mm:ss PM} and endDate { yyyy-mm-dd hh:mm:ss PM}. | [optional] 

### Return type

[**RecoveryPointResourceList**](RecoveryPointResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

