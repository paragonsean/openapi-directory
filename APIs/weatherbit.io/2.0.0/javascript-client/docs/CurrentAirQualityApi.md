# WeatherbitInteractiveSwaggerUiDocumentation.CurrentAirQualityApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currentAirqualitycityIdcityIdGet**](CurrentAirQualityApi.md#currentAirqualitycityIdcityIdGet) | **GET** /current/airquality?city_id&#x3D;{city_id} | Returns current air quality conditions - Given a City ID.
[**currentAirqualitycitycitycountrycountryGet**](CurrentAirQualityApi.md#currentAirqualitycitycitycountrycountryGet) | **GET** /current/airquality?city&#x3D;{city}&amp;country&#x3D;{country} | Returns current air quality conditions - Given City and/or State, Country.
[**currentAirqualitylatlatlonlonGet**](CurrentAirQualityApi.md#currentAirqualitylatlatlonlonGet) | **GET** /current/airquality?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns current air quality conditions - Given a lat/lon.
[**currentAirqualitypostalCodepostalCodeGet**](CurrentAirQualityApi.md#currentAirqualitypostalCodepostalCodeGet) | **GET** /current/airquality?postal_code&#x3D;{postal_code} | Returns current air quality conditions - Given a Postal Code.



## currentAirqualitycityIdcityIdGet

> AQCurrentGroup currentAirqualitycityIdcityIdGet(cityId, key, opts)

Returns current air quality conditions - Given a City ID.

Returns current air quality conditions.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentAirQualityApi();
let cityId = 56; // Number | City ID. Example: 4487042
let key = "key_example"; // String | Your registered API key.
let opts = {
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example - callback=func
};
apiInstance.currentAirqualitycityIdcityIdGet(cityId, key, opts, (error, data, response) => {
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

### Return type

[**AQCurrentGroup**](AQCurrentGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentAirqualitycitycitycountrycountryGet

> AQCurrentGroup currentAirqualitycitycitycountrycountryGet(city, country, key, opts)

Returns current air quality conditions - Given City and/or State, Country.

Returns current air quality conditions.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentAirQualityApi();
let city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
let country = "country_example"; // String | Country Code (2 letter).
let key = "key_example"; // String | Your registered API key.
let opts = {
  'state': "state_example", // String | Full name of state.
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.currentAirqualitycitycitycountrycountryGet(city, country, key, opts, (error, data, response) => {
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

### Return type

[**AQCurrentGroup**](AQCurrentGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentAirqualitylatlatlonlonGet

> AQCurrentGroup currentAirqualitylatlatlonlonGet(lat, lon, key, opts)

Returns current air quality conditions - Given a lat/lon.

Returns current air quality conditions.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentAirQualityApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let key = "key_example"; // String | Your registered API key.
let opts = {
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example - callback=func
};
apiInstance.currentAirqualitylatlatlonlonGet(lat, lon, key, opts, (error, data, response) => {
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

### Return type

[**AQCurrentGroup**](AQCurrentGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## currentAirqualitypostalCodepostalCodeGet

> AQCurrentGroup currentAirqualitypostalCodepostalCodeGet(postalCode, key, opts)

Returns current air quality conditions - Given a Postal Code.

Returns current air quality conditions.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.CurrentAirQualityApi();
let postalCode = 56; // Number | Postal Code. Example: 28546
let key = "key_example"; // String | Your registered API key.
let opts = {
  'country': "country_example", // String | Country Code (2 letter).
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example - callback=func
};
apiInstance.currentAirqualitypostalCodepostalCodeGet(postalCode, key, opts, (error, data, response) => {
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

### Return type

[**AQCurrentGroup**](AQCurrentGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

