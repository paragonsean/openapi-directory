# ElmahIoApi.UptimeChecksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uptimeChecksGetAll**](UptimeChecksApi.md#uptimeChecksGetAll) | **GET** /v3/uptimechecks | Fetch a list of uptime checks. Currently in closed beta. Get in contact to get access to this endpoint.



## uptimeChecksGetAll

> [UptimeCheck] uptimeChecksGetAll()

Fetch a list of uptime checks. Currently in closed beta. Get in contact to get access to this endpoint.

Required permission: &#x60;uptimechecks_read&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.UptimeChecksApi();
apiInstance.uptimeChecksGetAll((error, data, response) => {
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

[**[UptimeCheck]**](UptimeCheck.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

