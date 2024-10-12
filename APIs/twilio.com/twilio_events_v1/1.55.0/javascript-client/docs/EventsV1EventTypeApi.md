# TwilioEvents.EventsV1EventTypeApi

All URIs are relative to *https://events.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchEventType**](EventsV1EventTypeApi.md#fetchEventType) | **GET** /v1/Types/{Type} | 
[**listEventType**](EventsV1EventTypeApi.md#listEventType) | **GET** /v1/Types | 



## fetchEventType

> EventsV1EventType fetchEventType(type)



Fetch a specific Event Type.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1EventTypeApi();
let type = "type_example"; // String | A string that uniquely identifies this Event Type.
apiInstance.fetchEventType(type, (error, data, response) => {
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
 **type** | **String**| A string that uniquely identifies this Event Type. | 

### Return type

[**EventsV1EventType**](EventsV1EventType.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEventType

> ListEventTypeResponse listEventType(opts)



Retrieve a paginated list of all the available Event Types.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1EventTypeApi();
let opts = {
  'schemaId': "schemaId_example", // String | A string parameter filtering the results to return only the Event Types using a given schema.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listEventType(opts, (error, data, response) => {
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
 **schemaId** | **String**| A string parameter filtering the results to return only the Event Types using a given schema. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListEventTypeResponse**](ListEventTypeResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

