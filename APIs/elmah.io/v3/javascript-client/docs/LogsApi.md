# ElmahIoApi.LogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logsCreate**](LogsApi.md#logsCreate) | **POST** /v3/logs | Create a new log.
[**logsDiagnose**](LogsApi.md#logsDiagnose) | **GET** /v3/logs/{id}/_diagnose | Help diagnose logging problems.
[**logsDisable**](LogsApi.md#logsDisable) | **POST** /v3/logs/{id}/_disable | Disable a log by its ID.
[**logsEnable**](LogsApi.md#logsEnable) | **POST** /v3/logs/{id}/_enable | Enable a log by its ID.
[**logsGet**](LogsApi.md#logsGet) | **GET** /v3/logs/{id} | Fetch a log by its ID.
[**logsGetAll**](LogsApi.md#logsGetAll) | **GET** /v3/logs | Fetch a list of logs.



## logsCreate

> CreateLogResult logsCreate(opts)

Create a new log.

Required permission: &#x60;logs_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.LogsApi();
let opts = {
  'createLog': new ElmahIoApi.CreateLog() // CreateLog | The log object to create.
};
apiInstance.logsCreate(opts, (error, data, response) => {
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
 **createLog** | [**CreateLog**](CreateLog.md)| The log object to create. | [optional] 

### Return type

[**CreateLogResult**](CreateLogResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## logsDiagnose

> [String] logsDiagnose(id)

Help diagnose logging problems.

Required permission: &#x60;messages_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.LogsApi();
let id = "id_example"; // String | The ID of the log to diagnose.
apiInstance.logsDiagnose(id, (error, data, response) => {
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
 **id** | **String**| The ID of the log to diagnose. | 

### Return type

**[String]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## logsDisable

> logsDisable(id)

Disable a log by its ID.

Required permission: &#x60;logs_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.LogsApi();
let id = "id_example"; // String | The ID of the log to disable.
apiInstance.logsDisable(id, (error, data, response) => {
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
 **id** | **String**| The ID of the log to disable. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsEnable

> logsEnable(id)

Enable a log by its ID.

Required permission: &#x60;logs_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.LogsApi();
let id = "id_example"; // String | The ID of the log to enable.
apiInstance.logsEnable(id, (error, data, response) => {
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
 **id** | **String**| The ID of the log to enable. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logsGet

> Log logsGet(id)

Fetch a log by its ID.

Required permission: &#x60;logs_read&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.LogsApi();
let id = "id_example"; // String | The ID of the log to fetch.
apiInstance.logsGet(id, (error, data, response) => {
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
 **id** | **String**| The ID of the log to fetch. | 

### Return type

[**Log**](Log.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## logsGetAll

> [Log] logsGetAll()

Fetch a list of logs.

Required permission: &#x60;logs_read&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.LogsApi();
apiInstance.logsGetAll((error, data, response) => {
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

[**[Log]**](Log.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

