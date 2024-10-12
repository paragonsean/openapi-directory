# HandwryttenApi.FontsApi

All URIs are relative to *https://api.handwrytten.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fontsList**](FontsApi.md#fontsList) | **GET** /fonts/list | Lists Handwryting styles available for use



## fontsList

> [Font] fontsList()

Lists Handwryting styles available for use

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.FontsApi();
apiInstance.fontsList((error, data, response) => {
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

[**[Font]**](Font.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

