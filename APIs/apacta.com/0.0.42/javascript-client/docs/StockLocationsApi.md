# Apacta.StockLocationsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stockLocationsGet**](StockLocationsApi.md#stockLocationsGet) | **GET** /stock_locations | List stock_locations
[**stockLocationsLocationIdDelete**](StockLocationsApi.md#stockLocationsLocationIdDelete) | **DELETE** /stock_locations/{location_id} | Delete location
[**stockLocationsLocationIdGet**](StockLocationsApi.md#stockLocationsLocationIdGet) | **GET** /stock_locations/{location_id} | View single location
[**stockLocationsLocationIdPut**](StockLocationsApi.md#stockLocationsLocationIdPut) | **PUT** /stock_locations/{location_id} | Edit location
[**stockLocationsPost**](StockLocationsApi.md#stockLocationsPost) | **POST** /stock_locations | Add new stock_locations



## stockLocationsGet

> StockLocationsGet200Response stockLocationsGet(opts)

List stock_locations

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

let apiInstance = new Apacta.StockLocationsApi();
let opts = {
  'name': "name_example" // String | Used to filter on the `name` of the stock_locations
};
apiInstance.stockLocationsGet(opts, (error, data, response) => {
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
 **name** | **String**| Used to filter on the &#x60;name&#x60; of the stock_locations | [optional] 

### Return type

[**StockLocationsGet200Response**](StockLocationsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stockLocationsLocationIdDelete

> ClockingRecordsClockingRecordIdPut200Response stockLocationsLocationIdDelete(locationId)

Delete location

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

let apiInstance = new Apacta.StockLocationsApi();
let locationId = "locationId_example"; // String | 
apiInstance.stockLocationsLocationIdDelete(locationId, (error, data, response) => {
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
 **locationId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stockLocationsLocationIdGet

> StockLocationsLocationIdGet200Response stockLocationsLocationIdGet(locationId)

View single location

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

let apiInstance = new Apacta.StockLocationsApi();
let locationId = "locationId_example"; // String | 
apiInstance.stockLocationsLocationIdGet(locationId, (error, data, response) => {
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
 **locationId** | **String**|  | 

### Return type

[**StockLocationsLocationIdGet200Response**](StockLocationsLocationIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stockLocationsLocationIdPut

> ClockingRecordsClockingRecordIdPut200Response stockLocationsLocationIdPut(locationId)

Edit location

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

let apiInstance = new Apacta.StockLocationsApi();
let locationId = "locationId_example"; // String | 
apiInstance.stockLocationsLocationIdPut(locationId, (error, data, response) => {
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
 **locationId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stockLocationsPost

> ClockingRecordsPost201Response stockLocationsPost(opts)

Add new stock_locations

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

let apiInstance = new Apacta.StockLocationsApi();
let opts = {
  'stockLocationsPostRequest': new Apacta.StockLocationsPostRequest() // StockLocationsPostRequest | 
};
apiInstance.stockLocationsPost(opts, (error, data, response) => {
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
 **stockLocationsPostRequest** | [**StockLocationsPostRequest**](StockLocationsPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

