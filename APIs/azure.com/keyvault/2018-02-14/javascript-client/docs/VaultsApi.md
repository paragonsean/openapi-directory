# KeyVaultManagementClient.VaultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vaultsCheckNameAvailability**](VaultsApi.md#vaultsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault/checkNameAvailability | 
[**vaultsCreateOrUpdate**](VaultsApi.md#vaultsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} | 
[**vaultsDelete**](VaultsApi.md#vaultsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} | 
[**vaultsGet**](VaultsApi.md#vaultsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} | 
[**vaultsGetDeleted**](VaultsApi.md#vaultsGetDeleted) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault/locations/{location}/deletedVaults/{vaultName} | 
[**vaultsList**](VaultsApi.md#vaultsList) | **GET** /subscriptions/{subscriptionId}/resources | 
[**vaultsListByResourceGroup**](VaultsApi.md#vaultsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults | 
[**vaultsListBySubscription**](VaultsApi.md#vaultsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault/vaults | 
[**vaultsListDeleted**](VaultsApi.md#vaultsListDeleted) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault/deletedVaults | 
[**vaultsPurgeDeleted**](VaultsApi.md#vaultsPurgeDeleted) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.KeyVault/locations/{location}/deletedVaults/{vaultName}/purge | 
[**vaultsUpdate**](VaultsApi.md#vaultsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName} | 
[**vaultsUpdateAccessPolicy**](VaultsApi.md#vaultsUpdateAccessPolicy) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/accessPolicies/{operationKind} | 



## vaultsCheckNameAvailability

> CheckNameAvailabilityResult vaultsCheckNameAvailability(apiVersion, subscriptionId, vaultName)



Checks that the vault name is valid and is not already in use.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let vaultName = new KeyVaultManagementClient.VaultCheckNameAvailabilityParameters(); // VaultCheckNameAvailabilityParameters | The name of the vault.
apiInstance.vaultsCheckNameAvailability(apiVersion, subscriptionId, vaultName, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **vaultName** | [**VaultCheckNameAvailabilityParameters**](VaultCheckNameAvailabilityParameters.md)| The name of the vault. | 

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


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
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
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
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

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
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vaultsGetDeleted

> DeletedVault vaultsGetDeleted(vaultName, location, apiVersion, subscriptionId)



Gets the deleted Azure key vault.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let vaultName = "vaultName_example"; // String | The name of the vault.
let location = "location_example"; // String | The location of the deleted vault.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.vaultsGetDeleted(vaultName, location, apiVersion, subscriptionId, (error, data, response) => {
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
 **vaultName** | **String**| The name of the vault. | 
 **location** | **String**| The location of the deleted vault. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DeletedVault**](DeletedVault.md)

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
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
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
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **top** | **Number**| Maximum number of results to return. | [optional] 

### Return type

[**VaultListResult**](VaultListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vaultsListBySubscription

> VaultListResult vaultsListBySubscription(apiVersion, subscriptionId, opts)



The List operation gets information about the vaults associated with the subscription.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56 // Number | Maximum number of results to return.
};
apiInstance.vaultsListBySubscription(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **top** | **Number**| Maximum number of results to return. | [optional] 

### Return type

[**VaultListResult**](VaultListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vaultsListDeleted

> DeletedVaultListResult vaultsListDeleted(apiVersion, subscriptionId)



Gets information about the deleted vaults in a subscription.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.vaultsListDeleted(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DeletedVaultListResult**](DeletedVaultListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vaultsPurgeDeleted

> vaultsPurgeDeleted(vaultName, location, apiVersion, subscriptionId)



Permanently deletes the specified vault. aka Purges the deleted Azure key vault.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let vaultName = "vaultName_example"; // String | The name of the soft-deleted vault.
let location = "location_example"; // String | The location of the soft-deleted vault.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.vaultsPurgeDeleted(vaultName, location, apiVersion, subscriptionId, (error, data, response) => {
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
 **vaultName** | **String**| The name of the soft-deleted vault. | 
 **location** | **String**| The location of the soft-deleted vault. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vaultsUpdate

> Vault vaultsUpdate(resourceGroupName, vaultName, apiVersion, subscriptionId, parameters)



Update a key vault in the specified subscription.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the server belongs.
let vaultName = "vaultName_example"; // String | Name of the vault
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new KeyVaultManagementClient.VaultPatchParameters(); // VaultPatchParameters | Parameters to patch the vault
apiInstance.vaultsUpdate(resourceGroupName, vaultName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VaultPatchParameters**](VaultPatchParameters.md)| Parameters to patch the vault | 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vaultsUpdateAccessPolicy

> VaultAccessPolicyParameters vaultsUpdateAccessPolicy(resourceGroupName, vaultName, operationKind, apiVersion, subscriptionId, parameters)



Update access policies in a key vault in the specified subscription.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.VaultsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
let vaultName = "vaultName_example"; // String | Name of the vault
let operationKind = "operationKind_example"; // String | Name of the operation
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new KeyVaultManagementClient.VaultAccessPolicyParameters(); // VaultAccessPolicyParameters | Access policy to merge into the vault
apiInstance.vaultsUpdateAccessPolicy(resourceGroupName, vaultName, operationKind, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **vaultName** | **String**| Name of the vault | 
 **operationKind** | **String**| Name of the operation | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VaultAccessPolicyParameters**](VaultAccessPolicyParameters.md)| Access policy to merge into the vault | 

### Return type

[**VaultAccessPolicyParameters**](VaultAccessPolicyParameters.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

