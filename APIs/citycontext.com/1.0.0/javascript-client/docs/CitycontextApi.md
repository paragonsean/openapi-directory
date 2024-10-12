# CityContext.CitycontextApi

All URIs are relative to *http://api.citycontext.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**byPoint**](CitycontextApi.md#byPoint) | **GET** /@{lat},{lon} | Query by coordinates (SRID 4326 - decimal degrees)
[**byPostcode**](CitycontextApi.md#byPostcode) | **GET** /postcodes/{postcode} | Query by postcode
[**usage**](CitycontextApi.md#usage) | **GET** /usage | Get usage in current month



## byPoint

> PointInfo byPoint(lat, lon, opts)

Query by coordinates (SRID 4326 - decimal degrees)

### Example

```javascript
import CityContext from 'city_context';
let defaultClient = CityContext.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new CityContext.CitycontextApi();
let lat = 3.4; // Number | Latitude
let lon = 3.4; // Number | Longitude
let opts = {
  'schoolSearchRadius': 56, // Number | Search radius for schools, in metres, between 100 and 4000
  'parkSearchRadius': 56 // Number | Search radius for parks, in metres, between 100 and 2000
};
apiInstance.byPoint(lat, lon, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude | 
 **lon** | **Number**| Longitude | 
 **schoolSearchRadius** | **Number**| Search radius for schools, in metres, between 100 and 4000 | [optional] 
 **parkSearchRadius** | **Number**| Search radius for parks, in metres, between 100 and 2000 | [optional] 

### Return type

[**PointInfo**](PointInfo.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## byPostcode

> PointInfo byPostcode(postcode, opts)

Query by postcode

### Example

```javascript
import CityContext from 'city_context';
let defaultClient = CityContext.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new CityContext.CitycontextApi();
let postcode = "postcode_example"; // String | Postcode
let opts = {
  'schoolSearchRadius': 56, // Number | Search radius for schools, in metres, between 100 and 4000
  'parkSearchRadius': 56 // Number | Search radius for parks, in metres, between 100 and 2000
};
apiInstance.byPostcode(postcode, opts, (error, data, response) => {
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
 **postcode** | **String**| Postcode | 
 **schoolSearchRadius** | **Number**| Search radius for schools, in metres, between 100 and 4000 | [optional] 
 **parkSearchRadius** | **Number**| Search radius for parks, in metres, between 100 and 2000 | [optional] 

### Return type

[**PointInfo**](PointInfo.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usage

> Usage usage()

Get usage in current month

### Example

```javascript
import CityContext from 'city_context';
let defaultClient = CityContext.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new CityContext.CitycontextApi();
apiInstance.usage((error, data, response) => {
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

[**Usage**](Usage.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

