# KeyVaultClient.CertificatesApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupCertificate**](CertificatesApi.md#backupCertificate) | **POST** /certificates/{certificate-name}/backup | Backs up the specified certificate.
[**createCertificate**](CertificatesApi.md#createCertificate) | **POST** /certificates/{certificate-name}/create | Creates a new certificate.
[**deleteCertificate**](CertificatesApi.md#deleteCertificate) | **DELETE** /certificates/{certificate-name} | Deletes a certificate from a specified key vault.
[**deleteCertificateContacts**](CertificatesApi.md#deleteCertificateContacts) | **DELETE** /certificates/contacts | Deletes the certificate contacts for a specified key vault.
[**deleteCertificateIssuer**](CertificatesApi.md#deleteCertificateIssuer) | **DELETE** /certificates/issuers/{issuer-name} | Deletes the specified certificate issuer.
[**deleteCertificateOperation**](CertificatesApi.md#deleteCertificateOperation) | **DELETE** /certificates/{certificate-name}/pending | Deletes the creation operation for a specific certificate.
[**getCertificate**](CertificatesApi.md#getCertificate) | **GET** /certificates/{certificate-name}/{certificate-version} | Gets information about a certificate.
[**getCertificateContacts**](CertificatesApi.md#getCertificateContacts) | **GET** /certificates/contacts | Lists the certificate contacts for a specified key vault.
[**getCertificateIssuer**](CertificatesApi.md#getCertificateIssuer) | **GET** /certificates/issuers/{issuer-name} | Lists the specified certificate issuer.
[**getCertificateIssuers**](CertificatesApi.md#getCertificateIssuers) | **GET** /certificates/issuers | List certificate issuers for a specified key vault.
[**getCertificateOperation**](CertificatesApi.md#getCertificateOperation) | **GET** /certificates/{certificate-name}/pending | Gets the creation operation of a certificate.
[**getCertificatePolicy**](CertificatesApi.md#getCertificatePolicy) | **GET** /certificates/{certificate-name}/policy | Lists the policy for a certificate.
[**getCertificateVersions**](CertificatesApi.md#getCertificateVersions) | **GET** /certificates/{certificate-name}/versions | List the versions of a certificate.
[**getCertificates**](CertificatesApi.md#getCertificates) | **GET** /certificates | List certificates in a specified key vault
[**importCertificate**](CertificatesApi.md#importCertificate) | **POST** /certificates/{certificate-name}/import | Imports a certificate into a specified key vault.
[**mergeCertificate**](CertificatesApi.md#mergeCertificate) | **POST** /certificates/{certificate-name}/pending/merge | Merges a certificate or a certificate chain with a key pair existing on the server.
[**restoreCertificate**](CertificatesApi.md#restoreCertificate) | **POST** /certificates/restore | Restores a backed up certificate to a vault.
[**setCertificateContacts**](CertificatesApi.md#setCertificateContacts) | **PUT** /certificates/contacts | Sets the certificate contacts for the specified key vault.
[**setCertificateIssuer**](CertificatesApi.md#setCertificateIssuer) | **PUT** /certificates/issuers/{issuer-name} | Sets the specified certificate issuer.
[**updateCertificate**](CertificatesApi.md#updateCertificate) | **PATCH** /certificates/{certificate-name}/{certificate-version} | Updates the specified attributes associated with the given certificate.
[**updateCertificateIssuer**](CertificatesApi.md#updateCertificateIssuer) | **PATCH** /certificates/issuers/{issuer-name} | Updates the specified certificate issuer.
[**updateCertificateOperation**](CertificatesApi.md#updateCertificateOperation) | **PATCH** /certificates/{certificate-name}/pending | Updates a certificate operation.
[**updateCertificatePolicy**](CertificatesApi.md#updateCertificatePolicy) | **PATCH** /certificates/{certificate-name}/policy | Updates the policy for a certificate.



## backupCertificate

> BackupCertificateResult backupCertificate(certificateName, apiVersion)

Backs up the specified certificate.

Requests that a backup of the specified certificate be downloaded to the client. All versions of the certificate will be downloaded. This operation requires the certificates/backup permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.backupCertificate(certificateName, apiVersion, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**BackupCertificateResult**](BackupCertificateResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createCertificate

> CertificateOperation createCertificate(certificateName, apiVersion, parameters)

Creates a new certificate.

If this is the first version, the certificate resource is created. This operation requires the certificates/create permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.CertificateCreateParameters(); // CertificateCreateParameters | The parameters to create a certificate.
apiInstance.createCertificate(certificateName, apiVersion, parameters, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate. | 
 **apiVersion** | **String**| Client API version. | 
 **parameters** | [**CertificateCreateParameters**](CertificateCreateParameters.md)| The parameters to create a certificate. | 

### Return type

[**CertificateOperation**](CertificateOperation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCertificate

> DeletedCertificateBundle deleteCertificate(certificateName, apiVersion)

Deletes a certificate from a specified key vault.

Deletes all versions of a certificate object along with its associated policy. Delete certificate cannot be used to remove individual versions of a certificate object. This operation requires the certificates/delete permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.deleteCertificate(certificateName, apiVersion, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**DeletedCertificateBundle**](DeletedCertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCertificateContacts

> Contacts deleteCertificateContacts(apiVersion)

Deletes the certificate contacts for a specified key vault.

Deletes the certificate contacts for a specified key vault certificate. This operation requires the certificates/managecontacts permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.deleteCertificateContacts(apiVersion, (error, data, response) => {
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

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCertificateIssuer

> IssuerBundle deleteCertificateIssuer(issuerName, apiVersion)

Deletes the specified certificate issuer.

The DeleteCertificateIssuer operation permanently removes the specified certificate issuer from the vault. This operation requires the certificates/manageissuers/deleteissuers permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let issuerName = "issuerName_example"; // String | The name of the issuer.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.deleteCertificateIssuer(issuerName, apiVersion, (error, data, response) => {
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
 **issuerName** | **String**| The name of the issuer. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**IssuerBundle**](IssuerBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCertificateOperation

> CertificateOperation deleteCertificateOperation(certificateName, apiVersion)

Deletes the creation operation for a specific certificate.

Deletes the creation operation for a specified certificate that is in the process of being created. The certificate is no longer created. This operation requires the certificates/update permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.deleteCertificateOperation(certificateName, apiVersion, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**CertificateOperation**](CertificateOperation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCertificate

> CertificateBundle getCertificate(certificateName, certificateVersion, apiVersion)

Gets information about a certificate.

Gets information about a specific certificate. This operation requires the certificates/get permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate in the given vault.
let certificateVersion = "certificateVersion_example"; // String | The version of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getCertificate(certificateName, certificateVersion, apiVersion, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate in the given vault. | 
 **certificateVersion** | **String**| The version of the certificate. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCertificateContacts

> Contacts getCertificateContacts(apiVersion)

Lists the certificate contacts for a specified key vault.

The GetCertificateContacts operation returns the set of certificate contact resources in the specified key vault. This operation requires the certificates/managecontacts permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getCertificateContacts(apiVersion, (error, data, response) => {
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

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCertificateIssuer

> IssuerBundle getCertificateIssuer(issuerName, apiVersion)

Lists the specified certificate issuer.

The GetCertificateIssuer operation returns the specified certificate issuer resources in the specified key vault. This operation requires the certificates/manageissuers/getissuers permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let issuerName = "issuerName_example"; // String | The name of the issuer.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getCertificateIssuer(issuerName, apiVersion, (error, data, response) => {
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
 **issuerName** | **String**| The name of the issuer. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**IssuerBundle**](IssuerBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCertificateIssuers

> CertificateIssuerListResult getCertificateIssuers(apiVersion, opts)

List certificate issuers for a specified key vault.

The GetCertificateIssuers operation returns the set of certificate issuer resources in the specified key vault. This operation requires the certificates/manageissuers/getissuers permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56 // Number | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
};
apiInstance.getCertificateIssuers(apiVersion, opts, (error, data, response) => {
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

### Return type

[**CertificateIssuerListResult**](CertificateIssuerListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCertificateOperation

> CertificateOperation getCertificateOperation(certificateName, apiVersion)

Gets the creation operation of a certificate.

Gets the creation operation associated with a specified certificate. This operation requires the certificates/get permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getCertificateOperation(certificateName, apiVersion, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**CertificateOperation**](CertificateOperation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCertificatePolicy

> CertificatePolicy getCertificatePolicy(certificateName, apiVersion)

Lists the policy for a certificate.

The GetCertificatePolicy operation returns the specified certificate policy resources in the specified key vault. This operation requires the certificates/get permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate in a given key vault.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.getCertificatePolicy(certificateName, apiVersion, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate in a given key vault. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**CertificatePolicy**](CertificatePolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCertificateVersions

> CertificateListResult getCertificateVersions(certificateName, apiVersion, opts)

List the versions of a certificate.

The GetCertificateVersions operation returns the versions of a certificate in the specified key vault. This operation requires the certificates/list permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56 // Number | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
};
apiInstance.getCertificateVersions(certificateName, apiVersion, opts, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate. | 
 **apiVersion** | **String**| Client API version. | 
 **maxresults** | **Number**| Maximum number of results to return in a page. If not specified the service will return up to 25 results. | [optional] 

### Return type

[**CertificateListResult**](CertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCertificates

> CertificateListResult getCertificates(apiVersion, opts)

List certificates in a specified key vault

The GetCertificates operation returns the set of certificates resources in the specified key vault. This operation requires the certificates/list permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'maxresults': 56, // Number | Maximum number of results to return in a page. If not specified the service will return up to 25 results.
  'includePending': true // Boolean | Specifies whether to include certificates which are not completely provisioned.
};
apiInstance.getCertificates(apiVersion, opts, (error, data, response) => {
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

[**CertificateListResult**](CertificateListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importCertificate

> CertificateBundle importCertificate(certificateName, apiVersion, parameters)

Imports a certificate into a specified key vault.

Imports an existing valid certificate, containing a private key, into Azure Key Vault. The certificate to be imported can be in either PFX or PEM format. If the certificate is in PEM format the PEM file must contain the key as well as x509 certificates. This operation requires the certificates/import permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.CertificateImportParameters(); // CertificateImportParameters | The parameters to import the certificate.
apiInstance.importCertificate(certificateName, apiVersion, parameters, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate. | 
 **apiVersion** | **String**| Client API version. | 
 **parameters** | [**CertificateImportParameters**](CertificateImportParameters.md)| The parameters to import the certificate. | 

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mergeCertificate

> CertificateBundle mergeCertificate(certificateName, apiVersion, parameters)

Merges a certificate or a certificate chain with a key pair existing on the server.

The MergeCertificate operation performs the merging of a certificate or certificate chain with a key pair currently available in the service. This operation requires the certificates/create permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.CertificateMergeParameters(); // CertificateMergeParameters | The parameters to merge certificate.
apiInstance.mergeCertificate(certificateName, apiVersion, parameters, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate. | 
 **apiVersion** | **String**| Client API version. | 
 **parameters** | [**CertificateMergeParameters**](CertificateMergeParameters.md)| The parameters to merge certificate. | 

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## restoreCertificate

> CertificateBundle restoreCertificate(apiVersion, parameters)

Restores a backed up certificate to a vault.

Restores a backed up certificate, and all its versions, to a vault. This operation requires the certificates/restore permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.CertificateRestoreParameters(); // CertificateRestoreParameters | The parameters to restore the certificate.
apiInstance.restoreCertificate(apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**CertificateRestoreParameters**](CertificateRestoreParameters.md)| The parameters to restore the certificate. | 

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setCertificateContacts

> Contacts setCertificateContacts(apiVersion, contacts)

Sets the certificate contacts for the specified key vault.

Sets the certificate contacts for the specified key vault. This operation requires the certificates/managecontacts permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let contacts = new KeyVaultClient.Contacts(); // Contacts | The contacts for the key vault certificate.
apiInstance.setCertificateContacts(apiVersion, contacts, (error, data, response) => {
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
 **contacts** | [**Contacts**](Contacts.md)| The contacts for the key vault certificate. | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setCertificateIssuer

> IssuerBundle setCertificateIssuer(issuerName, apiVersion, parameter)

Sets the specified certificate issuer.

The SetCertificateIssuer operation adds or updates the specified certificate issuer. This operation requires the certificates/setissuers permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let issuerName = "issuerName_example"; // String | The name of the issuer.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameter = new KeyVaultClient.CertificateIssuerSetParameters(); // CertificateIssuerSetParameters | Certificate issuer set parameter.
apiInstance.setCertificateIssuer(issuerName, apiVersion, parameter, (error, data, response) => {
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
 **issuerName** | **String**| The name of the issuer. | 
 **apiVersion** | **String**| Client API version. | 
 **parameter** | [**CertificateIssuerSetParameters**](CertificateIssuerSetParameters.md)| Certificate issuer set parameter. | 

### Return type

[**IssuerBundle**](IssuerBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCertificate

> CertificateBundle updateCertificate(certificateName, certificateVersion, apiVersion, parameters)

Updates the specified attributes associated with the given certificate.

The UpdateCertificate operation applies the specified update on the given certificate; the only elements updated are the certificate&#39;s attributes. This operation requires the certificates/update permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate in the given key vault.
let certificateVersion = "certificateVersion_example"; // String | The version of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameters = new KeyVaultClient.CertificateUpdateParameters(); // CertificateUpdateParameters | The parameters for certificate update.
apiInstance.updateCertificate(certificateName, certificateVersion, apiVersion, parameters, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate in the given key vault. | 
 **certificateVersion** | **String**| The version of the certificate. | 
 **apiVersion** | **String**| Client API version. | 
 **parameters** | [**CertificateUpdateParameters**](CertificateUpdateParameters.md)| The parameters for certificate update. | 

### Return type

[**CertificateBundle**](CertificateBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCertificateIssuer

> IssuerBundle updateCertificateIssuer(issuerName, apiVersion, parameter)

Updates the specified certificate issuer.

The UpdateCertificateIssuer operation performs an update on the specified certificate issuer entity. This operation requires the certificates/setissuers permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let issuerName = "issuerName_example"; // String | The name of the issuer.
let apiVersion = "apiVersion_example"; // String | Client API version.
let parameter = new KeyVaultClient.CertificateIssuerUpdateParameters(); // CertificateIssuerUpdateParameters | Certificate issuer update parameter.
apiInstance.updateCertificateIssuer(issuerName, apiVersion, parameter, (error, data, response) => {
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
 **issuerName** | **String**| The name of the issuer. | 
 **apiVersion** | **String**| Client API version. | 
 **parameter** | [**CertificateIssuerUpdateParameters**](CertificateIssuerUpdateParameters.md)| Certificate issuer update parameter. | 

### Return type

[**IssuerBundle**](IssuerBundle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCertificateOperation

> CertificateOperation updateCertificateOperation(certificateName, apiVersion, certificateOperation)

Updates a certificate operation.

Updates a certificate creation operation that is already in progress. This operation requires the certificates/update permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate.
let apiVersion = "apiVersion_example"; // String | Client API version.
let certificateOperation = new KeyVaultClient.CertificateOperationUpdateParameter(); // CertificateOperationUpdateParameter | The certificate operation response.
apiInstance.updateCertificateOperation(certificateName, apiVersion, certificateOperation, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate. | 
 **apiVersion** | **String**| Client API version. | 
 **certificateOperation** | [**CertificateOperationUpdateParameter**](CertificateOperationUpdateParameter.md)| The certificate operation response. | 

### Return type

[**CertificateOperation**](CertificateOperation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCertificatePolicy

> CertificatePolicy updateCertificatePolicy(certificateName, apiVersion, certificatePolicy)

Updates the policy for a certificate.

Set specified members in the certificate policy. Leave others as null. This operation requires the certificates/update permission.

### Example

```javascript
import KeyVaultClient from 'key_vault_client';

let apiInstance = new KeyVaultClient.CertificatesApi();
let certificateName = "certificateName_example"; // String | The name of the certificate in the given vault.
let apiVersion = "apiVersion_example"; // String | Client API version.
let certificatePolicy = new KeyVaultClient.CertificatePolicy(); // CertificatePolicy | The policy for the certificate.
apiInstance.updateCertificatePolicy(certificateName, apiVersion, certificatePolicy, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate in the given vault. | 
 **apiVersion** | **String**| Client API version. | 
 **certificatePolicy** | [**CertificatePolicy**](CertificatePolicy.md)| The policy for the certificate. | 

### Return type

[**CertificatePolicy**](CertificatePolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

