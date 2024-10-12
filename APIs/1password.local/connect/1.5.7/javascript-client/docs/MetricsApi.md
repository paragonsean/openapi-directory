# 1PasswordConnect.MetricsApi

All URIs are relative to *http://1password.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPrometheusMetrics**](MetricsApi.md#getPrometheusMetrics) | **GET** /metrics | Query server for exposed Prometheus metrics



## getPrometheusMetrics

> String getPrometheusMetrics()

Query server for exposed Prometheus metrics

See Prometheus documentation for a complete data model.

### Example

```javascript
import 1PasswordConnect from '1_password_connect';

let apiInstance = new 1PasswordConnect.MetricsApi();
apiInstance.getPrometheusMetrics((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

