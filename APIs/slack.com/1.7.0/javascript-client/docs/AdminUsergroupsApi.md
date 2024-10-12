# SlackWebApi.AdminUsergroupsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminUsergroupsAddChannels**](AdminUsergroupsApi.md#adminUsergroupsAddChannels) | **POST** /admin.usergroups.addChannels | 
[**adminUsergroupsAddTeams**](AdminUsergroupsApi.md#adminUsergroupsAddTeams) | **POST** /admin.usergroups.addTeams | 
[**adminUsergroupsListChannels**](AdminUsergroupsApi.md#adminUsergroupsListChannels) | **GET** /admin.usergroups.listChannels | 
[**adminUsergroupsRemoveChannels**](AdminUsergroupsApi.md#adminUsergroupsRemoveChannels) | **POST** /admin.usergroups.removeChannels | 



## adminUsergroupsAddChannels

> DefaultSuccessTemplate adminUsergroupsAddChannels(token, channelIds, usergroupId, opts)



Add one or more default channels to an IDP group.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.usergroups:write`
let channelIds = "channelIds_example"; // String | Comma separated string of channel IDs.
let usergroupId = "usergroupId_example"; // String | ID of the IDP group to add default channels for.
let opts = {
  'teamId': "teamId_example" // String | The workspace to add default channels in.
};
apiInstance.adminUsergroupsAddChannels(token, channelIds, usergroupId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.usergroups:write&#x60; | 
 **channelIds** | **String**| Comma separated string of channel IDs. | 
 **usergroupId** | **String**| ID of the IDP group to add default channels for. | 
 **teamId** | **String**| The workspace to add default channels in. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminUsergroupsAddTeams

> DefaultSuccessTemplate adminUsergroupsAddTeams(token, teamIds, usergroupId, opts)



Associate one or more default workspaces with an organization-wide IDP group.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
let teamIds = "teamIds_example"; // String | A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the organization associated with the token.
let usergroupId = "usergroupId_example"; // String | An encoded usergroup (IDP Group) ID.
let opts = {
  'autoProvision': true // Boolean | When `true`, this method automatically creates new workspace accounts for the IDP group members.
};
apiInstance.adminUsergroupsAddTeams(token, teamIds, usergroupId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:write&#x60; | 
 **teamIds** | **String**| A comma separated list of encoded team (workspace) IDs. Each workspace *MUST* belong to the organization associated with the token. | 
 **usergroupId** | **String**| An encoded usergroup (IDP Group) ID. | 
 **autoProvision** | **Boolean**| When &#x60;true&#x60;, this method automatically creates new workspace accounts for the IDP group members. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminUsergroupsListChannels

> DefaultSuccessTemplate adminUsergroupsListChannels(token, usergroupId, opts)



List the channels linked to an org-level IDP group (user group).

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.usergroups:read`
let usergroupId = "usergroupId_example"; // String | ID of the IDP group to list default channels for.
let opts = {
  'teamId': "teamId_example", // String | ID of the the workspace.
  'includeNumMembers': true // Boolean | Flag to include or exclude the count of members per channel.
};
apiInstance.adminUsergroupsListChannels(token, usergroupId, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.usergroups:read&#x60; | 
 **usergroupId** | **String**| ID of the IDP group to list default channels for. | 
 **teamId** | **String**| ID of the the workspace. | [optional] 
 **includeNumMembers** | **Boolean**| Flag to include or exclude the count of members per channel. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## adminUsergroupsRemoveChannels

> DefaultSuccessTemplate adminUsergroupsRemoveChannels(token, channelIds, usergroupId)



Remove one or more default channels from an org-level IDP group (user group).

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminUsergroupsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.usergroups:write`
let channelIds = "channelIds_example"; // String | Comma-separated string of channel IDs
let usergroupId = "usergroupId_example"; // String | ID of the IDP Group
apiInstance.adminUsergroupsRemoveChannels(token, channelIds, usergroupId, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.usergroups:write&#x60; | 
 **channelIds** | **String**| Comma-separated string of channel IDs | 
 **usergroupId** | **String**| ID of the IDP Group | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

