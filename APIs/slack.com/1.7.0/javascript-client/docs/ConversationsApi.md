# SlackWebApi.ConversationsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversationsArchive**](ConversationsApi.md#conversationsArchive) | **POST** /conversations.archive | 
[**conversationsClose**](ConversationsApi.md#conversationsClose) | **POST** /conversations.close | 
[**conversationsCreate**](ConversationsApi.md#conversationsCreate) | **POST** /conversations.create | 
[**conversationsHistory**](ConversationsApi.md#conversationsHistory) | **GET** /conversations.history | 
[**conversationsInfo**](ConversationsApi.md#conversationsInfo) | **GET** /conversations.info | 
[**conversationsInvite**](ConversationsApi.md#conversationsInvite) | **POST** /conversations.invite | 
[**conversationsJoin**](ConversationsApi.md#conversationsJoin) | **POST** /conversations.join | 
[**conversationsKick**](ConversationsApi.md#conversationsKick) | **POST** /conversations.kick | 
[**conversationsLeave**](ConversationsApi.md#conversationsLeave) | **POST** /conversations.leave | 
[**conversationsList**](ConversationsApi.md#conversationsList) | **GET** /conversations.list | 
[**conversationsMark**](ConversationsApi.md#conversationsMark) | **POST** /conversations.mark | 
[**conversationsMembers**](ConversationsApi.md#conversationsMembers) | **GET** /conversations.members | 
[**conversationsOpen**](ConversationsApi.md#conversationsOpen) | **POST** /conversations.open | 
[**conversationsRename**](ConversationsApi.md#conversationsRename) | **POST** /conversations.rename | 
[**conversationsReplies**](ConversationsApi.md#conversationsReplies) | **GET** /conversations.replies | 
[**conversationsSetPurpose**](ConversationsApi.md#conversationsSetPurpose) | **POST** /conversations.setPurpose | 
[**conversationsSetTopic**](ConversationsApi.md#conversationsSetTopic) | **POST** /conversations.setTopic | 
[**conversationsUnarchive**](ConversationsApi.md#conversationsUnarchive) | **POST** /conversations.unarchive | 



## conversationsArchive

> ConversationsArchiveSuccessSchema conversationsArchive(opts)



Archives a conversation.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example" // String | ID of conversation to archive
};
apiInstance.conversationsArchive(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| ID of conversation to archive | [optional] 

### Return type

[**ConversationsArchiveSuccessSchema**](ConversationsArchiveSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsClose

> ConversationsCloseSuccessSchema conversationsClose(opts)



Closes a direct message or multi-person direct message.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example" // String | Conversation to close.
};
apiInstance.conversationsClose(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| Conversation to close. | [optional] 

### Return type

[**ConversationsCloseSuccessSchema**](ConversationsCloseSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsCreate

> ConversationsCreateSuccessSchema conversationsCreate(opts)



Initiates a public or private channel-based conversation

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'isPrivate': true, // Boolean | Create a private channel instead of a public one
  'name': "name_example" // String | Name of the public or private channel to create
};
apiInstance.conversationsCreate(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **isPrivate** | **Boolean**| Create a private channel instead of a public one | [optional] 
 **name** | **String**| Name of the public or private channel to create | [optional] 

### Return type

[**ConversationsCreateSuccessSchema**](ConversationsCreateSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsHistory

> ConversationsHistorySuccessSchema conversationsHistory(opts)



Fetches a conversation&#39;s history of messages and events.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:history`
  'channel': "channel_example", // String | Conversation ID to fetch history for.
  'latest': 3.4, // Number | End of time range of messages to include in results.
  'oldest': 3.4, // Number | Start of time range of messages to include in results.
  'inclusive': true, // Boolean | Include messages with latest or oldest timestamp in results only when either timestamp is specified.
  'limit': 56, // Number | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.
  'cursor': "cursor_example" // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
};
apiInstance.conversationsHistory(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:history&#x60; | [optional] 
 **channel** | **String**| Conversation ID to fetch history for. | [optional] 
 **latest** | **Number**| End of time range of messages to include in results. | [optional] 
 **oldest** | **Number**| Start of time range of messages to include in results. | [optional] 
 **inclusive** | **Boolean**| Include messages with latest or oldest timestamp in results only when either timestamp is specified. | [optional] 
 **limit** | **Number**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached. | [optional] 
 **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] 

### Return type

[**ConversationsHistorySuccessSchema**](ConversationsHistorySuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conversationsInfo

> ConversationsInfoSuccessSchema conversationsInfo(opts)



Retrieve information about a conversation.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:read`
  'channel': "channel_example", // String | Conversation ID to learn more about
  'includeLocale': true, // Boolean | Set this to `true` to receive the locale for this conversation. Defaults to `false`
  'includeNumMembers': true // Boolean | Set to `true` to include the member count for the specified conversation. Defaults to `false`
};
apiInstance.conversationsInfo(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:read&#x60; | [optional] 
 **channel** | **String**| Conversation ID to learn more about | [optional] 
 **includeLocale** | **Boolean**| Set this to &#x60;true&#x60; to receive the locale for this conversation. Defaults to &#x60;false&#x60; | [optional] 
 **includeNumMembers** | **Boolean**| Set to &#x60;true&#x60; to include the member count for the specified conversation. Defaults to &#x60;false&#x60; | [optional] 

### Return type

[**ConversationsInfoSuccessSchema**](ConversationsInfoSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conversationsInvite

> ConversationsInviteErrorSchema conversationsInvite(opts)



Invites users to a channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example", // String | The ID of the public or private channel to invite user(s) to.
  'users': "users_example" // String | A comma separated list of user IDs. Up to 1000 users may be listed.
};
apiInstance.conversationsInvite(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| The ID of the public or private channel to invite user(s) to. | [optional] 
 **users** | **String**| A comma separated list of user IDs. Up to 1000 users may be listed. | [optional] 

### Return type

[**ConversationsInviteErrorSchema**](ConversationsInviteErrorSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsJoin

> ConversationsJoinSuccessSchema conversationsJoin(opts)



Joins an existing conversation.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `channels:write`
  'channel': "channel_example" // String | ID of conversation to join
};
apiInstance.conversationsJoin(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;channels:write&#x60; | [optional] 
 **channel** | **String**| ID of conversation to join | [optional] 

### Return type

[**ConversationsJoinSuccessSchema**](ConversationsJoinSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsKick

> ConversationsKickSuccessSchema conversationsKick(opts)



Removes a user from a conversation.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example", // String | ID of conversation to remove user from.
  'user': "user_example" // String | User ID to be removed.
};
apiInstance.conversationsKick(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| ID of conversation to remove user from. | [optional] 
 **user** | **String**| User ID to be removed. | [optional] 

### Return type

[**ConversationsKickSuccessSchema**](ConversationsKickSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsLeave

> ConversationsLeaveSuccessSchema conversationsLeave(opts)



Leaves a conversation.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example" // String | Conversation to leave
};
apiInstance.conversationsLeave(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| Conversation to leave | [optional] 

### Return type

[**ConversationsLeaveSuccessSchema**](ConversationsLeaveSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsList

> ConversationsListSuccessSchema conversationsList(opts)



Lists all channels in a Slack team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:read`
  'excludeArchived': true, // Boolean | Set to `true` to exclude archived channels from the list
  'types': "types_example", // String | Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`
  'limit': 56, // Number | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000.
  'cursor': "cursor_example" // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
};
apiInstance.conversationsList(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:read&#x60; | [optional] 
 **excludeArchived** | **Boolean**| Set to &#x60;true&#x60; to exclude archived channels from the list | [optional] 
 **types** | **String**| Mix and match channel types by providing a comma-separated list of any combination of &#x60;public_channel&#x60;, &#x60;private_channel&#x60;, &#x60;mpim&#x60;, &#x60;im&#x60; | [optional] 
 **limit** | **Number**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. Must be an integer no larger than 1000. | [optional] 
 **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] 

### Return type

[**ConversationsListSuccessSchema**](ConversationsListSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conversationsMark

> ConversationsMarkSuccessSchema conversationsMark(opts)



Sets the read cursor in a channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example", // String | Channel or conversation to set the read cursor for.
  'ts': 3.4 // Number | Unique identifier of message you want marked as most recently seen in this conversation.
};
apiInstance.conversationsMark(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| Channel or conversation to set the read cursor for. | [optional] 
 **ts** | **Number**| Unique identifier of message you want marked as most recently seen in this conversation. | [optional] 

### Return type

[**ConversationsMarkSuccessSchema**](ConversationsMarkSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsMembers

> ConversationsMembersSuccessSchema conversationsMembers(opts)



Retrieve members of a conversation.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:read`
  'channel': "channel_example", // String | ID of the conversation to retrieve members for
  'limit': 56, // Number | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.
  'cursor': "cursor_example" // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
};
apiInstance.conversationsMembers(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:read&#x60; | [optional] 
 **channel** | **String**| ID of the conversation to retrieve members for | [optional] 
 **limit** | **Number**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached. | [optional] 
 **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] 

### Return type

[**ConversationsMembersSuccessSchema**](ConversationsMembersSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conversationsOpen

> ConversationsOpenSuccessSchema conversationsOpen(opts)



Opens or resumes a direct message or multi-person direct message.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example", // String | Resume a conversation by supplying an `im` or `mpim`'s ID. Or provide the `users` field instead.
  'returnIm': true, // Boolean | Boolean, indicates you want the full IM channel definition in the response.
  'users': "users_example" // String | Comma separated lists of users. If only one user is included, this creates a 1:1 DM.  The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a `channel` when not supplying `users`.
};
apiInstance.conversationsOpen(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| Resume a conversation by supplying an &#x60;im&#x60; or &#x60;mpim&#x60;&#39;s ID. Or provide the &#x60;users&#x60; field instead. | [optional] 
 **returnIm** | **Boolean**| Boolean, indicates you want the full IM channel definition in the response. | [optional] 
 **users** | **String**| Comma separated lists of users. If only one user is included, this creates a 1:1 DM.  The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a &#x60;channel&#x60; when not supplying &#x60;users&#x60;. | [optional] 

### Return type

[**ConversationsOpenSuccessSchema**](ConversationsOpenSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsRename

> ConversationsRenameSuccessSchema conversationsRename(opts)



Renames a conversation.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example", // String | ID of conversation to rename
  'name': "name_example" // String | New name for conversation.
};
apiInstance.conversationsRename(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| ID of conversation to rename | [optional] 
 **name** | **String**| New name for conversation. | [optional] 

### Return type

[**ConversationsRenameSuccessSchema**](ConversationsRenameSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsReplies

> ConversationsRepliesSuccessSchema conversationsReplies(opts)



Retrieve a thread of messages posted to a conversation

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:history`
  'channel': "channel_example", // String | Conversation ID to fetch thread from.
  'ts': 3.4, // Number | Unique identifier of a thread's parent message. `ts` must be the timestamp of an existing message with 0 or more replies. If there are no replies then just the single message referenced by `ts` will return - it is just an ordinary, unthreaded message.
  'latest': 3.4, // Number | End of time range of messages to include in results.
  'oldest': 3.4, // Number | Start of time range of messages to include in results.
  'inclusive': true, // Boolean | Include messages with latest or oldest timestamp in results only when either timestamp is specified.
  'limit': 56, // Number | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.
  'cursor': "cursor_example" // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
};
apiInstance.conversationsReplies(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:history&#x60; | [optional] 
 **channel** | **String**| Conversation ID to fetch thread from. | [optional] 
 **ts** | **Number**| Unique identifier of a thread&#39;s parent message. &#x60;ts&#x60; must be the timestamp of an existing message with 0 or more replies. If there are no replies then just the single message referenced by &#x60;ts&#x60; will return - it is just an ordinary, unthreaded message. | [optional] 
 **latest** | **Number**| End of time range of messages to include in results. | [optional] 
 **oldest** | **Number**| Start of time range of messages to include in results. | [optional] 
 **inclusive** | **Boolean**| Include messages with latest or oldest timestamp in results only when either timestamp is specified. | [optional] 
 **limit** | **Number**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached. | [optional] 
 **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] 

### Return type

[**ConversationsRepliesSuccessSchema**](ConversationsRepliesSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conversationsSetPurpose

> ConversationsSetPurposeSuccessSchema conversationsSetPurpose(opts)



Sets the purpose for a conversation.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example", // String | Conversation to set the purpose of
  'purpose': "purpose_example" // String | A new, specialer purpose
};
apiInstance.conversationsSetPurpose(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| Conversation to set the purpose of | [optional] 
 **purpose** | **String**| A new, specialer purpose | [optional] 

### Return type

[**ConversationsSetPurposeSuccessSchema**](ConversationsSetPurposeSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsSetTopic

> ConversationsSetTopicSuccessSchema conversationsSetTopic(opts)



Sets the topic for a conversation.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example", // String | Conversation to set the topic of
  'topic': "topic_example" // String | The new topic string. Does not support formatting or linkification.
};
apiInstance.conversationsSetTopic(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| Conversation to set the topic of | [optional] 
 **topic** | **String**| The new topic string. Does not support formatting or linkification. | [optional] 

### Return type

[**ConversationsSetTopicSuccessSchema**](ConversationsSetTopicSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## conversationsUnarchive

> ConversationsUnarchiveSuccessSchema conversationsUnarchive(opts)



Reverses conversation archival.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ConversationsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `conversations:write`
  'channel': "channel_example" // String | ID of conversation to unarchive
};
apiInstance.conversationsUnarchive(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;conversations:write&#x60; | [optional] 
 **channel** | **String**| ID of conversation to unarchive | [optional] 

### Return type

[**ConversationsUnarchiveSuccessSchema**](ConversationsUnarchiveSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

