# Mailscript.DaemonApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDaemonToken**](DaemonApi.md#getDaemonToken) | **GET** /daemons/{daemon}/token | Get a token for opening a daemon connection



## getDaemonToken

> GetDaemonToken200Response getDaemonToken(daemon)

Get a token for opening a daemon connection

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.DaemonApi();
let daemon = "daemon_example"; // String | name of Daemon
apiInstance.getDaemonToken(daemon, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **daemon** | **String**| name of Daemon | 

### Return type

[**GetDaemonToken200Response**](GetDaemonToken200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

