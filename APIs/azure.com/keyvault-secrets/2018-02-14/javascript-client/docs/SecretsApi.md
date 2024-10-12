# KeyVaultManagementClient.SecretsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secretsCreateOrUpdate**](SecretsApi.md#secretsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName} | 
[**secretsGet**](SecretsApi.md#secretsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName} | 
[**secretsList**](SecretsApi.md#secretsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets | 
[**secretsUpdate**](SecretsApi.md#secretsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/secrets/{secretName} | 



## secretsCreateOrUpdate

> Secret secretsCreateOrUpdate(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId, parameters)



Create or update a secret in a key vault in the specified subscription.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.SecretsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
let vaultName = "vaultName_example"; // String | Name of the vault
let secretName = "secretName_example"; // String | Name of the secret
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new KeyVaultManagementClient.SecretCreateOrUpdateParameters(); // SecretCreateOrUpdateParameters | Parameters to create or update the secret
apiInstance.secretsCreateOrUpdate(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **secretName** | **String**| Name of the secret | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**SecretCreateOrUpdateParameters**](SecretCreateOrUpdateParameters.md)| Parameters to create or update the secret | 

### Return type

[**Secret**](Secret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## secretsGet

> Secret secretsGet(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId)



Gets the specified secret.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.SecretsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
let vaultName = "vaultName_example"; // String | The name of the vault.
let secretName = "secretName_example"; // String | The name of the secret.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.secretsGet(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId, (error, data, response) => {
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
 **secretName** | **String**| The name of the secret. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Secret**](Secret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretsList

> SecretListResult secretsList(resourceGroupName, vaultName, apiVersion, subscriptionId, opts)



The List operation gets information about the secrets in a vault.  NOTE: This API is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.SecretsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
let vaultName = "vaultName_example"; // String | The name of the vault.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56 // Number | Maximum number of results to return.
};
apiInstance.secretsList(resourceGroupName, vaultName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **top** | **Number**| Maximum number of results to return. | [optional] 

### Return type

[**SecretListResult**](SecretListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretsUpdate

> Secret secretsUpdate(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId, parameters)



Update a secret in the specified subscription.  NOTE: This API is intended for internal use in ARM deployments.  Users should use the data-plane REST service for interaction with vault secrets.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';

let apiInstance = new KeyVaultManagementClient.SecretsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the vault belongs.
let vaultName = "vaultName_example"; // String | Name of the vault
let secretName = "secretName_example"; // String | Name of the secret
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new KeyVaultManagementClient.SecretPatchParameters(); // SecretPatchParameters | Parameters to patch the secret
apiInstance.secretsUpdate(resourceGroupName, vaultName, secretName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **secretName** | **String**| Name of the secret | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**SecretPatchParameters**](SecretPatchParameters.md)| Parameters to patch the secret | 

### Return type

[**Secret**](Secret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

