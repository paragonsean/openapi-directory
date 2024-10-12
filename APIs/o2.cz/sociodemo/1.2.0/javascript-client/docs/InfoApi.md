# SocioDemoApi.InfoApi

All URIs are relative to *https://developer.o2.cz/sociodemo/sandbox/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInfo**](InfoApi.md#getInfo) | **GET** /info | Information about versions of application and data.



## getInfo

> InfoResult getInfo()

Information about versions of application and data.

### Example

```javascript
import SocioDemoApi from 'socio_demo_api';

let apiInstance = new SocioDemoApi.InfoApi();
apiInstance.getInfo((error, data, response) => {
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

[**InfoResult**](InfoResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

