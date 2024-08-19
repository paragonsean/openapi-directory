# WeatherbitInteractiveSwaggerUiDocumentation.AirQualityForecastApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecastAirqualitycityIdcityIdGet**](AirQualityForecastApi.md#forecastAirqualitycityIdcityIdGet) | **GET** /forecast/airquality?city_id&#x3D;{city_id} | Returns 72 hour (hourly) Air Quality forecast - Given a City ID.
[**forecastAirqualitycitycitycountrycountryGet**](AirQualityForecastApi.md#forecastAirqualitycitycitycountrycountryGet) | **GET** /forecast/airquality?city&#x3D;{city}&amp;country&#x3D;{country} | Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country.
[**forecastAirqualitylatlatlonlonGet**](AirQualityForecastApi.md#forecastAirqualitylatlatlonlonGet) | **GET** /forecast/airquality?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon.
[**forecastAirqualitypostalCodepostalCodeGet**](AirQualityForecastApi.md#forecastAirqualitypostalCodepostalCodeGet) | **GET** /forecast/airquality?postal_code&#x3D;{postal_code} | Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code.



## forecastAirqualitycityIdcityIdGet

> AQHourly forecastAirqualitycityIdcityIdGet(cityId, key, opts)

Returns 72 hour (hourly) Air Quality forecast - Given a City ID.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.AirQualityForecastApi();
let cityId = 56; // Number | City ID. Example: 4487042
let key = "key_example"; // String | Your registered API key.
let opts = {
  'callback': "callback_example", // String | Wraps return in jsonp callback. Example - callback=func
  'hours': 56 // Number | Number of hours to return.
};
apiInstance.forecastAirqualitycityIdcityIdGet(cityId, key, opts, (error, data, response) => {
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
 **callback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] 
 **hours** | **Number**| Number of hours to return. | [optional] 

### Return type

[**AQHourly**](AQHourly.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forecastAirqualitycitycitycountrycountryGet

> AQHourly forecastAirqualitycitycitycountrycountryGet(city, country, key, opts)

Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.AirQualityForecastApi();
let city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
let country = "country_example"; // String | Country Code (2 letter).
let key = "key_example"; // String | Your registered API key.
let opts = {
  'state': "state_example", // String | Full name of state.
  'callback': "callback_example", // String | Wraps return in jsonp callback. Example: callback=func
  'hours': 56 // Number | Number of hours to return.
};
apiInstance.forecastAirqualitycitycitycountrycountryGet(city, country, key, opts, (error, data, response) => {
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
 **callback** | **String**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional] 
 **hours** | **Number**| Number of hours to return. | [optional] 

### Return type

[**AQHourly**](AQHourly.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forecastAirqualitylatlatlonlonGet

> AQHourly forecastAirqualitylatlatlonlonGet(lat, lon, key, opts)

Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.AirQualityForecastApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let key = "key_example"; // String | Your registered API key.
let opts = {
  'callback': "callback_example", // String | Wraps return in jsonp callback. Example - callback=func
  'hours': 56 // Number | Number of hours to return.
};
apiInstance.forecastAirqualitylatlatlonlonGet(lat, lon, key, opts, (error, data, response) => {
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
 **callback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] 
 **hours** | **Number**| Number of hours to return. | [optional] 

### Return type

[**AQHourly**](AQHourly.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## forecastAirqualitypostalCodepostalCodeGet

> AQHourly forecastAirqualitypostalCodepostalCodeGet(postalCode, key, opts)

Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code.

Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.AirQualityForecastApi();
let postalCode = 56; // Number | Postal Code. Example: 28546
let key = "key_example"; // String | Your registered API key.
let opts = {
  'country': "country_example", // String | Country Code (2 letter).
  'callback': "callback_example", // String | Wraps return in jsonp callback. Example - callback=func
  'hours': 56 // Number | Number of hours to return.
};
apiInstance.forecastAirqualitypostalCodepostalCodeGet(postalCode, key, opts, (error, data, response) => {
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
 **callback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] 
 **hours** | **Number**| Number of hours to return. | [optional] 

### Return type

[**AQHourly**](AQHourly.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

