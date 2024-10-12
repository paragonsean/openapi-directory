# CleverCloudApi.EventsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventsEventSocketGet_0**](EventsApi.md#eventsEventSocketGet_0) | **GET** /events/event-socket | 
[**notificationsInfoEventsGet_0**](EventsApi.md#notificationsInfoEventsGet_0) | **GET** /notifications/info/events | 



## eventsEventSocketGet_0

> eventsEventSocketGet_0()



Retrieve events as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.EventsApi();
apiInstance.eventsEventSocketGet_0((error, data, response) => {
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


## notificationsInfoEventsGet_0

> notificationsInfoEventsGet_0()



list available events

### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.EventsApi();
apiInstance.notificationsInfoEventsGet_0((error, data, response) => {
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

