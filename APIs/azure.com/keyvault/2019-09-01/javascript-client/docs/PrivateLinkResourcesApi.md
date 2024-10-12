# KeyVaultManagementClient.PrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateLinkResourcesListByVault**](PrivateLinkResourcesApi.md#privateLinkResourcesListByVault) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateLinkResources | 



## privateLinkResourcesListByVault

> PrivateLinkResourceListResult privateLinkResourcesListByVault(subscriptionId, resourceGroupName, vaultName, apiVersion)



Gets the private link resources supported for the key vault.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.PrivateLinkResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group that contains the key vault.
let vaultName = "vaultName_example"; // String | The name of the key vault.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.privateLinkResourcesListByVault(subscriptionId, resourceGroupName, vaultName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group that contains the key vault. | 
 **vaultName** | **String**| The name of the key vault. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**PrivateLinkResourceListResult**](PrivateLinkResourceListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

