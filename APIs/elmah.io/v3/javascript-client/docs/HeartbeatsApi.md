# ElmahIoApi.HeartbeatsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heartbeatsCreate**](HeartbeatsApi.md#heartbeatsCreate) | **POST** /v3/heartbeats/{logId}/{id} | Create a new heartbeat.



## heartbeatsCreate

> heartbeatsCreate(id, logId, opts)

Create a new heartbeat.

Required permission: &#x60;heartbeats_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.HeartbeatsApi();
let id = "id_example"; // String | The ID of the heartbeat check.
let logId = "logId_example"; // String | The ID of the log containing the heartbeat check.
let opts = {
  'createHeartbeat': new ElmahIoApi.CreateHeartbeat() // CreateHeartbeat | The details of the heartbeat.
};
apiInstance.heartbeatsCreate(id, logId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the heartbeat check. | 
 **logId** | **String**| The ID of the log containing the heartbeat check. | 
 **createHeartbeat** | [**CreateHeartbeat**](CreateHeartbeat.md)| The details of the heartbeat. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined

