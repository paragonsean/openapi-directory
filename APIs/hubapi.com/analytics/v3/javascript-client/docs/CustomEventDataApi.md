# EventsSendEventCompletions.CustomEventDataApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postEventsV3SendSend**](CustomEventDataApi.md#postEventsV3SendSend) | **POST** /events/v3/send | Send custom event completion



## postEventsV3SendSend

> postEventsV3SendSend(behavioralEventHttpCompletionRequest)

Send custom event completion

Endpoint to send an instance of a custom event.

### Example

```javascript
import EventsSendEventCompletions from 'events_send_event_completions';
let defaultClient = EventsSendEventCompletions.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new EventsSendEventCompletions.CustomEventDataApi();
let behavioralEventHttpCompletionRequest = new EventsSendEventCompletions.BehavioralEventHttpCompletionRequest(); // BehavioralEventHttpCompletionRequest | 
apiInstance.postEventsV3SendSend(behavioralEventHttpCompletionRequest, (error, data, response) => {
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
 **behavioralEventHttpCompletionRequest** | [**BehavioralEventHttpCompletionRequest**](BehavioralEventHttpCompletionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

