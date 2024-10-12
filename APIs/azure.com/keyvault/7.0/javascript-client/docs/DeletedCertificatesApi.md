# KeyVaultClient.DeletedCertificatesApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDeletedCertificate**](DeletedCertificatesApi.md#getDeletedCertificate) | **GET** /deletedcertificates/{certificate-name} | Retrieves information about the specified deleted certificate.
[**getDeletedCertificates**](DeletedCertificatesApi.md#getDeletedCertificates) | **GET** /deletedcertificates | Lists the deleted certificates in the specified vault currently available for recovery.
[**purgeDeletedCertificate**](DeletedCertificatesApi.md#purgeDeletedCertificate) | **DELETE** /deletedcertificates/{certificate-name} | Permanently deletes the specified deleted certificate.
[**recoverDeletedCertificate**](DeletedCertificatesApi.md#recoverDeletedCertificate) | **POST** /deletedcertificates/{certificate-name}/recover | Recovers the deleted certificate back to its current version under /certificates.



## getDeletedCertificate

> DeletedCertificateBundle getDeletedCertificate(certificateName, apiVersion)

Retrieves information about the specified deleted certificate.

The GetDeletedCertificate operation retrieves the deleted certificate information plus its attributes, such as retention interval, scheduled permanent deletion and the current deletion recovery level. This operation requires the certificates/get permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedCertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getDeletedCertificate(certificateName, apiVersion, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**DeletedCertificateBundle**](DeletedCertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeletedCertificates

> DeletedCertificateListResult getDeletedCertificates(apiVersion, opts)

Lists the deleted certificates in the specified vault currently available for recovery.

The GetDeletedCertificates operation retrieves the certificates in the current vault which are in a deleted state and ready for recovery or purging. This operation includes deletion-specific information. This operation requires the certificates/get/list permission. This operation can only be enabled on soft-delete enabled vaults.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedCertificatesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56, // Number | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
  'includePending': true // Boolean | Specifies whether to include certificates which are not completely provisioned.
};
apiInstance.getDeletedCertificates(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **maxresults** | **Number**| Maximum number of results to return in a page. If not specified the service will return up to 25 results. | [optional] 
 **includePending** | **Boolean**| Specifies whether to include certificates which are not completely provisioned. | [optional] 

### Return type

[**DeletedCertificateListResult**](DeletedCertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## purgeDeletedCertificate

> purgeDeletedCertificate(certificateName, apiVersion)

Permanently deletes the specified deleted certificate.

The PurgeDeletedCertificate operation performs an irreversible deletion of the specified certificate, without possibility for recovery. The operation is not available if the recovery level does not specify &#39;Purgeable&#39;. This operation requires the certificate/purge permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedCertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.purgeDeletedCertificate(certificateName, apiVersion, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoverDeletedCertificate

> CertificateBundle recoverDeletedCertificate(certificateName, apiVersion)

Recovers the deleted certificate back to its current version under /certificates.

The RecoverDeletedCertificate operation performs the reversal of the Delete operation. The operation is applicable in vaults enabled for soft-delete, and must be issued during the retention interval (available in the deleted certificate&#39;s attributes). This operation requires the certificates/recover permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.DeletedCertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the deleted certificate
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.recoverDeletedCertificate(certificateName, apiVersion, (error, data, response) => {
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
 **certificateName** | **String**| The name of the deleted certificate | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

