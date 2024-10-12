# PendoFeedbackApi.SystemApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthCheckPingGet**](SystemApi.md#healthCheckPingGet) | **GET** /health-check/ping | Health check for API



## healthCheckPingGet

> healthCheckPingGet()

Health check for API

Provides a response for automatic checks that the API and load balancers are healthy

### Example

```javascript
import PendoFeedbackApi from 'pendo_feedback_api';

let apiInstance = new PendoFeedbackApi.SystemApi();
apiInstance.healthCheckPingGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

