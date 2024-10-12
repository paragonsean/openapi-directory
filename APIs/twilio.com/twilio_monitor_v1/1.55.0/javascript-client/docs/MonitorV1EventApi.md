# TwilioMonitor.MonitorV1EventApi

All URIs are relative to *https://monitor.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchEvent**](MonitorV1EventApi.md#fetchEvent) | **GET** /v1/Events/{Sid} | 
[**listEvent**](MonitorV1EventApi.md#listEvent) | **GET** /v1/Events | 



## fetchEvent

> MonitorV1Event fetchEvent(sid)





### Example

```javascript
import TwilioMonitor from 'twilio_monitor';
let defaultClient = TwilioMonitor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMonitor.MonitorV1EventApi();
let sid = "sid_example"; // String | The SID of the Event resource to fetch.
apiInstance.fetchEvent(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Event resource to fetch. | 

### Return type

[**MonitorV1Event**](MonitorV1Event.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEvent

> ListEventResponse listEvent(opts)



Returns a list of events in the account, sorted by event-date.

### Example

```javascript
import TwilioMonitor from 'twilio_monitor';
let defaultClient = TwilioMonitor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMonitor.MonitorV1EventApi();
let opts = {
  'actorSid': "actorSid_example", // String | Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials.
  'eventType': "eventType_example", // String | Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types).
  'resourceSid': "resourceSid_example", // String | Only include events that refer to this resource. Useful for discovering the history of a specific resource.
  'sourceIpAddress': "sourceIpAddress_example", // String | Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listEvent(opts, (error, data, response) => {
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
 **actorSid** | **String**| Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials. | [optional] 
 **eventType** | **String**| Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types). | [optional] 
 **resourceSid** | **String**| Only include events that refer to this resource. Useful for discovering the history of a specific resource. | [optional] 
 **sourceIpAddress** | **String**| Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console. | [optional] 
 **startDate** | **Date**| Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
 **endDate** | **Date**| Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListEventResponse**](ListEventResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

