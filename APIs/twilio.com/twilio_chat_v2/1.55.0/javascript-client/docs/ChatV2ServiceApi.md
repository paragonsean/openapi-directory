# TwilioChat.ChatV2ServiceApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createService**](ChatV2ServiceApi.md#createService) | **POST** /v2/Services | 
[**deleteService**](ChatV2ServiceApi.md#deleteService) | **DELETE** /v2/Services/{Sid} | 
[**fetchService**](ChatV2ServiceApi.md#fetchService) | **GET** /v2/Services/{Sid} | 
[**listService**](ChatV2ServiceApi.md#listService) | **GET** /v2/Services | 
[**updateService**](ChatV2ServiceApi.md#updateService) | **POST** /v2/Services/{Sid} | 



## createService

> ChatV2Service createService(friendlyName)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2ServiceApi();
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new resource.
apiInstance.createService(friendlyName, (error, data, response) => {
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
 **friendlyName** | **String**| A descriptive string that you create to describe the new resource. | 

### Return type

[**ChatV2Service**](ChatV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteService

> deleteService(sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2ServiceApi();
let sid = "sid_example"; // String | The SID of the Service resource to delete.
apiInstance.deleteService(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Service resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchService

> ChatV2Service fetchService(sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2ServiceApi();
let sid = "sid_example"; // String | The SID of the Service resource to fetch.
apiInstance.fetchService(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Service resource to fetch. | 

### Return type

[**ChatV2Service**](ChatV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listService

> ListServiceResponse listService(opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2ServiceApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listService(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateService

> ChatV2Service updateService(sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV2ServiceApi();
let sid = "sid_example"; // String | The SID of the Service resource to update.
let opts = {
  'consumptionReportInterval': 56, // Number | DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints.
  'defaultChannelCreatorRoleSid': "defaultChannelCreatorRoleSid_example", // String | The channel role assigned to a channel creator when they join a new channel. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles.
  'defaultChannelRoleSid': "defaultChannelRoleSid_example", // String | The channel role assigned to users when they are added to a channel. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles.
  'defaultServiceRoleSid': "defaultServiceRoleSid_example", // String | The service role assigned to users when they are added to the service. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource.
  'limitsChannelMembers': 56, // Number | The maximum number of Members that can be added to Channels within this Service. Can be up to 1,000.
  'limitsUserChannels': 56, // Number | The maximum number of Channels Users can be a Member of within this Service. Can be up to 1,000.
  'mediaCompatibilityMessage': "mediaCompatibilityMessage_example", // String | The message to send when a media message has no text. Can be used as placeholder message.
  'notificationsAddedToChannelEnabled': true, // Boolean | Whether to send a notification when a member is added to a channel. The default is `false`.
  'notificationsAddedToChannelSound': "notificationsAddedToChannelSound_example", // String | The name of the sound to play when a member is added to a channel and `notifications.added_to_channel.enabled` is `true`.
  'notificationsAddedToChannelTemplate': "notificationsAddedToChannelTemplate_example", // String | The template to use to create the notification text displayed when a member is added to a channel and `notifications.added_to_channel.enabled` is `true`.
  'notificationsInvitedToChannelEnabled': true, // Boolean | Whether to send a notification when a user is invited to a channel. The default is `false`.
  'notificationsInvitedToChannelSound': "notificationsInvitedToChannelSound_example", // String | The name of the sound to play when a user is invited to a channel and `notifications.invited_to_channel.enabled` is `true`.
  'notificationsInvitedToChannelTemplate': "notificationsInvitedToChannelTemplate_example", // String | The template to use to create the notification text displayed when a user is invited to a channel and `notifications.invited_to_channel.enabled` is `true`.
  'notificationsLogEnabled': true, // Boolean | Whether to log notifications. The default is `false`.
  'notificationsNewMessageBadgeCountEnabled': true, // Boolean | Whether the new message badge is enabled. The default is `false`.
  'notificationsNewMessageEnabled': true, // Boolean | Whether to send a notification when a new message is added to a channel. The default is `false`.
  'notificationsNewMessageSound': "notificationsNewMessageSound_example", // String | The name of the sound to play when a new message is added to a channel and `notifications.new_message.enabled` is `true`.
  'notificationsNewMessageTemplate': "notificationsNewMessageTemplate_example", // String | The template to use to create the notification text displayed when a new message is added to a channel and `notifications.new_message.enabled` is `true`.
  'notificationsRemovedFromChannelEnabled': true, // Boolean | Whether to send a notification to a user when they are removed from a channel. The default is `false`.
  'notificationsRemovedFromChannelSound': "notificationsRemovedFromChannelSound_example", // String | The name of the sound to play to a user when they are removed from a channel and `notifications.removed_from_channel.enabled` is `true`.
  'notificationsRemovedFromChannelTemplate': "notificationsRemovedFromChannelTemplate_example", // String | The template to use to create the notification text displayed to a user when they are removed from a channel and `notifications.removed_from_channel.enabled` is `true`.
  'postWebhookRetryCount': 56, // Number | The number of times to retry a call to the `post_webhook_url` if the request times out (after 5 seconds) or it receives a 429, 503, or 504 HTTP response. The default is 0, which means the call won't be retried.
  'postWebhookUrl': "postWebhookUrl_example", // String | The URL for post-event webhooks, which are called by using the `webhook_method`. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
  'preWebhookRetryCount': 56, // Number | The number of times to retry a call to the `pre_webhook_url` if the request times out (after 5 seconds) or it receives a 429, 503, or 504 HTTP response. Default retry count is 0 times, which means the call won't be retried.
  'preWebhookUrl': "preWebhookUrl_example", // String | The URL for pre-event webhooks, which are called by using the `webhook_method`. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
  'reachabilityEnabled': true, // Boolean | Whether to enable the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) for this Service instance. The default is `false`.
  'readStatusEnabled': true, // Boolean | Whether to enable the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature. The default is `true`.
  'typingIndicatorTimeout': 56, // Number | How long in seconds after a `started typing` event until clients should assume that user is no longer typing, even if no `ended typing` message was received.  The default is 5 seconds.
  'webhookFilters': ["null"], // [String] | The list of webhook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
  'webhookMethod': "webhookMethod_example" // String | The HTTP method to use for calls to the `pre_webhook_url` and `post_webhook_url` webhooks.  Can be: `POST` or `GET` and the default is `POST`. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
};
apiInstance.updateService(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the Service resource to update. | 
 **consumptionReportInterval** | **Number**| DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints. | [optional] 
 **defaultChannelCreatorRoleSid** | **String**| The channel role assigned to a channel creator when they join a new channel. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles. | [optional] 
 **defaultChannelRoleSid** | **String**| The channel role assigned to users when they are added to a channel. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles. | [optional] 
 **defaultServiceRoleSid** | **String**| The service role assigned to users when they are added to the service. See the [Role resource](https://www.twilio.com/docs/chat/rest/role-resource) for more info about roles. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. | [optional] 
 **limitsChannelMembers** | **Number**| The maximum number of Members that can be added to Channels within this Service. Can be up to 1,000. | [optional] 
 **limitsUserChannels** | **Number**| The maximum number of Channels Users can be a Member of within this Service. Can be up to 1,000. | [optional] 
 **mediaCompatibilityMessage** | **String**| The message to send when a media message has no text. Can be used as placeholder message. | [optional] 
 **notificationsAddedToChannelEnabled** | **Boolean**| Whether to send a notification when a member is added to a channel. The default is &#x60;false&#x60;. | [optional] 
 **notificationsAddedToChannelSound** | **String**| The name of the sound to play when a member is added to a channel and &#x60;notifications.added_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **notificationsAddedToChannelTemplate** | **String**| The template to use to create the notification text displayed when a member is added to a channel and &#x60;notifications.added_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **notificationsInvitedToChannelEnabled** | **Boolean**| Whether to send a notification when a user is invited to a channel. The default is &#x60;false&#x60;. | [optional] 
 **notificationsInvitedToChannelSound** | **String**| The name of the sound to play when a user is invited to a channel and &#x60;notifications.invited_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **notificationsInvitedToChannelTemplate** | **String**| The template to use to create the notification text displayed when a user is invited to a channel and &#x60;notifications.invited_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **notificationsLogEnabled** | **Boolean**| Whether to log notifications. The default is &#x60;false&#x60;. | [optional] 
 **notificationsNewMessageBadgeCountEnabled** | **Boolean**| Whether the new message badge is enabled. The default is &#x60;false&#x60;. | [optional] 
 **notificationsNewMessageEnabled** | **Boolean**| Whether to send a notification when a new message is added to a channel. The default is &#x60;false&#x60;. | [optional] 
 **notificationsNewMessageSound** | **String**| The name of the sound to play when a new message is added to a channel and &#x60;notifications.new_message.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **notificationsNewMessageTemplate** | **String**| The template to use to create the notification text displayed when a new message is added to a channel and &#x60;notifications.new_message.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **notificationsRemovedFromChannelEnabled** | **Boolean**| Whether to send a notification to a user when they are removed from a channel. The default is &#x60;false&#x60;. | [optional] 
 **notificationsRemovedFromChannelSound** | **String**| The name of the sound to play to a user when they are removed from a channel and &#x60;notifications.removed_from_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **notificationsRemovedFromChannelTemplate** | **String**| The template to use to create the notification text displayed to a user when they are removed from a channel and &#x60;notifications.removed_from_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **postWebhookRetryCount** | **Number**| The number of times to retry a call to the &#x60;post_webhook_url&#x60; if the request times out (after 5 seconds) or it receives a 429, 503, or 504 HTTP response. The default is 0, which means the call won&#39;t be retried. | [optional] 
 **postWebhookUrl** | **String**| The URL for post-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] 
 **preWebhookRetryCount** | **Number**| The number of times to retry a call to the &#x60;pre_webhook_url&#x60; if the request times out (after 5 seconds) or it receives a 429, 503, or 504 HTTP response. Default retry count is 0 times, which means the call won&#39;t be retried. | [optional] 
 **preWebhookUrl** | **String**| The URL for pre-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] 
 **reachabilityEnabled** | **Boolean**| Whether to enable the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) for this Service instance. The default is &#x60;false&#x60;. | [optional] 
 **readStatusEnabled** | **Boolean**| Whether to enable the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature. The default is &#x60;true&#x60;. | [optional] 
 **typingIndicatorTimeout** | **Number**| How long in seconds after a &#x60;started typing&#x60; event until clients should assume that user is no longer typing, even if no &#x60;ended typing&#x60; message was received.  The default is 5 seconds. | [optional] 
 **webhookFilters** | [**[String]**](String.md)| The list of webhook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] 
 **webhookMethod** | **String**| The HTTP method to use for calls to the &#x60;pre_webhook_url&#x60; and &#x60;post_webhook_url&#x60; webhooks.  Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] 

### Return type

[**ChatV2Service**](ChatV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

