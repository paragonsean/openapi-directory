# TwilioConversations.ConversationsV1ConfigurationApi

All URIs are relative to *https://conversations.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchConfiguration**](ConversationsV1ConfigurationApi.md#fetchConfiguration) | **GET** /v1/Configuration | 
[**fetchServiceConfiguration**](ConversationsV1ConfigurationApi.md#fetchServiceConfiguration) | **GET** /v1/Services/{ChatServiceSid}/Configuration | 
[**updateConfiguration**](ConversationsV1ConfigurationApi.md#updateConfiguration) | **POST** /v1/Configuration | 
[**updateServiceConfiguration**](ConversationsV1ConfigurationApi.md#updateServiceConfiguration) | **POST** /v1/Services/{ChatServiceSid}/Configuration | 



## fetchConfiguration

> ConversationsV1Configuration fetchConfiguration()



Fetch the global configuration of conversations on your account

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConfigurationApi();
apiInstance.fetchConfiguration((error, data, response) => {
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

[**ConversationsV1Configuration**](ConversationsV1Configuration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchServiceConfiguration

> ConversationsV1ServiceServiceConfiguration fetchServiceConfiguration(chatServiceSid)



Fetch the configuration of a conversation service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConfigurationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the Service configuration resource to fetch.
apiInstance.fetchServiceConfiguration(chatServiceSid, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the Service configuration resource to fetch. | 

### Return type

[**ConversationsV1ServiceServiceConfiguration**](ConversationsV1ServiceServiceConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateConfiguration

> ConversationsV1Configuration updateConfiguration(opts)



Update the global configuration of conversations on your account

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConfigurationApi();
let opts = {
  'defaultChatServiceSid': "defaultChatServiceSid_example", // String | The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to use when creating a conversation.
  'defaultClosedTimer': "defaultClosedTimer_example", // String | Default ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
  'defaultInactiveTimer': "defaultInactiveTimer_example", // String | Default ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
  'defaultMessagingServiceSid': "defaultMessagingServiceSid_example" // String | The SID of the default [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to use when creating a conversation.
};
apiInstance.updateConfiguration(opts, (error, data, response) => {
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
 **defaultChatServiceSid** | **String**| The SID of the default [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to use when creating a conversation. | [optional] 
 **defaultClosedTimer** | **String**| Default ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] 
 **defaultInactiveTimer** | **String**| Default ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] 
 **defaultMessagingServiceSid** | **String**| The SID of the default [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) to use when creating a conversation. | [optional] 

### Return type

[**ConversationsV1Configuration**](ConversationsV1Configuration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateServiceConfiguration

> ConversationsV1ServiceServiceConfiguration updateServiceConfiguration(chatServiceSid, opts)



Update configuration settings of a conversation service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConfigurationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the Service configuration resource to update.
let opts = {
  'defaultChatServiceRoleSid': "defaultChatServiceRoleSid_example", // String | The service-level role assigned to users when they are added to the service. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
  'defaultConversationCreatorRoleSid': "defaultConversationCreatorRoleSid_example", // String | The conversation-level role assigned to a conversation creator when they join a new conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
  'defaultConversationRoleSid': "defaultConversationRoleSid_example", // String | The conversation-level role assigned to users when they are added to a conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles.
  'reachabilityEnabled': true // Boolean | Whether the [Reachability Indicator](https://www.twilio.com/docs/conversations/reachability) is enabled for this Conversations Service. The default is `false`.
};
apiInstance.updateServiceConfiguration(chatServiceSid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the Service configuration resource to update. | 
 **defaultChatServiceRoleSid** | **String**| The service-level role assigned to users when they are added to the service. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles. | [optional] 
 **defaultConversationCreatorRoleSid** | **String**| The conversation-level role assigned to a conversation creator when they join a new conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles. | [optional] 
 **defaultConversationRoleSid** | **String**| The conversation-level role assigned to users when they are added to a conversation. See [Conversation Role](https://www.twilio.com/docs/conversations/api/role-resource) for more info about roles. | [optional] 
 **reachabilityEnabled** | **Boolean**| Whether the [Reachability Indicator](https://www.twilio.com/docs/conversations/reachability) is enabled for this Conversations Service. The default is &#x60;false&#x60;. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConfiguration**](ConversationsV1ServiceServiceConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

