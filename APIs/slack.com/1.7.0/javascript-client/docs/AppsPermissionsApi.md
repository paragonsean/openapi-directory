# SlackWebApi.AppsPermissionsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsPermissionsInfo**](AppsPermissionsApi.md#appsPermissionsInfo) | **GET** /apps.permissions.info | 
[**appsPermissionsRequest**](AppsPermissionsApi.md#appsPermissionsRequest) | **GET** /apps.permissions.request | 



## appsPermissionsInfo

> AppsPermissionsInfoSchema appsPermissionsInfo(opts)



Returns list of permissions this app has on a team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsPermissionsApi();
let opts = {
  'token': "token_example" // String | Authentication token. Requires scope: `none`
};
apiInstance.appsPermissionsInfo(opts, (error, data, response) => {
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


## appsPermissionsRequest

> AppsPermissionsRequestSchema appsPermissionsRequest(token, scopes, triggerId)



Allows an app to request additional scopes

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AppsPermissionsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let scopes = "scopes_example"; // String | A comma separated list of scopes to request for
let triggerId = "triggerId_example"; // String | Token used to trigger the permissions API
apiInstance.appsPermissionsRequest(token, scopes, triggerId, (error, data, response) => {
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

