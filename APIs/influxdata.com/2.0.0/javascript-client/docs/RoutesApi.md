# InfluxOssApiService.RoutesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRoutes**](RoutesApi.md#getRoutes) | **GET** / | List all top level routes



## getRoutes

> Routes getRoutes(opts)

List all top level routes

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.RoutesApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getRoutes(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Routes**](Routes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

