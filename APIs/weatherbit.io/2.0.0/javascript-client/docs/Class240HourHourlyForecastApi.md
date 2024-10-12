# WeatherbitInteractiveSwaggerUiDocumentation.Class240HourHourlyForecastApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecastHourlycityIdcityIdGet**](Class240HourHourlyForecastApi.md#forecastHourlycityIdcityIdGet) | **GET** /forecast/hourly?city_id&#x3D;{city_id} | Returns an hourly forecast - Given a City ID.
[**forecastHourlycitycitycountrycountryGet**](Class240HourHourlyForecastApi.md#forecastHourlycitycitycountrycountryGet) | **GET** /forecast/hourly?city&#x3D;{city}&amp;country&#x3D;{country} | Returns an hourly forecast - Given City and/or State, Country.
[**forecastHourlylatlatlonlonGet**](Class240HourHourlyForecastApi.md#forecastHourlylatlatlonlonGet) | **GET** /forecast/hourly?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns an hourly forecast - Given a lat/lon.
[**forecastHourlypostalCodepostalCodeGet**](Class240HourHourlyForecastApi.md#forecastHourlypostalCodepostalCodeGet) | **GET** /forecast/hourly?postal_code&#x3D;{postal_code} | Returns an hourly forecast - Given a Postal Code.



## forecastHourlycityIdcityIdGet

> ForecastHourly forecastHourlycityIdcityIdGet(cityId, key, opts)

Returns an hourly forecast - Given a City ID.

 Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC.  

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.Class240HourHourlyForecastApi();
let cityId = 56; // Number | City ID. Example: 4487042
let key = "key_example"; // String | Your registered API key.
let opts = {
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example", // String | Wraps return in jsonp callback. Example - callback=func
  'hours': 56 // Number | Number of hours to return.
};
apiInstance.forecastHourlycityIdcityIdGet(cityId, key, opts, (error, data, response) => {
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
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] 
 **hours** | **Number**| Number of hours to return. | [optional] 

### Return type

[**ForecastHourly**](ForecastHourly.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forecastHourlycitycitycountrycountryGet

> ForecastHourly forecastHourlycitycitycountrycountryGet(city, country, key, opts)

Returns an hourly forecast - Given City and/or State, Country.

 Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. 

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.Class240HourHourlyForecastApi();
let city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
let country = "country_example"; // String | Country Code (2 letter).
let key = "key_example"; // String | Your registered API key.
let opts = {
  'state': "state_example", // String | Full name of state.
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example", // String | Wraps return in jsonp callback. Example: callback=func
  'hours': 56 // Number | Number of hours to return.
};
apiInstance.forecastHourlycitycitycountrycountryGet(city, country, key, opts, (error, data, response) => {
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
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 
 **hours** | **Number**| Number of hours to return. | [optional] 

### Return type

[**ForecastHourly**](ForecastHourly.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forecastHourlylatlatlonlonGet

> ForecastHourly forecastHourlylatlatlonlonGet(lat, lon, key, opts)

Returns an hourly forecast - Given a lat/lon.

Returns an hourly forecast, where each point represents a one hour period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC.  

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.Class240HourHourlyForecastApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let key = "key_example"; // String | Your registered API key.
let opts = {
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example", // String | Wraps return in jsonp callback. Example - callback=func
  'hours': 56 // Number | Number of hours to return.
};
apiInstance.forecastHourlylatlatlonlonGet(lat, lon, key, opts, (error, data, response) => {
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
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] 
 **hours** | **Number**| Number of hours to return. | [optional] 

### Return type

[**ForecastHourly**](ForecastHourly.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forecastHourlypostalCodepostalCodeGet

> ForecastHourly forecastHourlypostalCodepostalCodeGet(postalCode, key, opts)

Returns an hourly forecast - Given a Postal Code.

 Returns an hourly forecast, where each point represents a one hour   period. Every point has a datetime string in the format \&quot;YYYY-MM-DD:HH\&quot;. Time is UTC.  

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.Class240HourHourlyForecastApi();
let postalCode = 56; // Number | Postal Code. Example: 28546
let key = "key_example"; // String | Your registered API key.
let opts = {
  'country': "country_example", // String | Country Code (2 letter).
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example", // String | Wraps return in jsonp callback. Example - callback=func
  'hours': 56 // Number | Number of hours to return.
};
apiInstance.forecastHourlypostalCodepostalCodeGet(postalCode, key, opts, (error, data, response) => {
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
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] 
 **hours** | **Number**| Number of hours to return. | [optional] 

### Return type

[**ForecastHourly**](ForecastHourly.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

