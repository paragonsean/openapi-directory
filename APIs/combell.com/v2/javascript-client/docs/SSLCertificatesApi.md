# PublicApi.SSLCertificatesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadCertificate**](SSLCertificatesApi.md#downloadCertificate) | **GET** /sslcertificates/{sha1Fingerprint}/download | Download a SSL certificate
[**getSslCertificate**](SSLCertificatesApi.md#getSslCertificate) | **GET** /sslcertificates/{sha1Fingerprint} | Detail of a SSL certificate
[**getSslCertificates**](SSLCertificatesApi.md#getSslCertificates) | **GET** /sslcertificates | Overview of SSL certificates



## downloadCertificate

> File downloadCertificate(sha1Fingerprint, fileFormat, password, sha1Fingerprint2)

Download a SSL certificate

Returns the certifcate as binary data with the content-type and the filename information in the response headers.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.SSLCertificatesApi();
let sha1Fingerprint = "sha1Fingerprint_example"; // String | The SHA-1 fingerprint of the certificate.
let fileFormat = new PublicApi.SslCertificateFileFormat(); // SslCertificateFileFormat | The file format of the returned file stream:  <ul><li>PFX: Also known as PKCS #12, is a single, password protected certificate archive that contains the entire certificate chain plus the matching private key.</li></ul>
let password = "password_example"; // String | The password used to protect the certificate file.<br />
let sha1Fingerprint2 = "sha1Fingerprint_example"; // String | Automatically added
apiInstance.downloadCertificate(sha1Fingerprint, fileFormat, password, sha1Fingerprint2, (error, data, response) => {
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
 **sha1Fingerprint** | **String**| The SHA-1 fingerprint of the certificate. | 
 **fileFormat** | [**SslCertificateFileFormat**](.md)| The file format of the returned file stream:  &lt;ul&gt;&lt;li&gt;PFX: Also known as PKCS #12, is a single, password protected certificate archive that contains the entire certificate chain plus the matching private key.&lt;/li&gt;&lt;/ul&gt; | 
 **password** | **String**| The password used to protect the certificate file.&lt;br /&gt; | 
 **sha1Fingerprint2** | **String**| Automatically added | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSslCertificate

> SslCertificateDetail getSslCertificate(sha1Fingerprint, sha1Fingerprint2)

Detail of a SSL certificate

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.SSLCertificatesApi();
let sha1Fingerprint = "sha1Fingerprint_example"; // String | The SHA-1 fingerprint of the certificate.
let sha1Fingerprint2 = "sha1Fingerprint_example"; // String | Automatically added
apiInstance.getSslCertificate(sha1Fingerprint, sha1Fingerprint2, (error, data, response) => {
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
 **sha1Fingerprint** | **String**| The SHA-1 fingerprint of the certificate. | 
 **sha1Fingerprint2** | **String**| Automatically added | 

### Return type

[**SslCertificateDetail**](SslCertificateDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSslCertificates

> [SslCertificate] getSslCertificates(opts)

Overview of SSL certificates

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.SSLCertificatesApi();
let opts = {
  'skip': 56, // Number | The number of items to skip in the resultset.
  'take': 56 // Number | The number of items to return in the resultset. The returned count can be equal or less than this number.
};
apiInstance.getSslCertificates(opts, (error, data, response) => {
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
 **skip** | **Number**| The number of items to skip in the resultset. | [optional] 
 **take** | **Number**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] 

### Return type

[**[SslCertificate]**](SslCertificate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

