# SlackWebApi.AdminAppsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminAppsApprove**](AdminAppsApi.md#adminAppsApprove) | **POST** /admin.apps.approve | 
[**adminAppsRestrict**](AdminAppsApi.md#adminAppsRestrict) | **POST** /admin.apps.restrict | 



## adminAppsApprove

> DefaultSuccessTemplate adminAppsApprove(token, opts)



Approve an app for installation on a workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminAppsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.apps:write`
let opts = {
  'appId': "appId_example", // String | The id of the app to approve.
  'requestId': "requestId_example", // String | The id of the request to approve.
  'teamId': "teamId_example" // String | 
};
apiInstance.adminAppsApprove(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.apps:write&#x60; | 
 **appId** | **String**| The id of the app to approve. | [optional] 
 **requestId** | **String**| The id of the request to approve. | [optional] 
 **teamId** | **String**|  | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## adminAppsRestrict

> DefaultSuccessTemplate adminAppsRestrict(token, opts)



Restrict an app for installation on a workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminAppsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.apps:write`
let opts = {
  'appId': "appId_example", // String | The id of the app to restrict.
  'requestId': "requestId_example", // String | The id of the request to restrict.
  'teamId': "teamId_example" // String | 
};
apiInstance.adminAppsRestrict(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.apps:write&#x60; | 
 **appId** | **String**| The id of the app to restrict. | [optional] 
 **requestId** | **String**| The id of the request to restrict. | [optional] 
 **teamId** | **String**|  | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

