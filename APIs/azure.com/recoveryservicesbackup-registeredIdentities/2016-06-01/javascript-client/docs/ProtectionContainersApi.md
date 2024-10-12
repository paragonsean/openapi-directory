# RecoveryServicesBackupClient.ProtectionContainersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectionContainersUnregister**](ProtectionContainersApi.md#protectionContainersUnregister) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/registeredIdentities/{identityName} | 



## protectionContainersUnregister

> protectionContainersUnregister(subscriptionId, resourceGroupName, vaultName, apiVersion, identityName)



Unregisters the given container from your Recovery Services vault.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionContainersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let apiVersion = "apiVersion_example"; // String | Client API version.
let identityName = "identityName_example"; // String | Name of the protection container to unregister.
apiInstance.protectionContainersUnregister(subscriptionId, resourceGroupName, vaultName, apiVersion, identityName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | 
 **vaultName** | **String**| The name of the Recovery Services vault. | 
 **apiVersion** | **String**| Client API version. | 
 **identityName** | **String**| Name of the protection container to unregister. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

