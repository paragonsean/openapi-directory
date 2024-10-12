# SlackWebApi.AppsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsEventAuthorizationsList_0**](AppsApi.md#appsEventAuthorizationsList_0) | **GET** /apps.event.authorizations.list | 
[**appsPermissionsInfo_0**](AppsApi.md#appsPermissionsInfo_0) | **GET** /apps.permissions.info | 
[**appsPermissionsRequest_0**](AppsApi.md#appsPermissionsRequest_0) | **GET** /apps.permissions.request | 
[**appsPermissionsResourcesList_0**](AppsApi.md#appsPermissionsResourcesList_0) | **GET** /apps.permissions.resources.list | 
[**appsPermissionsScopesList_0**](AppsApi.md#appsPermissionsScopesList_0) | **GET** /apps.permissions.scopes.list | 
[**appsPermissionsUsersList_0**](AppsApi.md#appsPermissionsUsersList_0) | **GET** /apps.permissions.users.list | 
[**appsPermissionsUsersRequest_0**](AppsApi.md#appsPermissionsUsersRequest_0) | **GET** /apps.permissions.users.request | 
[**appsUninstall**](AppsApi.md#appsUninstall) | **GET** /apps.uninstall | 



## appsEventAuthorizationsList_0

> DefaultSuccessTemplate appsEventAuthorizationsList_0(token, eventContext, opts)



Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `authorizations:read`
let eventContext = "eventContext_example"; // String | 
let opts = {
  'cursor': "cursor_example", // String | 
  'limit': 56 // Number | 
};
apiInstance.appsEventAuthorizationsList_0(token, eventContext, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;authorizations:read&#x60; | 
 **eventContext** | **String**|  | 
 **cursor** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsPermissionsInfo_0

> AppsPermissionsInfoSchema appsPermissionsInfo_0(opts)



Returns list of permissions this app has on a team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsApi();
let opts = {
  'token': "token_example" // String | Authentication token. Requires scope: `none`
};
apiInstance.appsPermissionsInfo_0(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | [optional] 

### Return type

[**AppsPermissionsInfoSchema**](AppsPermissionsInfoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsPermissionsRequest_0

> AppsPermissionsRequestSchema appsPermissionsRequest_0(token, scopes, triggerId)



Allows an app to request additional scopes

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let scopes = "scopes_example"; // String | A comma separated list of scopes to request for
let triggerId = "triggerId_example"; // String | Token used to trigger the permissions API
apiInstance.appsPermissionsRequest_0(token, scopes, triggerId, (error, data, response) => {
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
 **scopes** | **String**| A comma separated list of scopes to request for | 
 **triggerId** | **String**| Token used to trigger the permissions API | 

### Return type

[**AppsPermissionsRequestSchema**](AppsPermissionsRequestSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsPermissionsResourcesList_0

> AppsPermissionsResourcesListSuccessSchema appsPermissionsResourcesList_0(token, opts)



Returns list of resource grants this app has on a team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let opts = {
  'cursor': "cursor_example", // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
  'limit': 56 // Number | The maximum number of items to return.
};
apiInstance.appsPermissionsResourcesList_0(token, opts, (error, data, response) => {
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

[**AppsPermissionsResourcesListSuccessSchema**](AppsPermissionsResourcesListSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsPermissionsScopesList_0

> ApiPermissionsScopesListSuccessSchema appsPermissionsScopesList_0(token)



Returns list of scopes this app has on a team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
apiInstance.appsPermissionsScopesList_0(token, (error, data, response) => {
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


## appsPermissionsUsersList_0

> DefaultSuccessTemplate appsPermissionsUsersList_0(token, opts)



Returns list of user grants and corresponding scopes this app has on a team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let opts = {
  'cursor': "cursor_example", // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
  'limit': 56 // Number | The maximum number of items to return.
};
apiInstance.appsPermissionsUsersList_0(token, opts, (error, data, response) => {
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


## appsPermissionsUsersRequest_0

> DefaultSuccessTemplate appsPermissionsUsersRequest_0(token, scopes, triggerId, user)



Enables an app to trigger a permissions modal to grant an app access to a user access scope.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let scopes = "scopes_example"; // String | A comma separated list of user scopes to request for
let triggerId = "triggerId_example"; // String | Token used to trigger the request
let user = "user_example"; // String | The user this scope is being requested for
apiInstance.appsPermissionsUsersRequest_0(token, scopes, triggerId, user, (error, data, response) => {
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


## appsUninstall

> AppsUninstallSchema appsUninstall(opts)



Uninstalls your app from a workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `none`
  'clientId': "clientId_example", // String | Issued when you created your application.
  'clientSecret': "clientSecret_example" // String | Issued when you created your application.
};
apiInstance.appsUninstall(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;none&#x60; | [optional] 
 **clientId** | **String**| Issued when you created your application. | [optional] 
 **clientSecret** | **String**| Issued when you created your application. | [optional] 

### Return type

[**AppsUninstallSchema**](AppsUninstallSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

