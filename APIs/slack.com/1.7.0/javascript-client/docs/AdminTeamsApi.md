# SlackWebApi.AdminTeamsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminTeamsCreate**](AdminTeamsApi.md#adminTeamsCreate) | **POST** /admin.teams.create | 
[**adminTeamsList**](AdminTeamsApi.md#adminTeamsList) | **GET** /admin.teams.list | 



## adminTeamsCreate

> DefaultSuccessTemplate adminTeamsCreate(token, teamDomain, teamName, opts)



Create an Enterprise team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminTeamsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:write`
let teamDomain = "teamDomain_example"; // String | Team domain (for example, slacksoftballteam).
let teamName = "teamName_example"; // String | Team name (for example, Slack Softball Team).
let opts = {
  'teamDescription': "teamDescription_example", // String | Description for the team.
  'teamDiscoverability': "teamDiscoverability_example" // String | Who can join the team. A team's discoverability can be `open`, `closed`, `invite_only`, or `unlisted`.
};
apiInstance.adminTeamsCreate(token, teamDomain, teamName, opts, (error, data, response) => {
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
 **teamDomain** | **String**| Team domain (for example, slacksoftballteam). | 
 **teamName** | **String**| Team name (for example, Slack Softball Team). | 
 **teamDescription** | **String**| Description for the team. | [optional] 
 **teamDiscoverability** | **String**| Who can join the team. A team&#39;s discoverability can be &#x60;open&#x60;, &#x60;closed&#x60;, &#x60;invite_only&#x60;, or &#x60;unlisted&#x60;. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminTeamsList

> DefaultSuccessTemplate adminTeamsList(token, opts)



List all teams on an Enterprise organization

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminTeamsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:read`
let opts = {
  'limit': 56, // Number | The maximum number of items to return. Must be between 1 - 100 both inclusive.
  'cursor': "cursor_example" // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.
};
apiInstance.adminTeamsList(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.teams:read&#x60; | 
 **limit** | **Number**| The maximum number of items to return. Must be between 1 - 100 both inclusive. | [optional] 
 **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

