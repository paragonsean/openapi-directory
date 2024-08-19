# NeoWsNearEarthObjectWebService.StatsApi

All URIs are relative to *http://www.neowsapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieveCurrentNeoStatistics**](StatsApi.md#retrieveCurrentNeoStatistics) | **GET** /rest/v1/stats | Get the Near Earth Object data set totals



## retrieveCurrentNeoStatistics

> Statistics retrieveCurrentNeoStatistics()

Get the Near Earth Object data set totals

retrieveCurrentNeoStatistics

### Example

```javascript
import NeoWsNearEarthObjectWebService from 'neo_ws__near_earth_object_web_service';

let apiInstance = new NeoWsNearEarthObjectWebService.StatsApi();
apiInstance.retrieveCurrentNeoStatistics((error, data, response) => {
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

[**Statistics**](Statistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

