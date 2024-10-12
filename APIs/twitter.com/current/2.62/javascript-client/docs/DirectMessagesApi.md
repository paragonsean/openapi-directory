# TwitterApiV2.DirectMessagesApi

All URIs are relative to *https://api.twitter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dmConversationByIdEventIdCreate**](DirectMessagesApi.md#dmConversationByIdEventIdCreate) | **POST** /2/dm_conversations/{dm_conversation_id}/messages | Send a new message to a DM Conversation
[**dmConversationIdCreate**](DirectMessagesApi.md#dmConversationIdCreate) | **POST** /2/dm_conversations | Create a new DM Conversation
[**dmConversationWithUserEventIdCreate**](DirectMessagesApi.md#dmConversationWithUserEventIdCreate) | **POST** /2/dm_conversations/with/{participant_id}/messages | Send a new message to a user
[**getDmConversationsIdDmEvents**](DirectMessagesApi.md#getDmConversationsIdDmEvents) | **GET** /2/dm_conversations/{id}/dm_events | Get DM Events for a DM Conversation
[**getDmConversationsWithParticipantIdDmEvents**](DirectMessagesApi.md#getDmConversationsWithParticipantIdDmEvents) | **GET** /2/dm_conversations/with/{participant_id}/dm_events | Get DM Events for a DM Conversation
[**getDmEvents**](DirectMessagesApi.md#getDmEvents) | **GET** /2/dm_events | Get recent DM Events



## dmConversationByIdEventIdCreate

> CreateDmEventResponse dmConversationByIdEventIdCreate(dmConversationId, opts)

Send a new message to a DM Conversation

Creates a new message for a DM Conversation specified by DM Conversation ID

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.DirectMessagesApi();
let dmConversationId = "dmConversationId_example"; // String | The DM Conversation ID.
let opts = {
  'createMessageRequest': new TwitterApiV2.CreateMessageRequest() // CreateMessageRequest | 
};
apiInstance.dmConversationByIdEventIdCreate(dmConversationId, opts, (error, data, response) => {
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
 **dmConversationId** | **String**| The DM Conversation ID. | 
 **createMessageRequest** | [**CreateMessageRequest**](CreateMessageRequest.md)|  | [optional] 

### Return type

[**CreateDmEventResponse**](CreateDmEventResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## dmConversationIdCreate

> CreateDmEventResponse dmConversationIdCreate(opts)

Create a new DM Conversation

Creates a new DM Conversation.

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.DirectMessagesApi();
let opts = {
  'createDmConversationRequest': new TwitterApiV2.CreateDmConversationRequest() // CreateDmConversationRequest | 
};
apiInstance.dmConversationIdCreate(opts, (error, data, response) => {
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
 **createDmConversationRequest** | [**CreateDmConversationRequest**](CreateDmConversationRequest.md)|  | [optional] 

### Return type

[**CreateDmEventResponse**](CreateDmEventResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## dmConversationWithUserEventIdCreate

> CreateDmEventResponse dmConversationWithUserEventIdCreate(participantId, opts)

Send a new message to a user

Creates a new message for a DM Conversation with a participant user by ID

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.DirectMessagesApi();
let participantId = "participantId_example"; // String | The ID of the recipient user that will receive the DM.
let opts = {
  'createMessageRequest': new TwitterApiV2.CreateMessageRequest() // CreateMessageRequest | 
};
apiInstance.dmConversationWithUserEventIdCreate(participantId, opts, (error, data, response) => {
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
 **participantId** | **String**| The ID of the recipient user that will receive the DM. | 
 **createMessageRequest** | [**CreateMessageRequest**](CreateMessageRequest.md)|  | [optional] 

### Return type

[**CreateDmEventResponse**](CreateDmEventResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/problem+json


## getDmConversationsIdDmEvents

> Get2DmConversationsIdDmEventsResponse getDmConversationsIdDmEvents(id, opts)

Get DM Events for a DM Conversation

Returns DM Events for a DM Conversation

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.DirectMessagesApi();
let id = "id_example"; // String | The DM Conversation ID.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'eventTypes': ["null"], // [String] | The set of event_types to include in the results.
  'dmEventFields': ["null"], // [String] | A comma separated list of DmEvent fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.getDmConversationsIdDmEvents(id, opts, (error, data, response) => {
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
 **id** | **String**| The DM Conversation ID. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **eventTypes** | [**[String]**](String.md)| The set of event_types to include in the results. | [optional] 
 **dmEventFields** | [**[String]**](String.md)| A comma separated list of DmEvent fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2DmConversationsIdDmEventsResponse**](Get2DmConversationsIdDmEventsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getDmConversationsWithParticipantIdDmEvents

> Get2DmConversationsWithParticipantIdDmEventsResponse getDmConversationsWithParticipantIdDmEvents(participantId, opts)

Get DM Events for a DM Conversation

Returns DM Events for a DM Conversation

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.DirectMessagesApi();
let participantId = "participantId_example"; // String | The ID of the participant user for the One to One DM conversation.
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'eventTypes': ["null"], // [String] | The set of event_types to include in the results.
  'dmEventFields': ["null"], // [String] | A comma separated list of DmEvent fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.getDmConversationsWithParticipantIdDmEvents(participantId, opts, (error, data, response) => {
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
 **participantId** | **String**| The ID of the participant user for the One to One DM conversation. | 
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **eventTypes** | [**[String]**](String.md)| The set of event_types to include in the results. | [optional] 
 **dmEventFields** | [**[String]**](String.md)| A comma separated list of DmEvent fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2DmConversationsWithParticipantIdDmEventsResponse**](Get2DmConversationsWithParticipantIdDmEventsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json


## getDmEvents

> Get2DmEventsResponse getDmEvents(opts)

Get recent DM Events

Returns recent DM Events across DM conversations

### Example

```javascript
import TwitterApiV2 from 'twitter_api_v2';
let defaultClient = TwitterApiV2.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2UserToken
let OAuth2UserToken = defaultClient.authentications['OAuth2UserToken'];
OAuth2UserToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TwitterApiV2.DirectMessagesApi();
let opts = {
  'maxResults': 100, // Number | The maximum number of results.
  'paginationToken': "paginationToken_example", // String | This parameter is used to get a specified 'page' of results.
  'eventTypes': ["null"], // [String] | The set of event_types to include in the results.
  'dmEventFields': ["null"], // [String] | A comma separated list of DmEvent fields to display.
  'expansions': ["null"], // [String] | A comma separated list of fields to expand.
  'mediaFields': ["null"], // [String] | A comma separated list of Media fields to display.
  'userFields': ["null"], // [String] | A comma separated list of User fields to display.
  'tweetFields': ["null"] // [String] | A comma separated list of Tweet fields to display.
};
apiInstance.getDmEvents(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results. | [optional] [default to 100]
 **paginationToken** | **String**| This parameter is used to get a specified &#39;page&#39; of results. | [optional] 
 **eventTypes** | [**[String]**](String.md)| The set of event_types to include in the results. | [optional] 
 **dmEventFields** | [**[String]**](String.md)| A comma separated list of DmEvent fields to display. | [optional] 
 **expansions** | [**[String]**](String.md)| A comma separated list of fields to expand. | [optional] 
 **mediaFields** | [**[String]**](String.md)| A comma separated list of Media fields to display. | [optional] 
 **userFields** | [**[String]**](String.md)| A comma separated list of User fields to display. | [optional] 
 **tweetFields** | [**[String]**](String.md)| A comma separated list of Tweet fields to display. | [optional] 

### Return type

[**Get2DmEventsResponse**](Get2DmEventsResponse.md)

### Authorization

[OAuth2UserToken](../README.md#OAuth2UserToken), [UserToken](../README.md#UserToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json

