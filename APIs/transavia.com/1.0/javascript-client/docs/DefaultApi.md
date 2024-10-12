# AirportsApiV2.DefaultApi

All URIs are relative to *https://api.transavia.com/v2/airports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call58d8bcb7a9e6240e200cff24**](DefaultApi.md#call58d8bcb7a9e6240e200cff24) | **GET** / | All airports
[**call58d8bcb7a9e6240e200cff25**](DefaultApi.md#call58d8bcb7a9e6240e200cff25) | **GET** /{id} | Airport by id.
[**call58d8bcb8a9e6240e200cff26**](DefaultApi.md#call58d8bcb8a9e6240e200cff26) | **GET** /countrycode/{countryCode} | Airport(s) by country code.
[**call58d8bcb8a9e6240e200cff27**](DefaultApi.md#call58d8bcb8a9e6240e200cff27) | **GET** /nearest | Nearest airport(s) by geo coordinates.
[**call58d8bcb8a9e6240e200cff28**](DefaultApi.md#call58d8bcb8a9e6240e200cff28) | **GET** /nearest/{id} | Nearest airport(s) by airport id.



## call58d8bcb7a9e6240e200cff24

> [AirportDto] call58d8bcb7a9e6240e200cff24()

All airports

Retrieve all airports.

### Example

```javascript
import AirportsApiV2 from 'airports_api_v2';
let defaultClient = AirportsApiV2.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new AirportsApiV2.DefaultApi();
apiInstance.call58d8bcb7a9e6240e200cff24((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[AirportDto]**](AirportDto.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## call58d8bcb7a9e6240e200cff25

> AirportDetailsDto call58d8bcb7a9e6240e200cff25(id)

Airport by id.

Retrieve airport by id.

### Example

```javascript
import AirportsApiV2 from 'airports_api_v2';
let defaultClient = AirportsApiV2.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new AirportsApiV2.DefaultApi();
let id = "id_example"; // String | Airport code (3-character IATA code).
apiInstance.call58d8bcb7a9e6240e200cff25(id, (error, data, response) => {
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
 **id** | **String**| Airport code (3-character IATA code). | 

### Return type

[**AirportDetailsDto**](AirportDetailsDto.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## call58d8bcb8a9e6240e200cff26

> [AirportDto] call58d8bcb8a9e6240e200cff26(countryCode)

Airport(s) by country code.

Retrieve airports by country code.

### Example

```javascript
import AirportsApiV2 from 'airports_api_v2';
let defaultClient = AirportsApiV2.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new AirportsApiV2.DefaultApi();
let countryCode = "countryCode_example"; // String | Comma-separated list of country codes (2-character ISO 3166-1). More than 3 country codes is not allowed.
apiInstance.call58d8bcb8a9e6240e200cff26(countryCode, (error, data, response) => {
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
 **countryCode** | **String**| Comma-separated list of country codes (2-character ISO 3166-1). More than 3 country codes is not allowed. | 

### Return type

[**[AirportDto]**](AirportDto.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## call58d8bcb8a9e6240e200cff27

> [NearestAirportDto] call58d8bcb8a9e6240e200cff27(opts)

Nearest airport(s) by geo coordinates.

Retrieve nearest airports by geo coordinates (latitude/longitude).

### Example

```javascript
import AirportsApiV2 from 'airports_api_v2';
let defaultClient = AirportsApiV2.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new AirportsApiV2.DefaultApi();
let opts = {
  'latitude': "latitude_example", // String | Latitude in decimals, lower than -90.0 and higher than 90.0 is not allowed.
  'longitude': "longitude_example", // String | Longitude in decimals, lower than -180.0 and higher than 180.0 is not allowed.
  'maxDistanceInKm': "maxDistanceInKm_example", // String | Maximum distance in kilometers, lower than 1 and higher than 500 is not allowed. If not set, max value is applied.
  'limit': "limit_example" // String | Limits the result, lower than 0 is not allowed. If not set, the result is not limited.
};
apiInstance.call58d8bcb8a9e6240e200cff27(opts, (error, data, response) => {
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
 **latitude** | **String**| Latitude in decimals, lower than -90.0 and higher than 90.0 is not allowed. | [optional] 
 **longitude** | **String**| Longitude in decimals, lower than -180.0 and higher than 180.0 is not allowed. | [optional] 
 **maxDistanceInKm** | **String**| Maximum distance in kilometers, lower than 1 and higher than 500 is not allowed. If not set, max value is applied. | [optional] 
 **limit** | **String**| Limits the result, lower than 0 is not allowed. If not set, the result is not limited. | [optional] 

### Return type

[**[NearestAirportDto]**](NearestAirportDto.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## call58d8bcb8a9e6240e200cff28

> [NearestAirportDto] call58d8bcb8a9e6240e200cff28(id, opts)

Nearest airport(s) by airport id.

Retrieve nearest airports by station id.

### Example

```javascript
import AirportsApiV2 from 'airports_api_v2';
let defaultClient = AirportsApiV2.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
let apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new AirportsApiV2.DefaultApi();
let id = "id_example"; // String | Airport (IATA code) to search nearest airports for.
let opts = {
  'maxDistanceInKm': "maxDistanceInKm_example", // String | Maximum distance in kilometers, lower than 1 and higher than 500 is not allowed. If not set, max value is applied.
  'limit': "limit_example" // String | Limits the result, lower than 0 is not allowed. If not set, the result is not limited.
};
apiInstance.call58d8bcb8a9e6240e200cff28(id, opts, (error, data, response) => {
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
 **id** | **String**| Airport (IATA code) to search nearest airports for. | 
 **maxDistanceInKm** | **String**| Maximum distance in kilometers, lower than 1 and higher than 500 is not allowed. If not set, max value is applied. | [optional] 
 **limit** | **String**| Limits the result, lower than 0 is not allowed. If not set, the result is not limited. | [optional] 

### Return type

[**[NearestAirportDto]**](NearestAirportDto.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

