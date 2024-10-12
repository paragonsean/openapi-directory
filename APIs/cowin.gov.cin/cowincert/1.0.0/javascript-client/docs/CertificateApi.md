# CoWinCertificateApi.CertificateApi

All URIs are relative to *https://cowin.gov.cin/cert/external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCertificatePdf**](CertificateApi.md#getCertificatePdf) | **POST** /pdf/certificate | Download the certificate in pdf format



## getCertificatePdf

> getCertificatePdf(body)

Download the certificate in pdf format

### Example

```javascript
import CoWinCertificateApi from 'co_win_certificate_api';
let defaultClient = CoWinCertificateApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: cert_auth
let cert_auth = defaultClient.authentications['cert_auth'];
cert_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CoWinCertificateApi.CertificateApi();
let body = new CoWinCertificateApi.CertificateRequest(); // CertificateRequest | 
apiInstance.getCertificatePdf(body, (error, data, response) => {
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
 **body** | [**CertificateRequest**](CertificateRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[cert_auth](../README.md#cert_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

