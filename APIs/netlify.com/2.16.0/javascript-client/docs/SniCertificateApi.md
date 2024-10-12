# NetlifysApiDocumentation.SniCertificateApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provisionSiteTLSCertificate**](SniCertificateApi.md#provisionSiteTLSCertificate) | **POST** /sites/{site_id}/ssl | 
[**showSiteTLSCertificate**](SniCertificateApi.md#showSiteTLSCertificate) | **GET** /sites/{site_id}/ssl | 



## provisionSiteTLSCertificate

> SniCertificate provisionSiteTLSCertificate(siteId, opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SniCertificateApi();
let siteId = "siteId_example"; // String | 
let opts = {
  'certificate': "certificate_example", // String | 
  'key': "key_example", // String | 
  'caCertificates': "caCertificates_example" // String | 
};
apiInstance.provisionSiteTLSCertificate(siteId, opts, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **certificate** | **String**|  | [optional] 
 **key** | **String**|  | [optional] 
 **caCertificates** | **String**|  | [optional] 

### Return type

[**SniCertificate**](SniCertificate.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showSiteTLSCertificate

> SniCertificate showSiteTLSCertificate(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SniCertificateApi();
let siteId = "siteId_example"; // String | 
apiInstance.showSiteTLSCertificate(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

[**SniCertificate**](SniCertificate.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

