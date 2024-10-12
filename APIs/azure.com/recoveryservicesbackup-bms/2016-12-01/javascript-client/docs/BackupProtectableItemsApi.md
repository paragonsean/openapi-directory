# RecoveryServicesBackupClient.BackupProtectableItemsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupProtectableItemsList**](BackupProtectableItemsApi.md#backupProtectableItemsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupProtectableItems | 



## backupProtectableItemsList

> WorkloadProtectableItemResourceList backupProtectableItemsList(apiVersion, vaultName, resourceGroupName, subscriptionId, opts)



Provides a pageable list of protectable objects within your subscription according to the query filter and the  pagination parameters.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.BackupProtectableItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let opts = {
  'filter': "filter_example", // String | OData filter options.
  'skipToken': "skipToken_example" // String | skipToken Filter.
};
apiInstance.backupProtectableItemsList(apiVersion, vaultName, resourceGroupName, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| OData filter options. | [optional] 
 **skipToken** | **String**| skipToken Filter. | [optional] 

### Return type

[**WorkloadProtectableItemResourceList**](WorkloadProtectableItemResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

