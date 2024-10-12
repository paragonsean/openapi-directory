# SlackWebApi.AdminAppsRestrictedApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminAppsRestrictedList**](AdminAppsRestrictedApi.md#adminAppsRestrictedList) | **GET** /admin.apps.restricted.list | 



## adminAppsRestrictedList

> DefaultSuccessTemplate adminAppsRestrictedList(token, opts)



List restricted apps for an org or workspace.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminAppsRestrictedApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.apps:read`
let opts = {
  'limit': 56, // Number | The maximum number of items to return. Must be between 1 - 1000 both inclusive.
  'cursor': "cursor_example", // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page
  'teamId': "teamId_example", // String | 
  'enterpriseId': "enterpriseId_example" // String | 
};
apiInstance.adminAppsRestrictedList(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.apps:read&#x60; | 
 **limit** | **Number**| The maximum number of items to return. Must be between 1 - 1000 both inclusive. | [optional] 
 **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page | [optional] 
 **teamId** | **String**|  | [optional] 
 **enterpriseId** | **String**|  | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

