# TwilioEvents.EventsV1SinkApi

All URIs are relative to *https://events.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSink**](EventsV1SinkApi.md#createSink) | **POST** /v1/Sinks | 
[**deleteSink**](EventsV1SinkApi.md#deleteSink) | **DELETE** /v1/Sinks/{Sid} | 
[**fetchSink**](EventsV1SinkApi.md#fetchSink) | **GET** /v1/Sinks/{Sid} | 
[**listSink**](EventsV1SinkApi.md#listSink) | **GET** /v1/Sinks | 
[**updateSink**](EventsV1SinkApi.md#updateSink) | **POST** /v1/Sinks/{Sid} | 



## createSink

> EventsV1Sink createSink(description, sinkConfiguration, sinkType)



Create a new Sink

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SinkApi();
let description = "description_example"; // String | A human readable description for the Sink **This value should not contain PII.**
let sinkConfiguration = null; // Object | The information required for Twilio to connect to the provided Sink encoded as JSON.
let sinkType = "sinkType_example"; // SinkEnumSinkType | 
apiInstance.createSink(description, sinkConfiguration, sinkType, (error, data, response) => {
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
 **description** | **String**| A human readable description for the Sink **This value should not contain PII.** | 
 **sinkConfiguration** | [**Object**](Object.md)| The information required for Twilio to connect to the provided Sink encoded as JSON. | 
 **sinkType** | **SinkEnumSinkType**|  | 

### Return type

[**EventsV1Sink**](EventsV1Sink.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSink

> deleteSink(sid)



Delete a specific Sink.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SinkApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Sink.
apiInstance.deleteSink(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this Sink. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSink

> EventsV1Sink fetchSink(sid)



Fetch a specific Sink.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SinkApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Sink.
apiInstance.fetchSink(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this Sink. | 

### Return type

[**EventsV1Sink**](EventsV1Sink.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSink

> ListSinkResponse listSink(opts)



Retrieve a paginated list of Sinks belonging to the account used to make the request.

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SinkApi();
let opts = {
  'inUse': true, // Boolean | A boolean query parameter filtering the results to return sinks used/not used by a subscription.
  'status': "status_example", // String | A String query parameter filtering the results by status `initialized`, `validating`, `active` or `failed`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSink(opts, (error, data, response) => {
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
 **inUse** | **Boolean**| A boolean query parameter filtering the results to return sinks used/not used by a subscription. | [optional] 
 **status** | **String**| A String query parameter filtering the results by status &#x60;initialized&#x60;, &#x60;validating&#x60;, &#x60;active&#x60; or &#x60;failed&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSinkResponse**](ListSinkResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSink

> EventsV1Sink updateSink(sid, description)



Update a specific Sink

### Example

```javascript
import TwilioEvents from 'twilio_events';
let defaultClient = TwilioEvents.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioEvents.EventsV1SinkApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Sink.
let description = "description_example"; // String | A human readable description for the Sink **This value should not contain PII.**
apiInstance.updateSink(sid, description, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this Sink. | 
 **description** | **String**| A human readable description for the Sink **This value should not contain PII.** | 

### Return type

[**EventsV1Sink**](EventsV1Sink.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

