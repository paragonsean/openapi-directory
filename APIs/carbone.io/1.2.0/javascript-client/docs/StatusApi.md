# CarboneApi.StatusApi

All URIs are relative to *https://api.carbone.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statusGet**](StatusApi.md#statusGet) | **GET** /status | Fetch the API status and version



## statusGet

> StatusGet200Response statusGet()

Fetch the API status and version

### Example

```javascript
import CarboneApi from 'carbone_api';

let apiInstance = new CarboneApi.StatusApi();
apiInstance.statusGet((error, data, response) => {
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

[**StatusGet200Response**](StatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

