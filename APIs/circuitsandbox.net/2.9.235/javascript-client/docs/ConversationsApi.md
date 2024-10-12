# RestApiVersion2.ConversationsApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addFavorite**](ConversationsApi.md#addFavorite) | **POST** /conversations/{convId}/favorite | Adds a conversation to the favorites
[**addLabel**](ConversationsApi.md#addLabel) | **POST** /users/labels | Add a user label
[**addModerators**](ConversationsApi.md#addModerators) | **POST** /conversations/{convId}/moderators | Add moderators
[**addParticipantCommunity**](ConversationsApi.md#addParticipantCommunity) | **POST** /conversations/community/{convId}/participants | Adds participants to a community
[**addParticipantGroup**](ConversationsApi.md#addParticipantGroup) | **POST** /conversations/group/{convId}/participants | Adds participants to a group conversation
[**addTextItem**](ConversationsApi.md#addTextItem) | **POST** /conversations/{convId}/messages | Adds a message to a conversation
[**addTextItemWithParent**](ConversationsApi.md#addTextItemWithParent) | **POST** /conversations/{convId}/messages/{itemId} | Adds a message to an item
[**archiveConversation**](ConversationsApi.md#archiveConversation) | **POST** /conversations/{convId}/archive | Archives conversation
[**assignLabel**](ConversationsApi.md#assignLabel) | **POST** /conversations/{convId}/label | Adds a label to a conversation
[**createCommunityConversation**](ConversationsApi.md#createCommunityConversation) | **POST** /conversations/community | Creates a community conversation
[**createDirectConversation**](ConversationsApi.md#createDirectConversation) | **POST** /conversations/direct | Creates a 1-to-1 conversation
[**createGroupConversation**](ConversationsApi.md#createGroupConversation) | **POST** /conversations/group | Creates a group conversation
[**deleteFavorite**](ConversationsApi.md#deleteFavorite) | **DELETE** /conversations/{convId}/favorite | Removes a conversation from favorites
[**deleteTextItem**](ConversationsApi.md#deleteTextItem) | **DELETE** /conversations/{convId}/messages/{itemId} | Deletes a message from a conversation
[**flagItem**](ConversationsApi.md#flagItem) | **POST** /conversations/{convId}/messages/{itemId}/flag | Adds a flag to a message in a conversation
[**getCommunityConversations**](ConversationsApi.md#getCommunityConversations) | **GET** /conversations/community | Gets a list of communities
[**getConversationItems**](ConversationsApi.md#getConversationItems) | **GET** /conversations/{convId}/items | Gets a list of conversation items
[**getConversationbyId**](ConversationsApi.md#getConversationbyId) | **GET** /conversations/{convId} | Gets a conversation
[**getConversations**](ConversationsApi.md#getConversations) | **GET** /conversations | Gets a list of conversations
[**getConversationsById**](ConversationsApi.md#getConversationsById) | **GET** /conversations/byIds | Gets conversations
[**getConversationsByLabel**](ConversationsApi.md#getConversationsByLabel) | **GET** /conversations/label/{labelId} | Returns conversations with a certain label
[**getDirectConversation**](ConversationsApi.md#getDirectConversation) | **GET** /conversations/direct | Checks for a 1-to-1 conversation
[**getFavoriteConversations**](ConversationsApi.md#getFavoriteConversations) | **GET** /conversations/favorite | Gets favorite conversations
[**getFlagItem**](ConversationsApi.md#getFlagItem) | **GET** /conversations/{convId}/messages/flag | Gets a list of the flagged messages of a conversation
[**getFlagItemConv**](ConversationsApi.md#getFlagItemConv) | **GET** /conversations/messages/flag | Gets a list of the flagged messages
[**getJoinDetails**](ConversationsApi.md#getJoinDetails) | **GET** /conversations/{convId}/conversationdetails | Gets the conference details of a conversation
[**getJoinDetailsMultiple**](ConversationsApi.md#getJoinDetailsMultiple) | **GET** /conversations/conversationdetails | Gets the conference details for multiple conversations
[**getParticipantsByConvId**](ConversationsApi.md#getParticipantsByConvId) | **GET** /conversations/{convId}/participants | Performs a list of participants
[**getPinnedConversations**](ConversationsApi.md#getPinnedConversations) | **GET** /conversations/{convId}/pins | Returns pinned topics of a conversation
[**getSingleConversationtem**](ConversationsApi.md#getSingleConversationtem) | **GET** /conversations/messages/{itemId} | Returns a text item
[**joinCommunityConversation**](ConversationsApi.md#joinCommunityConversation) | **POST** /conversations/community/{convId}/join | Adds the authenticated user to a community
[**likeItem**](ConversationsApi.md#likeItem) | **POST** /conversations/{convId}/messages/{itemId}/like | Adds a \&quot;like\&quot; to a message
[**moderateConversation**](ConversationsApi.md#moderateConversation) | **POST** /conversations/moderate/{convId} | Set conversation moderated
[**pinAConversation**](ConversationsApi.md#pinAConversation) | **POST** /conversations/{convId}/pins/{itemId} | Pins a topic of a conversation
[**removeLabel**](ConversationsApi.md#removeLabel) | **DELETE** /users/labels/{labelId} | Remove a user label
[**removeModerators**](ConversationsApi.md#removeModerators) | **DELETE** /conversations/{convId}/moderators | Remove moderators
[**removeParticipantCommunity**](ConversationsApi.md#removeParticipantCommunity) | **DELETE** /conversations/community/{convId}/participants | Removes participants from a community
[**removeParticipantGroup**](ConversationsApi.md#removeParticipantGroup) | **DELETE** /conversations/group/{convId}/participants | Removes participants from a group conversation
[**resolveInvitationToken**](ConversationsApi.md#resolveInvitationToken) | **GET** /conversations/resolveinvitetoken | Resolves an invite token to a conversation
[**searchConversations**](ConversationsApi.md#searchConversations) | **GET** /conversations/search | Performs a conversation search
[**unFlagItem**](ConversationsApi.md#unFlagItem) | **DELETE** /conversations/{convId}/messages/{itemId}/flag | Removes the flag from a message
[**unPinAConversation**](ConversationsApi.md#unPinAConversation) | **DELETE** /conversations/{convId}/pins/{itemId} | Unpins a topic of a conversation
[**unassignLabel**](ConversationsApi.md#unassignLabel) | **DELETE** /conversations/{convId}/label/{labelId} | Removes a label from a conversation
[**undoArchiveConversation**](ConversationsApi.md#undoArchiveConversation) | **DELETE** /conversations/{convId}/archive | Unmute conversation
[**unlikeItem**](ConversationsApi.md#unlikeItem) | **DELETE** /conversations/{convId}/messages/{itemId}/like | Removes a \&quot;like\&quot; from a message
[**unmoderateConversation**](ConversationsApi.md#unmoderateConversation) | **POST** /conversations/unmoderate/{convId} | Set conversation unmoderated
[**updateConversationCommunity**](ConversationsApi.md#updateConversationCommunity) | **PUT** /conversations/community/{convId} | Updates the information of a community
[**updateConversationGroup**](ConversationsApi.md#updateConversationGroup) | **PUT** /conversations/group/{convId} | Updates the information of a group conversation
[**updateProfile**](ConversationsApi.md#updateProfile) | **PUT** /users/profile | Updates the user profile
[**updateTextItem**](ConversationsApi.md#updateTextItem) | **PUT** /conversations/{convId}/messages/{itemId} | Updates a message



## addFavorite

> addFavorite(convId)

Adds a conversation to the favorites

Adds a conversation to the favorites. Favorites can be displayed in a separate side tab inside of the Circuit client to have a better overview of important conversations. OauthScopes: WRITE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation which will be marked as favorite
apiInstance.addFavorite(convId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation which will be marked as favorite | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addLabel

> Label addLabel(label)

Add a user label

Add a label to the list of user labels OauthScopes: WRITE_USER_PROFILE, ORGANIZE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let label = "label_example"; // String | The label value to add
apiInstance.addLabel(label, (error, data, response) => {
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
 **label** | **String**| The label value to add | 

### Return type

[**Label**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## addModerators

> addModerators(convId, moderators)

Add moderators

Adds a list of moderators to a conversation OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the moderators are added
let moderators = ["null"]; // [String] | The list of moderator ids to add 
apiInstance.addModerators(convId, moderators, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the moderators are added | 
 **moderators** | [**[String]**](String.md)| The list of moderator ids to add  | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## addParticipantCommunity

> Conversation addParticipantCommunity(convId, participants)

Adds participants to a community

Adds one or more participants to the given community. This operation can only be performed by a user who is already a member of the community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the participant has to be added.
let participants = ["null"]; // [String] | The IDs or the unique email addresses of the Circuit users that should to be added.
apiInstance.addParticipantCommunity(convId, participants, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the participant has to be added. | 
 **participants** | [**[String]**](String.md)| The IDs or the unique email addresses of the Circuit users that should to be added. | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## addParticipantGroup

> Conversation addParticipantGroup(convId, participants)

Adds participants to a group conversation

Adds one or more participants to the given group conversation. This operation can only be performed by a user who is already a member of the conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the participant has to be added.
let participants = ["null"]; // [String] | The IDs or the unique email addresses of the Circuit users that should to be added.
apiInstance.addParticipantGroup(convId, participants, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the participant has to be added. | 
 **participants** | [**[String]**](String.md)| The IDs or the unique email addresses of the Circuit users that should to be added. | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## addTextItem

> ConversationItem addTextItem(convId, opts)

Adds a message to a conversation

Adds a message to the given conversation. This operation can be only performed on behalf of a user who is already a member of the conversation. OauthScopes: WRITE_CONVERSATIONS, CREATE_CONVERSATIONS_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the new item has to be added
let opts = {
  'attachments': ["null"], // [String] | A comma separated list of attachment IDs from the file API.
  'content': "content_example", // String | The actual content of the item, is mandatory unless an attachment is added
  'formMetaData': "formMetaData_example", // String | The form meta data of the new text item
  'subject': "subject_example" // String | The subject (headline) of the new text item
};
apiInstance.addTextItem(convId, opts, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the new item has to be added | 
 **attachments** | [**[String]**](String.md)| A comma separated list of attachment IDs from the file API. | [optional] 
 **content** | **String**| The actual content of the item, is mandatory unless an attachment is added | [optional] 
 **formMetaData** | **String**| The form meta data of the new text item | [optional] 
 **subject** | **String**| The subject (headline) of the new text item | [optional] 

### Return type

[**ConversationItem**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## addTextItemWithParent

> ConversationItem addTextItemWithParent(convId, itemId, opts)

Adds a message to an item

Adds a message to the existing item. The added message will be a child item of the message with the given itemId. OauthScopes: WRITE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the new item has to be added
let itemId = "itemId_example"; // String | The ID of the item to which the new one has to be added as child
let opts = {
  'attachments': ["null"], // [String] | A comma separated list of attachment IDs from the file API.
  'content': "content_example", // String | The actual content of the item
  'formMetaData': "formMetaData_example", // String | The form meta data of the new text item
  'subject': "subject_example" // String | The subject (headline) of the new text item
};
apiInstance.addTextItemWithParent(convId, itemId, opts, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the new item has to be added | 
 **itemId** | **String**| The ID of the item to which the new one has to be added as child | 
 **attachments** | [**[String]**](String.md)| A comma separated list of attachment IDs from the file API. | [optional] 
 **content** | **String**| The actual content of the item | [optional] 
 **formMetaData** | **String**| The form meta data of the new text item | [optional] 
 **subject** | **String**| The subject (headline) of the new text item | [optional] 

### Return type

[**ConversationItem**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## archiveConversation

> archiveConversation(convId)

Archives conversation

Archives a conversation by muting it OauthScopes: WRITE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation which will be archived
apiInstance.archiveConversation(convId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation which will be archived | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## assignLabel

> Label assignLabel(convId, label)

Adds a label to a conversation

Adds a label to a conversation, you can search and organize your conversations based on these labels OauthScopes: WRITE_CONVERSATIONS, ORGANIZE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the label is added
let label = "label_example"; // String | The actual label 
apiInstance.assignLabel(convId, label, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the label is added | 
 **label** | **String**| The actual label  | 

### Return type

[**Label**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## createCommunityConversation

> Conversation createCommunityConversation(topic, opts)

Creates a community conversation

Creates a community. Communities are open conversations that anyone in a Circuit domain (tenant) can join without having to be added by another user. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let topic = "topic_example"; // String | An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
let opts = {
  'description': "description_example", // String | An optional description for the community conversation
  'participants': ["null"] // [String] | list of participants that will be part of this conversation, specified by the Circuit user ID or the unique email address. At least one participant needs to be added
};
apiInstance.createCommunityConversation(topic, opts, (error, data, response) => {
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
 **topic** | **String**| An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used) | 
 **description** | **String**| An optional description for the community conversation | [optional] 
 **participants** | [**[String]**](String.md)| list of participants that will be part of this conversation, specified by the Circuit user ID or the unique email address. At least one participant needs to be added | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## createDirectConversation

> Conversation createDirectConversation(participant)

Creates a 1-to-1 conversation

Creates a 1-to-1 conversation between the authenticated user and the user with the provided userId. In case there is already an existing 1-to-1 conversation between these users, the endpoint returns the existing conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let participant = "participant_example"; // String | The participant that will be part of this conversation together with the creator, specified by the Circuit user ID or the unique email address
apiInstance.createDirectConversation(participant, (error, data, response) => {
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
 **participant** | **String**| The participant that will be part of this conversation together with the creator, specified by the Circuit user ID or the unique email address | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## createGroupConversation

> Conversation createGroupConversation(participants, opts)

Creates a group conversation

Creates a group conversation between three or more users. The authenticated user is directly added to this conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let participants = ["null"]; // [String] | A list of participants that will be part of this conversation, specified by the Circuit user ID or the unique email address. At least one participant needs to be added
let opts = {
  'topic': "topic_example" // String | An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
};
apiInstance.createGroupConversation(participants, opts, (error, data, response) => {
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
 **participants** | [**[String]**](String.md)| A list of participants that will be part of this conversation, specified by the Circuit user ID or the unique email address. At least one participant needs to be added | 
 **topic** | **String**| An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used) | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## deleteFavorite

> deleteFavorite(convId)

Removes a conversation from favorites

Removes a conversation from favorites. Favorites can be displayed in a separate side tab inside of the Circuit client to have a better overview of important conversations. OauthScopes: WRITE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation which will be unmarked as favorite
apiInstance.deleteFavorite(convId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation which will be unmarked as favorite | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteTextItem

> ConversationItem deleteTextItem(convId, itemId)

Deletes a message from a conversation

Marks a message in the given conversation as deleted. Deleted messages are still part of the conversation, but their content is no more visible. This operation can only be performed on behalf of the message&#39;s creator. OauthScopes: WRITE_CONVERSATIONS, DELETE_CONVERSATIONS_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the item belongs
let itemId = "itemId_example"; // String | The ID of the item that will be deleted
apiInstance.deleteTextItem(convId, itemId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the item belongs | 
 **itemId** | **String**| The ID of the item that will be deleted | 

### Return type

[**ConversationItem**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## flagItem

> flagItem(convId, itemId, opts)

Adds a flag to a message in a conversation

Adds a flag to the given message in the given conversation. OauthScopes: WRITE_CONVERSATIONS, ORGANIZE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the item belongs
let itemId = "itemId_example"; // String | The ID of the item that will be flagged
let opts = {
  'itemCreationTime': "itemCreationTime_example", // String | The time when the item was created
  'parentId': "parentId_example" // String | The ID of the item's parent
};
apiInstance.flagItem(convId, itemId, opts, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the item belongs | 
 **itemId** | **String**| The ID of the item that will be flagged | 
 **itemCreationTime** | **String**| The time when the item was created | [optional] 
 **parentId** | **String**| The ID of the item&#39;s parent | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## getCommunityConversations

> [Conversation] getCommunityConversations(opts)

Gets a list of communities

Gets a list of communities. This endpoint can be used to explore the communities the authenticated user could join. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let opts = {
  'sort': "'ALPHABETICALLY'", // String | Defines the type of sorting for the community conversations (default is alphabetical)
  'order': "'ASCENDING'", // String | Defines the ordering of the conversations (default is ascending)
  'includeOwn': false, // Boolean | If set to false only conversations are returned where the user is no member of, otherwise all community conversations are returned
  'startIndex': 0, // Number | The index of the conversation that is the first one that has to be returned. E.g. if a request starts with startIndex 40 and results 20 the conversations 40 to 60 are returned
  'results': 25 // Number | The maximum number of returned results (default 25). The maximum allowed value is 100.
};
apiInstance.getCommunityConversations(opts, (error, data, response) => {
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
 **sort** | **String**| Defines the type of sorting for the community conversations (default is alphabetical) | [optional] [default to &#39;ALPHABETICALLY&#39;]
 **order** | **String**| Defines the ordering of the conversations (default is ascending) | [optional] [default to &#39;ASCENDING&#39;]
 **includeOwn** | **Boolean**| If set to false only conversations are returned where the user is no member of, otherwise all community conversations are returned | [optional] [default to false]
 **startIndex** | **Number**| The index of the conversation that is the first one that has to be returned. E.g. if a request starts with startIndex 40 and results 20 the conversations 40 to 60 are returned | [optional] [default to 0]
 **results** | **Number**| The maximum number of returned results (default 25). The maximum allowed value is 100. | [optional] [default to 25]

### Return type

[**[Conversation]**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getConversationItems

> [ConversationItem] getConversationItems(convId, opts)

Gets a list of conversation items

Gets a list of conversation items. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the items belong
let opts = {
  'modTime': new Date("2013-10-20T19:20:30+01:00"), // Date | The modification time of the item in UTC format. During the query the items before (default) or after this timestamps are returned. In case no timestamp is specified the current server time in UTC is used, i.e. the last 25 modified items are returned
  'direction': "'BEFORE'", // String | The direction of the search based on the modification time. Valid values are either BEFORE (default) or AFTER
  'results': 25 // Number | The maximum number of returned results (default 25). The maximum allowed value is 100.
};
apiInstance.getConversationItems(convId, opts, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the items belong | 
 **modTime** | **Date**| The modification time of the item in UTC format. During the query the items before (default) or after this timestamps are returned. In case no timestamp is specified the current server time in UTC is used, i.e. the last 25 modified items are returned | [optional] 
 **direction** | **String**| The direction of the search based on the modification time. Valid values are either BEFORE (default) or AFTER | [optional] [default to &#39;BEFORE&#39;]
 **results** | **Number**| The maximum number of returned results (default 25). The maximum allowed value is 100. | [optional] [default to 25]

### Return type

[**[ConversationItem]**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getConversationbyId

> Conversation getConversationbyId(convId)

Gets a conversation

Gets a conversation based on the given ID. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation which should be updated
apiInstance.getConversationbyId(convId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation which should be updated | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getConversations

> [Conversation] getConversations(opts)

Gets a list of conversations

Gets a list of conversations and communities the authenticated user participates in. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let opts = {
  'modTime': new Date("2013-10-20T19:20:30+01:00"), // Date | The modification time of the conversation in UTC format. During the query the conversations before (<i>default</i>) or after this timestamp are returned. In case no timestamp is specified the current server time in UTC is used, i.e. the last 25 modified conversations are returned
  'direction': "'BEFORE'", // String | The direction of the search based on the modification time. Valid values are either BEFORE (default) or AFTER
  'results': 25 // Number | The maximum number of returned results (default 25). The maximum allowed value is 100.
};
apiInstance.getConversations(opts, (error, data, response) => {
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
 **modTime** | **Date**| The modification time of the conversation in UTC format. During the query the conversations before (&lt;i&gt;default&lt;/i&gt;) or after this timestamp are returned. In case no timestamp is specified the current server time in UTC is used, i.e. the last 25 modified conversations are returned | [optional] 
 **direction** | **String**| The direction of the search based on the modification time. Valid values are either BEFORE (default) or AFTER | [optional] [default to &#39;BEFORE&#39;]
 **results** | **Number**| The maximum number of returned results (default 25). The maximum allowed value is 100. | [optional] [default to 25]

### Return type

[**[Conversation]**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getConversationsById

> [Conversation] getConversationsById(convIds)

Gets conversations

Gets conversation based on the given IDs. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convIds = ["null"]; // [String] | The array of IDs of the conversations which should be retrieved
apiInstance.getConversationsById(convIds, (error, data, response) => {
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
 **convIds** | [**[String]**](String.md)| The array of IDs of the conversations which should be retrieved | 

### Return type

[**[Conversation]**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getConversationsByLabel

> ConversationsPage getConversationsByLabel(labelId, opts)

Returns conversations with a certain label

Returns conversations with matching labels and paginated  OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let labelId = "labelId_example"; // String | Id of the label to look for
let opts = {
  'nextPagePointer': "nextPagePointer_example", // String | Pointer to the next page of conversations if there are any
  'pageSize': 25 // Number | Numbers of max conversations per page
};
apiInstance.getConversationsByLabel(labelId, opts, (error, data, response) => {
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
 **labelId** | **String**| Id of the label to look for | 
 **nextPagePointer** | **String**| Pointer to the next page of conversations if there are any | [optional] 
 **pageSize** | **Number**| Numbers of max conversations per page | [optional] [default to 25]

### Return type

[**ConversationsPage**](ConversationsPage.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getDirectConversation

> Conversation getDirectConversation(participant)

Checks for a 1-to-1 conversation

Checks if a 1-to-1 conversation between the authenticated user and the user with the provided userId exists. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let participant = "participant_example"; // String | The participant that will be part of this conversation together with the creator, specified by the Circuit user ID or the unique email address
apiInstance.getDirectConversation(participant, (error, data, response) => {
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
 **participant** | **String**| The participant that will be part of this conversation together with the creator, specified by the Circuit user ID or the unique email address | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getFavoriteConversations

> [ModelString] getFavoriteConversations()

Gets favorite conversations

Gets the conversationIds which are marked as favorites. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
apiInstance.getFavoriteConversations((error, data, response) => {
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

[**[ModelString]**](ModelString.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getFlagItem

> [ConversationItem] getFlagItem(convId)

Gets a list of the flagged messages of a conversation

Gets a list of all the flagged messages in the given conversation. OauthScopes: READ_CONVERSATIONS, ORGANIZE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the item belongs
apiInstance.getFlagItem(convId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the item belongs | 

### Return type

[**[ConversationItem]**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getFlagItemConv

> [ConversationItem] getFlagItemConv()

Gets a list of the flagged messages

Gets a list of all the messages the authenticated user has flagged. This endpoint should be used carefully in case where the authenticated user has a lot of flagged messages. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
apiInstance.getFlagItemConv((error, data, response) => {
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

[**[ConversationItem]**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getJoinDetails

> ConversationDetails getJoinDetails(convId)

Gets the conference details of a conversation

Gets the conference details of the given conversation. Conference details include the URL, which is used to join the conference through a web or mobile application, as well as the dial-in phone numbers and conference PIN, which are used to join the conference by phone. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation for which the join details should be returned
apiInstance.getJoinDetails(convId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation for which the join details should be returned | 

### Return type

[**ConversationDetails**](ConversationDetails.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getJoinDetailsMultiple

> [ConversationDetails] getJoinDetailsMultiple(convIds)

Gets the conference details for multiple conversations

Gets the conference details of the given conversations. Conference details include the URL, which is used to join the conference through a web or mobile application, as well as the dial-in phone numbers and conference PIN, which are used to join the conference by phone. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convIds = ["null"]; // [String] | An array of IDs of the conversations for which the join details should be returned
apiInstance.getJoinDetailsMultiple(convIds, (error, data, response) => {
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
 **convIds** | [**[String]**](String.md)| An array of IDs of the conversations for which the join details should be returned | 

### Return type

[**[ConversationDetails]**](ConversationDetails.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getParticipantsByConvId

> [ConversationParticipantsList] getParticipantsByConvId(convId, pageSize, opts)

Performs a list of participants

Performs a search for participants. The max number of participants is configurable. If more participants are available a search pointer is returned for consecutive calls. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The id of the conversation the participants are searched for.
let pageSize = 3.4; // Number | The page size of the hit list
let opts = {
  'name': "name_example", // String | Part of name to filter the results
  'type': "'REGULAR'", // String | Type of participant to filter the results
  'searchPointer': "searchPointer_example" // String | Pointer for paged output. Add to consecutive request to get next page
};
apiInstance.getParticipantsByConvId(convId, pageSize, opts, (error, data, response) => {
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
 **convId** | **String**| The id of the conversation the participants are searched for. | 
 **pageSize** | **Number**| The page size of the hit list | 
 **name** | **String**| Part of name to filter the results | [optional] 
 **type** | **String**| Type of participant to filter the results | [optional] [default to &#39;REGULAR&#39;]
 **searchPointer** | **String**| Pointer for paged output. Add to consecutive request to get next page | [optional] 

### Return type

[**[ConversationParticipantsList]**](ConversationParticipantsList.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getPinnedConversations

> [PinnedTopic] getPinnedConversations(convId)

Returns pinned topics of a conversation

Returns pinned topics of a conversation OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | ID of the conversation
apiInstance.getPinnedConversations(convId, (error, data, response) => {
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
 **convId** | **String**| ID of the conversation | 

### Return type

[**[PinnedTopic]**](PinnedTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getSingleConversationtem

> ConversationItem getSingleConversationtem(itemId)

Returns a text item

Returns a text item for a given item id OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let itemId = "itemId_example"; // String | The ID of the item that will be returned
apiInstance.getSingleConversationtem(itemId, (error, data, response) => {
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
 **itemId** | **String**| The ID of the item that will be returned | 

### Return type

[**ConversationItem**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## joinCommunityConversation

> Conversation joinCommunityConversation(convId)

Adds the authenticated user to a community

Adds the authenticated user to the given community (i.e., allows the user to join this community). Contrary to the operation of adding a new participant, this operation can only be performed by a user who is not yet a member of the community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation which the user will join
apiInstance.joinCommunityConversation(convId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation which the user will join | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## likeItem

> likeItem(convId, itemId)

Adds a \&quot;like\&quot; to a message

Adds a \&quot;like\&quot; to the given message in the given conversation OauthScopes: WRITE_CONVERSATIONS, UPDATE_CONVERSATION_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the item belongs
let itemId = "itemId_example"; // String | The ID of the item that will be liked
apiInstance.likeItem(convId, itemId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the item belongs | 
 **itemId** | **String**| The ID of the item that will be liked | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## moderateConversation

> moderateConversation(convId)

Set conversation moderated

Set a conversation in moderatd mode. Moderators can be added and removed OauthScopes: WRITE_CONVERSATIONS, MODERATE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation which will be set to moderated state
apiInstance.moderateConversation(convId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation which will be set to moderated state | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## pinAConversation

> Conversation pinAConversation(convId, itemId)

Pins a topic of a conversation

Pins a topic of a conversation OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation
let itemId = "itemId_example"; // String | The ID of the topic
apiInstance.pinAConversation(convId, itemId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation | 
 **itemId** | **String**| The ID of the topic | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## removeLabel

> Label removeLabel(labelId)

Remove a user label

Remove a label from the list of user labels OauthScopes: WRITE_USER_PROFILE, ORGANIZE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let labelId = "labelId_example"; // String | The label value to remove, either the unique ID or the label value
apiInstance.removeLabel(labelId, (error, data, response) => {
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
 **labelId** | **String**| The label value to remove, either the unique ID or the label value | 

### Return type

[**Label**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## removeModerators

> removeModerators(convId, moderators)

Remove moderators

Removes a list of moderators from a conversation OauthScopes: WRITE_CONVERSATIONS, MODERATE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation where the moderators are removed
let moderators = ["null"]; // [String] | The list of moderator ids to remove
apiInstance.removeModerators(convId, moderators, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation where the moderators are removed | 
 **moderators** | [**[String]**](String.md)| The list of moderator ids to remove | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## removeParticipantCommunity

> Conversation removeParticipantCommunity(convId, participants)

Removes participants from a community

Removes one or more participants from the given community. The last participant of a community cannot be removed. This operation can only be performed by a user who is already a member of the community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation from which the participant have to be removed
let participants = ["null"]; // [String] | The IDs or the unique email addresses of the Circuit users that have to be removed
apiInstance.removeParticipantCommunity(convId, participants, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation from which the participant have to be removed | 
 **participants** | [**[String]**](String.md)| The IDs or the unique email addresses of the Circuit users that have to be removed | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## removeParticipantGroup

> Conversation removeParticipantGroup(convId, participants)

Removes participants from a group conversation

Removes one or more participants from the given group conversation. The last participant of a group conversation cannot be removed. This operation can only be performed on behalf of a user who is already a member of the conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation from which the participant have to be removed
let participants = ["null"]; // [String] | The IDs or the unique email addresses of the Circuit users that have to be removed
apiInstance.removeParticipantGroup(convId, participants, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation from which the participant have to be removed | 
 **participants** | [**[String]**](String.md)| The IDs or the unique email addresses of the Circuit users that have to be removed | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## resolveInvitationToken

> Conversation resolveInvitationToken(token)

Resolves an invite token to a conversation

Resolves an invite token to a conversation OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let token = "token_example"; // String | The invite token to resolve
apiInstance.resolveInvitationToken(token, (error, data, response) => {
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
 **token** | **String**| The invite token to resolve | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## searchConversations

> ConversationSearchResult searchConversations(term, opts)

Performs a conversation search

Performs a search for conversation content. A maximum of 100 conversations is returned. If you hit this limit you should refine the search term. OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let term = "term_example"; // String | The search term
let opts = {
  'includeItemIds': false, // Boolean | Optional parameter to specify if a deep or normal search is executed. In a deep search all matching item IDs inside every conversation are returned (up to a maximum of 100). For a normal search only the conversation IDs are returned. Default is a normal search (without item IDs).
  'scope': "'ALL'" // String | The search scope, FILES||PEOPLE||MEMBERS||MESSAGES||SENTBY||ALL||CONVERSATIONS||LABEL||FILTER
};
apiInstance.searchConversations(term, opts, (error, data, response) => {
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
 **term** | **String**| The search term | 
 **includeItemIds** | **Boolean**| Optional parameter to specify if a deep or normal search is executed. In a deep search all matching item IDs inside every conversation are returned (up to a maximum of 100). For a normal search only the conversation IDs are returned. Default is a normal search (without item IDs). | [optional] [default to false]
 **scope** | **String**| The search scope, FILES||PEOPLE||MEMBERS||MESSAGES||SENTBY||ALL||CONVERSATIONS||LABEL||FILTER | [optional] [default to &#39;ALL&#39;]

### Return type

[**ConversationSearchResult**](ConversationSearchResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## unFlagItem

> unFlagItem(convId, itemId)

Removes the flag from a message

Removes the flag from a given message that is posted to the given conversation. OauthScopes: WRITE_CONVERSATIONS, ORGANIZE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the item belongs
let itemId = "itemId_example"; // String | The ID of the item that will be flagged
apiInstance.unFlagItem(convId, itemId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the item belongs | 
 **itemId** | **String**| The ID of the item that will be flagged | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## unPinAConversation

> Conversation unPinAConversation(convId, itemId)

Unpins a topic of a conversation

Unpins a topic of a conversation OauthScopes: READ_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation
let itemId = "itemId_example"; // String | The ID of the topic
apiInstance.unPinAConversation(convId, itemId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation | 
 **itemId** | **String**| The ID of the topic | 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## unassignLabel

> Label unassignLabel(convId, labelId)

Removes a label from a conversation

Removes a label from a conversation, you can search and organize your conversations based on these labels OauthScopes: WRITE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation from which the label is removed
let labelId = "labelId_example"; // String | The actual label 
apiInstance.unassignLabel(convId, labelId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation from which the label is removed | 
 **labelId** | **String**| The actual label  | 

### Return type

[**Label**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## undoArchiveConversation

> undoArchiveConversation(convId)

Unmute conversation

The conversation will no longer be archived but active again OauthScopes: WRITE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation which will be unmarked as muted
apiInstance.undoArchiveConversation(convId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation which will be unmarked as muted | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## unlikeItem

> unlikeItem(convId, itemId)

Removes a \&quot;like\&quot; from a message

Removes a \&quot;like\&quot; from the given message in the given conversation OauthScopes: WRITE_CONVERSATIONS, UPDATE_CONVERSATION_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the item belongs
let itemId = "itemId_example"; // String | The ID of the item that will be unliked
apiInstance.unlikeItem(convId, itemId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the item belongs | 
 **itemId** | **String**| The ID of the item that will be unliked | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## unmoderateConversation

> unmoderateConversation(convId)

Set conversation unmoderated

Set a conversation to unmoderatd mode OauthScopes: WRITE_CONVERSATIONS, MODERATE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation which will be set to unmoderated state
apiInstance.unmoderateConversation(convId, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation which will be set to unmoderated state | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateConversationCommunity

> Conversation updateConversationCommunity(convId, opts)

Updates the information of a community

Updates the information of the given community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation which should be updated
let opts = {
  'description': "description_example", // String | An optional description for the community conversation
  'topic': "topic_example" // String | An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
};
apiInstance.updateConversationCommunity(convId, opts, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation which should be updated | 
 **description** | **String**| An optional description for the community conversation | [optional] 
 **topic** | **String**| An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used) | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## updateConversationGroup

> Conversation updateConversationGroup(convId, opts)

Updates the information of a group conversation

Updates the information of the given group conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation which should be updated
let opts = {
  'topic': "topic_example" // String | An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
};
apiInstance.updateConversationGroup(convId, opts, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation which should be updated | 
 **topic** | **String**| An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used) | [optional] 

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## updateProfile

> User updateProfile(opts)

Updates the user profile

Updates the user profile of the authenticated user OauthScopes: WRITE_USER_PROFILE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let opts = {
  'firstname': "firstname_example", // String | The new firstname of the user
  'jobTitle': "jobTitle_example", // String | The new job title of the user
  'lastname': "lastname_example", // String | The new lastname of the user
  'locale': "locale_example" // String | The new locale of the user. One of EN_US, DE_DE, EN_GB, ES_ES, FR_FR, IT_IT, RU_RU, ZH_HANS_CN.
};
apiInstance.updateProfile(opts, (error, data, response) => {
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
 **firstname** | **String**| The new firstname of the user | [optional] 
 **jobTitle** | **String**| The new job title of the user | [optional] 
 **lastname** | **String**| The new lastname of the user | [optional] 
 **locale** | **String**| The new locale of the user. One of EN_US, DE_DE, EN_GB, ES_ES, FR_FR, IT_IT, RU_RU, ZH_HANS_CN. | [optional] 

### Return type

[**User**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## updateTextItem

> ConversationItem updateTextItem(convId, itemId, opts)

Updates a message

Updates the content or subject of the existing message. Only the creator of the message is allowed to perform this operation. OauthScopes: WRITE_CONVERSATIONS, UPDATE_CONVERSATION_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.ConversationsApi();
let convId = "convId_example"; // String | The ID of the conversation to which the item belongs
let itemId = "itemId_example"; // String | The ID of the item to update
let opts = {
  'attachments': ["null"], // [String] | A comma separated list of attachment IDs from the file API.
  'content': "content_example", // String | The actual content of the item
  'formMetaData': "formMetaData_example", // String | The form meta data of the new text item
  'subject': "subject_example" // String | The subject (headline) of the new text item
};
apiInstance.updateTextItem(convId, itemId, opts, (error, data, response) => {
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
 **convId** | **String**| The ID of the conversation to which the item belongs | 
 **itemId** | **String**| The ID of the item to update | 
 **attachments** | [**[String]**](String.md)| A comma separated list of attachment IDs from the file API. | [optional] 
 **content** | **String**| The actual content of the item | [optional] 
 **formMetaData** | **String**| The form meta data of the new text item | [optional] 
 **subject** | **String**| The subject (headline) of the new text item | [optional] 

### Return type

[**ConversationItem**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml

