# SliceboxApi.LogsApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logDelete**](LogsApi.md#logDelete) | **DELETE** /log | 
[**logGet**](LogsApi.md#logGet) | **GET** /log | 
[**logIdDelete**](LogsApi.md#logIdDelete) | **DELETE** /log/{id} | 



## logDelete

> logDelete()



delete all log messages

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.LogsApi();
apiInstance.logDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logGet

> [LogEntry] logGet(opts)



get a list of slicebox log messages

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.LogsApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of log messages
  'count': 20, // Number | size of returned slice of log messages
  'subject': "subject_example", // String | log subject to filter results by
  'type': "type_example" // String | log type (DEFAULT, INFO, WARN, ERROR) to filter results by
};
apiInstance.logGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of log messages | [optional] [default to 0]
 **count** | **Number**| size of returned slice of log messages | [optional] [default to 20]
 **subject** | **String**| log subject to filter results by | [optional] 
 **type** | **String**| log type (DEFAULT, INFO, WARN, ERROR) to filter results by | [optional] 

### Return type

[**[LogEntry]**](LogEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## logIdDelete

> logIdDelete(id)



Delete the log entry with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.LogsApi();
let id = 789; // Number | ID of log entry
apiInstance.logIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of log entry | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

