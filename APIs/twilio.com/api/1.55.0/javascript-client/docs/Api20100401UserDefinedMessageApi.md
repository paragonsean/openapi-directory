# TwilioApi.Api20100401UserDefinedMessageApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUserDefinedMessage**](Api20100401UserDefinedMessageApi.md#createUserDefinedMessage) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessages.json | 



## createUserDefinedMessage

> ApiV2010AccountCallUserDefinedMessage createUserDefinedMessage(accountSid, callSid, content, opts)



Create a new User Defined Message for the given Call SID.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401UserDefinedMessageApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created User Defined Message.
let callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message is associated with.
let content = "content_example"; // String | The User Defined Message in the form of URL-encoded JSON string.
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.
};
apiInstance.createUserDefinedMessage(accountSid, callSid, content, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created User Defined Message. | 
 **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message is associated with. | 
 **content** | **String**| The User Defined Message in the form of URL-encoded JSON string. | 
 **idempotencyKey** | **String**| A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated. | [optional] 

### Return type

[**ApiV2010AccountCallUserDefinedMessage**](ApiV2010AccountCallUserDefinedMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

