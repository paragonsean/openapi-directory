# SlackWebApi.AdminInviteRequestsDeniedApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminInviteRequestsDeniedList**](AdminInviteRequestsDeniedApi.md#adminInviteRequestsDeniedList) | **GET** /admin.inviteRequests.denied.list | 



## adminInviteRequestsDeniedList

> DefaultSuccessTemplate adminInviteRequestsDeniedList(token, opts)



List all denied workspace invite requests.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminInviteRequestsDeniedApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.invites:read`
let opts = {
  'teamId': "teamId_example", // String | ID for the workspace where the invite requests were made.
  'cursor': "cursor_example", // String | Value of the `next_cursor` field sent as part of the previous api response
  'limit': 56 // Number | The number of results that will be returned by the API on each invocation. Must be between 1 - 1000 both inclusive
};
apiInstance.adminInviteRequestsDeniedList(token, opts, (error, data, response) => {
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
 **cursor** | **String**| Value of the &#x60;next_cursor&#x60; field sent as part of the previous api response | [optional] 
 **limit** | **Number**| The number of results that will be returned by the API on each invocation. Must be between 1 - 1000 both inclusive | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

