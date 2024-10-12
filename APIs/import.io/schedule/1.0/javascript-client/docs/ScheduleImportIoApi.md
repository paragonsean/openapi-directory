# ImportIo.ScheduleImportIoApi

All URIs are relative to *https://schedule.import.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extractorExtractorIdDelete**](ScheduleImportIoApi.md#extractorExtractorIdDelete) | **DELETE** /extractor/{extractorId}/ | Delete an existing schedule
[**extractorExtractorIdGet**](ScheduleImportIoApi.md#extractorExtractorIdGet) | **GET** /extractor/{extractorId}/ | Get the schedule of a particular extractor
[**extractorGet**](ScheduleImportIoApi.md#extractorGet) | **GET** /extractor | Get the list of schedules for all your extractors
[**extractorPost**](ScheduleImportIoApi.md#extractorPost) | **POST** /extractor | Schedule and extractor to run at a specific time



## extractorExtractorIdDelete

> extractorExtractorIdDelete(extractorId)

Delete an existing schedule

### Example

```javascript
import ImportIo from 'import_io';
let defaultClient = ImportIo.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImportIo.ScheduleImportIoApi();
let extractorId = "extractorId_example"; // String | the id of the extractor with a schedule
apiInstance.extractorExtractorIdDelete(extractorId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extractorId** | **String**| the id of the extractor with a schedule | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## extractorExtractorIdGet

> Schedule extractorExtractorIdGet(extractorId)

Get the schedule of a particular extractor

### Example

```javascript
import ImportIo from 'import_io';
let defaultClient = ImportIo.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImportIo.ScheduleImportIoApi();
let extractorId = "extractorId_example"; // String | the id of the extractor with a schedule
apiInstance.extractorExtractorIdGet(extractorId, (error, data, response) => {
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
 **extractorId** | **String**| the id of the extractor with a schedule | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## extractorGet

> Schedule extractorGet()

Get the list of schedules for all your extractors

### Example

```javascript
import ImportIo from 'import_io';
let defaultClient = ImportIo.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImportIo.ScheduleImportIoApi();
apiInstance.extractorGet((error, data, response) => {
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

[**Schedule**](Schedule.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8


## extractorPost

> Schedule extractorPost(scheduleRequestBody)

Schedule and extractor to run at a specific time

### Example

```javascript
import ImportIo from 'import_io';
let defaultClient = ImportIo.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ImportIo.ScheduleImportIoApi();
let scheduleRequestBody = new ImportIo.ScheduleRequest(); // ScheduleRequest | Request body with the schema defined on the left. Interval is a cron string.
apiInstance.extractorPost(scheduleRequestBody, (error, data, response) => {
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
 **scheduleRequestBody** | [**ScheduleRequest**](ScheduleRequest.md)| Request body with the schema defined on the left. Interval is a cron string. | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json;charset=UTF-8

