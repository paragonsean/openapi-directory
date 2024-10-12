# SlackWebApi.AppsPermissionsScopesApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsPermissionsScopesList**](AppsPermissionsScopesApi.md#appsPermissionsScopesList) | **GET** /apps.permissions.scopes.list | 



## appsPermissionsScopesList

> ApiPermissionsScopesListSuccessSchema appsPermissionsScopesList(token)



Returns list of scopes this app has on a team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsPermissionsScopesApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
apiInstance.appsPermissionsScopesList(token, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | 

### Return type

[**ApiPermissionsScopesListSuccessSchema**](ApiPermissionsScopesListSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

