# HealthRepositoryProviderSpecificationsForHip.MonitoringApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05HeartbeatGet**](MonitoringApi.md#v05HeartbeatGet) | **GET** /v0.5/heartbeat | Get consent request status



## v05HeartbeatGet

> HeartbeatResponse v05HeartbeatGet()

Get consent request status

### Example

```javascript
import HealthRepositoryProviderSpecificationsForHip from 'health_repository_provider_specifications_for_hip';

let apiInstance = new HealthRepositoryProviderSpecificationsForHip.MonitoringApi();
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

