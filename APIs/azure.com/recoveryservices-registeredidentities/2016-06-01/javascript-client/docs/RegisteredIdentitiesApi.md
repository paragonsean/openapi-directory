# RecoveryServicesClient.RegisteredIdentitiesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registeredIdentitiesDelete**](RegisteredIdentitiesApi.md#registeredIdentitiesDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/registeredIdentities/{identityName} | 



## registeredIdentitiesDelete

> registeredIdentitiesDelete(subscriptionId, apiVersion, resourceGroupName, vaultName, identityName)



Unregisters the given container from your Recovery Services vault.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.RegisteredIdentitiesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let identityName = "identityName_example"; // String | Name of the protection container to unregister.
apiInstance.registeredIdentitiesDelete(subscriptionId, apiVersion, resourceGroupName, vaultName, identityName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **vaultName** | **String**| The name of the recovery services vault. | 
 **identityName** | **String**| Name of the protection container to unregister. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

