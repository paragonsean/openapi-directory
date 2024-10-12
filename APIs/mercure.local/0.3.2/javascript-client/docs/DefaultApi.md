# TheMercureProtocol.DefaultApi

All URIs are relative to *http://mercure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wellKnownMercureGet**](DefaultApi.md#wellKnownMercureGet) | **GET** /.well-known/mercure | Subscribe to updates
[**wellKnownMercurePost**](DefaultApi.md#wellKnownMercurePost) | **POST** /.well-known/mercure | Publish an update
[**wellKnownMercureSubscriptionsGet**](DefaultApi.md#wellKnownMercureSubscriptionsGet) | **GET** /.well-known/mercure/subscriptions | Active subscriptions
[**wellKnownMercureSubscriptionsTopicGet**](DefaultApi.md#wellKnownMercureSubscriptionsTopicGet) | **GET** /.well-known/mercure/subscriptions/{topic} | Active subscriptions for the given topic
[**wellKnownMercureSubscriptionsTopicSubscriberGet**](DefaultApi.md#wellKnownMercureSubscriptionsTopicSubscriberGet) | **GET** /.well-known/mercure/subscriptions/{topic}/{subscriber} | Active subscription for the given topic and subscriber



## wellKnownMercureGet

> wellKnownMercureGet(topic, opts)

Subscribe to updates

### Example

```javascript
import TheMercureProtocol from 'the_mercure_protocol';
let defaultClient = TheMercureProtocol.ApiClient.instance;
// Configure API key authorization: Cookie
let Cookie = defaultClient.authentications['Cookie'];
Cookie.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Cookie.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheMercureProtocol.DefaultApi();
let topic = ["null"]; // [String] | The topic to get updates from, can be a URI template (RFC6570).
let opts = {
  'lastEventID': "lastEventID_example", // String | The last received event id, to retrieve missed events.
  'lastEventID2': "lastEventID_example" // String | The last received event id, to retrieve missed events, takes precedence over the query parameter.
};
apiInstance.wellKnownMercureGet(topic, opts, (error, data, response) => {
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
 **topic** | [**[String]**](String.md)| The topic to get updates from, can be a URI template (RFC6570). | 
 **lastEventID** | **String**| The last received event id, to retrieve missed events. | [optional] 
 **lastEventID2** | **String**| The last received event id, to retrieve missed events, takes precedence over the query parameter. | [optional] 

### Return type

null (empty response body)

### Authorization

[Cookie](../README.md#Cookie), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/event-stream


## wellKnownMercurePost

> wellKnownMercurePost(data, topic, opts)

Publish an update

### Example

```javascript
import TheMercureProtocol from 'the_mercure_protocol';
let defaultClient = TheMercureProtocol.ApiClient.instance;
// Configure API key authorization: Cookie
let Cookie = defaultClient.authentications['Cookie'];
Cookie.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Cookie.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheMercureProtocol.DefaultApi();
let data = "data_example"; // String | The content of the new version of this topic.
let topic = ["null"]; // [String] | IRIs of the updated topic. If this key is present several times, the first occurrence is considered to be the canonical URL of the topic, and other ones are considered to be alternate URLs.
let opts = {
  'id': "id_example", // String | The topic's revision identifier: it will be used as the SSE's `id` property.
  '_private': true, // Boolean | To mark an update as private. If not provided, this update will be public.
  'retry': 56, // Number | The SSE's `retry` property (the reconnection time).
  'type': "type_example" // String | The SSE's `event` property (a specific event type).
};
apiInstance.wellKnownMercurePost(data, topic, opts, (error, data, response) => {
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
 **data** | **String**| The content of the new version of this topic. | 
 **topic** | [**[String]**](String.md)| IRIs of the updated topic. If this key is present several times, the first occurrence is considered to be the canonical URL of the topic, and other ones are considered to be alternate URLs. | 
 **id** | **String**| The topic&#39;s revision identifier: it will be used as the SSE&#39;s &#x60;id&#x60; property. | [optional] 
 **_private** | **Boolean**| To mark an update as private. If not provided, this update will be public. | [optional] 
 **retry** | **Number**| The SSE&#39;s &#x60;retry&#x60; property (the reconnection time). | [optional] 
 **type** | **String**| The SSE&#39;s &#x60;event&#x60; property (a specific event type). | [optional] 

### Return type

null (empty response body)

### Authorization

[Cookie](../README.md#Cookie), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: text/plain


## wellKnownMercureSubscriptionsGet

> Subscriptions wellKnownMercureSubscriptionsGet()

Active subscriptions

### Example

```javascript
import TheMercureProtocol from 'the_mercure_protocol';
let defaultClient = TheMercureProtocol.ApiClient.instance;
// Configure API key authorization: Cookie
let Cookie = defaultClient.authentications['Cookie'];
Cookie.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Cookie.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheMercureProtocol.DefaultApi();
apiInstance.wellKnownMercureSubscriptionsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Subscriptions**](Subscriptions.md)

### Authorization

[Cookie](../README.md#Cookie), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json


## wellKnownMercureSubscriptionsTopicGet

> Subscriptions wellKnownMercureSubscriptionsTopicGet(topic)

Active subscriptions for the given topic

### Example

```javascript
import TheMercureProtocol from 'the_mercure_protocol';
let defaultClient = TheMercureProtocol.ApiClient.instance;
// Configure API key authorization: Cookie
let Cookie = defaultClient.authentications['Cookie'];
Cookie.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Cookie.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheMercureProtocol.DefaultApi();
let topic = "topic_example"; // String | 
apiInstance.wellKnownMercureSubscriptionsTopicGet(topic, (error, data, response) => {
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
 **topic** | **String**|  | 

### Return type

[**Subscriptions**](Subscriptions.md)

### Authorization

[Cookie](../README.md#Cookie), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json


## wellKnownMercureSubscriptionsTopicSubscriberGet

> Subscriptions wellKnownMercureSubscriptionsTopicSubscriberGet(topic, subscriber)

Active subscription for the given topic and subscriber

### Example

```javascript
import TheMercureProtocol from 'the_mercure_protocol';
let defaultClient = TheMercureProtocol.ApiClient.instance;
// Configure API key authorization: Cookie
let Cookie = defaultClient.authentications['Cookie'];
Cookie.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Cookie.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new TheMercureProtocol.DefaultApi();
let topic = "topic_example"; // String | 
let subscriber = "subscriber_example"; // String | 
apiInstance.wellKnownMercureSubscriptionsTopicSubscriberGet(topic, subscriber, (error, data, response) => {
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
 **topic** | **String**|  | 
 **subscriber** | **String**|  | 

### Return type

[**Subscriptions**](Subscriptions.md)

### Authorization

[Cookie](../README.md#Cookie), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/ld+json

