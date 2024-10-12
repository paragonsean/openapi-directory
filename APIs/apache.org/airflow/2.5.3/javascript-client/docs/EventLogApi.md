# AirflowApiStable.EventLogApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEventLog**](EventLogApi.md#getEventLog) | **GET** /eventLogs/{event_log_id} | Get a log entry
[**getEventLogs**](EventLogApi.md#getEventLogs) | **GET** /eventLogs | List log entries



## getEventLog

> EventLog getEventLog(eventLogId)

Get a log entry

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.EventLogApi();
let eventLogId = 56; // Number | The event log ID.
apiInstance.getEventLog(eventLogId, (error, data, response) => {
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
 **eventLogId** | **Number**| The event log ID. | 

### Return type

[**EventLog**](EventLog.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventLogs

> EventLogCollection getEventLogs(opts)

List log entries

List log entries from event log.

### Example

```javascript
import AirflowApiStable from 'airflow_api__stable';

let apiInstance = new AirflowApiStable.EventLogApi();
let opts = {
  'limit': 100, // Number | The numbers of items to return.
  'offset': 56, // Number | The number of items to skip before starting to collect the result set.
  'orderBy': "orderBy_example" // String | The name of the field to order the results by. Prefix a field name with `-` to reverse the sort order.  *New in version 2.1.0* 
};
apiInstance.getEventLogs(opts, (error, data, response) => {
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
 **limit** | **Number**| The numbers of items to return. | [optional] [default to 100]
 **offset** | **Number**| The number of items to skip before starting to collect the result set. | [optional] 
 **orderBy** | **String**| The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 

### Return type

[**EventLogCollection**](EventLogCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

