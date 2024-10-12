# RequestBasketsApi.ServiceApi

All URIs are relative to *https://rbaskets.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiVersionGet**](ServiceApi.md#apiVersionGet) | **GET** /api/version | Get service version



## apiVersionGet

> Version apiVersionGet()

Get service version

Get service version.

### Example

```javascript
import RequestBasketsApi from 'request_baskets_api';

let apiInstance = new RequestBasketsApi.ServiceApi();
apiInstance.apiVersionGet((error, data, response) => {
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

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

