# TwilioChat.ChatV2WebhookApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createChannelWebhook**](ChatV2WebhookApi.md#createChannelWebhook) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks | 
[**deleteChannelWebhook**](ChatV2WebhookApi.md#deleteChannelWebhook) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} | 
[**fetchChannelWebhook**](ChatV2WebhookApi.md#fetchChannelWebhook) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} | 
[**listChannelWebhook**](ChatV2WebhookApi.md#listChannelWebhook) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks | 
[**updateChannelWebhook**](ChatV2WebhookApi.md#updateChannelWebhook) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Webhooks/{Sid} | 



## createChannelWebhook

> ChatV2ServiceChannelChannelWebhook createChannelWebhook(serviceSid, channelSid, type, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to create the Webhook resource under.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Channel Webhook resource belongs to. This value can be the Channel resource's `sid` or `unique_name`.
let type = "type_example"; // ChannelWebhookEnumType | 
let opts = {
  'configurationFilters': ["null"], // [String] | The events that cause us to call the Channel Webhook. Used when `type` is `webhook`. This parameter takes only one event. To specify more than one event, repeat this parameter for each event. For the list of possible events, see [Webhook Event Triggers](https://www.twilio.com/docs/chat/webhook-events#webhook-event-trigger).
  'configurationFlowSid': "configurationFlowSid_example", // String | The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-api/flow) to call when an event in `configuration.filters` occurs. Used only when `type` is `studio`.
  'configurationMethod': "configurationMethod_example", // ChannelWebhookEnumMethod | 
  'configurationRetryCount': 56, // Number | The number of times to retry the webhook if the first attempt fails. Can be an integer between 0 and 3, inclusive, and the default is 0.
  'configurationTriggers': ["null"], // [String] | A string that will cause us to call the webhook when it is present in a message body. This parameter takes only one trigger string. To specify more than one, repeat this parameter for each trigger string up to a total of 5 trigger strings. Used only when `type` = `trigger`.
  'configurationUrl': "configurationUrl_example" // String | The URL of the webhook to call using the `configuration.method`.
};
apiInstance.createChannelWebhook(serviceSid, channelSid, type, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to create the Webhook resource under. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Channel Webhook resource belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **type** | **ChannelWebhookEnumType**|  | 
 **configurationFilters** | [**[String]**](String.md)| The events that cause us to call the Channel Webhook. Used when &#x60;type&#x60; is &#x60;webhook&#x60;. This parameter takes only one event. To specify more than one event, repeat this parameter for each event. For the list of possible events, see [Webhook Event Triggers](https://www.twilio.com/docs/chat/webhook-events#webhook-event-trigger). | [optional] 
 **configurationFlowSid** | **String**| The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-api/flow) to call when an event in &#x60;configuration.filters&#x60; occurs. Used only when &#x60;type&#x60; is &#x60;studio&#x60;. | [optional] 
 **configurationMethod** | **ChannelWebhookEnumMethod**|  | [optional] 
 **configurationRetryCount** | **Number**| The number of times to retry the webhook if the first attempt fails. Can be an integer between 0 and 3, inclusive, and the default is 0. | [optional] 
 **configurationTriggers** | [**[String]**](String.md)| A string that will cause us to call the webhook when it is present in a message body. This parameter takes only one trigger string. To specify more than one, repeat this parameter for each trigger string up to a total of 5 trigger strings. Used only when &#x60;type&#x60; &#x3D; &#x60;trigger&#x60;. | [optional] 
 **configurationUrl** | **String**| The URL of the webhook to call using the &#x60;configuration.method&#x60;. | [optional] 

### Return type

[**ChatV2ServiceChannelChannelWebhook**](ChatV2ServiceChannelChannelWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteChannelWebhook

> deleteChannelWebhook(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to delete the Webhook resource from.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to delete belongs to. This value can be the Channel resource's `sid` or `unique_name`.
let sid = "sid_example"; // String | The SID of the Channel Webhook resource to delete.
apiInstance.deleteChannelWebhook(serviceSid, channelSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to delete the Webhook resource from. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to delete belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **sid** | **String**| The SID of the Channel Webhook resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchChannelWebhook

> ChatV2ServiceChannelChannelWebhook fetchChannelWebhook(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to fetch the Webhook resource from.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to fetch belongs to. This value can be the Channel resource's `sid` or `unique_name`.
let sid = "sid_example"; // String | The SID of the Channel Webhook resource to fetch.
apiInstance.fetchChannelWebhook(serviceSid, channelSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to fetch the Webhook resource from. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to fetch belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **sid** | **String**| The SID of the Channel Webhook resource to fetch. | 

### Return type

[**ChatV2ServiceChannelChannelWebhook**](ChatV2ServiceChannelChannelWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelWebhook

> ListChannelWebhookResponse listChannelWebhook(serviceSid, channelSid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to read the resources from.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resources to read belong to. This value can be the Channel resource's `sid` or `unique_name`.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listChannelWebhook(serviceSid, channelSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel to read the resources from. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resources to read belong to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListChannelWebhookResponse**](ListChannelWebhookResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateChannelWebhook

> ChatV2ServiceChannelChannelWebhook updateChannelWebhook(serviceSid, channelSid, sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2WebhookApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel that has the Webhook resource to update.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to update belongs to. This value can be the Channel resource's `sid` or `unique_name`.
let sid = "sid_example"; // String | The SID of the Channel Webhook resource to update.
let opts = {
  'configurationFilters': ["null"], // [String] | The events that cause us to call the Channel Webhook. Used when `type` is `webhook`. This parameter takes only one event. To specify more than one event, repeat this parameter for each event. For the list of possible events, see [Webhook Event Triggers](https://www.twilio.com/docs/chat/webhook-events#webhook-event-trigger).
  'configurationFlowSid': "configurationFlowSid_example", // String | The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-api/flow) to call when an event in `configuration.filters` occurs. Used only when `type` = `studio`.
  'configurationMethod': "configurationMethod_example", // ChannelWebhookEnumMethod | 
  'configurationRetryCount': 56, // Number | The number of times to retry the webhook if the first attempt fails. Can be an integer between 0 and 3, inclusive, and the default is 0.
  'configurationTriggers': ["null"], // [String] | A string that will cause us to call the webhook when it is present in a message body. This parameter takes only one trigger string. To specify more than one, repeat this parameter for each trigger string up to a total of 5 trigger strings. Used only when `type` = `trigger`.
  'configurationUrl': "configurationUrl_example" // String | The URL of the webhook to call using the `configuration.method`.
};
apiInstance.updateChannelWebhook(serviceSid, channelSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) with the Channel that has the Webhook resource to update. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Channel Webhook resource to update belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **sid** | **String**| The SID of the Channel Webhook resource to update. | 
 **configurationFilters** | [**[String]**](String.md)| The events that cause us to call the Channel Webhook. Used when &#x60;type&#x60; is &#x60;webhook&#x60;. This parameter takes only one event. To specify more than one event, repeat this parameter for each event. For the list of possible events, see [Webhook Event Triggers](https://www.twilio.com/docs/chat/webhook-events#webhook-event-trigger). | [optional] 
 **configurationFlowSid** | **String**| The SID of the Studio [Flow](https://www.twilio.com/docs/studio/rest-api/flow) to call when an event in &#x60;configuration.filters&#x60; occurs. Used only when &#x60;type&#x60; &#x3D; &#x60;studio&#x60;. | [optional] 
 **configurationMethod** | **ChannelWebhookEnumMethod**|  | [optional] 
 **configurationRetryCount** | **Number**| The number of times to retry the webhook if the first attempt fails. Can be an integer between 0 and 3, inclusive, and the default is 0. | [optional] 
 **configurationTriggers** | [**[String]**](String.md)| A string that will cause us to call the webhook when it is present in a message body. This parameter takes only one trigger string. To specify more than one, repeat this parameter for each trigger string up to a total of 5 trigger strings. Used only when &#x60;type&#x60; &#x3D; &#x60;trigger&#x60;. | [optional] 
 **configurationUrl** | **String**| The URL of the webhook to call using the &#x60;configuration.method&#x60;. | [optional] 

### Return type

[**ChatV2ServiceChannelChannelWebhook**](ChatV2ServiceChannelChannelWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

