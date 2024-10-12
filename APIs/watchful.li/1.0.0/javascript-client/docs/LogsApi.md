# WatchfulLi.LogsApi

All URIs are relative to *https://watchful.li/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteLogById**](LogsApi.md#deleteLogById) | **DELETE** /logs/{id} | Delete a specific log
[**getExportLogs**](LogsApi.md#getExportLogs) | **GET** /logs/export | Get a CSV or PDF file contain the list of logs
[**getFieldsLogs**](LogsApi.md#getFieldsLogs) | **GET** /logs/metadata | Get the list of fields
[**getTypesLogs**](LogsApi.md#getTypesLogs) | **GET** /logs/types | Get the list of log types
[**logsGet**](LogsApi.md#logsGet) | **GET** /logs | Get a list of logs



## deleteLogById

> String deleteLogById(id)

Delete a specific log

Delete a specific log

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.LogsApi();
let id = 789; // Number | ID of log that needs to be deleted
apiInstance.deleteLogById(id, (error, data, response) => {
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
 **id** | **Number**| ID of log that needs to be deleted | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getExportLogs

> getExportLogs(format, opts)

Get a CSV or PDF file contain the list of logs

Returns a file contain the list of logs

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.LogsApi();
let format = "format_example"; // String | Format of exported file (PDF or CSV)
let opts = {
  'site': 789, // Number | Site id of the log
  'filterType': "filterType_example", // String | Type of the log
  'search': "search_example", // String | Do a 'LIKE' search, you can also use '%'
  'startdate': "startdate_example", // String | Logs after this date, format YYYY-MM-DD HH:MM:SS
  'enddate': "enddate_example", // String | Logs before this date, format YYYY-MM-DD HH:MM:SS
  'limit': 789, // Number | Number of object to return (max 100, default 25)
  'startid': 789 // Number | Start of the return (default 0)
};
apiInstance.getExportLogs(format, opts, (error, data, response) => {
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
 **format** | **String**| Format of exported file (PDF or CSV) | 
 **site** | **Number**| Site id of the log | [optional] 
 **filterType** | **String**| Type of the log | [optional] 
 **search** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **startdate** | **String**| Logs after this date, format YYYY-MM-DD HH:MM:SS | [optional] 
 **enddate** | **String**| Logs before this date, format YYYY-MM-DD HH:MM:SS | [optional] 
 **limit** | **Number**| Number of object to return (max 100, default 25) | [optional] 
 **startid** | **Number**| Start of the return (default 0) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFieldsLogs

> String getFieldsLogs()

Get the list of fields

Returns a list of fields

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.LogsApi();
apiInstance.getFieldsLogs((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getTypesLogs

> String getTypesLogs()

Get the list of log types

Returns a list of log types

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.LogsApi();
apiInstance.getTypesLogs((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## logsGet

> Log logsGet(opts)

Get a list of logs

Returns a list of logs

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.LogsApi();
let opts = {
  'logType': "logType_example", // String | Type of the log
  'logEntry': "logEntry_example", // String | Do a 'LIKE' search, you can also use '%'
  'from': "from_example", // String | Logs after this date, format YYYY-MM-DD HH:MM:SS
  'to': "to_example", // String | Logs before this date, format YYYY-MM-DD HH:MM:SS
  'fields': "fields_example", // String | Fields to return separate by comas: name,id
  'limit': 789, // Number | Number of object to return (max 100, default 25)
  'limitstart': 789, // Number | Start of the return (default 0)
  'order': "order_example" // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
};
apiInstance.logsGet(opts, (error, data, response) => {
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
 **logType** | **String**| Type of the log | [optional] 
 **logEntry** | **String**| Do a &#39;LIKE&#39; search, you can also use &#39;%&#39; | [optional] 
 **from** | **String**| Logs after this date, format YYYY-MM-DD HH:MM:SS | [optional] 
 **to** | **String**| Logs before this date, format YYYY-MM-DD HH:MM:SS | [optional] 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 
 **limit** | **Number**| Number of object to return (max 100, default 25) | [optional] 
 **limitstart** | **Number**| Start of the return (default 0) | [optional] 
 **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] 

### Return type

[**Log**](Log.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain

