# Apacta.TimeEntryRatesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeEntryRatesGet**](TimeEntryRatesApi.md#timeEntryRatesGet) | **GET** /time_entry_rates | List time entry rates
[**timeEntryRatesPost**](TimeEntryRatesApi.md#timeEntryRatesPost) | **POST** /time_entry_rates | Add new time entry rate
[**timeEntryRatesTimeEntryRateIdGet**](TimeEntryRatesApi.md#timeEntryRatesTimeEntryRateIdGet) | **GET** /time_entry_rates/{time_entry_rate_id} | View time entry rate
[**timeEntryRatesTimeEntryRateIdPut**](TimeEntryRatesApi.md#timeEntryRatesTimeEntryRateIdPut) | **PUT** /time_entry_rates/{time_entry_rate_id} | Edit time entry rate



## timeEntryRatesGet

> TimeEntryRatesGet200Response timeEntryRatesGet()

List time entry rates

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

let apiInstance = new Apacta.TimeEntryRatesApi();
apiInstance.timeEntryRatesGet((error, data, response) => {
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

[**TimeEntryRatesGet200Response**](TimeEntryRatesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntryRatesPost

> ClockingRecordsPost201Response timeEntryRatesPost(opts)

Add new time entry rate

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

let apiInstance = new Apacta.TimeEntryRatesApi();
let opts = {
  'timeEntriesPostRequest': new Apacta.TimeEntriesPostRequest() // TimeEntriesPostRequest | 
};
apiInstance.timeEntryRatesPost(opts, (error, data, response) => {
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
 **timeEntriesPostRequest** | [**TimeEntriesPostRequest**](TimeEntriesPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeEntryRatesTimeEntryRateIdGet

> TimeEntryRatesTimeEntryRateIdGet200Response timeEntryRatesTimeEntryRateIdGet(timeEntryRateId)

View time entry rate

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

let apiInstance = new Apacta.TimeEntryRatesApi();
let timeEntryRateId = "timeEntryRateId_example"; // String | 
apiInstance.timeEntryRatesTimeEntryRateIdGet(timeEntryRateId, (error, data, response) => {
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
 **timeEntryRateId** | **String**|  | 

### Return type

[**TimeEntryRatesTimeEntryRateIdGet200Response**](TimeEntryRatesTimeEntryRateIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntryRatesTimeEntryRateIdPut

> ClockingRecordsClockingRecordIdPut200Response timeEntryRatesTimeEntryRateIdPut(timeEntryRateId)

Edit time entry rate

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

let apiInstance = new Apacta.TimeEntryRatesApi();
let timeEntryRateId = "timeEntryRateId_example"; // String | 
apiInstance.timeEntryRatesTimeEntryRateIdPut(timeEntryRateId, (error, data, response) => {
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
 **timeEntryRateId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

