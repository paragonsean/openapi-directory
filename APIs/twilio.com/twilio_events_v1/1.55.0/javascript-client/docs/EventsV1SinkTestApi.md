# TwilioEvents.EventsV1SinkTestApi

All URIs are relative to *https://events.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSinkTest**](EventsV1SinkTestApi.md#createSinkTest) | **POST** /v1/Sinks/{Sid}/Test | 



## createSinkTest

> EventsV1SinkSinkTest createSinkTest(sid)



Create a new Sink Test Event for the given Sink.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SinkTestApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the Sink to be Tested.
apiInstance.createSinkTest(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies the Sink to be Tested. | 

### Return type

[**EventsV1SinkSinkTest**](EventsV1SinkSinkTest.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

