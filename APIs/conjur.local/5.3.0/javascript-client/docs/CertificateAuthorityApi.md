# Conjur.CertificateAuthorityApi

All URIs are relative to *http://conjur.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sign**](CertificateAuthorityApi.md#sign) | **POST** /ca/{account}/{service_id}/sign | Gets a signed certificate from the configured Certificate Authority service.



## sign

> Sign201Response sign(account, serviceId, csr, ttl, opts)

Gets a signed certificate from the configured Certificate Authority service.

Gets a signed certificate from the configured Certificate Authority service.  The request must include a valid Certificate Signing Request, and a desired TTL in ISO 8601 format.  *** IMPORTANT *** This endpoint is part of an early implementation of support for using Conjur as a certificate authority, and is currently available at the Community (or early alpha) level. This endpoint is still subject to breaking changes in the future. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.CertificateAuthorityApi();
let account = "account_example"; // String | Organization account name
let serviceId = "ca-service"; // String | Name of the Certificate Authority service
let csr = "csr_example"; // String | 
let ttl = "ttl_example"; // String | 
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'accept': "application/x-pem-file" // String | Setting the Accept header to `application/x-pem-file` allows Conjur to respond with a formatted certificate
};
apiInstance.sign(account, serviceId, csr, ttl, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **serviceId** | **String**| Name of the Certificate Authority service | 
 **csr** | **String**|  | 
 **ttl** | **String**|  | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **accept** | **String**| Setting the Accept header to &#x60;application/x-pem-file&#x60; allows Conjur to respond with a formatted certificate | [optional] 

### Return type

[**Sign201Response**](Sign201Response.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/x-pem-file

