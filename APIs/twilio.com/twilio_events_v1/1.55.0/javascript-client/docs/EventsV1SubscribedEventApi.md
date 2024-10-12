# TwilioEvents.EventsV1SubscribedEventApi

All URIs are relative to *https://events.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSubscribedEvent**](EventsV1SubscribedEventApi.md#createSubscribedEvent) | **POST** /v1/Subscriptions/{SubscriptionSid}/SubscribedEvents | 
[**deleteSubscribedEvent**](EventsV1SubscribedEventApi.md#deleteSubscribedEvent) | **DELETE** /v1/Subscriptions/{SubscriptionSid}/SubscribedEvents/{Type} | 
[**fetchSubscribedEvent**](EventsV1SubscribedEventApi.md#fetchSubscribedEvent) | **GET** /v1/Subscriptions/{SubscriptionSid}/SubscribedEvents/{Type} | 
[**listSubscribedEvent**](EventsV1SubscribedEventApi.md#listSubscribedEvent) | **GET** /v1/Subscriptions/{SubscriptionSid}/SubscribedEvents | 
[**updateSubscribedEvent**](EventsV1SubscribedEventApi.md#updateSubscribedEvent) | **POST** /v1/Subscriptions/{SubscriptionSid}/SubscribedEvents/{Type} | 



## createSubscribedEvent

> EventsV1SubscriptionSubscribedEvent createSubscribedEvent(subscriptionSid, type, opts)



Add an event type to a Subscription.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SubscribedEventApi();
let subscriptionSid = "subscriptionSid_example"; // String | The unique SID identifier of the Subscription.
let type = "type_example"; // String | Type of event being subscribed to.
let opts = {
  'schemaVersion': 56 // Number | The schema version that the Subscription should use.
};
apiInstance.createSubscribedEvent(subscriptionSid, type, opts, (error, data, response) => {
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
 **subscriptionSid** | **String**| The unique SID identifier of the Subscription. | 
 **type** | **String**| Type of event being subscribed to. | 
 **schemaVersion** | **Number**| The schema version that the Subscription should use. | [optional] 

### Return type

[**EventsV1SubscriptionSubscribedEvent**](EventsV1SubscriptionSubscribedEvent.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSubscribedEvent

> deleteSubscribedEvent(subscriptionSid, type)



Remove an event type from a Subscription.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SubscribedEventApi();
let subscriptionSid = "subscriptionSid_example"; // String | The unique SID identifier of the Subscription.
let type = "type_example"; // String | Type of event being subscribed to.
apiInstance.deleteSubscribedEvent(subscriptionSid, type, (error, data, response) => {
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
 **subscriptionSid** | **String**| The unique SID identifier of the Subscription. | 
 **type** | **String**| Type of event being subscribed to. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSubscribedEvent

> EventsV1SubscriptionSubscribedEvent fetchSubscribedEvent(subscriptionSid, type)



Read an Event for a Subscription.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SubscribedEventApi();
let subscriptionSid = "subscriptionSid_example"; // String | The unique SID identifier of the Subscription.
let type = "type_example"; // String | Type of event being subscribed to.
apiInstance.fetchSubscribedEvent(subscriptionSid, type, (error, data, response) => {
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
 **subscriptionSid** | **String**| The unique SID identifier of the Subscription. | 
 **type** | **String**| Type of event being subscribed to. | 

### Return type

[**EventsV1SubscriptionSubscribedEvent**](EventsV1SubscriptionSubscribedEvent.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSubscribedEvent

> ListSubscribedEventResponse listSubscribedEvent(subscriptionSid, opts)



Retrieve a list of all Subscribed Event types for a Subscription.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SubscribedEventApi();
let subscriptionSid = "subscriptionSid_example"; // String | The unique SID identifier of the Subscription.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSubscribedEvent(subscriptionSid, opts, (error, data, response) => {
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
 **subscriptionSid** | **String**| The unique SID identifier of the Subscription. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSubscribedEventResponse**](ListSubscribedEventResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSubscribedEvent

> EventsV1SubscriptionSubscribedEvent updateSubscribedEvent(subscriptionSid, type, opts)



Update an Event for a Subscription.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SubscribedEventApi();
let subscriptionSid = "subscriptionSid_example"; // String | The unique SID identifier of the Subscription.
let type = "type_example"; // String | Type of event being subscribed to.
let opts = {
  'schemaVersion': 56 // Number | The schema version that the Subscription should use.
};
apiInstance.updateSubscribedEvent(subscriptionSid, type, opts, (error, data, response) => {
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
 **subscriptionSid** | **String**| The unique SID identifier of the Subscription. | 
 **type** | **String**| Type of event being subscribed to. | 
 **schemaVersion** | **Number**| The schema version that the Subscription should use. | [optional] 

### Return type

[**EventsV1SubscriptionSubscribedEvent**](EventsV1SubscriptionSubscribedEvent.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

