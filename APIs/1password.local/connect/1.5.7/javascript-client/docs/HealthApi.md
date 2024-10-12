# 1PasswordConnect.HealthApi

All URIs are relative to *http://1password.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHeartbeat**](HealthApi.md#getHeartbeat) | **GET** /heartbeat | Ping the server for liveness
[**getServerHealth**](HealthApi.md#getServerHealth) | **GET** /health | Get state of the server and its dependencies.



## getHeartbeat

> String getHeartbeat()

Ping the server for liveness

### Example

```javascript
import 1PasswordConnect from '1_password_connect';

let apiInstance = new 1PasswordConnect.HealthApi();
apiInstance.getHeartbeat((error, data, response) => {
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


## getServerHealth

> GetServerHealth200Response getServerHealth()

Get state of the server and its dependencies.

### Example

```javascript
import 1PasswordConnect from '1_password_connect';

let apiInstance = new 1PasswordConnect.HealthApi();
apiInstance.getServerHealth((error, data, response) => {
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

[**GetServerHealth200Response**](GetServerHealth200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

