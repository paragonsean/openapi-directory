# HealthDataConsentManager.MonitoringApi

All URIs are relative to *https://dev.ndhm.gov.in/cm*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05HeartbeatGet**](MonitoringApi.md#v05HeartbeatGet) | **GET** /v0.5/heartbeat | Get consent request status



## v05HeartbeatGet

> HeartbeatResponse v05HeartbeatGet()

Get consent request status

### Example

```javascript
import HealthDataConsentManager from 'health_data_consent_manager';

let apiInstance = new HealthDataConsentManager.MonitoringApi();
apiInstance.v05HeartbeatGet((error, data, response) => {
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

[**HeartbeatResponse**](HeartbeatResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

