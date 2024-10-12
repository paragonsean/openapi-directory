# PeelTuneInApi.HealthApi

All URIs are relative to *http://hashtag.peel-ci.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHealth**](HealthApi.md#getHealth) | **GET** /health | Get health of Tune-in service (which includes its uptime).



## getHealth

> getHealth()

Get health of Tune-in service (which includes its uptime).

### Example

```javascript
import PeelTuneInApi from 'peel_tune_in_api';

let apiInstance = new PeelTuneInApi.HealthApi();
apiInstance.getHealth((error, data, response) => {
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

