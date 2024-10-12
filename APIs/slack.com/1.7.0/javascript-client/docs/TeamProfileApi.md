# SlackWebApi.TeamProfileApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teamProfileGet**](TeamProfileApi.md#teamProfileGet) | **GET** /team.profile.get | 



## teamProfileGet

> TeamProfileGetSuccessSchema teamProfileGet(token, opts)



Retrieve a team&#39;s profile.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.TeamProfileApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users.profile:read`
let opts = {
  'visibility': "visibility_example" // String | Filter by visibility.
};
apiInstance.teamProfileGet(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:read&#x60; | 
 **visibility** | **String**| Filter by visibility. | [optional] 

### Return type

[**TeamProfileGetSuccessSchema**](TeamProfileGetSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

