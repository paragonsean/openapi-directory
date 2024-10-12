# BinLookupApi.LookupApi

All URIs are relative to *https://api.bintable.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**binLookup**](LookupApi.md#binLookup) | **GET** /{bin} | Lookup for bin



## binLookup

> [ResponseItem] binLookup(bin, apiKey)

Lookup for bin

By passing in the appropriate BIN, you can lookup for card meta data in bintable.com API 

### Example

```javascript
import BinLookupApi from 'bin_lookup_api';

let apiInstance = new BinLookupApi.LookupApi();
let bin = "bin_example"; // String | pass the required BIN code
let apiKey = "apiKey_example"; // String | The API key, which you can get from bintable.com website.
apiInstance.binLookup(bin, apiKey, (error, data, response) => {
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
 **bin** | **String**| pass the required BIN code | 
 **apiKey** | **String**| The API key, which you can get from bintable.com website. | 

### Return type

[**[ResponseItem]**](ResponseItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

