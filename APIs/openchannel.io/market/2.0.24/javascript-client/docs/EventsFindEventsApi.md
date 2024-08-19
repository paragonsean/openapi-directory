# OpenChannelMarketApi.EventsFindEventsApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventsEventIdGet**](EventsFindEventsApi.md#eventsEventIdGet) | **GET** /events/{eventId} | Returns an event



## eventsEventIdGet

> Event eventsEventIdGet(eventId)

Returns an event

- Results are returned for the market provided within the basic authentication credentials 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.EventsFindEventsApi();
let eventId = "eventId_example"; // String | The id of the event
apiInstance.eventsEventIdGet(eventId, (error, data, response) => {
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
 **eventId** | **String**| The id of the event | 

### Return type

[**Event**](Event.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

