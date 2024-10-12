# Balldontlie.StatsApi

All URIs are relative to *https://balldontlie.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allStatsExampleParameters**](StatsApi.md#allStatsExampleParameters) | **GET** /api/v1/stats | all stats (example parameters)



## allStatsExampleParameters

> allStatsExampleParameters(opts)

all stats (example parameters)

all stats (example parameters)

### Example

```javascript
import Balldontlie from 'balldontlie';

let apiInstance = new Balldontlie.StatsApi();
let opts = {
  'season': "2018", // String | 
  'playerIds': "237" // String | 
};
apiInstance.allStatsExampleParameters(opts, (error, data, response) => {
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
 **season** | **String**|  | [optional] 
 **playerIds** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

