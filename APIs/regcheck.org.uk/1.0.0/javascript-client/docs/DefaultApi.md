# CarRegistrationApi.DefaultApi

All URIs are relative to *https://regcheck.local/infiniteloopltd/CarRegistration/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check**](DefaultApi.md#check) | **GET** /Check | Gets details of a UK Vehicle



## check

> [Object] check(searchString)

Gets details of a UK Vehicle

Gets details of a UK Vehicle 

### Example

```javascript
import CarRegistrationApi from 'car_registration_api';

let apiInstance = new CarRegistrationApi.DefaultApi();
let searchString = "searchString_example"; // String | A registration number
apiInstance.check(searchString, (error, data, response) => {
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
 **searchString** | **String**| A registration number | 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

