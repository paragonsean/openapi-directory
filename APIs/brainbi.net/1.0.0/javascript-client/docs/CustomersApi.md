# Brainbi.CustomersApi

All URIs are relative to *http://,*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers**](CustomersApi.md#customers) | **GET** /api/customers | Customers



## customers

> customers(opts)

Customers

This resource lists all cusomters that are currently saved in your account.

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.CustomersApi();
let opts = {
  '': "" // String | 
};
apiInstance.customers(opts, (error, data, response) => {
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
 **** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

