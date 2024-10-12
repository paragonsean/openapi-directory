# MonVoyagePasCherComPublicApi.ServicesAPIsApi

All URIs are relative to *https://api.mon-voyage-pas-cher.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDistance**](ServicesAPIsApi.md#getDistance) | **GET** /distance | Calculate distance between lats/longs
[**getElevation**](ServicesAPIsApi.md#getElevation) | **GET** /elevation | Search elevation informations from lat/long
[**getSun**](ServicesAPIsApi.md#getSun) | **GET** /sun_positions | Search position of sun from lat/long and date
[**getTimezone**](ServicesAPIsApi.md#getTimezone) | **GET** /timezone | Search timezone and time informations from lat/long



## getDistance

> DistanceResponse getDistance(locationA, locationB, opts)

Calculate distance between lats/longs

This webservice is providing you the ability to calculate the distance between 2 lat/long points, it returns you the value in km or miles

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.ServicesAPIsApi();
let locationA = "locationA_example"; // String | The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point A
let locationB = "locationB_example"; // String | The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point B
let opts = {
  'unit': "'kms'" // String | The unit of length you want the elevation returned either meters or feet returned
};
apiInstance.getDistance(locationA, locationB, opts, (error, data, response) => {
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
 **locationA** | **String**| The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point A | 
 **locationB** | **String**| The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point B | 
 **unit** | **String**| The unit of length you want the elevation returned either meters or feet returned | [optional] [default to &#39;kms&#39;]

### Return type

[**DistanceResponse**](DistanceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getElevation

> ElevationResponse getElevation(locations, opts)

Search elevation informations from lat/long

This webservice is providing you the ability to retrieve the elevation in meters or feet of ONE or MULTIPLE given latitude/longitude point(s). &lt;br /&gt;If you use MULTIPLE lat/long point, the maximum number of point you can send in one request is 256. Be aware that if MULTIPLE mode, the results are de-deplicated if you are sending the same latitude/longitude point multiple times.&lt;br /&gt;If your workload is a batch of millions of lat/long point, You will also get better throughput if you send around 100 lat/long points in one request than the maximum. This maximum is mostly allowed for people trying to graph altitudes.

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.ServicesAPIsApi();
let locations = "'67.85572,20.22513'"; // String | The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) or a list of coordinates separated using the pipe ('|') character. The maximum number of coordinates you can send at one time is 20 ( ex. 67.85572,20.22513|27.85572,20.22513 )
let opts = {
  'unit': "'meters'" // String | The unit of length you want the elevation returned either meters or feet returned
};
apiInstance.getElevation(locations, opts, (error, data, response) => {
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
 **locations** | **String**| The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) or a list of coordinates separated using the pipe (&#39;|&#39;) character. The maximum number of coordinates you can send at one time is 20 ( ex. 67.85572,20.22513|27.85572,20.22513 ) | [default to &#39;67.85572,20.22513&#39;]
 **unit** | **String**| The unit of length you want the elevation returned either meters or feet returned | [optional] [default to &#39;meters&#39;]

### Return type

[**ElevationResponse**](ElevationResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSun

> SunPositionResponse getSun(location, opts)

Search position of sun from lat/long and date

This webservice is providing you the ability to retrieve the time of each phases of the sunlight cycle. Sunset, sunrise, sunriseEnd, golden hour, solarNoon, dawn, dusk and more for a given location and date. If the date if not provided, the response provided return informations for today at UTC time.

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.ServicesAPIsApi();
let location = "location_example"; // String | Here you can send either a latitude / longitude
let opts = {
  'date': new Date("2013-10-20") // Date | The date for what you will get the data ( full-date notation as defined by RFC 3339, section 5.6, for example, 2017-07-21 ), if not provided as parameter, today is going to be used
};
apiInstance.getSun(location, opts, (error, data, response) => {
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
 **location** | **String**| Here you can send either a latitude / longitude | 
 **date** | **Date**| The date for what you will get the data ( full-date notation as defined by RFC 3339, section 5.6, for example, 2017-07-21 ), if not provided as parameter, today is going to be used | [optional] 

### Return type

[**SunPositionResponse**](SunPositionResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTimezone

> TimezoneResponse getTimezone(location)

Search timezone and time informations from lat/long

This webservice is providing you the ability to retrieve the tz database time zones ( https://en.wikipedia.org/wiki/List_of_tz_database_time_zones )  from a given location ( )latitude and longitude or IATA code ). It also returns you the current time at the provided location.

### Example

```javascript
import MonVoyagePasCherComPublicApi from 'mon_voyage_pas_cher_com_public_api';
let defaultClient = MonVoyagePasCherComPublicApi.ApiClient.instance;
// Configure API key authorization: x-api-key
let x-api-key = defaultClient.authentications['x-api-key'];
x-api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//x-api-key.apiKeyPrefix = 'Token';

let apiInstance = new MonVoyagePasCherComPublicApi.ServicesAPIsApi();
let location = "'45.8326307,6.8650517'"; // String | Here you can send either a latitude / longitude ( ex. 67.85572,20.22513 ) or a IATA Code ( ex. LHR for London Heathrow)
apiInstance.getTimezone(location, (error, data, response) => {
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
 **location** | **String**| Here you can send either a latitude / longitude ( ex. 67.85572,20.22513 ) or a IATA Code ( ex. LHR for London Heathrow) | [default to &#39;45.8326307,6.8650517&#39;]

### Return type

[**TimezoneResponse**](TimezoneResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

