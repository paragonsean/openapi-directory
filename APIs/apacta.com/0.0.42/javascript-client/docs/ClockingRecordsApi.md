# Apacta.ClockingRecordsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clockingRecordsCheckoutPost**](ClockingRecordsApi.md#clockingRecordsCheckoutPost) | **POST** /clocking_records/checkout | Checkout active clocking record for authenticated user
[**clockingRecordsClockingRecordIdDelete**](ClockingRecordsApi.md#clockingRecordsClockingRecordIdDelete) | **DELETE** /clocking_records/{clocking_record_id} | Delete a clocking record
[**clockingRecordsClockingRecordIdGet**](ClockingRecordsApi.md#clockingRecordsClockingRecordIdGet) | **GET** /clocking_records/{clocking_record_id} | Details of 1 clocking_record
[**clockingRecordsClockingRecordIdPut**](ClockingRecordsApi.md#clockingRecordsClockingRecordIdPut) | **PUT** /clocking_records/{clocking_record_id} | Edit a clocking record
[**clockingRecordsGet**](ClockingRecordsApi.md#clockingRecordsGet) | **GET** /clocking_records | Get a list of clocking records
[**clockingRecordsPost**](ClockingRecordsApi.md#clockingRecordsPost) | **POST** /clocking_records | Create clocking record for authenticated user



## clockingRecordsCheckoutPost

> ClockingRecordsCheckoutPost201Response clockingRecordsCheckoutPost()

Checkout active clocking record for authenticated user

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

let apiInstance = new Apacta.ClockingRecordsApi();
apiInstance.clockingRecordsCheckoutPost((error, data, response) => {
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

[**ClockingRecordsCheckoutPost201Response**](ClockingRecordsCheckoutPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clockingRecordsClockingRecordIdDelete

> ClockingRecordsClockingRecordIdDelete200Response clockingRecordsClockingRecordIdDelete(clockingRecordId)

Delete a clocking record

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

let apiInstance = new Apacta.ClockingRecordsApi();
let clockingRecordId = "clockingRecordId_example"; // String | 
apiInstance.clockingRecordsClockingRecordIdDelete(clockingRecordId, (error, data, response) => {
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
 **clockingRecordId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdDelete200Response**](ClockingRecordsClockingRecordIdDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clockingRecordsClockingRecordIdGet

> ClockingRecordsClockingRecordIdGet200Response clockingRecordsClockingRecordIdGet(clockingRecordId)

Details of 1 clocking_record

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

let apiInstance = new Apacta.ClockingRecordsApi();
let clockingRecordId = "clockingRecordId_example"; // String | 
apiInstance.clockingRecordsClockingRecordIdGet(clockingRecordId, (error, data, response) => {
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
 **clockingRecordId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdGet200Response**](ClockingRecordsClockingRecordIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clockingRecordsClockingRecordIdPut

> ClockingRecordsClockingRecordIdPut200Response clockingRecordsClockingRecordIdPut(clockingRecordId)

Edit a clocking record

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

let apiInstance = new Apacta.ClockingRecordsApi();
let clockingRecordId = "clockingRecordId_example"; // String | 
apiInstance.clockingRecordsClockingRecordIdPut(clockingRecordId, (error, data, response) => {
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
 **clockingRecordId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clockingRecordsGet

> ClockingRecordsGet200Response clockingRecordsGet(opts)

Get a list of clocking records

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

let apiInstance = new Apacta.ClockingRecordsApi();
let opts = {
  'active': true // Boolean | Used to search for active clocking records
};
apiInstance.clockingRecordsGet(opts, (error, data, response) => {
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
 **active** | **Boolean**| Used to search for active clocking records | [optional] 

### Return type

[**ClockingRecordsGet200Response**](ClockingRecordsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clockingRecordsPost

> ClockingRecordsPost201Response clockingRecordsPost(clockingRecordsPostRequest)

Create clocking record for authenticated user

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

let apiInstance = new Apacta.ClockingRecordsApi();
let clockingRecordsPostRequest = new Apacta.ClockingRecordsPostRequest(); // ClockingRecordsPostRequest | 
apiInstance.clockingRecordsPost(clockingRecordsPostRequest, (error, data, response) => {
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
 **clockingRecordsPostRequest** | [**ClockingRecordsPostRequest**](ClockingRecordsPostRequest.md)|  | 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

