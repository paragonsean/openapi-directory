# SlackWebApi.AdminInviteRequestsApprovedApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminInviteRequestsApprovedList**](AdminInviteRequestsApprovedApi.md#adminInviteRequestsApprovedList) | **GET** /admin.inviteRequests.approved.list | 



## adminInviteRequestsApprovedList

> DefaultSuccessTemplate adminInviteRequestsApprovedList(token, opts)



List all approved workspace invite requests.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminInviteRequestsApprovedApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.invites:read`
let opts = {
  'teamId': "teamId_example", // String | ID for the workspace where the invite requests were made.
  'cursor': "cursor_example", // String | Value of the `next_cursor` field sent as part of the previous API response
  'limit': 56 // Number | The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive
};
apiInstance.adminInviteRequestsApprovedList(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.invites:read&#x60; | 
 **teamId** | **String**| ID for the workspace where the invite requests were made. | [optional] 
 **cursor** | **String**| Value of the &#x60;next_cursor&#x60; field sent as part of the previous API response | [optional] 
 **limit** | **Number**| The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

