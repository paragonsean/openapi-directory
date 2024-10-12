# MesheryApi.SchedulesAPIApi

All URIs are relative to *http://meshery.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idDeleteSchedules**](SchedulesAPIApi.md#idDeleteSchedules) | **DELETE** /api/user/schedules/{id} | Handle DELETE reqeuest for Schedules
[**idGetSchedules**](SchedulesAPIApi.md#idGetSchedules) | **GET** /api/user/schedules | Handle GET reqeuest for Schedules
[**idGetSingleSchedule**](SchedulesAPIApi.md#idGetSingleSchedule) | **GET** /api/user/schedules/{id} | Handle GET reqeuest for Schedules
[**idPostSchedules**](SchedulesAPIApi.md#idPostSchedules) | **POST** /api/user/schedules | Handle POST reqeuest for Schedules



## idDeleteSchedules

> SchedulesAPIResponse idDeleteSchedules(id)

Handle DELETE reqeuest for Schedules

Deletes a schedule with the given id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SchedulesAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idDeleteSchedules(id, (error, data, response) => {
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
 **id** | **String**| id for a specific | 

### Return type

[**SchedulesAPIResponse**](SchedulesAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetSchedules

> SchedulesAPIResponse idGetSchedules()

Handle GET reqeuest for Schedules

Returns the list of all the schedules saved by the current user

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SchedulesAPIApi();
apiInstance.idGetSchedules((error, data, response) => {
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

[**SchedulesAPIResponse**](SchedulesAPIResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idGetSingleSchedule

> Schedule idGetSingleSchedule(id)

Handle GET reqeuest for Schedules

Fetches and returns the schedule with the given id

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SchedulesAPIApi();
let id = "id_example"; // String | id for a specific
apiInstance.idGetSingleSchedule(id, (error, data, response) => {
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
 **id** | **String**| id for a specific | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## idPostSchedules

> Schedule idPostSchedules()

Handle POST reqeuest for Schedules

Save schedule using the current provider&#39;s persistence mechanism

### Example

```javascript
import MesheryApi from 'meshery_api_';
let defaultClient = MesheryApi.ApiClient.instance;
// Configure API key authorization: token
let token = defaultClient.authentications['token'];
token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//token.apiKeyPrefix = 'Token';

let apiInstance = new MesheryApi.SchedulesAPIApi();
apiInstance.idPostSchedules((error, data, response) => {
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

[token](../README.md#token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

