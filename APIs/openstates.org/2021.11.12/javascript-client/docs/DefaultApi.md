# OpenStatesApiV3.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsMetricsGet**](DefaultApi.md#metricsMetricsGet) | **GET** /metrics | Metrics



## metricsMetricsGet

> Object metricsMetricsGet()

Metrics

Endpoint that serves Prometheus metrics.

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.DefaultApi();
apiInstance.metricsMetricsGet((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

