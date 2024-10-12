# SlackWebApi.AdminConversationsEkmApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adminConversationsEkmListOriginalConnectedChannelInfo**](AdminConversationsEkmApi.md#adminConversationsEkmListOriginalConnectedChannelInfo) | **GET** /admin.conversations.ekm.listOriginalConnectedChannelInfo | 



## adminConversationsEkmListOriginalConnectedChannelInfo

> DefaultSuccessTemplate adminConversationsEkmListOriginalConnectedChannelInfo(token, opts)



List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.AdminConversationsEkmApi();
let token = "token_example"; // String | Authentication token. Requires scope: `admin.conversations:read`
let opts = {
  'channelIds': "channelIds_example", // String | A comma-separated list of channels to filter to.
  'teamIds': "teamIds_example", // String | A comma-separated list of the workspaces to which the channels you would like returned belong.
  'limit': 56, // Number | The maximum number of items to return. Must be between 1 - 1000 both inclusive.
  'cursor': "cursor_example" // String | Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.
};
apiInstance.adminConversationsEkmListOriginalConnectedChannelInfo(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;admin.conversations:read&#x60; | 
 **channelIds** | **String**| A comma-separated list of channels to filter to. | [optional] 
 **teamIds** | **String**| A comma-separated list of the workspaces to which the channels you would like returned belong. | [optional] 
 **limit** | **Number**| The maximum number of items to return. Must be between 1 - 1000 both inclusive. | [optional] 
 **cursor** | **String**| Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

