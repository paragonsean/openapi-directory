# SlackWebApi.AdminTeamsOwnersApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminTeamsOwnersList**](AdminTeamsOwnersApi.md#adminTeamsOwnersList) | **GET** /admin.teams.owners.list | 



## adminTeamsOwnersList

> DefaultSuccessTemplate adminTeamsOwnersList(token, teamId, opts)



List all of the owners on a given workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminTeamsOwnersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.teams:read`
let teamId = "teamId_example"; // String | 
let opts = {
  'limit': 56, // Number | The maximum number of items to return. Must be between 1 - 1000 both inclusive.
  'cursor': "cursor_example" // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.
};
apiInstance.adminTeamsOwnersList(token, teamId, opts, (error, data, response) => {
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
 **teamId** | **String**|  | 
 **limit** | **Number**| The maximum number of items to return. Must be between 1 - 1000 both inclusive. | [optional] 
 **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

