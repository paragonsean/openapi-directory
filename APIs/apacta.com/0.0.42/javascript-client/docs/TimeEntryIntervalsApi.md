# Apacta.TimeEntryIntervalsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeEntryIntervalsGet**](TimeEntryIntervalsApi.md#timeEntryIntervalsGet) | **GET** /time_entry_intervals | List possible time entry intervals
[**timeEntryIntervalsTimeEntryIntervalIdGet**](TimeEntryIntervalsApi.md#timeEntryIntervalsTimeEntryIntervalIdGet) | **GET** /time_entry_intervals/{time_entry_interval_id} | View time entry interval



## timeEntryIntervalsGet

> TimeEntryIntervalsGet200Response timeEntryIntervalsGet()

List possible time entry intervals

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

let apiInstance = new Apacta.TimeEntryIntervalsApi();
apiInstance.timeEntryIntervalsGet((error, data, response) => {
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

[**TimeEntryIntervalsGet200Response**](TimeEntryIntervalsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntryIntervalsTimeEntryIntervalIdGet

> TimeEntryIntervalsTimeEntryIntervalIdGet200Response timeEntryIntervalsTimeEntryIntervalIdGet(timeEntryIntervalId)

View time entry interval

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

let apiInstance = new Apacta.TimeEntryIntervalsApi();
let timeEntryIntervalId = "timeEntryIntervalId_example"; // String | 
apiInstance.timeEntryIntervalsTimeEntryIntervalIdGet(timeEntryIntervalId, (error, data, response) => {
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
 **timeEntryIntervalId** | **String**|  | 

### Return type

[**TimeEntryIntervalsTimeEntryIntervalIdGet200Response**](TimeEntryIntervalsTimeEntryIntervalIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

