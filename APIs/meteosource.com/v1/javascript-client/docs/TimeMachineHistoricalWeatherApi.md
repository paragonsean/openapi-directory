# InteractiveDocumentationForYourPremiumPlan.TimeMachineHistoricalWeatherApi

All URIs are relative to */api/v1/premium*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeMachineTimeMachineGet**](TimeMachineHistoricalWeatherApi.md#timeMachineTimeMachineGet) | **GET** /time_machine | Returns weather data for a single location and given day in the past



## timeMachineTimeMachineGet

> TimeMachineTimeMachine timeMachineTimeMachineGet(date, opts)

Returns weather data for a single location and given day in the past

## Actual weather data for a single location and day in the past  The output contains actual weather data for each day up to 20 years in the past, and long-term statistics of selected weather variables aggregated over 40 years.  ### Location specification The location of the weather data must be specified. There are two ways to do this: 1. Specify the GPS coordinates of the location using the parameters &#x60;lat&#x60; and &#x60;lon&#x60;. 2. **OR** specify the name of the place using the parameter &#x60;place_id&#x60;. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name).  *Note: For mountains, it is usually better to specify the &#x60;place_id&#x60; rather than the &#x60;lat&#x60; and &#x60;lon&#x60;. When you use &#x60;place_id&#x60;, you are guaranteed to receive data for the precise elevation of the peak. When you specify the coordinates, the elevation can be less precise.*

### Example

```javascript
import InteractiveDocumentationForYourPremiumPlan from 'interactive_documentation_for_your_premium_plan';
let defaultClient = InteractiveDocumentationForYourPremiumPlan.ApiClient.instance;
// Configure API key authorization: APIKeyHeader
let APIKeyHeader = defaultClient.authentications['APIKeyHeader'];
APIKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new InteractiveDocumentationForYourPremiumPlan.TimeMachineHistoricalWeatherApi();
let date = new Date("2013-10-20"); // Date | The day of the data in the past. Specify in `YYYY-MM-DD` format, e.g. `2021-08-24`. 
let opts = {
  'placeId': "placeId_example", // String | Identifier of a place. To obtain the `place_id` for the location you want, please use endpoints `/find_places_prefix` (search by prefix) or `/find_places` (search by full name).
  'lat': "lat_example", // String | Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4
  'lon': "lon_example", // String | Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4
  'timezone': "timezone_example", // String | Timezone to be used for the date fields. If not specified, local timezone of the location will be used. The format is according to the tzinfo database, so values like `Europe/Prague` or `UTC` can be used. Alternatively you may use the value ``auto`` in which case the local timezone of the location is used. The full list of valid timezone strings can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). 
  'units': new InteractiveDocumentationForYourPremiumPlan.Units(), // Units | Unit system to be used. The available values are:  * `auto`: Select the system automatically, based on the forecast location. * `metric`: Metric (SI) units (`°C`, `mm/h`, `m/s`, `cm`, `km`, `hPa`). * `us`: Imperial units (`°F`, `in/h`, `mph`, `in`, `mi`, `Hg`). * `uk`: Same as ``metric``, except that visibility is in `miles` and wind speeds are in `mph`. * `ca`: Same as ``metric``, except that wind speeds are in `km/h` and pressure is in `kPa`. 
  'key': "key_example" // String | Your unique API key. You can either specify it in this parameter, or set it in `X-API-Key` header.
};
apiInstance.timeMachineTimeMachineGet(date, opts, (error, data, response) => {
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
 **date** | **Date**| The day of the data in the past. Specify in &#x60;YYYY-MM-DD&#x60; format, e.g. &#x60;2021-08-24&#x60;.  | 
 **placeId** | **String**| Identifier of a place. To obtain the &#x60;place_id&#x60; for the location you want, please use endpoints &#x60;/find_places_prefix&#x60; (search by prefix) or &#x60;/find_places&#x60; (search by full name). | [optional] 
 **lat** | **String**| Latitude in format 12N, 12.3N, 12.3, or 13S, 13.2S, -13.4 | [optional] 
 **lon** | **String**| Longitude in format 12E, 12.3E, 12.3, or 13W, 13.2W, -13.4 | [optional] 
 **timezone** | **String**| Timezone to be used for the date fields. If not specified, local timezone of the location will be used. The format is according to the tzinfo database, so values like &#x60;Europe/Prague&#x60; or &#x60;UTC&#x60; can be used. Alternatively you may use the value &#x60;&#x60;auto&#x60;&#x60; in which case the local timezone of the location is used. The full list of valid timezone strings can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).  | [optional] 
 **units** | [**Units**](.md)| Unit system to be used. The available values are:  * &#x60;auto&#x60;: Select the system automatically, based on the forecast location. * &#x60;metric&#x60;: Metric (SI) units (&#x60;°C&#x60;, &#x60;mm/h&#x60;, &#x60;m/s&#x60;, &#x60;cm&#x60;, &#x60;km&#x60;, &#x60;hPa&#x60;). * &#x60;us&#x60;: Imperial units (&#x60;°F&#x60;, &#x60;in/h&#x60;, &#x60;mph&#x60;, &#x60;in&#x60;, &#x60;mi&#x60;, &#x60;Hg&#x60;). * &#x60;uk&#x60;: Same as &#x60;&#x60;metric&#x60;&#x60;, except that visibility is in &#x60;miles&#x60; and wind speeds are in &#x60;mph&#x60;. * &#x60;ca&#x60;: Same as &#x60;&#x60;metric&#x60;&#x60;, except that wind speeds are in &#x60;km/h&#x60; and pressure is in &#x60;kPa&#x60;.  | [optional] 
 **key** | **String**| Your unique API key. You can either specify it in this parameter, or set it in &#x60;X-API-Key&#x60; header. | [optional] 

### Return type

[**TimeMachineTimeMachine**](TimeMachineTimeMachine.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

