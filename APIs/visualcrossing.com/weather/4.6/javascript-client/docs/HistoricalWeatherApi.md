# VisualCrossingWeatherApi.HistoricalWeatherApi

All URIs are relative to *https://weather.visualcrossing.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**visualCrossingWebServicesRestServicesWeatherdataHistoryGet**](HistoricalWeatherApi.md#visualCrossingWebServicesRestServicesWeatherdataHistoryGet) | **GET** /VisualCrossingWebServices/rest/services/weatherdata/history | Retrieves hourly or daily historical weather records.



## visualCrossingWebServicesRestServicesWeatherdataHistoryGet

> visualCrossingWebServicesRestServicesWeatherdataHistoryGet(opts)

Retrieves hourly or daily historical weather records.

The weather history data is suitable for retrieving hourly or daily historical weather records.

### Example

```javascript
import VisualCrossingWeatherApi from 'visual_crossing_weather_api';

let apiInstance = new VisualCrossingWeatherApi.HistoricalWeatherApi();
let opts = {
  'maxDistance': "-1", // String | 
  'shortColumnNames': false, // Boolean | 
  'endDateTime': "2020-02-04T00%3A00%3A00", // String | 
  'aggregateHours': "24", // String | 
  'collectStationContributions': false, // Boolean | 
  'startDateTime': "2020-01-28T00%3A00%3A00", // String | 
  'maxStations': "-1", // String | 
  'allowAsynch': false, // Boolean | 
  'locations': "Sterling%2C%20VA%2C%20US", // String | 
  'includeNormals': false, // Boolean | 
  'contentType': "json", // String | 
  'unitGroup': "us", // String | 
  'key': "INSERT_YOUR_KEY" // String | 
};
apiInstance.visualCrossingWebServicesRestServicesWeatherdataHistoryGet(opts, (error, data, response) => {
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
 **maxDistance** | **String**|  | [optional] 
 **shortColumnNames** | **Boolean**|  | [optional] 
 **endDateTime** | **String**|  | [optional] 
 **aggregateHours** | **String**|  | [optional] 
 **collectStationContributions** | **Boolean**|  | [optional] 
 **startDateTime** | **String**|  | [optional] 
 **maxStations** | **String**|  | [optional] 
 **allowAsynch** | **Boolean**|  | [optional] 
 **locations** | **String**|  | [optional] 
 **includeNormals** | **Boolean**|  | [optional] 
 **contentType** | **String**|  | [optional] 
 **unitGroup** | **String**|  | [optional] 
 **key** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

