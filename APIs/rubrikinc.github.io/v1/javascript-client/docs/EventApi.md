# RubrikRestApi.EventApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEventsCsvDownloadLink**](EventApi.md#getEventsCsvDownloadLink) | **GET** /event/csv_download_link | Download summary of events as a CSV file
[**queryEventV1**](EventApi.md#queryEventV1) | **GET** /event | Get information for all events
[**queryLatestEventsV1**](EventApi.md#queryLatestEventsV1) | **GET** /event/latest | Get latest events with their associated event series information



## getEventsCsvDownloadLink

> EventCsvDownloadResponse getEventsCsvDownloadLink(opts)

Download summary of events as a CSV file

Download summary of the related events that match the value specified in the following categories: event type, status, object name or ID, eventSeriesId, object type, and limit events by dates.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.EventApi();
let opts = {
  'limit': 56, // Number | Maximum number of events to retrieve. Default value is 100.
  'eventSeriesStatus': "eventSeriesStatus_example", // String | Filter by the current status of the event series.
  'eventStatus': "eventStatus_example", // String | Filter by the status of the latest event in the event series.
  'eventType': "eventType_example", // String | Filter by the type of the latest event in the event series.
  'eventSeverity': "eventSeverity_example", // String | Filter by the severity of the latest event in the event series.
  'objectIds': ["null"], // [String] | Filter the object IDs in the latest event series by matches to a comma-separated list of object IDs.
  'objectType': "objectType_example", // String | Filter the events in the event series by a specified object type.
  'objectName': "objectName_example", // String | Filter latest events according to the provided name using prefix search for resources and exact search for usernames.
  'afterId': "afterId_example", // String | An (event_series_id, time) tuple. When specified, returns all event series whose latest event timestamp comes after the time value of after_id based on the sort order defined by the order_by_time parameter.
  'beforeDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter out event series that have events occurring after the specified date.
  'afterDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter out event series that have events occurring before the specified date.
  'orderByTime': "orderByTime_example" // String | The events in a series are ordered by timestamp. Specify desc to show the latest entries first. Specify asc to show the oldest entries first. The default behavior is desc.
};
apiInstance.getEventsCsvDownloadLink(opts, (error, data, response) => {
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
 **limit** | **Number**| Maximum number of events to retrieve. Default value is 100. | [optional] 
 **eventSeriesStatus** | **String**| Filter by the current status of the event series. | [optional] 
 **eventStatus** | **String**| Filter by the status of the latest event in the event series. | [optional] 
 **eventType** | **String**| Filter by the type of the latest event in the event series. | [optional] 
 **eventSeverity** | **String**| Filter by the severity of the latest event in the event series. | [optional] 
 **objectIds** | [**[String]**](String.md)| Filter the object IDs in the latest event series by matches to a comma-separated list of object IDs. | [optional] 
 **objectType** | **String**| Filter the events in the event series by a specified object type. | [optional] 
 **objectName** | **String**| Filter latest events according to the provided name using prefix search for resources and exact search for usernames. | [optional] 
 **afterId** | **String**| An (event_series_id, time) tuple. When specified, returns all event series whose latest event timestamp comes after the time value of after_id based on the sort order defined by the order_by_time parameter. | [optional] 
 **beforeDate** | **Date**| Filter out event series that have events occurring after the specified date. | [optional] 
 **afterDate** | **Date**| Filter out event series that have events occurring before the specified date. | [optional] 
 **orderByTime** | **String**| The events in a series are ordered by timestamp. Specify desc to show the latest entries first. Specify asc to show the oldest entries first. The default behavior is desc. | [optional] 

### Return type

[**EventCsvDownloadResponse**](EventCsvDownloadResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryEventV1

> EventsAndSeriesSummariesV1 queryEventV1(opts)

Get information for all events

Returns information for all events. Only Global or Read Only Admins and Support users have authorization to use this endpoint. Accepts filters. For similar functionality to the previous /internal/event endpoint, use the /v1/event/latest endpoint.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.EventApi();
let opts = {
  'limit': 56, // Number | Maximum number of events retrieved.
  'afterId': "afterId_example", // String | An (event_id, time) tuple. When specified, returns all events with timestamps that come after the time value of after_id based on the sort order defined by the order_by_time parameter.
  'beforeDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter the events occurring after the specified date.
  'afterDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter the events occurring before the specified date.
  'orderByTime': "orderByTime_example", // String | The events are ordered by timestamp. Specify desc to show the latest entries first. Specify asc to show the oldest entries first. The default behavior is asc.
  'shouldIncludeEventSeries': true // Boolean | A Boolean value that determines whether to include event series summary for every event. If set to 'true', a list of event series summary will be returned and each summary has an empty list of events. If set to 'false', an empty list of event series summary will be returned. The default value is 'false'. Setting it to 'true' will increase the response time.
};
apiInstance.queryEventV1(opts, (error, data, response) => {
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
 **limit** | **Number**| Maximum number of events retrieved. | [optional] 
 **afterId** | **String**| An (event_id, time) tuple. When specified, returns all events with timestamps that come after the time value of after_id based on the sort order defined by the order_by_time parameter. | [optional] 
 **beforeDate** | **Date**| Filter the events occurring after the specified date. | [optional] 
 **afterDate** | **Date**| Filter the events occurring before the specified date. | [optional] 
 **orderByTime** | **String**| The events are ordered by timestamp. Specify desc to show the latest entries first. Specify asc to show the oldest entries first. The default behavior is asc. | [optional] 
 **shouldIncludeEventSeries** | **Boolean**| A Boolean value that determines whether to include event series summary for every event. If set to &#39;true&#39;, a list of event series summary will be returned and each summary has an empty list of events. If set to &#39;false&#39;, an empty list of event series summary will be returned. The default value is &#39;false&#39;. Setting it to &#39;true&#39; will increase the response time. | [optional] 

### Return type

[**EventsAndSeriesSummariesV1**](EventsAndSeriesSummariesV1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryLatestEventsV1

> ActivityLogSummaryV1ListResponse queryLatestEventsV1(opts)

Get latest events with their associated event series information

Get the latest event, event series status, and the number of warning events for all event series. This endpoint has similar/enhanced functionality to the previously deprecated /internal/event endpoint.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.EventApi();
let opts = {
  'limit': 56, // Number | Maximum number of events retrieved.
  'eventSeriesStatus': "eventSeriesStatus_example", // String | Filter by the current status of the event series.
  'eventStatus': "eventStatus_example", // String | Filter by the status of the latest event in the event series.
  'eventType': "eventType_example", // String | Filter by the type of the latest event in the event series.
  'eventSeverity': "eventSeverity_example", // String | Filter by the severity of the latest event in the event series.
  'objectIds': ["null"], // [String] | Filter the object IDs in the latest event series by matches to a comma-separated list of object IDs.
  'objectType': "objectType_example", // String | Filter the events in the event series by a specified object type.
  'objectName': "objectName_example", // String | Filter latest events according to the provided name using prefix search for resources and exact search for usernames.
  'afterId': "afterId_example", // String | An (event_series_id, time) tuple. When specified, returns all event series whose latest event timestamp comes after the time value of after_id based on the sort order defined by the order_by_time parameter.
  'beforeDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter out event series that have events occurring after the specified date.
  'afterDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter out event series that have events occurring before the specified date.
  'orderByTime': "orderByTime_example", // String | The events in a series are ordered by timestamp. Specify desc to show the latest entries first. Specify asc to show the oldest entries first. The default behavior is desc.
  'shouldIncludeEventSeries': true // Boolean | A Boolean value that determines whether to include all events in the event series. The default value is 'false'. Setting it to 'true' will significantly increase the response time.
};
apiInstance.queryLatestEventsV1(opts, (error, data, response) => {
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
 **limit** | **Number**| Maximum number of events retrieved. | [optional] 
 **eventSeriesStatus** | **String**| Filter by the current status of the event series. | [optional] 
 **eventStatus** | **String**| Filter by the status of the latest event in the event series. | [optional] 
 **eventType** | **String**| Filter by the type of the latest event in the event series. | [optional] 
 **eventSeverity** | **String**| Filter by the severity of the latest event in the event series. | [optional] 
 **objectIds** | [**[String]**](String.md)| Filter the object IDs in the latest event series by matches to a comma-separated list of object IDs. | [optional] 
 **objectType** | **String**| Filter the events in the event series by a specified object type. | [optional] 
 **objectName** | **String**| Filter latest events according to the provided name using prefix search for resources and exact search for usernames. | [optional] 
 **afterId** | **String**| An (event_series_id, time) tuple. When specified, returns all event series whose latest event timestamp comes after the time value of after_id based on the sort order defined by the order_by_time parameter. | [optional] 
 **beforeDate** | **Date**| Filter out event series that have events occurring after the specified date. | [optional] 
 **afterDate** | **Date**| Filter out event series that have events occurring before the specified date. | [optional] 
 **orderByTime** | **String**| The events in a series are ordered by timestamp. Specify desc to show the latest entries first. Specify asc to show the oldest entries first. The default behavior is desc. | [optional] 
 **shouldIncludeEventSeries** | **Boolean**| A Boolean value that determines whether to include all events in the event series. The default value is &#39;false&#39;. Setting it to &#39;true&#39; will significantly increase the response time. | [optional] 

### Return type

[**ActivityLogSummaryV1ListResponse**](ActivityLogSummaryV1ListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

