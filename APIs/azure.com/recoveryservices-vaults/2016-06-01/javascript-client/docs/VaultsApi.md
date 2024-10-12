# RecoveryServicesClient.VaultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vaultsCreateOrUpdate**](VaultsApi.md#vaultsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName} | 
[**vaultsDelete**](VaultsApi.md#vaultsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName} | 
[**vaultsGet**](VaultsApi.md#vaultsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName} | 
[**vaultsListByResourceGroup**](VaultsApi.md#vaultsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults | 
[**vaultsListBySubscriptionId**](VaultsApi.md#vaultsListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/vaults | 
[**vaultsUpdate**](VaultsApi.md#vaultsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName} | 



## vaultsCreateOrUpdate

> Vault vaultsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, vaultName, vault)



Creates or updates a Recovery Services vault.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let vault = new RecoveryServicesClient.Vault(); // Vault | Recovery Services Vault to be created.
apiInstance.vaultsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, vaultName, vault, (error, data, response) => {
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
 **vault** | [**Vault**](Vault.md)| Recovery Services Vault to be created. | 

### Return type

[**Vault**](Vault.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vaultsDelete

> vaultsDelete(subscriptionId, apiVersion, resourceGroupName, vaultName)



Deletes a vault.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
apiInstance.vaultsDelete(subscriptionId, apiVersion, resourceGroupName, vaultName, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## vaultsGet

> Vault vaultsGet(subscriptionId, apiVersion, resourceGroupName, vaultName)



Get the Vault details.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
apiInstance.vaultsGet(subscriptionId, apiVersion, resourceGroupName, vaultName, (error, data, response) => {
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

[**Vault**](Vault.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vaultsListByResourceGroup

> VaultList vaultsListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)



Retrieve a list of Vaults.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
apiInstance.vaultsListByResourceGroup(subscriptionId, apiVersion, resourceGroupName, (error, data, response) => {
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

### Return type

[**VaultList**](VaultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vaultsListBySubscriptionId

> VaultList vaultsListBySubscriptionId(subscriptionId, apiVersion)



Fetches all the resources of the specified type in the subscription.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.vaultsListBySubscriptionId(subscriptionId, apiVersion, (error, data, response) => {
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

### Return type

[**VaultList**](VaultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vaultsUpdate

> Vault vaultsUpdate(subscriptionId, apiVersion, resourceGroupName, vaultName, vault)



Updates the vault.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let vault = new RecoveryServicesClient.PatchVault(); // PatchVault | Recovery Services Vault to be created.
apiInstance.vaultsUpdate(subscriptionId, apiVersion, resourceGroupName, vaultName, vault, (error, data, response) => {
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
 **vault** | [**PatchVault**](PatchVault.md)| Recovery Services Vault to be created. | 

### Return type

[**Vault**](Vault.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

