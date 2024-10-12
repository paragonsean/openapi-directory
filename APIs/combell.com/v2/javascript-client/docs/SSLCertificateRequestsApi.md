# PublicApi.SSLCertificateRequestsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSslCertificateRequest**](SSLCertificateRequestsApi.md#addSslCertificateRequest) | **POST** /sslcertificaterequests | Add a SSL certificate request
[**getSslCertificateRequest**](SSLCertificateRequestsApi.md#getSslCertificateRequest) | **GET** /sslcertificaterequests/{id} | Detail of a SSL certificate request
[**getSslCertificateRequests**](SSLCertificateRequestsApi.md#getSslCertificateRequests) | **GET** /sslcertificaterequests | Overview of SSL certificate requests
[**verifySslCertificateRequestDomainValidations**](SSLCertificateRequestsApi.md#verifySslCertificateRequestDomainValidations) | **PUT** /sslcertificaterequests/{id} | Verify the SSL certificate request domain validations



## addSslCertificateRequest

> addSslCertificateRequest(opts)

Add a SSL certificate request

Executing this method causes the purchase of a paying product.&lt;br /&gt;  Log on to our website to see your current (renewal) prices or contact our Sales department.&lt;br /&gt;  Please note that promotional pricing does not apply for purchases made through our API.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.SSLCertificateRequestsApi();
let opts = {
  'createSslCertificateRequest': new PublicApi.CreateSslCertificateRequest() // CreateSslCertificateRequest | 
};
apiInstance.addSslCertificateRequest(opts, (error, data, response) => {
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
 **createSslCertificateRequest** | [**CreateSslCertificateRequest**](CreateSslCertificateRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getSslCertificateRequest

> SslCertificateRequestDetail getSslCertificateRequest(id)

Detail of a SSL certificate request

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.SSLCertificateRequestsApi();
let id = 56; // Number | The id of the certificate request.
apiInstance.getSslCertificateRequest(id, (error, data, response) => {
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
 **id** | **Number**| The id of the certificate request. | 

### Return type

[**SslCertificateRequestDetail**](SslCertificateRequestDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSslCertificateRequests

> [SslCertificateRequest] getSslCertificateRequests(opts)

Overview of SSL certificate requests

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.SSLCertificateRequestsApi();
let opts = {
  'skip': 56, // Number | The number of items to skip in the resultset.
  'take': 56 // Number | The number of items to return in the resultset. The returned count can be equal or less than this number.
};
apiInstance.getSslCertificateRequests(opts, (error, data, response) => {
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

[**[SslCertificateRequest]**](SslCertificateRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## verifySslCertificateRequestDomainValidations

> verifySslCertificateRequestDomainValidations(id)

Verify the SSL certificate request domain validations

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.SSLCertificateRequestsApi();
let id = 56; // Number | The id of the certificate request.
apiInstance.verifySslCertificateRequestDomainValidations(id, (error, data, response) => {
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
 **id** | **Number**| The id of the certificate request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

