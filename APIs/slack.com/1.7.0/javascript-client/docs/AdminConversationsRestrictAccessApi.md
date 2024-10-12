# SlackWebApi.AdminConversationsRestrictAccessApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminConversationsRestrictAccessAddGroup**](AdminConversationsRestrictAccessApi.md#adminConversationsRestrictAccessAddGroup) | **POST** /admin.conversations.restrictAccess.addGroup | 
[**adminConversationsRestrictAccessListGroups**](AdminConversationsRestrictAccessApi.md#adminConversationsRestrictAccessListGroups) | **GET** /admin.conversations.restrictAccess.listGroups | 
[**adminConversationsRestrictAccessRemoveGroup**](AdminConversationsRestrictAccessApi.md#adminConversationsRestrictAccessRemoveGroup) | **POST** /admin.conversations.restrictAccess.removeGroup | 



## adminConversationsRestrictAccessAddGroup

> DefaultSuccessTemplate adminConversationsRestrictAccessAddGroup(channelId, groupId, token, opts)



Add an allowlist of IDP groups for accessing a channel

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsRestrictAccessApi();
let channelId = "channelId_example"; // String | The channel to link this group to.
let groupId = "groupId_example"; // String | The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to be an allowlist for the private channel.
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
let opts = {
  'teamId': "teamId_example" // String | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
};
apiInstance.adminConversationsRestrictAccessAddGroup(channelId, groupId, token, opts, (error, data, response) => {
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
 **channelId** | **String**| The channel to link this group to. | 
 **groupId** | **String**| The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to be an allowlist for the private channel. | 
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 
 **teamId** | **String**| The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminConversationsRestrictAccessListGroups

> DefaultSuccessTemplate adminConversationsRestrictAccessListGroups(token, channelId, opts)



List all IDP Groups linked to a channel

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsRestrictAccessApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:read`
let channelId = "channelId_example"; // String | 
let opts = {
  'teamId': "teamId_example" // String | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
};
apiInstance.adminConversationsRestrictAccessListGroups(token, channelId, opts, (error, data, response) => {
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
 **channelId** | **String**|  | 
 **teamId** | **String**| The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminConversationsRestrictAccessRemoveGroup

> DefaultSuccessTemplate adminConversationsRestrictAccessRemoveGroup(channelId, groupId, teamId, token)



Remove a linked IDP group linked from a private channel

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsRestrictAccessApi();
let channelId = "channelId_example"; // String | The channel to remove the linked group from.
let groupId = "groupId_example"; // String | The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to remove from the private channel.
let teamId = "teamId_example"; // String | The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization.
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:write`
apiInstance.adminConversationsRestrictAccessRemoveGroup(channelId, groupId, teamId, token, (error, data, response) => {
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
 **channelId** | **String**| The channel to remove the linked group from. | 
 **groupId** | **String**| The [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-Grid-org) ID to remove from the private channel. | 
 **teamId** | **String**| The workspace where the channel exists. This argument is required for channels only tied to one workspace, and optional for channels that are shared across an organization. | 
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:write&#x60; | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

