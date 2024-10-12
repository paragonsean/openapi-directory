# TwilioChat.ChatV1ServiceApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createService**](ChatV1ServiceApi.md#createService) | **POST** /v1/Services | 
[**deleteService**](ChatV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} | 
[**fetchService**](ChatV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} | 
[**listService**](ChatV1ServiceApi.md#listService) | **GET** /v1/Services | 
[**updateService**](ChatV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} | 



## createService

> ChatV1Service createService(friendlyName)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1ServiceApi();
let friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
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
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | 

### Return type

[**ChatV1Service**](ChatV1Service.md)

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

let apiInstance = new TwilioChat.ChatV1ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to delete.
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchService

> ChatV1Service fetchService(sid)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to fetch.
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to fetch. | 

### Return type

[**ChatV1Service**](ChatV1Service.md)

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

let apiInstance = new TwilioChat.ChatV1ServiceApi();
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

> ChatV1Service updateService(sid, opts)





### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV1ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to update.
let opts = {
  'consumptionReportInterval': 56, // Number | DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints.
  'defaultChannelCreatorRoleSid': "defaultChannelCreatorRoleSid_example", // String | The channel role assigned to a channel creator when they join a new channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details.
  'defaultChannelRoleSid': "defaultChannelRoleSid_example", // String | The channel role assigned to users when they are added to a channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details.
  'defaultServiceRoleSid': "defaultServiceRoleSid_example", // String | The service role assigned to users when they are added to the service. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'limitsChannelMembers': 56, // Number | The maximum number of Members that can be added to Channels within this Service. Can be up to 1,000.
  'limitsUserChannels': 56, // Number | The maximum number of Channels Users can be a Member of within this Service. Can be up to 1,000.
  'notificationsAddedToChannelEnabled': true, // Boolean | Whether to send a notification when a member is added to a channel. Can be: `true` or `false` and the default is `false`.
  'notificationsAddedToChannelTemplate': "notificationsAddedToChannelTemplate_example", // String | The template to use to create the notification text displayed when a member is added to a channel and `notifications.added_to_channel.enabled` is `true`.
  'notificationsInvitedToChannelEnabled': true, // Boolean | Whether to send a notification when a user is invited to a channel. Can be: `true` or `false` and the default is `false`.
  'notificationsInvitedToChannelTemplate': "notificationsInvitedToChannelTemplate_example", // String | The template to use to create the notification text displayed when a user is invited to a channel and `notifications.invited_to_channel.enabled` is `true`.
  'notificationsNewMessageEnabled': true, // Boolean | Whether to send a notification when a new message is added to a channel. Can be: `true` or `false` and the default is `false`.
  'notificationsNewMessageTemplate': "notificationsNewMessageTemplate_example", // String | The template to use to create the notification text displayed when a new message is added to a channel and `notifications.new_message.enabled` is `true`.
  'notificationsRemovedFromChannelEnabled': true, // Boolean | Whether to send a notification to a user when they are removed from a channel. Can be: `true` or `false` and the default is `false`.
  'notificationsRemovedFromChannelTemplate': "notificationsRemovedFromChannelTemplate_example", // String | The template to use to create the notification text displayed to a user when they are removed from a channel and `notifications.removed_from_channel.enabled` is `true`.
  'postWebhookUrl': "postWebhookUrl_example", // String | The URL for post-event webhooks, which are called by using the `webhook_method`. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details.
  'preWebhookUrl': "preWebhookUrl_example", // String | The URL for pre-event webhooks, which are called by using the `webhook_method`. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details.
  'reachabilityEnabled': true, // Boolean | Whether to enable the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) for this Service instance. The default is `false`.
  'readStatusEnabled': true, // Boolean | Whether to enable the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature. The default is `true`.
  'typingIndicatorTimeout': 56, // Number | How long in seconds after a `started typing` event until clients should assume that user is no longer typing, even if no `ended typing` message was received.  The default is 5 seconds.
  'webhookFilters': ["null"], // [String] | The list of WebHook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
  'webhookMethod': "webhookMethod_example", // String | The HTTP method to use for calls to the `pre_webhook_url` and `post_webhook_url` webhooks.  Can be: `POST` or `GET` and the default is `POST`. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details.
  'webhooksOnChannelAddMethod': "webhooksOnChannelAddMethod_example", // String | The HTTP method to use when calling the `webhooks.on_channel_add.url`.
  'webhooksOnChannelAddUrl': "webhooksOnChannelAddUrl_example", // String | The URL of the webhook to call in response to the `on_channel_add` event using the `webhooks.on_channel_add.method` HTTP method.
  'webhooksOnChannelAddedMethod': "webhooksOnChannelAddedMethod_example", // String | The URL of the webhook to call in response to the `on_channel_added` event`.
  'webhooksOnChannelAddedUrl': "webhooksOnChannelAddedUrl_example", // String | The URL of the webhook to call in response to the `on_channel_added` event using the `webhooks.on_channel_added.method` HTTP method.
  'webhooksOnChannelDestroyMethod': "webhooksOnChannelDestroyMethod_example", // String | The HTTP method to use when calling the `webhooks.on_channel_destroy.url`.
  'webhooksOnChannelDestroyUrl': "webhooksOnChannelDestroyUrl_example", // String | The URL of the webhook to call in response to the `on_channel_destroy` event using the `webhooks.on_channel_destroy.method` HTTP method.
  'webhooksOnChannelDestroyedMethod': "webhooksOnChannelDestroyedMethod_example", // String | The HTTP method to use when calling the `webhooks.on_channel_destroyed.url`.
  'webhooksOnChannelDestroyedUrl': "webhooksOnChannelDestroyedUrl_example", // String | The URL of the webhook to call in response to the `on_channel_added` event using the `webhooks.on_channel_destroyed.method` HTTP method.
  'webhooksOnChannelUpdateMethod': "webhooksOnChannelUpdateMethod_example", // String | The HTTP method to use when calling the `webhooks.on_channel_update.url`.
  'webhooksOnChannelUpdateUrl': "webhooksOnChannelUpdateUrl_example", // String | The URL of the webhook to call in response to the `on_channel_update` event using the `webhooks.on_channel_update.method` HTTP method.
  'webhooksOnChannelUpdatedMethod': "webhooksOnChannelUpdatedMethod_example", // String | The HTTP method to use when calling the `webhooks.on_channel_updated.url`.
  'webhooksOnChannelUpdatedUrl': "webhooksOnChannelUpdatedUrl_example", // String | The URL of the webhook to call in response to the `on_channel_updated` event using the `webhooks.on_channel_updated.method` HTTP method.
  'webhooksOnMemberAddMethod': "webhooksOnMemberAddMethod_example", // String | The HTTP method to use when calling the `webhooks.on_member_add.url`.
  'webhooksOnMemberAddUrl': "webhooksOnMemberAddUrl_example", // String | The URL of the webhook to call in response to the `on_member_add` event using the `webhooks.on_member_add.method` HTTP method.
  'webhooksOnMemberAddedMethod': "webhooksOnMemberAddedMethod_example", // String | The HTTP method to use when calling the `webhooks.on_channel_updated.url`.
  'webhooksOnMemberAddedUrl': "webhooksOnMemberAddedUrl_example", // String | The URL of the webhook to call in response to the `on_channel_updated` event using the `webhooks.on_channel_updated.method` HTTP method.
  'webhooksOnMemberRemoveMethod': "webhooksOnMemberRemoveMethod_example", // String | The HTTP method to use when calling the `webhooks.on_member_remove.url`.
  'webhooksOnMemberRemoveUrl': "webhooksOnMemberRemoveUrl_example", // String | The URL of the webhook to call in response to the `on_member_remove` event using the `webhooks.on_member_remove.method` HTTP method.
  'webhooksOnMemberRemovedMethod': "webhooksOnMemberRemovedMethod_example", // String | The HTTP method to use when calling the `webhooks.on_member_removed.url`.
  'webhooksOnMemberRemovedUrl': "webhooksOnMemberRemovedUrl_example", // String | The URL of the webhook to call in response to the `on_member_removed` event using the `webhooks.on_member_removed.method` HTTP method.
  'webhooksOnMessageRemoveMethod': "webhooksOnMessageRemoveMethod_example", // String | The HTTP method to use when calling the `webhooks.on_message_remove.url`.
  'webhooksOnMessageRemoveUrl': "webhooksOnMessageRemoveUrl_example", // String | The URL of the webhook to call in response to the `on_message_remove` event using the `webhooks.on_message_remove.method` HTTP method.
  'webhooksOnMessageRemovedMethod': "webhooksOnMessageRemovedMethod_example", // String | The HTTP method to use when calling the `webhooks.on_message_removed.url`.
  'webhooksOnMessageRemovedUrl': "webhooksOnMessageRemovedUrl_example", // String | The URL of the webhook to call in response to the `on_message_removed` event using the `webhooks.on_message_removed.method` HTTP method.
  'webhooksOnMessageSendMethod': "webhooksOnMessageSendMethod_example", // String | The HTTP method to use when calling the `webhooks.on_message_send.url`.
  'webhooksOnMessageSendUrl': "webhooksOnMessageSendUrl_example", // String | The URL of the webhook to call in response to the `on_message_send` event using the `webhooks.on_message_send.method` HTTP method.
  'webhooksOnMessageSentMethod': "webhooksOnMessageSentMethod_example", // String | The URL of the webhook to call in response to the `on_message_sent` event`.
  'webhooksOnMessageSentUrl': "webhooksOnMessageSentUrl_example", // String | The URL of the webhook to call in response to the `on_message_sent` event using the `webhooks.on_message_sent.method` HTTP method.
  'webhooksOnMessageUpdateMethod': "webhooksOnMessageUpdateMethod_example", // String | The HTTP method to use when calling the `webhooks.on_message_update.url`.
  'webhooksOnMessageUpdateUrl': "webhooksOnMessageUpdateUrl_example", // String | The URL of the webhook to call in response to the `on_message_update` event using the `webhooks.on_message_update.method` HTTP method.
  'webhooksOnMessageUpdatedMethod': "webhooksOnMessageUpdatedMethod_example", // String | The HTTP method to use when calling the `webhooks.on_message_updated.url`.
  'webhooksOnMessageUpdatedUrl': "webhooksOnMessageUpdatedUrl_example" // String | The URL of the webhook to call in response to the `on_message_updated` event using the `webhooks.on_message_updated.method` HTTP method.
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to update. | 
 **consumptionReportInterval** | **Number**| DEPRECATED. The interval in seconds between consumption reports submission batches from client endpoints. | [optional] 
 **defaultChannelCreatorRoleSid** | **String**| The channel role assigned to a channel creator when they join a new channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details. | [optional] 
 **defaultChannelRoleSid** | **String**| The channel role assigned to users when they are added to a channel. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details. | [optional] 
 **defaultServiceRoleSid** | **String**| The service role assigned to users when they are added to the service. See the [Roles endpoint](https://www.twilio.com/docs/chat/api/roles) for more details. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **limitsChannelMembers** | **Number**| The maximum number of Members that can be added to Channels within this Service. Can be up to 1,000. | [optional] 
 **limitsUserChannels** | **Number**| The maximum number of Channels Users can be a Member of within this Service. Can be up to 1,000. | [optional] 
 **notificationsAddedToChannelEnabled** | **Boolean**| Whether to send a notification when a member is added to a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] 
 **notificationsAddedToChannelTemplate** | **String**| The template to use to create the notification text displayed when a member is added to a channel and &#x60;notifications.added_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **notificationsInvitedToChannelEnabled** | **Boolean**| Whether to send a notification when a user is invited to a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] 
 **notificationsInvitedToChannelTemplate** | **String**| The template to use to create the notification text displayed when a user is invited to a channel and &#x60;notifications.invited_to_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **notificationsNewMessageEnabled** | **Boolean**| Whether to send a notification when a new message is added to a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] 
 **notificationsNewMessageTemplate** | **String**| The template to use to create the notification text displayed when a new message is added to a channel and &#x60;notifications.new_message.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **notificationsRemovedFromChannelEnabled** | **Boolean**| Whether to send a notification to a user when they are removed from a channel. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] 
 **notificationsRemovedFromChannelTemplate** | **String**| The template to use to create the notification text displayed to a user when they are removed from a channel and &#x60;notifications.removed_from_channel.enabled&#x60; is &#x60;true&#x60;. | [optional] 
 **postWebhookUrl** | **String**| The URL for post-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details. | [optional] 
 **preWebhookUrl** | **String**| The URL for pre-event webhooks, which are called by using the &#x60;webhook_method&#x60;. See [Webhook Events](https://www.twilio.com/docs/api/chat/webhooks) for more details. | [optional] 
 **reachabilityEnabled** | **Boolean**| Whether to enable the [Reachability Indicator](https://www.twilio.com/docs/chat/reachability-indicator) for this Service instance. The default is &#x60;false&#x60;. | [optional] 
 **readStatusEnabled** | **Boolean**| Whether to enable the [Message Consumption Horizon](https://www.twilio.com/docs/chat/consumption-horizon) feature. The default is &#x60;true&#x60;. | [optional] 
 **typingIndicatorTimeout** | **Number**| How long in seconds after a &#x60;started typing&#x60; event until clients should assume that user is no longer typing, even if no &#x60;ended typing&#x60; message was received.  The default is 5 seconds. | [optional] 
 **webhookFilters** | [**[String]**](String.md)| The list of WebHook events that are enabled for this Service instance. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] 
 **webhookMethod** | **String**| The HTTP method to use for calls to the &#x60;pre_webhook_url&#x60; and &#x60;post_webhook_url&#x60; webhooks.  Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. See [Webhook Events](https://www.twilio.com/docs/chat/webhook-events) for more details. | [optional] 
 **webhooksOnChannelAddMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_add.url&#x60;. | [optional] 
 **webhooksOnChannelAddUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_channel_add&#x60; event using the &#x60;webhooks.on_channel_add.method&#x60; HTTP method. | [optional] 
 **webhooksOnChannelAddedMethod** | **String**| The URL of the webhook to call in response to the &#x60;on_channel_added&#x60; event&#x60;. | [optional] 
 **webhooksOnChannelAddedUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_channel_added&#x60; event using the &#x60;webhooks.on_channel_added.method&#x60; HTTP method. | [optional] 
 **webhooksOnChannelDestroyMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_destroy.url&#x60;. | [optional] 
 **webhooksOnChannelDestroyUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_channel_destroy&#x60; event using the &#x60;webhooks.on_channel_destroy.method&#x60; HTTP method. | [optional] 
 **webhooksOnChannelDestroyedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_destroyed.url&#x60;. | [optional] 
 **webhooksOnChannelDestroyedUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_channel_added&#x60; event using the &#x60;webhooks.on_channel_destroyed.method&#x60; HTTP method. | [optional] 
 **webhooksOnChannelUpdateMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_update.url&#x60;. | [optional] 
 **webhooksOnChannelUpdateUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_channel_update&#x60; event using the &#x60;webhooks.on_channel_update.method&#x60; HTTP method. | [optional] 
 **webhooksOnChannelUpdatedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_updated.url&#x60;. | [optional] 
 **webhooksOnChannelUpdatedUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_channel_updated&#x60; event using the &#x60;webhooks.on_channel_updated.method&#x60; HTTP method. | [optional] 
 **webhooksOnMemberAddMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_member_add.url&#x60;. | [optional] 
 **webhooksOnMemberAddUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_member_add&#x60; event using the &#x60;webhooks.on_member_add.method&#x60; HTTP method. | [optional] 
 **webhooksOnMemberAddedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_channel_updated.url&#x60;. | [optional] 
 **webhooksOnMemberAddedUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_channel_updated&#x60; event using the &#x60;webhooks.on_channel_updated.method&#x60; HTTP method. | [optional] 
 **webhooksOnMemberRemoveMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_member_remove.url&#x60;. | [optional] 
 **webhooksOnMemberRemoveUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_member_remove&#x60; event using the &#x60;webhooks.on_member_remove.method&#x60; HTTP method. | [optional] 
 **webhooksOnMemberRemovedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_member_removed.url&#x60;. | [optional] 
 **webhooksOnMemberRemovedUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_member_removed&#x60; event using the &#x60;webhooks.on_member_removed.method&#x60; HTTP method. | [optional] 
 **webhooksOnMessageRemoveMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_message_remove.url&#x60;. | [optional] 
 **webhooksOnMessageRemoveUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_message_remove&#x60; event using the &#x60;webhooks.on_message_remove.method&#x60; HTTP method. | [optional] 
 **webhooksOnMessageRemovedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_message_removed.url&#x60;. | [optional] 
 **webhooksOnMessageRemovedUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_message_removed&#x60; event using the &#x60;webhooks.on_message_removed.method&#x60; HTTP method. | [optional] 
 **webhooksOnMessageSendMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_message_send.url&#x60;. | [optional] 
 **webhooksOnMessageSendUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_message_send&#x60; event using the &#x60;webhooks.on_message_send.method&#x60; HTTP method. | [optional] 
 **webhooksOnMessageSentMethod** | **String**| The URL of the webhook to call in response to the &#x60;on_message_sent&#x60; event&#x60;. | [optional] 
 **webhooksOnMessageSentUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_message_sent&#x60; event using the &#x60;webhooks.on_message_sent.method&#x60; HTTP method. | [optional] 
 **webhooksOnMessageUpdateMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_message_update.url&#x60;. | [optional] 
 **webhooksOnMessageUpdateUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_message_update&#x60; event using the &#x60;webhooks.on_message_update.method&#x60; HTTP method. | [optional] 
 **webhooksOnMessageUpdatedMethod** | **String**| The HTTP method to use when calling the &#x60;webhooks.on_message_updated.url&#x60;. | [optional] 
 **webhooksOnMessageUpdatedUrl** | **String**| The URL of the webhook to call in response to the &#x60;on_message_updated&#x60; event using the &#x60;webhooks.on_message_updated.method&#x60; HTTP method. | [optional] 

### Return type

[**ChatV1Service**](ChatV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

