# RecoveryServicesBackupClient.RecoveryPointsCrrApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recoveryPointsCrrList**](RecoveryPointsCrrApi.md#recoveryPointsCrrList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/ | 



## recoveryPointsCrrList

> RecoveryPointResourceList recoveryPointsCrrList(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, opts)



Lists the backup copies for the backed up item.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.RecoveryPointsCrrApi();
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
apiInstance.recoveryPointsCrrList(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, opts, (error, data, response) => {
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

