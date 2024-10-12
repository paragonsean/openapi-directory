# TwilioEvents.EventsV1SubscriptionApi

All URIs are relative to *https://events.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSubscription**](EventsV1SubscriptionApi.md#createSubscription) | **POST** /v1/Subscriptions | 
[**deleteSubscription**](EventsV1SubscriptionApi.md#deleteSubscription) | **DELETE** /v1/Subscriptions/{Sid} | 
[**fetchSubscription**](EventsV1SubscriptionApi.md#fetchSubscription) | **GET** /v1/Subscriptions/{Sid} | 
[**listSubscription**](EventsV1SubscriptionApi.md#listSubscription) | **GET** /v1/Subscriptions | 
[**updateSubscription**](EventsV1SubscriptionApi.md#updateSubscription) | **POST** /v1/Subscriptions/{Sid} | 



## createSubscription

> EventsV1Subscription createSubscription(description, sinkSid, types)



Create a new Subscription.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SubscriptionApi();
let description = "description_example"; // String | A human readable description for the Subscription **This value should not contain PII.**
let sinkSid = "sinkSid_example"; // String | The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
let types = [null]; // [Object] | An array of objects containing the subscribed Event Types
apiInstance.createSubscription(description, sinkSid, types, (error, data, response) => {
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
 **description** | **String**| A human readable description for the Subscription **This value should not contain PII.** | 
 **sinkSid** | **String**| The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created. | 
 **types** | [**[Object]**](Object.md)| An array of objects containing the subscribed Event Types | 

### Return type

[**EventsV1Subscription**](EventsV1Subscription.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSubscription

> deleteSubscription(sid)



Delete a specific Subscription.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SubscriptionApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Subscription.
apiInstance.deleteSubscription(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this Subscription. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSubscription

> EventsV1Subscription fetchSubscription(sid)



Fetch a specific Subscription.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SubscriptionApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Subscription.
apiInstance.fetchSubscription(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this Subscription. | 

### Return type

[**EventsV1Subscription**](EventsV1Subscription.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSubscription

> ListSubscriptionResponse listSubscription(opts)



Retrieve a paginated list of Subscriptions belonging to the account used to make the request.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SubscriptionApi();
let opts = {
  'sinkSid': "sinkSid_example", // String | The SID of the sink that the list of Subscriptions should be filtered by.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSubscription(opts, (error, data, response) => {
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
 **sinkSid** | **String**| The SID of the sink that the list of Subscriptions should be filtered by. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSubscriptionResponse**](ListSubscriptionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSubscription

> EventsV1Subscription updateSubscription(sid, opts)



Update a Subscription.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SubscriptionApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Subscription.
let opts = {
  'description': "description_example", // String | A human readable description for the Subscription.
  'sinkSid': "sinkSid_example" // String | The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created.
};
apiInstance.updateSubscription(sid, opts, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this Subscription. | 
 **description** | **String**| A human readable description for the Subscription. | [optional] 
 **sinkSid** | **String**| The SID of the sink that events selected by this subscription should be sent to. Sink must be active for the subscription to be created. | [optional] 

### Return type

[**EventsV1Subscription**](EventsV1Subscription.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

