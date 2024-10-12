# Apacta.TimeEntryTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkActivateTimeEntryTypes**](TimeEntryTypesApi.md#bulkActivateTimeEntryTypes) | **POST** /time_entry_types/bulkActivate | Bulk activate time entry types
[**bulkDeactivateTimeEntryTypes**](TimeEntryTypesApi.md#bulkDeactivateTimeEntryTypes) | **POST** /time_entry_types/bulkDeactivate | Bulk deactivate time entry types
[**bulkDeleteTimeEntryTypes**](TimeEntryTypesApi.md#bulkDeleteTimeEntryTypes) | **DELETE** /time_entry_types/bulkDelete | Bulk delete time entry types
[**timeEntryTypesGet**](TimeEntryTypesApi.md#timeEntryTypesGet) | **GET** /time_entry_types | List time entries types
[**timeEntryTypesPost**](TimeEntryTypesApi.md#timeEntryTypesPost) | **POST** /time_entry_types | Add new time entry type
[**timeEntryTypesTimeEntryTypeIdDelete**](TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdDelete) | **DELETE** /time_entry_types/{time_entry_type_id} | Delete time entry type
[**timeEntryTypesTimeEntryTypeIdGet**](TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdGet) | **GET** /time_entry_types/{time_entry_type_id} | View time entry type
[**timeEntryTypesTimeEntryTypeIdPut**](TimeEntryTypesApi.md#timeEntryTypesTimeEntryTypeIdPut) | **PUT** /time_entry_types/{time_entry_type_id} | Edit time entry type



## bulkActivateTimeEntryTypes

> EmptySuccessResponse bulkActivateTimeEntryTypes(bulkActionRequestBody)

Bulk activate time entry types

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

let apiInstance = new Apacta.TimeEntryTypesApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | Time entry types ids
apiInstance.bulkActivateTimeEntryTypes(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Time entry types ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkDeactivateTimeEntryTypes

> EmptySuccessResponse bulkDeactivateTimeEntryTypes(bulkActionRequestBody)

Bulk deactivate time entry types

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

let apiInstance = new Apacta.TimeEntryTypesApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | Time entry types ids
apiInstance.bulkDeactivateTimeEntryTypes(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Time entry types ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bulkDeleteTimeEntryTypes

> EmptySuccessResponse bulkDeleteTimeEntryTypes(bulkActionRequestBody)

Bulk delete time entry types

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

let apiInstance = new Apacta.TimeEntryTypesApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | Time entry types ids
apiInstance.bulkDeleteTimeEntryTypes(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Time entry types ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeEntryTypesGet

> TimeEntryTypesGet200Response timeEntryTypesGet()

List time entries types

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

let apiInstance = new Apacta.TimeEntryTypesApi();
apiInstance.timeEntryTypesGet((error, data, response) => {
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

[**TimeEntryTypesGet200Response**](TimeEntryTypesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntryTypesPost

> ClockingRecordsPost201Response timeEntryTypesPost(opts)

Add new time entry type

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

let apiInstance = new Apacta.TimeEntryTypesApi();
let opts = {
  'timeEntryTypesPostRequest': new Apacta.TimeEntryTypesPostRequest() // TimeEntryTypesPostRequest | 
};
apiInstance.timeEntryTypesPost(opts, (error, data, response) => {
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
 **timeEntryTypesPostRequest** | [**TimeEntryTypesPostRequest**](TimeEntryTypesPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## timeEntryTypesTimeEntryTypeIdDelete

> ClockingRecordsClockingRecordIdPut200Response timeEntryTypesTimeEntryTypeIdDelete(timeEntryTypeId)

Delete time entry type

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

let apiInstance = new Apacta.TimeEntryTypesApi();
let timeEntryTypeId = "timeEntryTypeId_example"; // String | 
apiInstance.timeEntryTypesTimeEntryTypeIdDelete(timeEntryTypeId, (error, data, response) => {
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
 **timeEntryTypeId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntryTypesTimeEntryTypeIdGet

> TimeEntryTypesTimeEntryTypeIdGet200Response timeEntryTypesTimeEntryTypeIdGet(timeEntryTypeId)

View time entry type

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

let apiInstance = new Apacta.TimeEntryTypesApi();
let timeEntryTypeId = "timeEntryTypeId_example"; // String | 
apiInstance.timeEntryTypesTimeEntryTypeIdGet(timeEntryTypeId, (error, data, response) => {
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
 **timeEntryTypeId** | **String**|  | 

### Return type

[**TimeEntryTypesTimeEntryTypeIdGet200Response**](TimeEntryTypesTimeEntryTypeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## timeEntryTypesTimeEntryTypeIdPut

> ClockingRecordsClockingRecordIdPut200Response timeEntryTypesTimeEntryTypeIdPut(timeEntryTypeId)

Edit time entry type

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

let apiInstance = new Apacta.TimeEntryTypesApi();
let timeEntryTypeId = "timeEntryTypeId_example"; // String | 
apiInstance.timeEntryTypesTimeEntryTypeIdPut(timeEntryTypeId, (error, data, response) => {
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
 **timeEntryTypeId** | **String**|  | 

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

