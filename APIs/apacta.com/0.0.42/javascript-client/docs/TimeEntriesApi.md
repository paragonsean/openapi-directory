# Apacta.TimeEntriesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeEntriesGet**](TimeEntriesApi.md#timeEntriesGet) | **GET** /time_entries | List time entries
[**timeEntriesPost**](TimeEntriesApi.md#timeEntriesPost) | **POST** /time_entries | Add new time entry
[**timeEntriesTimeEntryIdDelete**](TimeEntriesApi.md#timeEntriesTimeEntryIdDelete) | **DELETE** /time_entries/{time_entry_id} | Delete time entry
[**timeEntriesTimeEntryIdGet**](TimeEntriesApi.md#timeEntriesTimeEntryIdGet) | **GET** /time_entries/{time_entry_id} | View time entry
[**timeEntriesTimeEntryIdPut**](TimeEntriesApi.md#timeEntriesTimeEntryIdPut) | **PUT** /time_entries/{time_entry_id} | Edit time entry



## timeEntriesGet

> TimeEntriesGet200Response timeEntriesGet(opts)

List time entries

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

let apiInstance = new Apacta.TimeEntriesApi();
let opts = {
  'userId': "userId_example", // String | 
  'formId': "formId_example", // String | 
  'projectId': "projectId_example", // String | 
  'gtFromTime': "gtFromTime_example", // String | 
  'ltFromTime': "ltFromTime_example", // String | 
  'gtToTime': "gtToTime_example", // String | 
  'ltToTime': "ltToTime_example", // String | 
  'ltSum': "ltSum_example", // String | 
  'gtSum': "gtSum_example" // String | 
};
apiInstance.timeEntriesGet(opts, (error, data, response) => {
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
 **userId** | **String**|  | [optional] 
 **formId** | **String**|  | [optional] 
 **projectId** | **String**|  | [optional] 
 **gtFromTime** | **String**|  | [optional] 
 **ltFromTime** | **String**|  | [optional] 
 **gtToTime** | **String**|  | [optional] 
 **ltToTime** | **String**|  | [optional] 
 **ltSum** | **String**|  | [optional] 
 **gtSum** | **String**|  | [optional] 

### Return type

[**TimeEntriesGet200Response**](TimeEntriesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntriesPost

> ClockingRecordsPost201Response timeEntriesPost(opts)

Add new time entry

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

let apiInstance = new Apacta.TimeEntriesApi();
let opts = {
  'timeEntriesPostRequest': new Apacta.TimeEntriesPostRequest() // TimeEntriesPostRequest | 
};
apiInstance.timeEntriesPost(opts, (error, data, response) => {
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


## timeEntriesTimeEntryIdDelete

> ClockingRecordsClockingRecordIdPut200Response timeEntriesTimeEntryIdDelete(timeEntryId)

Delete time entry

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

let apiInstance = new Apacta.TimeEntriesApi();
let timeEntryId = "timeEntryId_example"; // String | 
apiInstance.timeEntriesTimeEntryIdDelete(timeEntryId, (error, data, response) => {
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
 **timeEntryId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntriesTimeEntryIdGet

> TimeEntriesTimeEntryIdGet200Response timeEntriesTimeEntryIdGet(timeEntryId)

View time entry

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

let apiInstance = new Apacta.TimeEntriesApi();
let timeEntryId = "timeEntryId_example"; // String | 
apiInstance.timeEntriesTimeEntryIdGet(timeEntryId, (error, data, response) => {
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
 **timeEntryId** | **String**|  | 

### Return type

[**TimeEntriesTimeEntryIdGet200Response**](TimeEntriesTimeEntryIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntriesTimeEntryIdPut

> ClockingRecordsClockingRecordIdPut200Response timeEntriesTimeEntryIdPut(timeEntryId)

Edit time entry

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

let apiInstance = new Apacta.TimeEntriesApi();
let timeEntryId = "timeEntryId_example"; // String | 
apiInstance.timeEntriesTimeEntryIdPut(timeEntryId, (error, data, response) => {
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
 **timeEntryId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

