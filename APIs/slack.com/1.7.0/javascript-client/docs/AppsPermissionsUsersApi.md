# SlackWebApi.AppsPermissionsUsersApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsPermissionsUsersList**](AppsPermissionsUsersApi.md#appsPermissionsUsersList) | **GET** /apps.permissions.users.list | 
[**appsPermissionsUsersRequest**](AppsPermissionsUsersApi.md#appsPermissionsUsersRequest) | **GET** /apps.permissions.users.request | 



## appsPermissionsUsersList

> DefaultSuccessTemplate appsPermissionsUsersList(token, opts)



Returns list of user grants and corresponding scopes this app has on a team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsPermissionsUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let opts = {
  'cursor': "cursor_example", // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
  'limit': 56 // Number | The maximum number of items to return.
};
apiInstance.appsPermissionsUsersList(token, opts, (error, data, response) => {
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
 **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] 
 **limit** | **Number**| The maximum number of items to return. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsPermissionsUsersRequest

> DefaultSuccessTemplate appsPermissionsUsersRequest(token, scopes, triggerId, user)



Enables an app to trigger a permissions modal to grant an app access to a user access scope.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsPermissionsUsersApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let scopes = "scopes_example"; // String | A comma separated list of user scopes to request for
let triggerId = "triggerId_example"; // String | Token used to trigger the request
let user = "user_example"; // String | The user this scope is being requested for
apiInstance.appsPermissionsUsersRequest(token, scopes, triggerId, user, (error, data, response) => {
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
 **scopes** | **String**| A comma separated list of user scopes to request for | 
 **triggerId** | **String**| Token used to trigger the request | 
 **user** | **String**| The user this scope is being requested for | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

