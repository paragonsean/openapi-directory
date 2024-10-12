# SiteRecoveryManagementClient.ReplicationVaultSettingApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationVaultSettingCreate**](ReplicationVaultSettingApi.md#replicationVaultSettingCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationVaultSettings/{vaultSettingName} | Updates vault setting. A vault setting object is a singleton per vault and it is always present by default.
[**replicationVaultSettingGet**](ReplicationVaultSettingApi.md#replicationVaultSettingGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationVaultSettings/{vaultSettingName} | Gets the vault setting.
[**replicationVaultSettingList**](ReplicationVaultSettingApi.md#replicationVaultSettingList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationVaultSettings | Gets the list of vault setting.



## replicationVaultSettingCreate

> VaultSetting replicationVaultSettingCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, vaultSettingName, input)

Updates vault setting. A vault setting object is a singleton per vault and it is always present by default.

The operation to configure vault setting.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationVaultSettingApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let vaultSettingName = "vaultSettingName_example"; // String | Vault setting name.
let input = new SiteRecoveryManagementClient.VaultSettingCreationInput(); // VaultSettingCreationInput | Vault setting creation input.
apiInstance.replicationVaultSettingCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, vaultSettingName, input, (error, data, response) => {
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
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **vaultSettingName** | **String**| Vault setting name. | 
 **input** | [**VaultSettingCreationInput**](VaultSettingCreationInput.md)| Vault setting creation input. | 

### Return type

[**VaultSetting**](VaultSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationVaultSettingGet

> VaultSetting replicationVaultSettingGet(apiVersion, resourceName, resourceGroupName, subscriptionId, vaultSettingName)

Gets the vault setting.

Gets the vault setting. This includes the Migration Hub connection settings.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationVaultSettingApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let vaultSettingName = "vaultSettingName_example"; // String | Vault setting name.
apiInstance.replicationVaultSettingGet(apiVersion, resourceName, resourceGroupName, subscriptionId, vaultSettingName, (error, data, response) => {
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
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **vaultSettingName** | **String**| Vault setting name. | 

### Return type

[**VaultSetting**](VaultSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationVaultSettingList

> VaultSettingCollection replicationVaultSettingList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of vault setting.

Gets the list of vault setting. This includes the Migration Hub connection settings.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationVaultSettingApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
apiInstance.replicationVaultSettingList(apiVersion, resourceName, resourceGroupName, subscriptionId, (error, data, response) => {
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
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 

### Return type

[**VaultSettingCollection**](VaultSettingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

