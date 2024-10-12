# RecoveryServicesBackupClient.RecoveryPointsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recoveryPointsGet**](RecoveryPointsApi.md#recoveryPointsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId} | 
[**recoveryPointsList**](RecoveryPointsApi.md#recoveryPointsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints | 



## recoveryPointsGet

> RecoveryPointResource recoveryPointsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId)



Provides the information of the backed up data identified using RecoveryPointID. This is an asynchronous operation.  To know the status of the operation, call the GetProtectedItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.RecoveryPointsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with backed up item.
let containerName = "containerName_example"; // String | Container name associated with backed up item.
let protectedItemName = "protectedItemName_example"; // String | Backed up item name whose backup data needs to be fetched.
let recoveryPointId = "recoveryPointId_example"; // String | RecoveryPointID represents the backed up data to be fetched.
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
 **apiVersion** | **String**| Client Api Version. | 
 **vaultName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric name associated with backed up item. | 
 **containerName** | **String**| Container name associated with backed up item. | 
 **protectedItemName** | **String**| Backed up item name whose backup data needs to be fetched. | 
 **recoveryPointId** | **String**| RecoveryPointID represents the backed up data to be fetched. | 

### Return type

[**RecoveryPointResource**](RecoveryPointResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoveryPointsList

> RecoveryPointResourceList recoveryPointsList(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, opts)



Lists the backup copies for the backed up item.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.RecoveryPointsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the backed up item.
let containerName = "containerName_example"; // String | Container name associated with the backed up item.
let protectedItemName = "protectedItemName_example"; // String | Backed up item whose backup copies are to be fetched.
let opts = {
  'filter': "filter_example" // String | OData filter options.
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
 **apiVersion** | **String**| Client Api Version. | 
 **vaultName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric name associated with the backed up item. | 
 **containerName** | **String**| Container name associated with the backed up item. | 
 **protectedItemName** | **String**| Backed up item whose backup copies are to be fetched. | 
 **filter** | **String**| OData filter options. | [optional] 

### Return type

[**RecoveryPointResourceList**](RecoveryPointResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

