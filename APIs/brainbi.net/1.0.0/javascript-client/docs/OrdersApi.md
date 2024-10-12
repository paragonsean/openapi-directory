# Brainbi.OrdersApi

All URIs are relative to *http://,*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders**](OrdersApi.md#orders) | **GET** /api/orders | Orders
[**orders1**](OrdersApi.md#orders1) | **DELETE** /api/orders/1137 | Orders



## orders

> orders(opts)

Orders

This resource lists all orders that are currently saved in your account.

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.OrdersApi();
let opts = {
  '': "" // String | 
};
apiInstance.orders(opts, (error, data, response) => {
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


## orders1

> orders1(opts)

Orders

Orders

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.OrdersApi();
let opts = {
  '': "" // String | 
};
apiInstance.orders1(opts, (error, data, response) => {
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

- **Content-Type**: application/octet-stream
- **Accept**: Not defined

