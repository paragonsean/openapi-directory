# AvazaApiDocumentation.TaxApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxGet**](TaxApi.md#taxGet) | **GET** /api/Tax | Get List of Taxes configured in the Avaza account.



## taxGet

> TaxList taxGet()

Get List of Taxes configured in the Avaza account.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TaxApi();
apiInstance.taxGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TaxList**](TaxList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

