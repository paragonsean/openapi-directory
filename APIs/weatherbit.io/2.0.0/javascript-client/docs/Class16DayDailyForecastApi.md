# WeatherbitInteractiveSwaggerUiDocumentation.Class16DayDailyForecastApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecastDailycityIdcityIdGet**](Class16DayDailyForecastApi.md#forecastDailycityIdcityIdGet) | **GET** /forecast/daily?city_id&#x3D;{city_id} | Returns a daily forecast - Given a City ID.
[**forecastDailycitycitycountrycountryGet**](Class16DayDailyForecastApi.md#forecastDailycitycitycountrycountryGet) | **GET** /forecast/daily?city&#x3D;{city}&amp;country&#x3D;{country} | Returns a daily forecast - Given City and/or State, Country.
[**forecastDailylatlatlonlonGet**](Class16DayDailyForecastApi.md#forecastDailylatlatlonlonGet) | **GET** /forecast/daily?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns a daily forecast - Given Lat/Lon.
[**forecastDailypostalCodepostalCodeGet**](Class16DayDailyForecastApi.md#forecastDailypostalCodepostalCodeGet) | **GET** /forecast/daily?postal_code&#x3D;{postal_code} | Returns a daily forecast - Given a Postal Code.



## forecastDailycityIdcityIdGet

> ForecastDay forecastDailycityIdcityIdGet(cityId, key, opts)

Returns a daily forecast - Given a City ID.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC. 

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.Class16DayDailyForecastApi();
let cityId = 56; // Number | City ID. Example: 4487042
let key = "key_example"; // String | Your registered API key.
let opts = {
  'days': 3.4, // Number | Number of days to return. Default 16.
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.forecastDailycityIdcityIdGet(cityId, key, opts, (error, data, response) => {
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
 **cityId** | **Number**| City ID. Example: 4487042 | 
 **key** | **String**| Your registered API key. | 
 **days** | **Number**| Number of days to return. Default 16. | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**ForecastDay**](ForecastDay.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forecastDailycitycitycountrycountryGet

> ForecastDay forecastDailycitycitycountrycountryGet(city, country, key, opts)

Returns a daily forecast - Given City and/or State, Country.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. 

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.Class16DayDailyForecastApi();
let city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
let country = "country_example"; // String | Country Code (2 letter).
let key = "key_example"; // String | Your registered API key.
let opts = {
  'state': "state_example", // String | Full name of state.
  'days': 3.4, // Number | Number of days to return. Default 16.
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example - callback=func
};
apiInstance.forecastDailycitycitycountrycountryGet(city, country, key, opts, (error, data, response) => {
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
 **city** | **String**| City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR | 
 **country** | **String**| Country Code (2 letter). | 
 **key** | **String**| Your registered API key. | 
 **state** | **String**| Full name of state. | [optional] 
 **days** | **Number**| Number of days to return. Default 16. | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] 

### Return type

[**ForecastDay**](ForecastDay.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forecastDailylatlatlonlonGet

> ForecastDay forecastDailylatlatlonlonGet(lat, lon, key, opts)

Returns a daily forecast - Given Lat/Lon.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC.  

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.Class16DayDailyForecastApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let key = "key_example"; // String | Your registered API key.
let opts = {
  'days': 3.4, // Number | Number of days to return. Default 16.
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.forecastDailylatlatlonlonGet(lat, lon, key, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude component of location. | 
 **lon** | **Number**| Longitude component of location. | 
 **key** | **String**| Your registered API key. | 
 **days** | **Number**| Number of days to return. Default 16. | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**ForecastDay**](ForecastDay.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forecastDailypostalCodepostalCodeGet

> ForecastDay forecastDailypostalCodepostalCodeGet(postalCode, key, opts)

Returns a daily forecast - Given a Postal Code.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \&quot;YYYY-MM-DD\&quot;. One day begins at 00:00 UTC, and ends at 23:59 UTC. 

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.Class16DayDailyForecastApi();
let postalCode = 56; // Number | Postal Code. Example: 28546
let key = "key_example"; // String | Your registered API key.
let opts = {
  'country': "country_example", // String | Country Code (2 letter).
  'days': 3.4, // Number | Number of days to return. Default 16.
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.forecastDailypostalCodepostalCodeGet(postalCode, key, opts, (error, data, response) => {
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
 **postalCode** | **Number**| Postal Code. Example: 28546 | 
 **key** | **String**| Your registered API key. | 
 **country** | **String**| Country Code (2 letter). | [optional] 
 **days** | **Number**| Number of days to return. Default 16. | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**ForecastDay**](ForecastDay.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

