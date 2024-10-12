# WeatherbitInteractiveSwaggerUiDocumentation.HistoricalAirQualityApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**historyAirqualitycityIdcityIdGet**](HistoricalAirQualityApi.md#historyAirqualitycityIdcityIdGet) | **GET** /history/airquality?city_id&#x3D;{city_id} | Returns 72 hours of historical air quality conditions - Given a City ID.
[**historyAirqualitycitycitycountrycountryGet**](HistoricalAirQualityApi.md#historyAirqualitycitycitycountrycountryGet) | **GET** /history/airquality?city&#x3D;{city}&amp;country&#x3D;{country} | Returns 72 hours of historical quality conditions - Given City and/or State, Country.
[**historyAirqualitylatlatlonlonGet**](HistoricalAirQualityApi.md#historyAirqualitylatlatlonlonGet) | **GET** /history/airquality?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns 72 hours of historical air quality conditions - Given a lat/lon.
[**historyAirqualitypostalCodepostalCodeGet**](HistoricalAirQualityApi.md#historyAirqualitypostalCodepostalCodeGet) | **GET** /history/airquality?postal_code&#x3D;{postal_code} | Returns 72 hours of historical air quality conditions - Given a Postal Code.



## historyAirqualitycityIdcityIdGet

> AQCurrentGroup historyAirqualitycityIdcityIdGet(cityId, key, opts)

Returns 72 hours of historical air quality conditions - Given a City ID.

Returns historical air quality conditions.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.HistoricalAirQualityApi();
let cityId = 3.4; // Number | City ID.
let key = "key_example"; // String | Your registered API key.
let opts = {
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example - callback=func
};
apiInstance.historyAirqualitycityIdcityIdGet(cityId, key, opts, (error, data, response) => {
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
 **cityId** | **Number**| City ID. | 
 **key** | **String**| Your registered API key. | 
 **callback** | **String**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional] 

### Return type

[**AQCurrentGroup**](AQCurrentGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historyAirqualitycitycitycountrycountryGet

> AQCurrentGroup historyAirqualitycitycitycountrycountryGet(city, country, key, opts)

Returns 72 hours of historical quality conditions - Given City and/or State, Country.

Returns historical air quality conditions.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.HistoricalAirQualityApi();
let city = "city_example"; // String | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
let country = "country_example"; // String | Country Code (2 letter).
let key = "key_example"; // String | Your registered API key.
let opts = {
  'state': "state_example", // String | Full name of state.
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example: callback=func
};
apiInstance.historyAirqualitycitycitycountrycountryGet(city, country, key, opts, (error, data, response) => {
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


## historyAirqualitylatlatlonlonGet

> AQCurrentGroup historyAirqualitylatlatlonlonGet(lat, lon, key, opts)

Returns 72 hours of historical air quality conditions - Given a lat/lon.

Returns historical air quality conditions.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.HistoricalAirQualityApi();
let lat = 3.4; // Number | Latitude component of location.
let lon = 3.4; // Number | Longitude component of location.
let key = "key_example"; // String | Your registered API key.
let opts = {
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example - callback=func
};
apiInstance.historyAirqualitylatlatlonlonGet(lat, lon, key, opts, (error, data, response) => {
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


## historyAirqualitypostalCodepostalCodeGet

> AQCurrentGroup historyAirqualitypostalCodepostalCodeGet(postalCode, key, opts)

Returns 72 hours of historical air quality conditions - Given a Postal Code.

Returns historical air quality conditions.

### Example

```javascript
import WeatherbitInteractiveSwaggerUiDocumentation from 'weatherbit_interactive_swagger_ui_documentation';

let apiInstance = new WeatherbitInteractiveSwaggerUiDocumentation.HistoricalAirQualityApi();
let postalCode = 56; // Number | Postal Code. Example: 28546
let key = "key_example"; // String | Your registered API key.
let opts = {
  'country': "country_example", // String | Country Code (2 letter).
  'callback': "callback_example" // String | Wraps return in jsonp callback. Example - callback=func
};
apiInstance.historyAirqualitypostalCodepostalCodeGet(postalCode, key, opts, (error, data, response) => {
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

