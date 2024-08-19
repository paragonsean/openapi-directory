# RecoveryServicesClient.VaultCertificatesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vaultCertificatesCreate**](VaultCertificatesApi.md#vaultCertificatesCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/certificates/{certificateName} | 



## vaultCertificatesCreate

> VaultCertificateResponse vaultCertificatesCreate(subscriptionId, apiVersion, resourceGroupName, vaultName, certificateName, certificateRequest)



Uploads a certificate for a resource.

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.VaultCertificatesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let certificateName = "certificateName_example"; // String | Certificate friendly name.
let certificateRequest = new RecoveryServicesClient.CertificateRequest(); // CertificateRequest | Input parameters for uploading the vault certificate.
apiInstance.vaultCertificatesCreate(subscriptionId, apiVersion, resourceGroupName, vaultName, certificateName, certificateRequest, (error, data, response) => {
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
 **certificateName** | **String**| Certificate friendly name. | 
 **certificateRequest** | [**CertificateRequest**](CertificateRequest.md)| Input parameters for uploading the vault certificate. | 

### Return type

[**VaultCertificateResponse**](VaultCertificateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

