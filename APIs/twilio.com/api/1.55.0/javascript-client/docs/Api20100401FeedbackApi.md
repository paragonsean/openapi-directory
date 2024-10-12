# TwilioApi.Api20100401FeedbackApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMessageFeedback**](Api20100401FeedbackApi.md#createMessageFeedback) | **POST** /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Feedback.json | 



## createMessageFeedback

> ApiV2010AccountMessageMessageFeedback createMessageFeedback(accountSid, messageSid, opts)



Create Message Feedback to confirm a tracked user action was performed by the recipient of the associated Message

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401FeedbackApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource for which to create MessageFeedback.
let messageSid = "messageSid_example"; // String | The SID of the Message resource for which to create MessageFeedback.
let opts = {
  'outcome': "outcome_example" // MessageFeedbackEnumOutcome | 
};
apiInstance.createMessageFeedback(accountSid, messageSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) associated with the Message resource for which to create MessageFeedback. | 
 **messageSid** | **String**| The SID of the Message resource for which to create MessageFeedback. | 
 **outcome** | **MessageFeedbackEnumOutcome**|  | [optional] 

### Return type

[**ApiV2010AccountMessageMessageFeedback**](ApiV2010AccountMessageMessageFeedback.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

