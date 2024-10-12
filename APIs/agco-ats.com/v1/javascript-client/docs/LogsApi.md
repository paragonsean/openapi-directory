# AgcoApi.LogsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logsGetLog**](LogsApi.md#logsGetLog) | **GET** /api/v2/Logs/{ID} | Get a log by ID
[**logsGetLogs**](LogsApi.md#logsGetLogs) | **GET** /api/v2/Logs | Get the API System logs, most recent first.
[**logsPostLog**](LogsApi.md#logsPostLog) | **POST** /api/v2/Logs | Add a Log entry



## logsGetLog

> APIModelsLog logsGetLog(ID)

Get a log by ID

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LogsApi();
let ID = "ID_example"; // String | The Log ID
apiInstance.logsGetLog(ID, (error, data, response) => {
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
 **ID** | **String**| The Log ID | 

### Return type

[**APIModelsLog**](APIModelsLog.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## logsGetLogs

> APIPagedResponseAPIModelsLog logsGetLogs(opts)

Get the API System logs, most recent first.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LogsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.logsGetLogs(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseAPIModelsLog**](APIPagedResponseAPIModelsLog.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## logsPostLog

> String logsPostLog(message)

Add a Log entry

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.LogsApi();
let message = "message_example"; // String | Message to enter into the log
apiInstance.logsPostLog(message, (error, data, response) => {
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
 **message** | **String**| Message to enter into the log | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

