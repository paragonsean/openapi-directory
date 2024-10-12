# SlackWebApi.TeamApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teamAccessLogs**](TeamApi.md#teamAccessLogs) | **GET** /team.accessLogs | 
[**teamBillableInfo**](TeamApi.md#teamBillableInfo) | **GET** /team.billableInfo | 
[**teamInfo**](TeamApi.md#teamInfo) | **GET** /team.info | 
[**teamIntegrationLogs**](TeamApi.md#teamIntegrationLogs) | **GET** /team.integrationLogs | 
[**teamProfileGet_0**](TeamApi.md#teamProfileGet_0) | **GET** /team.profile.get | 



## teamAccessLogs

> TeamAccessLogsSchema teamAccessLogs(token, opts)



Gets the access logs for the current team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.TeamApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin`
let opts = {
  'before': "before_example", // String | End of time range of logs to include in results (inclusive).
  'count': "count_example", // String | 
  'page': "page_example" // String | 
};
apiInstance.teamAccessLogs(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin&#x60; | 
 **before** | **String**| End of time range of logs to include in results (inclusive). | [optional] 
 **count** | **String**|  | [optional] 
 **page** | **String**|  | [optional] 

### Return type

[**TeamAccessLogsSchema**](TeamAccessLogsSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamBillableInfo

> DefaultSuccessTemplate teamBillableInfo(token, opts)



Gets billable users information for the current team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.TeamApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin`
let opts = {
  'user': "user_example" // String | A user to retrieve the billable information for. Defaults to all users.
};
apiInstance.teamBillableInfo(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin&#x60; | 
 **user** | **String**| A user to retrieve the billable information for. Defaults to all users. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamInfo

> TeamInfoSchema teamInfo(token, opts)



Gets information about the current team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.TeamApi();
let token = "token_example"; // String | Authentication token. Requires scope: `team:read`
let opts = {
  'team': "team_example" // String | Team to get info on, if omitted, will return information about the current team. Will only return team that the authenticated token is allowed to see through external shared channels
};
apiInstance.teamInfo(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;team:read&#x60; | 
 **team** | **String**| Team to get info on, if omitted, will return information about the current team. Will only return team that the authenticated token is allowed to see through external shared channels | [optional] 

### Return type

[**TeamInfoSchema**](TeamInfoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamIntegrationLogs

> TeamIntegrationLogsSchema teamIntegrationLogs(token, opts)



Gets the integration logs for the current team.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.TeamApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin`
let opts = {
  'appId': "appId_example", // String | Filter logs to this Slack app. Defaults to all logs.
  'changeType': "changeType_example", // String | Filter logs with this change type. Defaults to all logs.
  'count': "count_example", // String | 
  'page': "page_example", // String | 
  'serviceId': "serviceId_example", // String | Filter logs to this service. Defaults to all logs.
  'user': "user_example" // String | Filter logs generated by this user’s actions. Defaults to all logs.
};
apiInstance.teamIntegrationLogs(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin&#x60; | 
 **appId** | **String**| Filter logs to this Slack app. Defaults to all logs. | [optional] 
 **changeType** | **String**| Filter logs with this change type. Defaults to all logs. | [optional] 
 **count** | **String**|  | [optional] 
 **page** | **String**|  | [optional] 
 **serviceId** | **String**| Filter logs to this service. Defaults to all logs. | [optional] 
 **user** | **String**| Filter logs generated by this user’s actions. Defaults to all logs. | [optional] 

### Return type

[**TeamIntegrationLogsSchema**](TeamIntegrationLogsSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamProfileGet_0

> TeamProfileGetSuccessSchema teamProfileGet_0(token, opts)



Retrieve a team&#39;s profile.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.TeamApi();
let token = "token_example"; // String | Authentication token. Requires scope: `users.profile:read`
let opts = {
  'visibility': "visibility_example" // String | Filter by visibility.
};
apiInstance.teamProfileGet_0(token, opts, (error, data, response) => {
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

