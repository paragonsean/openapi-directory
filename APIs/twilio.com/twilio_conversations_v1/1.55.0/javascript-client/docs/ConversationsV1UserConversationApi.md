# TwilioConversations.ConversationsV1UserConversationApi

All URIs are relative to *https://conversations.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteServiceUserConversation**](ConversationsV1UserConversationApi.md#deleteServiceUserConversation) | **DELETE** /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid} | 
[**deleteUserConversation**](ConversationsV1UserConversationApi.md#deleteUserConversation) | **DELETE** /v1/Users/{UserSid}/Conversations/{ConversationSid} | 
[**fetchServiceUserConversation**](ConversationsV1UserConversationApi.md#fetchServiceUserConversation) | **GET** /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid} | 
[**fetchUserConversation**](ConversationsV1UserConversationApi.md#fetchUserConversation) | **GET** /v1/Users/{UserSid}/Conversations/{ConversationSid} | 
[**listServiceUserConversation**](ConversationsV1UserConversationApi.md#listServiceUserConversation) | **GET** /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations | 
[**listUserConversation**](ConversationsV1UserConversationApi.md#listUserConversation) | **GET** /v1/Users/{UserSid}/Conversations | 
[**updateServiceUserConversation**](ConversationsV1UserConversationApi.md#updateServiceUserConversation) | **POST** /v1/Services/{ChatServiceSid}/Users/{UserSid}/Conversations/{ConversationSid} | 
[**updateUserConversation**](ConversationsV1UserConversationApi.md#updateUserConversation) | **POST** /v1/Users/{UserSid}/Conversations/{ConversationSid} | 



## deleteServiceUserConversation

> deleteServiceUserConversation(chatServiceSid, userSid, conversationSid)



Delete a specific User Conversation.

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserConversationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
let userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
let conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
apiInstance.deleteServiceUserConversation(chatServiceSid, userSid, conversationSid, (error, data, response) => {
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
 **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteUserConversation

> deleteUserConversation(userSid, conversationSid)



Delete a specific User Conversation.

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserConversationApi();
let userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
let conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
apiInstance.deleteUserConversation(userSid, conversationSid, (error, data, response) => {
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
 **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchServiceUserConversation

> ConversationsV1ServiceServiceUserServiceUserConversation fetchServiceUserConversation(chatServiceSid, userSid, conversationSid)



Fetch a specific User Conversation.

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserConversationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
let userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
let conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
apiInstance.fetchServiceUserConversation(chatServiceSid, userSid, conversationSid, (error, data, response) => {
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
 **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | 

### Return type

[**ConversationsV1ServiceServiceUserServiceUserConversation**](ConversationsV1ServiceServiceUserServiceUserConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchUserConversation

> ConversationsV1UserUserConversation fetchUserConversation(userSid, conversationSid)



Fetch a specific User Conversation.

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserConversationApi();
let userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
let conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
apiInstance.fetchUserConversation(userSid, conversationSid, (error, data, response) => {
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
 **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | 

### Return type

[**ConversationsV1UserUserConversation**](ConversationsV1UserUserConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceUserConversation

> ListServiceUserConversationResponse listServiceUserConversation(chatServiceSid, userSid, opts)



Retrieve a list of all User Conversations for the User.

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserConversationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
let userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listServiceUserConversation(chatServiceSid, userSid, opts, (error, data, response) => {
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
 **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceUserConversationResponse**](ListServiceUserConversationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUserConversation

> ListUserConversationResponse listUserConversation(userSid, opts)



Retrieve a list of all User Conversations for the User.

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserConversationApi();
let userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listUserConversation(userSid, opts, (error, data, response) => {
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
 **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListUserConversationResponse**](ListUserConversationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateServiceUserConversation

> ConversationsV1ServiceServiceUserServiceUserConversation updateServiceUserConversation(chatServiceSid, userSid, conversationSid, opts)



Update a specific User Conversation.

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserConversationApi();
let chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
let userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
let conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
let opts = {
  'lastReadMessageIndex': 56, // Number | The index of the last Message in the Conversation that the Participant has read.
  'lastReadTimestamp': new Date("2013-10-20T19:20:30+01:00"), // Date | The date of the last message read in conversation by the user, given in ISO 8601 format.
  'notificationLevel': "notificationLevel_example" // ServiceUserConversationEnumNotificationLevel | 
};
apiInstance.updateServiceUserConversation(chatServiceSid, userSid, conversationSid, opts, (error, data, response) => {
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
 **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | 
 **lastReadMessageIndex** | **Number**| The index of the last Message in the Conversation that the Participant has read. | [optional] 
 **lastReadTimestamp** | **Date**| The date of the last message read in conversation by the user, given in ISO 8601 format. | [optional] 
 **notificationLevel** | **ServiceUserConversationEnumNotificationLevel**|  | [optional] 

### Return type

[**ConversationsV1ServiceServiceUserServiceUserConversation**](ConversationsV1ServiceServiceUserServiceUserConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateUserConversation

> ConversationsV1UserUserConversation updateUserConversation(userSid, conversationSid, opts)



Update a specific User Conversation.

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1UserConversationApi();
let userSid = "userSid_example"; // String | The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
let conversationSid = "conversationSid_example"; // String | The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
let opts = {
  'lastReadMessageIndex': 56, // Number | The index of the last Message in the Conversation that the Participant has read.
  'lastReadTimestamp': new Date("2013-10-20T19:20:30+01:00"), // Date | The date of the last message read in conversation by the user, given in ISO 8601 format.
  'notificationLevel': "notificationLevel_example" // UserConversationEnumNotificationLevel | 
};
apiInstance.updateUserConversation(userSid, conversationSid, opts, (error, data, response) => {
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
 **userSid** | **String**| The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource. | 
 **conversationSid** | **String**| The unique SID identifier of the Conversation. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource). | 
 **lastReadMessageIndex** | **Number**| The index of the last Message in the Conversation that the Participant has read. | [optional] 
 **lastReadTimestamp** | **Date**| The date of the last message read in conversation by the user, given in ISO 8601 format. | [optional] 
 **notificationLevel** | **UserConversationEnumNotificationLevel**|  | [optional] 

### Return type

[**ConversationsV1UserUserConversation**](ConversationsV1UserUserConversation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

