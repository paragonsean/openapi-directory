# RecoveryServicesClient.VaultUsagesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usagesListByVaults**](VaultUsagesApi.md#usagesListByVaults) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/usages | 



## usagesListByVaults

> VaultUsageList usagesListByVaults(subscriptionId, apiVersion, resourceGroupName, vaultName)



Fetches the usages of the vault.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultUsagesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
apiInstance.usagesListByVaults(subscriptionId, apiVersion, resourceGroupName, vaultName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **vaultName** | **String**| The name of the recovery services vault. | 

### Return type

[**VaultUsageList**](VaultUsageList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

