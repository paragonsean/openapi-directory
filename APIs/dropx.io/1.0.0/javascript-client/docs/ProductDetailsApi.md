# DropX.ProductDetailsApi

All URIs are relative to *http://dropx.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsGet**](ProductDetailsApi.md#productsGet) | **GET** /products/ | Get product details by providing the product IDs



## productsGet

> productsGet(pids)

Get product details by providing the product IDs

Returns product details

### Example

```javascript
import DropX from 'drop_x';
let defaultClient = DropX.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DropX.ProductDetailsApi();
let pids = "pids_example"; // String | search array of ids
apiInstance.productsGet(pids, (error, data, response) => {
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
 **pids** | **String**| search array of ids | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

