# RecoveryServicesBackupClient.ProtectableItemsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectableItemsList**](ProtectableItemsApi.md#protectableItemsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupProtectableItems | 



## protectableItemsList

> WorkloadProtectableItemResourceList protectableItemsList(apiVersion, vaultName, resourceGroupName, subscriptionId, opts)



Based on the query filter and the pagination parameters, this operation provides a pageable list of objects within the subscription that can be protected.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectableItemsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let opts = {
  'filter': "filter_example", // String | Using the following query filters, you can sort a specific backup item based on: type of backup item, status, name of the item, and more.  providerType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql } and status eq { NotProtected , Protecting , Protected } and friendlyName {name} and skipToken eq {string which provides the next set of list} and topToken eq {int} and backupManagementType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql }.
  'skipToken': "skipToken_example" // String | The Skip Token filter.
};
apiInstance.protectableItemsList(apiVersion, vaultName, resourceGroupName, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| Using the following query filters, you can sort a specific backup item based on: type of backup item, status, name of the item, and more.  providerType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql } and status eq { NotProtected , Protecting , Protected } and friendlyName {name} and skipToken eq {string which provides the next set of list} and topToken eq {int} and backupManagementType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql }. | [optional] 
 **skipToken** | **String**| The Skip Token filter. | [optional] 

### Return type

[**WorkloadProtectableItemResourceList**](WorkloadProtectableItemResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

