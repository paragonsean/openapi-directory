# GroovViewPublicApi.LoggingApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadLogJson**](LoggingApi.md#downloadLogJson) | **GET** /v1/logging/groovLogs.json | 
[**downloadLogText**](LoggingApi.md#downloadLogText) | **GET** /v1/logging/groovLogs.txt | 



## downloadLogJson

> File downloadLogJson(opts)



Downloads the complete groov View log in JSON format. Added in groov View R4.2a.

### Example

```javascript
import GroovViewPublicApi from 'groov_view_public_api';
let defaultClient = GroovViewPublicApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GroovViewPublicApi.LoggingApi();
let opts = {
  'minimumLogLevel': "'INFO'", // String | How verbose the log should be.
  'lastTimestamp': 0.0, // Number | The earliest time to include in the log. Value is milliseconds since January 1, 1970 UTC.
  'filter': "filter_example" // String | Optional string to search for in the log.
};
apiInstance.downloadLogJson(opts, (error, data, response) => {
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
 **minimumLogLevel** | **String**| How verbose the log should be. | [optional] [default to &#39;INFO&#39;]
 **lastTimestamp** | **Number**| The earliest time to include in the log. Value is milliseconds since January 1, 1970 UTC. | [optional] [default to 0.0]
 **filter** | **String**| Optional string to search for in the log. | [optional] 

### Return type

**File**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## downloadLogText

> File downloadLogText(opts)



Downloads the complete groov View log. Added in groov View R4.2a.

### Example

```javascript
import GroovViewPublicApi from 'groov_view_public_api';
let defaultClient = GroovViewPublicApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GroovViewPublicApi.LoggingApi();
let opts = {
  'minimumLogLevel': "'INFO'", // String | How verbose the log should be.
  'lastTimestamp': 0.0, // Number | The earliest time to include in the log. Value is milliseconds since January 1, 1970 UTC.
  'filter': "filter_example" // String | Optional string to search for in the log.
};
apiInstance.downloadLogText(opts, (error, data, response) => {
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
 **minimumLogLevel** | **String**| How verbose the log should be. | [optional] [default to &#39;INFO&#39;]
 **lastTimestamp** | **Number**| The earliest time to include in the log. Value is milliseconds since January 1, 1970 UTC. | [optional] [default to 0.0]
 **filter** | **String**| Optional string to search for in the log. | [optional] 

### Return type

**File**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

