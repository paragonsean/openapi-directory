# KeyVaultManagementClient.VaultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vaultsCreateOrUpdate**](VaultsApi.md#vaultsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} | 
[**vaultsDelete**](VaultsApi.md#vaultsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} | 
[**vaultsGet**](VaultsApi.md#vaultsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} | 
[**vaultsList**](VaultsApi.md#vaultsList) | **GET** /subscriptions/{subscriptionId}/resources | 
[**vaultsListByResourceGroup**](VaultsApi.md#vaultsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults | 



## vaultsCreateOrUpdate

> Vault vaultsCreateOrUpdate(resourceGroupName, vaultName, apiVersion, subscriptionId, parameters)



Create or update a key vault in the specified subscription.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the server belongs.
let vaultName = "vaultName_example"; // String | Name of the vault
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new KeyVaultManagementClient.VaultCreateOrUpdateParameters(); // VaultCreateOrUpdateParameters | Parameters to create or update the vault
apiInstance.vaultsCreateOrUpdate(resourceGroupName, vaultName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Resource Group to which the server belongs. | 
 **vaultName** | **String**| Name of the vault | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VaultCreateOrUpdateParameters**](VaultCreateOrUpdateParameters.md)| Parameters to create or update the vault | 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vaultsDelete

> vaultsDelete(resourceGroupName, vaultName, apiVersion, subscriptionId)



Deletes the specified Azure key vault.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
let vaultName = "vaultName_example"; // String | The name of the vault to delete
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.vaultsDelete(resourceGroupName, vaultName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | 
 **vaultName** | **String**| The name of the vault to delete | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vaultsGet

> Vault vaultsGet(resourceGroupName, vaultName, apiVersion, subscriptionId)



Gets the specified Azure key vault.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
let vaultName = "vaultName_example"; // String | The name of the vault.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.vaultsGet(resourceGroupName, vaultName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | 
 **vaultName** | **String**| The name of the vault. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vaultsList

> ResourceListResult vaultsList(filter, apiVersion, subscriptionId, opts)



The List operation gets information about the vaults associated with the subscription.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let filter = "filter_example"; // String | The filter to apply on the operation.
let apiVersion = "apiVersion_example"; // String | Azure Resource Manager Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56 // Number | Maximum number of results to return.
};
apiInstance.vaultsList(filter, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. | 
 **apiVersion** | **String**| Azure Resource Manager Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **top** | **Number**| Maximum number of results to return. | [optional] 

### Return type

[**ResourceListResult**](ResourceListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vaultsListByResourceGroup

> VaultListResult vaultsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



The List operation gets information about the vaults associated with the subscription and within the specified resource group.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56 // Number | Maximum number of results to return.
};
apiInstance.vaultsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Resource Group to which the vault belongs. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **top** | **Number**| Maximum number of results to return. | [optional] 

### Return type

[**VaultListResult**](VaultListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

