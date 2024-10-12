# TwilioApi.Api20100401HealthCheckApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchHealthCheck**](Api20100401HealthCheckApi.md#fetchHealthCheck) | **GET** /healthcheck | 



## fetchHealthCheck

> FetchHealthCheck200Response fetchHealthCheck()



API HealthCheck

### Example

```javascript
import TwilioApi from 'twilio_api';

let apiInstance = new TwilioApi.Api20100401HealthCheckApi();
apiInstance.fetchHealthCheck((error, data, response) => {
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

[**FetchHealthCheck200Response**](FetchHealthCheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

