# TwilioChat.ChatV2MessageApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMessage**](ChatV2MessageApi.md#createMessage) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages | 
[**deleteMessage**](ChatV2MessageApi.md#deleteMessage) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} | 
[**fetchMessage**](ChatV2MessageApi.md#fetchMessage) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} | 
[**listMessage**](ChatV2MessageApi.md#listMessage) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages | 
[**updateMessage**](ChatV2MessageApi.md#updateMessage) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Messages/{Sid} | 



## createMessage

> ChatV2ServiceChannelMessage createMessage(serviceSid, channelSid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2MessageApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Message resource under.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Message resource belongs to. This value can be the Channel resource's `sid` or `unique_name`.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // MessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | A valid JSON string that contains application-specific data.
  'body': "body_example", // String | The message to send to the channel. Can be an empty string or `null`, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat's history is being recreated from a backup/separate source.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
  'from': "from_example", // String | The [Identity](https://www.twilio.com/docs/chat/identity) of the new message's author. The default value is `system`.
  'lastUpdatedBy': "lastUpdatedBy_example", // String | The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable.
  'mediaSid': "mediaSid_example" // String | The SID of the [Media](https://www.twilio.com/docs/chat/rest/media) to attach to the new Message.
};
apiInstance.createMessage(serviceSid, channelSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Message resource under. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Message resource belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **xTwilioWebhookEnabled** | **MessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] 
 **body** | **String**| The message to send to the channel. Can be an empty string or &#x60;null&#x60;, which sets the value as an empty string. You can send structured data in the body by serializing it as a string. | [optional] 
 **dateCreated** | **Date**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat&#39;s history is being recreated from a backup/separate source. | [optional] 
 **dateUpdated** | **Date**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. | [optional] 
 **from** | **String**| The [Identity](https://www.twilio.com/docs/chat/identity) of the new message&#39;s author. The default value is &#x60;system&#x60;. | [optional] 
 **lastUpdatedBy** | **String**| The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable. | [optional] 
 **mediaSid** | **String**| The SID of the [Media](https://www.twilio.com/docs/chat/rest/media) to attach to the new Message. | [optional] 

### Return type

[**ChatV2ServiceChannelMessage**](ChatV2ServiceChannelMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteMessage

> deleteMessage(serviceSid, channelSid, sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2MessageApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Message resource from.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to delete belongs to. This value can be the Channel resource's `sid` or `unique_name`.
let sid = "sid_example"; // String | The SID of the Message resource to delete.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // MessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteMessage(serviceSid, channelSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Message resource from. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to delete belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **sid** | **String**| The SID of the Message resource to delete. | 
 **xTwilioWebhookEnabled** | **MessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchMessage

> ChatV2ServiceChannelMessage fetchMessage(serviceSid, channelSid, sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2MessageApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Message resource from.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to fetch belongs to. This value can be the Channel resource's `sid` or `unique_name`.
let sid = "sid_example"; // String | The SID of the Message resource to fetch.
apiInstance.fetchMessage(serviceSid, channelSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Message resource from. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to fetch belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **sid** | **String**| The SID of the Message resource to fetch. | 

### Return type

[**ChatV2ServiceChannelMessage**](ChatV2ServiceChannelMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMessage

> ListMessageResponse listMessage(serviceSid, channelSid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2MessageApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Message resources from.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to read belongs to. This value can be the Channel resource's `sid` or `unique_name`.
let opts = {
  'order': "order_example", // MessageEnumOrderType | The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending) with `asc` as the default.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMessage(serviceSid, channelSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Message resources from. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to read belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **order** | **MessageEnumOrderType**| The sort order of the returned messages. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;asc&#x60; as the default. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMessageResponse**](ListMessageResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMessage

> ChatV2ServiceChannelMessage updateMessage(serviceSid, channelSid, sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2MessageApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Message resource in.
let channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to update belongs to. This value can be the Channel resource's `sid` or `unique_name`.
let sid = "sid_example"; // String | The SID of the Message resource to update.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // MessageEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | A valid JSON string that contains application-specific data.
  'body': "body_example", // String | The message to send to the channel. Can be an empty string or `null`, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat's history is being recreated from a backup/separate source.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
  'from': "from_example", // String | The [Identity](https://www.twilio.com/docs/chat/identity) of the message's author.
  'lastUpdatedBy': "lastUpdatedBy_example" // String | The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable.
};
apiInstance.updateMessage(serviceSid, channelSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Message resource in. | 
 **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to update belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | 
 **sid** | **String**| The SID of the Message resource to update. | 
 **xTwilioWebhookEnabled** | **MessageEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] 
 **body** | **String**| The message to send to the channel. Can be an empty string or &#x60;null&#x60;, which sets the value as an empty string. You can send structured data in the body by serializing it as a string. | [optional] 
 **dateCreated** | **Date**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat&#39;s history is being recreated from a backup/separate source. | [optional] 
 **dateUpdated** | **Date**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. | [optional] 
 **from** | **String**| The [Identity](https://www.twilio.com/docs/chat/identity) of the message&#39;s author. | [optional] 
 **lastUpdatedBy** | **String**| The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable. | [optional] 

### Return type

[**ChatV2ServiceChannelMessage**](ChatV2ServiceChannelMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

