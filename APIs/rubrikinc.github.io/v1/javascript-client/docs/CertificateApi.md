# RubrikRestApi.CertificateApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteCertificate**](CertificateApi.md#deleteCertificate) | **DELETE** /certificate/{id} | Delete imported certificate object
[**exportCertificate**](CertificateApi.md#exportCertificate) | **GET** /certificate/{id} | Get a certificate summary to export
[**importCertificate**](CertificateApi.md#importCertificate) | **POST** /certificate | Import a certificate
[**queryCertificates**](CertificateApi.md#queryCertificates) | **GET** /certificate | Get all certificates
[**updateCertificate**](CertificateApi.md#updateCertificate) | **PATCH** /certificate/{id} | Update a certificate entry



## deleteCertificate

> deleteCertificate(id)

Delete imported certificate object

Deletes an imported certificate.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.CertificateApi();
let id = "id_example"; // String | The certificate ID.
apiInstance.deleteCertificate(id, (error, data, response) => {
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
 **id** | **String**| The certificate ID. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## exportCertificate

> CertificateSummary exportCertificate(id)

Get a certificate summary to export

Get a certificate summary.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.CertificateApi();
let id = "id_example"; // String | ID of certificate to export.
apiInstance.exportCertificate(id, (error, data, response) => {
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
 **id** | **String**| ID of certificate to export. | 

### Return type

[**CertificateSummary**](CertificateSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## importCertificate

> CertificateSummary importCertificate(certificateImportRequest)

Import a certificate

Import a certificate.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.CertificateApi();
let certificateImportRequest = new RubrikRestApi.CertificateImportRequest(); // CertificateImportRequest | Request to import a certificate.
apiInstance.importCertificate(certificateImportRequest, (error, data, response) => {
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
 **certificateImportRequest** | [**CertificateImportRequest**](CertificateImportRequest.md)| Request to import a certificate. | 

### Return type

[**CertificateSummary**](CertificateSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryCertificates

> CertificateSummaryListResponse queryCertificates(opts)

Get all certificates

Get all certificates.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.CertificateApi();
let opts = {
  'name': "name_example", // String | Search by certificate name.
  'hasKey': true, // Boolean | Search certificates by whether or not they contain a private key. 
  'description': "description_example", // String | Search certificates by description.
  'expiration': "expiration_example", // String | Search certificates by expiration.
  'includeExpired': true, // Boolean | Specifies whether to include expired certificates. The default is false.
  'sortBy': "'Name'", // String | Attribute by which the list of certificates is sorted.
  'sortOrder': "'asc'" // String | Sort order, either ascending or descending.
};
apiInstance.queryCertificates(opts, (error, data, response) => {
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
 **name** | **String**| Search by certificate name. | [optional] 
 **hasKey** | **Boolean**| Search certificates by whether or not they contain a private key.  | [optional] 
 **description** | **String**| Search certificates by description. | [optional] 
 **expiration** | **String**| Search certificates by expiration. | [optional] 
 **includeExpired** | **Boolean**| Specifies whether to include expired certificates. The default is false. | [optional] 
 **sortBy** | **String**| Attribute by which the list of certificates is sorted. | [optional] [default to &#39;Name&#39;]
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to &#39;asc&#39;]

### Return type

[**CertificateSummaryListResponse**](CertificateSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCertificate

> CertificateSummary updateCertificate(id, certificatePatchRequest)

Update a certificate entry

Provide updated information for a certificate object.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.CertificateApi();
let id = "id_example"; // String | ID of certificate object to update.
let certificatePatchRequest = new RubrikRestApi.CertificatePatchRequest(); // CertificatePatchRequest | Patch request to update a certificate object.
apiInstance.updateCertificate(id, certificatePatchRequest, (error, data, response) => {
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
 **id** | **String**| ID of certificate object to update. | 
 **certificatePatchRequest** | [**CertificatePatchRequest**](CertificatePatchRequest.md)| Patch request to update a certificate object. | 

### Return type

[**CertificateSummary**](CertificateSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

