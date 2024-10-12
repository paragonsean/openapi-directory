# Signl4Api.EventsApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventsEventIdOverviewGet**](EventsApi.md#eventsEventIdOverviewGet) | **GET** /events/{eventId}/overview | Get overview event
[**eventsEventIdParametersGet**](EventsApi.md#eventsEventIdParametersGet) | **GET** /events/{eventId}/parameters | Get event parameters
[**eventsPagedPost**](EventsApi.md#eventsPagedPost) | **POST** /events/paged | Get overview event paged.



## eventsEventIdOverviewGet

> OverviewEvent eventsEventIdOverviewGet(eventId)

Get overview event

Get overview event by id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.EventsApi();
let eventId = "eventId_example"; // String | Id of event to get.
apiInstance.eventsEventIdOverviewGet(eventId, (error, data, response) => {
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
 **eventId** | **String**| Id of event to get. | 

### Return type

[**OverviewEvent**](OverviewEvent.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## eventsEventIdParametersGet

> [EventParameterInfo] eventsEventIdParametersGet(eventId)

Get event parameters

Get parameters of an event by id.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.EventsApi();
let eventId = "eventId_example"; // String | Event Id of the requested Alert.
apiInstance.eventsEventIdParametersGet(eventId, (error, data, response) => {
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
 **eventId** | **String**| Event Id of the requested Alert. | 

### Return type

[**[EventParameterInfo]**](EventParameterInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## eventsPagedPost

> OverviewEventPagedResultsPublic eventsPagedPost(opts)

Get overview event paged.

Get overview event paged. If there are more results, you also get a continuation token which you can add to the event filter.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.EventsApi();
let opts = {
  'maxResults': 56, // Number | Defines the limit of retrieved alert details per request. 1 to 100 are allowed per request.                   Number of alerts could be less if filtered but at least 1.
  'eventFilter': new Signl4Api.EventFilter() // EventFilter | The filter defines which alerts are supposed to be retrieved.
};
apiInstance.eventsPagedPost(opts, (error, data, response) => {
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
 **maxResults** | **Number**| Defines the limit of retrieved alert details per request. 1 to 100 are allowed per request.                   Number of alerts could be less if filtered but at least 1. | [optional] 
 **eventFilter** | [**EventFilter**](EventFilter.md)| The filter defines which alerts are supposed to be retrieved. | [optional] 

### Return type

[**OverviewEventPagedResultsPublic**](OverviewEventPagedResultsPublic.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain

