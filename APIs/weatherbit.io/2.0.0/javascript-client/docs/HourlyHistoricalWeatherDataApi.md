# WeatherbitInteractiveSwaggerUiDocumentation.HourlyHistoricalWeatherDataApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**historyHourlycityIdcityIdGet**](HourlyHistoricalWeatherDataApi.md#historyHourlycityIdcityIdGet) | **GET** /history/hourly?city_id&#x3D;{city_id} | Returns Historical Observations - Given a City ID
[**historyHourlycitycitycountrycountryGet**](HourlyHistoricalWeatherDataApi.md#historyHourlycitycitycountrycountryGet) | **GET** /history/hourly?city&#x3D;{city}&amp;country&#x3D;{country} | Returns Historical Observations - Given City and/or State, Country.
[**historyHourlylatlatlonlonGet**](HourlyHistoricalWeatherDataApi.md#historyHourlylatlatlonlonGet) | **GET** /history/hourly?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns Historical Observations - Given a lat/lon.
[**historyHourlypostalCodepostalCodeGet**](HourlyHistoricalWeatherDataApi.md#historyHourlypostalCodepostalCodeGet) | **GET** /history/hourly?postal_code&#x3D;{postal_code} | Returns Historical Observations - Given a Postal Code
[**historyHourlystationstationGet**](HourlyHistoricalWeatherDataApi.md#historyHourlystationstationGet) | **GET** /history/hourly?station&#x3D;{station} | Returns Historical Observations - Given a station ID.



## historyHourlycityIdcityIdGet

> History historyHourlycityIdcityIdGet(cityId, startDate, endDate, key, opts)

Returns Historical Observations - Given a City ID

Returns Historical Observations - Given a City ID. **(LIMIT 31 days per request)**

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.HourlyHistoricalWeatherDataApi();
let cityId = "cityId_example"; // String | City ID. Example: 4487042
let startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH)
let endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH)
let key = "key_example"; // String | Your registered API key.
let opts = {
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'tz': "tz_example", // String | Assume utc (default) or local time for start_date, end_date
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.historyHourlycityIdcityIdGet(cityId, startDate, endDate, key, opts, (error, data, response) => {
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
 **cityId** | **String**| City ID. Example: 4487042 | 
 **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH) | 
 **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH) | 
 **key** | **String**| Your registered API key. | 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **tz** | **String**| Assume utc (default) or local time for start_date, end_date | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**History**](History.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historyHourlycitycitycountrycountryGet

> History historyHourlycitycitycountrycountryGet(city, country, startDate, endDate, key, opts)

Returns Historical Observations - Given City and/or State, Country.

Returns Historical Observations - Given a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. **(LIMIT 31 days per request)**

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.HourlyHistoricalWeatherDataApi();
let city = "city_example"; // String | City search. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
let country = "country_example"; // String | Country Code (2 letter).
let startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
let endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
let key = "key_example"; // String | Your registered API key.
let opts = {
  'state': "state_example", // String | Full name of state.
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'tz': "tz_example", // String | Assume utc (default) or local time for start_date, end_date
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.historyHourlycitycitycountrycountryGet(city, country, startDate, endDate, key, opts, (error, data, response) => {
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
 **city** | **String**| City search. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR | 
 **country** | **String**| Country Code (2 letter). | 
 **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). | 
 **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). | 
 **key** | **String**| Your registered API key. | 
 **state** | **String**| Full name of state. | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **tz** | **String**| Assume utc (default) or local time for start_date, end_date | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**History**](History.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historyHourlylatlatlonlonGet

> History historyHourlylatlatlonlonGet(lat, lon, startDate, endDate, key, opts)

Returns Historical Observations - Given a lat/lon.

Returns Historical Observations - Given a lat, and lon. **(LIMIT 31 days per request)**

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.HourlyHistoricalWeatherDataApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
let endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
let key = "key_example"; // String | Your registered API key.
let opts = {
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'tz': "tz_example", // String | Assume utc (default) or local time for start_date, end_date
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.historyHourlylatlatlonlonGet(lat, lon, startDate, endDate, key, opts, (error, data, response) => {
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
 **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). | 
 **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). | 
 **key** | **String**| Your registered API key. | 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **tz** | **String**| Assume utc (default) or local time for start_date, end_date | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**History**](History.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historyHourlypostalCodepostalCodeGet

> History historyHourlypostalCodepostalCodeGet(postalCode, startDate, endDate, key, opts)

Returns Historical Observations - Given a Postal Code

Returns Historical Observations - Given a Postal Code. **(LIMIT 31 days per request)**

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.HourlyHistoricalWeatherDataApi();
let postalCode = "postalCode_example"; // String | Postal Code. Example: 28546
let startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH)
let endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH)
let key = "key_example"; // String | Your registered API key.
let opts = {
  'country': "country_example", // String | Country Code (2 letter).
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'tz': "tz_example", // String | Assume utc (default) or local time for start_date, end_date
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.historyHourlypostalCodepostalCodeGet(postalCode, startDate, endDate, key, opts, (error, data, response) => {
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
 **postalCode** | **String**| Postal Code. Example: 28546 | 
 **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH) | 
 **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH) | 
 **key** | **String**| Your registered API key. | 
 **country** | **String**| Country Code (2 letter). | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **tz** | **String**| Assume utc (default) or local time for start_date, end_date | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**History**](History.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historyHourlystationstationGet

> History historyHourlystationstationGet(station, startDate, endDate, key, opts)

Returns Historical Observations - Given a station ID.

Returns Historical Observations - Given a station ID. **(LIMIT 31 days per request)**

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.HourlyHistoricalWeatherDataApi();
let station = "station_example"; // String | Station ID.
let startDate = "startDate_example"; // String | Start Date (YYYY-MM-DD or YYYY-MM-DD:HH).
let endDate = "endDate_example"; // String | End Date (YYYY-MM-DD or YYYY-MM-DD:HH).
let key = "key_example"; // String | Your registered API key.
let opts = {
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'tz': "tz_example", // String | Assume utc (default) or local time for start_date, end_date
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.historyHourlystationstationGet(station, startDate, endDate, key, opts, (error, data, response) => {
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
 **station** | **String**| Station ID. | 
 **startDate** | **String**| Start Date (YYYY-MM-DD or YYYY-MM-DD:HH). | 
 **endDate** | **String**| End Date (YYYY-MM-DD or YYYY-MM-DD:HH). | 
 **key** | **String**| Your registered API key. | 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **tz** | **String**| Assume utc (default) or local time for start_date, end_date | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**History**](History.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

