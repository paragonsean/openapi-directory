# SlackWebApi.AdminConversationsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminConversationsArchive**](AdminConversationsApi.md#adminConversationsArchive) | **POST** /admin.conversations.archive | 
[**adminConversationsConvertToPrivate**](AdminConversationsApi.md#adminConversationsConvertToPrivate) | **POST** /admin.conversations.convertToPrivate | 
[**adminConversationsCreate**](AdminConversationsApi.md#adminConversationsCreate) | **POST** /admin.conversations.create | 
[**adminConversationsDelete**](AdminConversationsApi.md#adminConversationsDelete) | **POST** /admin.conversations.delete | 
[**adminConversationsDisconnectShared**](AdminConversationsApi.md#adminConversationsDisconnectShared) | **POST** /admin.conversations.disconnectShared | 
[**adminConversationsGetConversationPrefs**](AdminConversationsApi.md#adminConversationsGetConversationPrefs) | **GET** /admin.conversations.getConversationPrefs | 
[**adminConversationsGetTeams**](AdminConversationsApi.md#adminConversationsGetTeams) | **GET** /admin.conversations.getTeams | 
[**adminConversationsInvite**](AdminConversationsApi.md#adminConversationsInvite) | **POST** /admin.conversations.invite | 
[**adminConversationsRename**](AdminConversationsApi.md#adminConversationsRename) | **POST** /admin.conversations.rename | 
[**adminConversationsSearch**](AdminConversationsApi.md#adminConversationsSearch) | **GET** /admin.conversations.search | 
[**adminConversationsSetConversationPrefs**](AdminConversationsApi.md#adminConversationsSetConversationPrefs) | **POST** /admin.conversations.setConversationPrefs | 
[**adminConversationsSetTeams**](AdminConversationsApi.md#adminConversationsSetTeams) | **POST** /admin.conversations.setTeams | 
[**adminConversationsUnarchive**](AdminConversationsApi.md#adminConversationsUnarchive) | **POST** /admin.conversations.unarchive | 



## adminConversationsArchive

> AdminConversationsArchiveSchema adminConversationsArchive(token, channelId)



Archive a public or private channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let channelId = "channelId_example"; // String | The channel to archive.
apiInstance.adminConversationsArchive(token, channelId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **channelId** | **String**| The channel to archive. | 

### Return type

[**AdminConversationsArchiveSchema**](AdminConversationsArchiveSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminConversationsConvertToPrivate

> AdminConversationsConvertToPrivateSchema adminConversationsConvertToPrivate(token, channelId)



Convert a public channel to a private channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let channelId = "channelId_example"; // String | The channel to convert to private.
apiInstance.adminConversationsConvertToPrivate(token, channelId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **channelId** | **String**| The channel to convert to private. | 

### Return type

[**AdminConversationsConvertToPrivateSchema**](AdminConversationsConvertToPrivateSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminConversationsCreate

> AdminConversationsCreateSchema adminConversationsCreate(token, isPrivate, name, opts)



Create a public or private channel-based conversation.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let isPrivate = true; // Boolean | When `true`, creates a private channel instead of a public channel
let name = "name_example"; // String | Name of the public or private channel to create.
let opts = {
  'description': "description_example", // String | Description of the public or private channel to create.
  'orgWide': true, // Boolean | When `true`, the channel will be available org-wide. Note: if the channel is not `org_wide=true`, you must specify a `team_id` for this channel
  'teamId': "teamId_example" // String | The workspace to create the channel in. Note: this argument is required unless you set `org_wide=true`.
};
apiInstance.adminConversationsCreate(token, isPrivate, name, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **isPrivate** | **Boolean**| When &#x60;true&#x60;, creates a private channel instead of a public channel | 
 **name** | **String**| Name of the public or private channel to create. | 
 **description** | **String**| Description of the public or private channel to create. | [optional] 
 **orgWide** | **Boolean**| When &#x60;true&#x60;, the channel will be available org-wide. Note: if the channel is not &#x60;org_wide&#x3D;true&#x60;, you must specify a &#x60;team_id&#x60; for this channel | [optional] 
 **teamId** | **String**| The workspace to create the channel in. Note: this argument is required unless you set &#x60;org_wide&#x3D;true&#x60;. | [optional] 

### Return type

[**AdminConversationsCreateSchema**](AdminConversationsCreateSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminConversationsDelete

> AdminConversationsDeleteSchema adminConversationsDelete(token, channelId)



Delete a public or private channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let channelId = "channelId_example"; // String | The channel to delete.
apiInstance.adminConversationsDelete(token, channelId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **channelId** | **String**| The channel to delete. | 

### Return type

[**AdminConversationsDeleteSchema**](AdminConversationsDeleteSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminConversationsDisconnectShared

> AdminConversationsRenameSchema adminConversationsDisconnectShared(token, channelId, opts)



Disconnect a connected channel from one or more workspaces.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let channelId = "channelId_example"; // String | The channel to be disconnected from some workspaces.
let opts = {
  'leavingTeamIds': "leavingTeamIds_example" // String | The team to be removed from the channel. Currently only a single team id can be specified.
};
apiInstance.adminConversationsDisconnectShared(token, channelId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **channelId** | **String**| The channel to be disconnected from some workspaces. | 
 **leavingTeamIds** | **String**| The team to be removed from the channel. Currently only a single team id can be specified. | [optional] 

### Return type

[**AdminConversationsRenameSchema**](AdminConversationsRenameSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminConversationsGetConversationPrefs

> AdminConversationsGetConversationPrefsSchema adminConversationsGetConversationPrefs(token, channelId)



Get conversation preferences for a public or private channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:read`
let channelId = "channelId_example"; // String | The channel to get preferences for.
apiInstance.adminConversationsGetConversationPrefs(token, channelId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:read&#x60; | 
 **channelId** | **String**| The channel to get preferences for. | 

### Return type

[**AdminConversationsGetConversationPrefsSchema**](AdminConversationsGetConversationPrefsSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminConversationsGetTeams

> AdminConversationsGetTeamsSchema adminConversationsGetTeams(token, channelId, opts)



Get all the workspaces a given public or private channel is connected to within this Enterprise org.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:read`
let channelId = "channelId_example"; // String | The channel to determine connected workspaces within the organization for.
let opts = {
  'cursor': "cursor_example", // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page
  'limit': 56 // Number | The maximum number of items to return. Must be between 1 - 1000 both inclusive.
};
apiInstance.adminConversationsGetTeams(token, channelId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:read&#x60; | 
 **channelId** | **String**| The channel to determine connected workspaces within the organization for. | 
 **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page | [optional] 
 **limit** | **Number**| The maximum number of items to return. Must be between 1 - 1000 both inclusive. | [optional] 

### Return type

[**AdminConversationsGetTeamsSchema**](AdminConversationsGetTeamsSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminConversationsInvite

> AdminConversationsInviteSchema adminConversationsInvite(token, channelId, userIds)



Invite a user to a public or private channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let channelId = "channelId_example"; // String | The channel that the users will be invited to.
let userIds = "userIds_example"; // String | The users to invite.
apiInstance.adminConversationsInvite(token, channelId, userIds, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **channelId** | **String**| The channel that the users will be invited to. | 
 **userIds** | **String**| The users to invite. | 

### Return type

[**AdminConversationsInviteSchema**](AdminConversationsInviteSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminConversationsRename

> AdminConversationsRenameSchema1 adminConversationsRename(token, channelId, name)



Rename a public or private channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let channelId = "channelId_example"; // String | The channel to rename.
let name = "name_example"; // String | 
apiInstance.adminConversationsRename(token, channelId, name, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **channelId** | **String**| The channel to rename. | 
 **name** | **String**|  | 

### Return type

[**AdminConversationsRenameSchema1**](AdminConversationsRenameSchema1.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminConversationsSearch

> AdminConversationsSearchSchema adminConversationsSearch(token, opts)



Search for public or private channels in an Enterprise organization.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:read`
let opts = {
  'teamIds': "teamIds_example", // String | Comma separated string of team IDs, signifying the workspaces to search through.
  'query': "query_example", // String | Name of the the channel to query by.
  'limit': 56, // Number | Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10.
  'cursor': "cursor_example", // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.
  'searchChannelTypes': "searchChannelTypes_example", // String | The type of channel to include or exclude in the search. For example `private` will search private channels, while `private_exclude` will exclude them. For a full list of types, check the [Types section](#types).
  'sort': "sort_example", // String | Possible values are `relevant` (search ranking based on what we think is closest), `name` (alphabetical), `member_count` (number of users in the channel), and `created` (date channel was created). You can optionally pair this with the `sort_dir` arg to change how it is sorted 
  'sortDir': "sortDir_example" // String | Sort direction. Possible values are `asc` for ascending order like (1, 2, 3) or (a, b, c), and `desc` for descending order like (3, 2, 1) or (c, b, a)
};
apiInstance.adminConversationsSearch(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:read&#x60; | 
 **teamIds** | **String**| Comma separated string of team IDs, signifying the workspaces to search through. | [optional] 
 **query** | **String**| Name of the the channel to query by. | [optional] 
 **limit** | **Number**| Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10. | [optional] 
 **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page. | [optional] 
 **searchChannelTypes** | **String**| The type of channel to include or exclude in the search. For example &#x60;private&#x60; will search private channels, while &#x60;private_exclude&#x60; will exclude them. For a full list of types, check the [Types section](#types). | [optional] 
 **sort** | **String**| Possible values are &#x60;relevant&#x60; (search ranking based on what we think is closest), &#x60;name&#x60; (alphabetical), &#x60;member_count&#x60; (number of users in the channel), and &#x60;created&#x60; (date channel was created). You can optionally pair this with the &#x60;sort_dir&#x60; arg to change how it is sorted  | [optional] 
 **sortDir** | **String**| Sort direction. Possible values are &#x60;asc&#x60; for ascending order like (1, 2, 3) or (a, b, c), and &#x60;desc&#x60; for descending order like (3, 2, 1) or (c, b, a) | [optional] 

### Return type

[**AdminConversationsSearchSchema**](AdminConversationsSearchSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminConversationsSetConversationPrefs

> AdminConversationsSetConversationPrefsSchema adminConversationsSetConversationPrefs(token, channelId, prefs)



Set the posting permissions for a public or private channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let channelId = "channelId_example"; // String | The channel to set the prefs for
let prefs = "prefs_example"; // String | The prefs for this channel in a stringified JSON format.
apiInstance.adminConversationsSetConversationPrefs(token, channelId, prefs, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **channelId** | **String**| The channel to set the prefs for | 
 **prefs** | **String**| The prefs for this channel in a stringified JSON format. | 

### Return type

[**AdminConversationsSetConversationPrefsSchema**](AdminConversationsSetConversationPrefsSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminConversationsSetTeams

> DefaultSuccessTemplate adminConversationsSetTeams(token, channelId, opts)



Set the workspaces in an Enterprise grid org that connect to a public or private channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let channelId = "channelId_example"; // String | The encoded `channel_id` to add or remove to workspaces.
let opts = {
  'orgChannel': true, // Boolean | True if channel has to be converted to an org channel
  'targetTeamIds': "targetTeamIds_example", // String | A comma-separated list of workspaces to which the channel should be shared. Not required if the channel is being shared org-wide.
  'teamId': "teamId_example" // String | The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace shared channel.
};
apiInstance.adminConversationsSetTeams(token, channelId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **channelId** | **String**| The encoded &#x60;channel_id&#x60; to add or remove to workspaces. | 
 **orgChannel** | **Boolean**| True if channel has to be converted to an org channel | [optional] 
 **targetTeamIds** | **String**| A comma-separated list of workspaces to which the channel should be shared. Not required if the channel is being shared org-wide. | [optional] 
 **teamId** | **String**| The workspace to which the channel belongs. Omit this argument if the channel is a cross-workspace shared channel. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminConversationsUnarchive

> AdminConversationsUnarchiveSchema adminConversationsUnarchive(token, channelId)



Unarchive a public or private channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let channelId = "channelId_example"; // String | The channel to unarchive.
apiInstance.adminConversationsUnarchive(token, channelId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **channelId** | **String**| The channel to unarchive. | 

### Return type

[**AdminConversationsUnarchiveSchema**](AdminConversationsUnarchiveSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

