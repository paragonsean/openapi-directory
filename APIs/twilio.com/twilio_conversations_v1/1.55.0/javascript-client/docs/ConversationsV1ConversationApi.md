# TwilioConversations.ConversationsV1ConversationApi

All URIs are relative to *https://conversations.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConversation**](ConversationsV1ConversationApi.md#createConversation) | **POST** /v1/Conversations | 
[**createServiceConversation**](ConversationsV1ConversationApi.md#createServiceConversation) | **POST** /v1/Services/{ChatServiceSid}/Conversations | 
[**deleteConversation**](ConversationsV1ConversationApi.md#deleteConversation) | **DELETE** /v1/Conversations/{Sid} | 
[**deleteServiceConversation**](ConversationsV1ConversationApi.md#deleteServiceConversation) | **DELETE** /v1/Services/{ChatServiceSid}/Conversations/{Sid} | 
[**fetchConversation**](ConversationsV1ConversationApi.md#fetchConversation) | **GET** /v1/Conversations/{Sid} | 
[**fetchServiceConversation**](ConversationsV1ConversationApi.md#fetchServiceConversation) | **GET** /v1/Services/{ChatServiceSid}/Conversations/{Sid} | 
[**listConversation**](ConversationsV1ConversationApi.md#listConversation) | **GET** /v1/Conversations | 
[**listServiceConversation**](ConversationsV1ConversationApi.md#listServiceConversation) | **GET** /v1/Services/{ChatServiceSid}/Conversations | 
[**updateConversation**](ConversationsV1ConversationApi.md#updateConversation) | **POST** /v1/Conversations/{Sid} | 
[**updateServiceConversation**](ConversationsV1ConversationApi.md#updateServiceConversation) | **POST** /v1/Services/{ChatServiceSid}/Conversations/{Sid} | 



## createConversation

> ConversationsV1Conversation createConversation(opts)



Create a new conversation in your account&#39;s default service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConversationApi();
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
  'bindingsEmailAddress': "bindingsEmailAddress_example", // String | The default email address that will be used when sending outbound emails in this conversation.
  'bindingsEmailName': "bindingsEmailName_example", // String | The default name that will be used when sending outbound emails in this conversation.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was last updated.
  'friendlyName': "friendlyName_example", // String | The human-readable name of this conversation, limited to 256 characters. Optional.
  'messagingServiceSid': "messagingServiceSid_example", // String | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
  'state': "state_example", // ConversationEnumState | 
  'timersClosed': "timersClosed_example", // String | ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
  'timersInactive': "timersInactive_example", // String | ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
};
apiInstance.createConversation(opts, (error, data, response) => {
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
 **xTwilioWebhookEnabled** | **ConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] 
 **bindingsEmailAddress** | **String**| The default email address that will be used when sending outbound emails in this conversation. | [optional] 
 **bindingsEmailName** | **String**| The default name that will be used when sending outbound emails in this conversation. | [optional] 
 **dateCreated** | **Date**| The date that this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date that this resource was last updated. | [optional] 
 **friendlyName** | **String**| The human-readable name of this conversation, limited to 256 characters. Optional. | [optional] 
 **messagingServiceSid** | **String**| The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to. | [optional] 
 **state** | **ConversationEnumState**|  | [optional] 
 **timersClosed** | **String**| ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] 
 **timersInactive** | **String**| ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. | [optional] 

### Return type

[**ConversationsV1Conversation**](ConversationsV1Conversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## createServiceConversation

> ConversationsV1ServiceServiceConversation createServiceConversation(chatServiceSid, opts)



Create a new conversation in your service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConversationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ServiceConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
  'bindingsEmailAddress': "bindingsEmailAddress_example", // String | The default email address that will be used when sending outbound emails in this conversation.
  'bindingsEmailName': "bindingsEmailName_example", // String | The default name that will be used when sending outbound emails in this conversation.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was last updated.
  'friendlyName': "friendlyName_example", // String | The human-readable name of this conversation, limited to 256 characters. Optional.
  'messagingServiceSid': "messagingServiceSid_example", // String | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
  'state': "state_example", // ServiceConversationEnumState | 
  'timersClosed': "timersClosed_example", // String | ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
  'timersInactive': "timersInactive_example", // String | ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
};
apiInstance.createServiceConversation(chatServiceSid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with. | 
 **xTwilioWebhookEnabled** | **ServiceConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] 
 **bindingsEmailAddress** | **String**| The default email address that will be used when sending outbound emails in this conversation. | [optional] 
 **bindingsEmailName** | **String**| The default name that will be used when sending outbound emails in this conversation. | [optional] 
 **dateCreated** | **Date**| The date that this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date that this resource was last updated. | [optional] 
 **friendlyName** | **String**| The human-readable name of this conversation, limited to 256 characters. Optional. | [optional] 
 **messagingServiceSid** | **String**| The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to. | [optional] 
 **state** | **ServiceConversationEnumState**|  | [optional] 
 **timersClosed** | **String**| ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] 
 **timersInactive** | **String**| ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConversation**](ConversationsV1ServiceServiceConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteConversation

> deleteConversation(sid, opts)



Remove a conversation from your account&#39;s default service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConversationApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // ConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteConversation(sid, opts, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | 
 **xTwilioWebhookEnabled** | **ConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteServiceConversation

> deleteServiceConversation(chatServiceSid, sid, opts)



Remove a conversation from your service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConversationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example" // ServiceConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
};
apiInstance.deleteServiceConversation(chatServiceSid, sid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | 
 **xTwilioWebhookEnabled** | **ServiceConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchConversation

> ConversationsV1Conversation fetchConversation(sid)



Fetch a conversation from your account&#39;s default service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConversationApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
apiInstance.fetchConversation(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | 

### Return type

[**ConversationsV1Conversation**](ConversationsV1Conversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchServiceConversation

> ConversationsV1ServiceServiceConversation fetchServiceConversation(chatServiceSid, sid)



Fetch a conversation from your service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConversationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
apiInstance.fetchServiceConversation(chatServiceSid, sid, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | 

### Return type

[**ConversationsV1ServiceServiceConversation**](ConversationsV1ServiceServiceConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConversation

> ListConversationResponse listConversation(opts)



Retrieve a list of conversations in your account&#39;s default service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConversationApi();
let opts = {
  'startDate': "startDate_example", // String | Start date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the start time of the date is used (YYYY-MM-DDT00:00:00Z). Can be combined with other filters.
  'endDate': "endDate_example", // String | End date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the end time of the date is used (YYYY-MM-DDT23:59:59Z). Can be combined with other filters.
  'state': "state_example", // ConversationEnumState | State for sorting and filtering list of Conversations. Can be `active`, `inactive` or `closed`
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listConversation(opts, (error, data, response) => {
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
 **startDate** | **String**| Start date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the start time of the date is used (YYYY-MM-DDT00:00:00Z). Can be combined with other filters. | [optional] 
 **endDate** | **String**| End date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the end time of the date is used (YYYY-MM-DDT23:59:59Z). Can be combined with other filters. | [optional] 
 **state** | **ConversationEnumState**| State for sorting and filtering list of Conversations. Can be &#x60;active&#x60;, &#x60;inactive&#x60; or &#x60;closed&#x60; | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListConversationResponse**](ListConversationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceConversation

> ListServiceConversationResponse listServiceConversation(chatServiceSid, opts)



Retrieve a list of conversations in your service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConversationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
let opts = {
  'startDate': "startDate_example", // String | Start date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the start time of the date is used (YYYY-MM-DDT00:00:00Z). Can be combined with other filters.
  'endDate': "endDate_example", // String | End date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the end time of the date is used (YYYY-MM-DDT23:59:59Z). Can be combined with other filters.
  'state': "state_example", // ServiceConversationEnumState | State for sorting and filtering list of Conversations. Can be `active`, `inactive` or `closed`
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listServiceConversation(chatServiceSid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with. | 
 **startDate** | **String**| Start date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the start time of the date is used (YYYY-MM-DDT00:00:00Z). Can be combined with other filters. | [optional] 
 **endDate** | **String**| End date or time in ISO8601 format for filtering list of Conversations. If a date is provided, the end time of the date is used (YYYY-MM-DDT23:59:59Z). Can be combined with other filters. | [optional] 
 **state** | **ServiceConversationEnumState**| State for sorting and filtering list of Conversations. Can be &#x60;active&#x60;, &#x60;inactive&#x60; or &#x60;closed&#x60; | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceConversationResponse**](ListServiceConversationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateConversation

> ConversationsV1Conversation updateConversation(sid, opts)



Update an existing conversation in your account&#39;s default service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConversationApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
  'bindingsEmailAddress': "bindingsEmailAddress_example", // String | The default email address that will be used when sending outbound emails in this conversation.
  'bindingsEmailName': "bindingsEmailName_example", // String | The default name that will be used when sending outbound emails in this conversation.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was last updated.
  'friendlyName': "friendlyName_example", // String | The human-readable name of this conversation, limited to 256 characters. Optional.
  'messagingServiceSid': "messagingServiceSid_example", // String | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
  'state': "state_example", // ConversationEnumState | 
  'timersClosed': "timersClosed_example", // String | ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
  'timersInactive': "timersInactive_example", // String | ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
};
apiInstance.updateConversation(sid, opts, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | 
 **xTwilioWebhookEnabled** | **ConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] 
 **bindingsEmailAddress** | **String**| The default email address that will be used when sending outbound emails in this conversation. | [optional] 
 **bindingsEmailName** | **String**| The default name that will be used when sending outbound emails in this conversation. | [optional] 
 **dateCreated** | **Date**| The date that this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date that this resource was last updated. | [optional] 
 **friendlyName** | **String**| The human-readable name of this conversation, limited to 256 characters. Optional. | [optional] 
 **messagingServiceSid** | **String**| The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to. | [optional] 
 **state** | **ConversationEnumState**|  | [optional] 
 **timersClosed** | **String**| ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] 
 **timersInactive** | **String**| ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. | [optional] 

### Return type

[**ConversationsV1Conversation**](ConversationsV1Conversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateServiceConversation

> ConversationsV1ServiceServiceConversation updateServiceConversation(chatServiceSid, sid, opts)



Update an existing conversation in your service

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1ConversationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ServiceConversationEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'attributes': "attributes_example", // String | An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
  'bindingsEmailAddress': "bindingsEmailAddress_example", // String | The default email address that will be used when sending outbound emails in this conversation.
  'bindingsEmailName': "bindingsEmailName_example", // String | The default name that will be used when sending outbound emails in this conversation.
  'dateCreated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was created.
  'dateUpdated': new Date("2013-10-20T19:20:30+01:00"), // Date | The date that this resource was last updated.
  'friendlyName': "friendlyName_example", // String | The human-readable name of this conversation, limited to 256 characters. Optional.
  'messagingServiceSid': "messagingServiceSid_example", // String | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to.
  'state': "state_example", // ServiceConversationEnumState | 
  'timersClosed': "timersClosed_example", // String | ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
  'timersInactive': "timersInactive_example", // String | ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
};
apiInstance.updateServiceConversation(chatServiceSid, sid, opts, (error, data, response) => {
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
 **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with. | 
 **sid** | **String**| A 34 character string that uniquely identifies this resource. Can also be the &#x60;unique_name&#x60; of the Conversation. | 
 **xTwilioWebhookEnabled** | **ServiceConversationEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **attributes** | **String**| An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\&quot;{}\\\&quot; will be returned. | [optional] 
 **bindingsEmailAddress** | **String**| The default email address that will be used when sending outbound emails in this conversation. | [optional] 
 **bindingsEmailName** | **String**| The default name that will be used when sending outbound emails in this conversation. | [optional] 
 **dateCreated** | **Date**| The date that this resource was created. | [optional] 
 **dateUpdated** | **Date**| The date that this resource was last updated. | [optional] 
 **friendlyName** | **String**| The human-readable name of this conversation, limited to 256 characters. Optional. | [optional] 
 **messagingServiceSid** | **String**| The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this conversation belongs to. | [optional] 
 **state** | **ServiceConversationEnumState**|  | [optional] 
 **timersClosed** | **String**| ISO8601 duration when conversation will be switched to &#x60;closed&#x60; state. Minimum value for this timer is 10 minutes. | [optional] 
 **timersInactive** | **String**| ISO8601 duration when conversation will be switched to &#x60;inactive&#x60; state. Minimum value for this timer is 1 minute. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. | [optional] 

### Return type

[**ConversationsV1ServiceServiceConversation**](ConversationsV1ServiceServiceConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

