# TwilioEvents.EventsV1SinkValidateApi

All URIs are relative to *https://events.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSinkValidate**](EventsV1SinkValidateApi.md#createSinkValidate) | **POST** /v1/Sinks/{Sid}/Validate | 



## createSinkValidate

> EventsV1SinkSinkValidate createSinkValidate(sid, testId)



Validate that a test event for a Sink was received.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SinkValidateApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the Sink being validated.
let testId = "testId_example"; // String | A 34 character string that uniquely identifies the test event for a Sink being validated.
apiInstance.createSinkValidate(sid, testId, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies the Sink being validated. | 
 **testId** | **String**| A 34 character string that uniquely identifies the test event for a Sink being validated. | 

### Return type

[**EventsV1SinkSinkValidate**](EventsV1SinkSinkValidate.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

