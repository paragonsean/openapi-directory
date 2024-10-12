# PlatformApi.StatsApi

All URIs are relative to *https://rest.ably.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStats**](StatsApi.md#getStats) | **GET** /stats | Retrieve usage statistics for an application
[**getTime**](StatsApi.md#getTime) | **GET** /time | Get the service time



## getStats

> Object getStats(opts)

Retrieve usage statistics for an application

The Ably system can be queried to obtain usage statistics for a given application, and results are provided aggregated across all channels in use in the application in the specified period. Stats may be used to track usage against account quotas.

### Example

```javascript
import PlatformApi from 'platform_api';
let defaultClient = PlatformApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PlatformApi.StatsApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example", // String | The response format you would like
  'start': "start_example", // String | 
  'limit': 56, // Number | 
  'end': "'now'", // String | 
  'direction': "'backwards'", // String | 
  'unit': "'minute'" // String | Specifies the unit of aggregation in the returned results.
};
apiInstance.getStats(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 
 **start** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 
 **end** | **String**|  | [optional] [default to &#39;now&#39;]
 **direction** | **String**|  | [optional] [default to &#39;backwards&#39;]
 **unit** | **String**| Specifies the unit of aggregation in the returned results. | [optional] [default to &#39;minute&#39;]

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html


## getTime

> [Number] getTime(opts)

Get the service time

This returns the service time in milliseconds since the epoch.

### Example

```javascript
import PlatformApi from 'platform_api';

let apiInstance = new PlatformApi.StatsApi();
let opts = {
  'xAblyVersion': "xAblyVersion_example", // String | The version of the API you wish to use.
  'format': "format_example" // String | The response format you would like
};
apiInstance.getTime(opts, (error, data, response) => {
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
 **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] 
 **format** | **String**| The response format you would like | [optional] 

### Return type

**[Number]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/x-msgpack, text/html

