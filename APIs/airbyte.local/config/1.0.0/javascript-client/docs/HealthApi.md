# AirbyteConfigurationApi.HealthApi

All URIs are relative to *http://airbyte.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHealthCheck**](HealthApi.md#getHealthCheck) | **GET** /v1/health | Health Check



## getHealthCheck

> HealthCheckRead getHealthCheck()

Health Check

### Example

```javascript
import AirbyteConfigurationApi from 'airbyte_configuration_api';

let apiInstance = new AirbyteConfigurationApi.HealthApi();
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

[**HealthCheckRead**](HealthCheckRead.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

