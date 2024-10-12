# UpApi.UtilityEndpointsApi

All URIs are relative to *https://api.up.com.au/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**utilPingGet**](UtilityEndpointsApi.md#utilPingGet) | **GET** /util/ping | Ping



## utilPingGet

> PingResponse utilPingGet()

Ping

Make a basic ping request to the API. This is useful to verify that authentication is functioning correctly. On authentication success an HTTP &#x60;200&#x60; status is returned. On failure an HTTP &#x60;401&#x60; error response is returned. 

### Example

```javascript
import UpApi from 'up_api';
let defaultClient = UpApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new UpApi.UtilityEndpointsApi();
apiInstance.utilPingGet((error, data, response) => {
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

[**PingResponse**](PingResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

