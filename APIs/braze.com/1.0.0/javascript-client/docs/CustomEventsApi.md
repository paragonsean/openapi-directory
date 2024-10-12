# BrazeEndpoints.CustomEventsApi

All URIs are relative to *https://rest.iad-01.braze.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customEventsAnalytics_0**](CustomEventsApi.md#customEventsAnalytics_0) | **GET** /events/data_series | Custom Events Analytics
[**customEventsList_0**](CustomEventsApi.md#customEventsList_0) | **GET** /events/list | Custom Events List



## customEventsAnalytics_0

> customEventsAnalytics_0(opts)

Custom Events Analytics

This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.  ### Components Used -[Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;count\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.CustomEventsApi();
let opts = {
  'event': "event_name", // String | (Required) String  The name of the custom event for which to return analytics 
  'length': "24", // String | (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive
  'unit': "hour", // String | (Optional) String  Unit of time between data points - can be \"day\" or \"hour\" (defaults to \"day\")
  'endingAt': "2014-12-10T23:59:59-05:00", // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
  'appId': "{{app_identifier}}", // String | (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app
  'segmentId': "{{segment_identifier}}" // String | (Optional) String  Segment API identifier indicating the analytics enabled segment for which event analytics should be returned
};
apiInstance.customEventsAnalytics_0(opts, (error, data, response) => {
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
 **event** | **String**| (Required) String  The name of the custom event for which to return analytics  | [optional] 
 **length** | **String**| (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] 
 **unit** | **String**| (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;) | [optional] 
 **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] 
 **appId** | **String**| (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app | [optional] 
 **segmentId** | **String**| (Optional) String  Segment API identifier indicating the analytics enabled segment for which event analytics should be returned | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## customEventsList_0

> customEventsList_0(opts)

Custom Events List

This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;events\&quot; : [         \&quot;Event A\&quot;,         \&quot;Event B\&quot;,         \&quot;Event C\&quot;,         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes  The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.CustomEventsApi();
let opts = {
  'page': "3" // String | (Optional) Integer  The page of event names to return, defaults to 0 (returns the first set of up to 250)
};
apiInstance.customEventsList_0(opts, (error, data, response) => {
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
 **page** | **String**| (Optional) Integer  The page of event names to return, defaults to 0 (returns the first set of up to 250) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

