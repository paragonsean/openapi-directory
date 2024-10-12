# Apacta.CitiesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**citiesCityIdGet**](CitiesApi.md#citiesCityIdGet) | **GET** /cities/{city_id} | Get details about one city
[**citiesGet**](CitiesApi.md#citiesGet) | **GET** /cities | Get list of cities supported in Apacta



## citiesCityIdGet

> CitiesCityIdGet200Response citiesCityIdGet(cityId)

Get details about one city

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CitiesApi();
let cityId = "cityId_example"; // String | 
apiInstance.citiesCityIdGet(cityId, (error, data, response) => {
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
 **cityId** | **String**|  | 

### Return type

[**CitiesCityIdGet200Response**](CitiesCityIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## citiesGet

> CitiesGet200Response citiesGet(opts)

Get list of cities supported in Apacta

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.CitiesApi();
let opts = {
  'zipCode': "zipCode_example", // String | Used to search for a city with specific zip code
  'name': "name_example", // String | Used to search for a city by name
  'includeAll': true // Boolean | Used to search for a city without filtering by country
};
apiInstance.citiesGet(opts, (error, data, response) => {
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
 **zipCode** | **String**| Used to search for a city with specific zip code | [optional] 
 **name** | **String**| Used to search for a city by name | [optional] 
 **includeAll** | **Boolean**| Used to search for a city without filtering by country | [optional] 

### Return type

[**CitiesGet200Response**](CitiesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

