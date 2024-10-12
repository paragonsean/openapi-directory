# GoUpcBarcodeLookupApi.ProductApi

All URIs are relative to *https://go-upc.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProductInfo**](ProductApi.md#getProductInfo) | **GET** /code/{code} | Retrieve product info for a particular barcode number (UPC, EAN, or ISBN).



## getProductInfo

> GetProductInfo200Response getProductInfo(code)

Retrieve product info for a particular barcode number (UPC, EAN, or ISBN).

### Example

```javascript
import GoUpcBarcodeLookupApi from 'go_upc_barcode_lookup_api';
let defaultClient = GoUpcBarcodeLookupApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new GoUpcBarcodeLookupApi.ProductApi();
let code = "code_example"; // String | 
apiInstance.getProductInfo(code, (error, data, response) => {
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
 **code** | **String**|  | 

### Return type

[**GetProductInfo200Response**](GetProductInfo200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

