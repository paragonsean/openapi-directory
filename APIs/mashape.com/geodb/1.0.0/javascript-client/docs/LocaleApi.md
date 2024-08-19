# GeoDbCitiesApi.LocaleApi

All URIs are relative to *https://wft-geo-db.p.rapidapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCurrenciesUsingGET**](LocaleApi.md#getCurrenciesUsingGET) | **GET** /locale/currencies | Find currencies
[**getLanguagesUsingGET**](LocaleApi.md#getLanguagesUsingGET) | **GET** /locale/languages | Get languages
[**getLocalesUsingGET**](LocaleApi.md#getLocalesUsingGET) | **GET** /locale/locales | Get locales
[**getTimeZoneDateTimeUsingGET**](LocaleApi.md#getTimeZoneDateTimeUsingGET) | **GET** /locale/timezones/{zoneId}/dateTime | Get time-zone date-time
[**getTimeZoneTimeUsingGET**](LocaleApi.md#getTimeZoneTimeUsingGET) | **GET** /locale/timezones/{zoneId}/time | Get time-zone time
[**getTimeZoneUsingGET**](LocaleApi.md#getTimeZoneUsingGET) | **GET** /locale/timezones/{zoneId} | Get time-zone
[**getTimezonesUsingGET**](LocaleApi.md#getTimezonesUsingGET) | **GET** /locale/timezones | Get time-zones



## getCurrenciesUsingGET

> CurrenciesResponse getCurrenciesUsingGET(countryId, opts)

Find currencies

Find currencies, filtering by optional criteria. If no criteria are set, you will get back all known currencies.

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.LocaleApi();
let countryId = "countryId_example"; // String | Currencies for this country id
let opts = {
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0 // Number | The zero-ary offset index into the results
};
apiInstance.getCurrenciesUsingGET(countryId, opts, (error, data, response) => {
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
 **countryId** | **String**| Currencies for this country id | 
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]

### Return type

[**CurrenciesResponse**](CurrenciesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLanguagesUsingGET

> LanguagesResponse getLanguagesUsingGET(opts)

Get languages

Get all supported languages

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.LocaleApi();
let opts = {
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0 // Number | The zero-ary offset index into the results
};
apiInstance.getLanguagesUsingGET(opts, (error, data, response) => {
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
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]

### Return type

[**LanguagesResponse**](LanguagesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLocalesUsingGET

> LocalesResponse getLocalesUsingGET(opts)

Get locales

Get all known locales

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.LocaleApi();
let opts = {
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0 // Number | The zero-ary offset index into the results
};
apiInstance.getLocalesUsingGET(opts, (error, data, response) => {
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
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]

### Return type

[**LocalesResponse**](LocalesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTimeZoneDateTimeUsingGET

> DateTimeResponse getTimeZoneDateTimeUsingGET(zoneId)

Get time-zone date-time

Get time-zone date-time

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.LocaleApi();
let zoneId = "zoneId_example"; // String | A time-zone id
apiInstance.getTimeZoneDateTimeUsingGET(zoneId, (error, data, response) => {
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
 **zoneId** | **String**| A time-zone id | 

### Return type

[**DateTimeResponse**](DateTimeResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTimeZoneTimeUsingGET

> TimeResponse getTimeZoneTimeUsingGET(zoneId)

Get time-zone time

Get time-zone time

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.LocaleApi();
let zoneId = "zoneId_example"; // String | A time-zone id
apiInstance.getTimeZoneTimeUsingGET(zoneId, (error, data, response) => {
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
 **zoneId** | **String**| A time-zone id | 

### Return type

[**TimeResponse**](TimeResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTimeZoneUsingGET

> TimeZoneResponse getTimeZoneUsingGET(zoneId)

Get time-zone

Get time-zone

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.LocaleApi();
let zoneId = "zoneId_example"; // String | A time-zone id
apiInstance.getTimeZoneUsingGET(zoneId, (error, data, response) => {
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
 **zoneId** | **String**| A time-zone id | 

### Return type

[**TimeZoneResponse**](TimeZoneResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTimezonesUsingGET

> TimeZonesResponse getTimezonesUsingGET(opts)

Get time-zones

Get all known time-zones

### Example

```javascript
import GeoDbCitiesApi from 'geo_db_cities_api';
let defaultClient = GeoDbCitiesApi.ApiClient.instance;
// Configure API key authorization: UserSecurity
let UserSecurity = defaultClient.authentications['UserSecurity'];
UserSecurity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//UserSecurity.apiKeyPrefix = 'Token';

let apiInstance = new GeoDbCitiesApi.LocaleApi();
let opts = {
  'hateoasMode': true, // Boolean | Include HATEOAS-style links in results
  'limit': 10, // Number | The maximum number of results to retrieve
  'offset': 0 // Number | The zero-ary offset index into the results
};
apiInstance.getTimezonesUsingGET(opts, (error, data, response) => {
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
 **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true]
 **limit** | **Number**| The maximum number of results to retrieve | [optional] [default to 10]
 **offset** | **Number**| The zero-ary offset index into the results | [optional] [default to 0]

### Return type

[**TimeZonesResponse**](TimeZonesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

