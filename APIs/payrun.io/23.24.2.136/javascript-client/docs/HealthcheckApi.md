# PayRunIo.HealthcheckApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHealthCheck**](HealthcheckApi.md#getHealthCheck) | **GET** /Healthcheck | Get health check status



## getHealthCheck

> HealthCheck getHealthCheck()

Get health check status

Returns the health status of the application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HealthcheckApi();
apiInstance.getHealthCheck((error, data, response) => {
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

[**HealthCheck**](HealthCheck.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

