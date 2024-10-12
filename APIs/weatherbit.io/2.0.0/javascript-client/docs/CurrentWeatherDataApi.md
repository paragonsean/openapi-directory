# WeatherbitInteractiveSwaggerUiDocumentation.CurrentWeatherDataApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currentcitiescitiesGet**](CurrentWeatherDataApi.md#currentcitiescitiesGet) | **GET** /current?cities&#x3D;{cities} | Returns a group of observations given a list of cities
[**currentcityIdcityIdGet**](CurrentWeatherDataApi.md#currentcityIdcityIdGet) | **GET** /current?city_id&#x3D;{city_id} | Returns a current observation by city id.
[**currentcitycitycountrycountryGet**](CurrentWeatherDataApi.md#currentcitycitycountrycountryGet) | **GET** /current?city&#x3D;{city}&amp;country&#x3D;{country} | Returns a Current Observation - Given City and/or State, Country.
[**currentlatlatlonlonGet**](CurrentWeatherDataApi.md#currentlatlatlonlonGet) | **GET** /current?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns a Current Observation - Given a lat/lon.
[**currentpointspointsGet**](CurrentWeatherDataApi.md#currentpointspointsGet) | **GET** /current?points&#x3D;{points} | Returns a group of observations given a list of points in the format (lat1, lon1), (lat2, lon2), (latN, lonN), ...
[**currentpostalCodepostalCodeGet**](CurrentWeatherDataApi.md#currentpostalCodepostalCodeGet) | **GET** /current?postal_code&#x3D;{postal_code} | Returns a current observation by postal code.
[**currentstationsstationsGet**](CurrentWeatherDataApi.md#currentstationsstationsGet) | **GET** /current?stations&#x3D;{stations} | Returns a group of observations given a list of stations
[**currentstationstationGet**](CurrentWeatherDataApi.md#currentstationstationGet) | **GET** /current?station&#x3D;{station} | Returns a Current Observation. - Given a station ID.



## currentcitiescitiesGet

> CurrentObsGroup currentcitiescitiesGet(cities, key, opts)

Returns a group of observations given a list of cities

Returns a group of Current Observations - Given a list of City IDs. 

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentWeatherDataApi();
let cities = "cities_example"; // String | Comma separated list of City ID's. Example: 4487042, 4494942, 4504871
let key = "key_example"; // String | Your registered API key.
let opts = {
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'marine': "marine_example", // String | Marine stations only (buoys, oil platforms, etc)
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback - Example - callback=func
};
apiInstance.currentcitiescitiesGet(cities, key, opts, (error, data, response) => {
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
 **cities** | **String**| Comma separated list of City ID&#39;s. Example: 4487042, 4494942, 4504871 | 
 **key** | **String**| Your registered API key. | 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **marine** | **String**| Marine stations only (buoys, oil platforms, etc) | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] 

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentcityIdcityIdGet

> CurrentObsGroup currentcityIdcityIdGet(cityId, key, opts)

Returns a current observation by city id.

Returns current weather observation - Given a City ID. 

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentWeatherDataApi();
let cityId = "cityId_example"; // String | City ID. Example: 4487042
let key = "key_example"; // String | Your registered API key.
let opts = {
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'include': "include_example", // String | Include 1 hour - minutely forecast in the response
  'marine': "marine_example", // String | Marine stations only (buoys, oil platforms, etc)
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback - Example - callback=func
};
apiInstance.currentcityIdcityIdGet(cityId, key, opts, (error, data, response) => {
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
 **key** | **String**| Your registered API key. | 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **include** | **String**| Include 1 hour - minutely forecast in the response | [optional] 
 **marine** | **String**| Marine stations only (buoys, oil platforms, etc) | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] 

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentcitycitycountrycountryGet

> CurrentObsGroup currentcitycitycountrycountryGet(city, country, key, opts)

Returns a Current Observation - Given City and/or State, Country.

Returns a Current Observation - Given a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentWeatherDataApi();
let city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
let country = "country_example"; // String | Country Code (2 letter).
let key = "key_example"; // String | Your registered API key.
let opts = {
  'include': "include_example", // String | Include 1 hour - minutely forecast in the response
  'state': "state_example", // String | Full name of state.
  'marine': "marine_example", // String | Marine stations only (buoys, oil platforms, etc)
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback - Example - callback=func
};
apiInstance.currentcitycitycountrycountryGet(city, country, key, opts, (error, data, response) => {
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
 **include** | **String**| Include 1 hour - minutely forecast in the response | [optional] 
 **state** | **String**| Full name of state. | [optional] 
 **marine** | **String**| Marine stations only (buoys, oil platforms, etc) | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] 

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentlatlatlonlonGet

> CurrentObsGroup currentlatlatlonlonGet(lat, lon, key, opts)

Returns a Current Observation - Given a lat/lon.

Returns a Current Observation - given a lat, and a lon.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentWeatherDataApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let key = "key_example"; // String | Your registered API key.
let opts = {
  'include': "include_example", // String | Include 1 hour - minutely forecast in the response
  'marine': "marine_example", // String | Marine stations only (buoys, oil platforms, etc)
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback - Example - callback=func
};
apiInstance.currentlatlatlonlonGet(lat, lon, key, opts, (error, data, response) => {
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
 **include** | **String**| Include 1 hour - minutely forecast in the response | [optional] 
 **marine** | **String**| Marine stations only (buoys, oil platforms, etc) | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] 

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentpointspointsGet

> CurrentObsGroup currentpointspointsGet(points, key, opts)

Returns a group of observations given a list of points in the format (lat1, lon1), (lat2, lon2), (latN, lonN), ...

Returns a group of Current Observations - Given a list of points (lat1, lon1), (lat2, lon2), (latN, lonN), ...

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentWeatherDataApi();
let points = "points_example"; // String | Comma separated list of points. Example: (35.5, -75.5),(45, 65),(45.12, -130.5)
let key = "key_example"; // String | Your registered API key.
let opts = {
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.currentpointspointsGet(points, key, opts, (error, data, response) => {
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
 **points** | **String**| Comma separated list of points. Example: (35.5, -75.5),(45, 65),(45.12, -130.5) | 
 **key** | **String**| Your registered API key. | 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentpostalCodepostalCodeGet

> CurrentObsGroup currentpostalCodepostalCodeGet(postalCode, key, opts)

Returns a current observation by postal code.

Returns current weather observation - Given a Postal Code. 

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentWeatherDataApi();
let postalCode = "postalCode_example"; // String | Postal Code. Example: 28546
let key = "key_example"; // String | Your registered API key.
let opts = {
  'country': "country_example", // String | Country Code (2 letter).
  'include': "include_example", // String | Include 1 hour - minutely forecast in the response
  'marine': "marine_example", // String | Marine stations only (buoys, oil platforms, etc)
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback - Example - callback=func
};
apiInstance.currentpostalCodepostalCodeGet(postalCode, key, opts, (error, data, response) => {
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
 **key** | **String**| Your registered API key. | 
 **country** | **String**| Country Code (2 letter). | [optional] 
 **include** | **String**| Include 1 hour - minutely forecast in the response | [optional] 
 **marine** | **String**| Marine stations only (buoys, oil platforms, etc) | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional] 

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentstationsstationsGet

> CurrentObsGroup currentstationsstationsGet(stations, key, opts)

Returns a group of observations given a list of stations

Returns a group of Current Observations - Given a list of Station Call IDs. 

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentWeatherDataApi();
let stations = "stations_example"; // String | Comma separated list of Station Call ID's. Example: KRDU,KBFI,KVNY
let key = "key_example"; // String | Your registered API key.
let opts = {
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.currentstationsstationsGet(stations, key, opts, (error, data, response) => {
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
 **stations** | **String**| Comma separated list of Station Call ID&#39;s. Example: KRDU,KBFI,KVNY | 
 **key** | **String**| Your registered API key. | 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentstationstationGet

> CurrentObsGroup currentstationstationGet(station, key, opts)

Returns a Current Observation. - Given a station ID.

Returns a Current Observation - Given a station ID.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentWeatherDataApi();
let station = "station_example"; // String | Station Call ID.
let key = "key_example"; // String | Your registered API key.
let opts = {
  'include': "include_example", // String | Include 1 hour - minutely forecast in the response
  'units': "units_example", // String | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a>
  'lang': "lang_example", // String | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a>
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.currentstationstationGet(station, key, opts, (error, data, response) => {
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
 **station** | **String**| Station Call ID. | 
 **key** | **String**| Your registered API key. | 
 **include** | **String**| Include 1 hour - minutely forecast in the response | [optional] 
 **units** | **String**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional] 
 **lang** | **String**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional] 
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

