# SlackWebApi.RtmApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rtmConnect**](RtmApi.md#rtmConnect) | **GET** /rtm.connect | 



## rtmConnect

> RtmConnectSchema rtmConnect(token, opts)



Starts a Real Time Messaging session.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.RtmApi();
let token = "token_example"; // String | Authentication token. Requires scope: `rtm:stream`
let opts = {
  'batchPresenceAware': true, // Boolean | Batch presence deliveries via subscription. Enabling changes the shape of `presence_change` events. See [batch presence](/docs/presence-and-status#batching).
  'presenceSub': true // Boolean | Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions).
};
apiInstance.rtmConnect(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;rtm:stream&#x60; | 
 **batchPresenceAware** | **Boolean**| Batch presence deliveries via subscription. Enabling changes the shape of &#x60;presence_change&#x60; events. See [batch presence](/docs/presence-and-status#batching). | [optional] 
 **presenceSub** | **Boolean**| Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions). | [optional] 

### Return type

[**RtmConnectSchema**](RtmConnectSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

