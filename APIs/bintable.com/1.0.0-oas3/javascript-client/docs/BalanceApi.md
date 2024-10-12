# BinLookupApi.BalanceApi

All URIs are relative to *https://api.bintable.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balanceLookup**](BalanceApi.md#balanceLookup) | **GET** /balance | Check Balance



## balanceLookup

> [ResponseItem] balanceLookup(apiKey)

Check Balance

Get Account balance and expiry

### Example

```javascript
import BinLookupApi from 'bin_lookup_api';

let apiInstance = new BinLookupApi.BalanceApi();
let apiKey = "apiKey_example"; // String | The API key, which you can get from bintable.com website.
apiInstance.balanceLookup(apiKey, (error, data, response) => {
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
 **apiKey** | **String**| The API key, which you can get from bintable.com website. | 

### Return type

[**[ResponseItem]**](ResponseItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

