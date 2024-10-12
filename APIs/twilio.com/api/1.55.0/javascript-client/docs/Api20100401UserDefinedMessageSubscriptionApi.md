# TwilioApi.Api20100401UserDefinedMessageSubscriptionApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUserDefinedMessageSubscription**](Api20100401UserDefinedMessageSubscriptionApi.md#createUserDefinedMessageSubscription) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions.json | 
[**deleteUserDefinedMessageSubscription**](Api20100401UserDefinedMessageSubscriptionApi.md#deleteUserDefinedMessageSubscription) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/UserDefinedMessageSubscriptions/{Sid}.json | 



## createUserDefinedMessageSubscription

> ApiV2010AccountCallUserDefinedMessageSubscription createUserDefinedMessageSubscription(accountSid, callSid, callback, opts)



Subscribe to User Defined Messages for a given Call SID.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401UserDefinedMessageSubscriptionApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
let callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Messages subscription is associated with. This refers to the Call SID that is producing the user defined messages.
let callback = "callback_example"; // String | The URL we should call using the `method` to send user defined events to your application. URLs must contain a valid hostname (underscores are not permitted).
let opts = {
  'idempotencyKey': "idempotencyKey_example", // String | A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated.
  'method': "method_example" // String | The HTTP method Twilio will use when requesting the above `Url`. Either `GET` or `POST`. Default is `POST`.
};
apiInstance.createUserDefinedMessageSubscription(accountSid, callSid, callback, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages. | 
 **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Messages subscription is associated with. This refers to the Call SID that is producing the user defined messages. | 
 **callback** | **String**| The URL we should call using the &#x60;method&#x60; to send user defined events to your application. URLs must contain a valid hostname (underscores are not permitted). | 
 **idempotencyKey** | **String**| A unique string value to identify API call. This should be a unique string value per API call and can be a randomly generated. | [optional] 
 **method** | **String**| The HTTP method Twilio will use when requesting the above &#x60;Url&#x60;. Either &#x60;GET&#x60; or &#x60;POST&#x60;. Default is &#x60;POST&#x60;. | [optional] 

### Return type

[**ApiV2010AccountCallUserDefinedMessageSubscription**](ApiV2010AccountCallUserDefinedMessageSubscription.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteUserDefinedMessageSubscription

> deleteUserDefinedMessageSubscription(accountSid, callSid, sid)



Delete a specific User Defined Message Subscription.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401UserDefinedMessageSubscriptionApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages.
let callSid = "callSid_example"; // String | The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages.
let sid = "sid_example"; // String | The SID that uniquely identifies this User Defined Message Subscription.
apiInstance.deleteUserDefinedMessageSubscription(accountSid, callSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that subscribed to the User Defined Messages. | 
 **callSid** | **String**| The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the User Defined Message Subscription is associated with. This refers to the Call SID that is producing the User Defined Messages. | 
 **sid** | **String**| The SID that uniquely identifies this User Defined Message Subscription. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

