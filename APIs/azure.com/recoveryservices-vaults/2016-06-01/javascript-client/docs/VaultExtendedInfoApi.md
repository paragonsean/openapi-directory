# RecoveryServicesClient.VaultExtendedInfoApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vaultExtendedInfoCreateOrUpdate**](VaultExtendedInfoApi.md#vaultExtendedInfoCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/extendedInformation/vaultExtendedInfo | 
[**vaultExtendedInfoGet**](VaultExtendedInfoApi.md#vaultExtendedInfoGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/extendedInformation/vaultExtendedInfo | 
[**vaultExtendedInfoUpdate**](VaultExtendedInfoApi.md#vaultExtendedInfoUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/extendedInformation/vaultExtendedInfo | 



## vaultExtendedInfoCreateOrUpdate

> VaultExtendedInfoResource vaultExtendedInfoCreateOrUpdate(subscriptionId, resourceGroupName, vaultName, apiVersion, resourceResourceExtendedInfoDetails)



Create vault extended info.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultExtendedInfoApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceResourceExtendedInfoDetails = new RecoveryServicesClient.VaultExtendedInfoResource(); // VaultExtendedInfoResource | Details of ResourceExtendedInfo
apiInstance.vaultExtendedInfoCreateOrUpdate(subscriptionId, resourceGroupName, vaultName, apiVersion, resourceResourceExtendedInfoDetails, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **vaultName** | **String**| The name of the recovery services vault. | 
 **apiVersion** | **String**| Client Api Version. | 
 **resourceResourceExtendedInfoDetails** | [**VaultExtendedInfoResource**](VaultExtendedInfoResource.md)| Details of ResourceExtendedInfo | 

### Return type

[**VaultExtendedInfoResource**](VaultExtendedInfoResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## vaultExtendedInfoGet

> VaultExtendedInfoResource vaultExtendedInfoGet(subscriptionId, apiVersion, resourceGroupName, vaultName)



Get the vault extended info.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultExtendedInfoApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
apiInstance.vaultExtendedInfoGet(subscriptionId, apiVersion, resourceGroupName, vaultName, (error, data, response) => {
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

[**VaultExtendedInfoResource**](VaultExtendedInfoResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vaultExtendedInfoUpdate

> VaultExtendedInfoResource vaultExtendedInfoUpdate(subscriptionId, resourceGroupName, vaultName, apiVersion, resourceResourceExtendedInfoDetails)



Update vault extended info.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultExtendedInfoApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceResourceExtendedInfoDetails = new RecoveryServicesClient.VaultExtendedInfoResource(); // VaultExtendedInfoResource | Details of ResourceExtendedInfo
apiInstance.vaultExtendedInfoUpdate(subscriptionId, resourceGroupName, vaultName, apiVersion, resourceResourceExtendedInfoDetails, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **vaultName** | **String**| The name of the recovery services vault. | 
 **apiVersion** | **String**| Client Api Version. | 
 **resourceResourceExtendedInfoDetails** | [**VaultExtendedInfoResource**](VaultExtendedInfoResource.md)| Details of ResourceExtendedInfo | 

### Return type

[**VaultExtendedInfoResource**](VaultExtendedInfoResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

