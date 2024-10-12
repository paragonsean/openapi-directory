# SlackWebApi.ChatScheduledMessagesApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chatScheduledMessagesList**](ChatScheduledMessagesApi.md#chatScheduledMessagesList) | **GET** /chat.scheduledMessages.list | 



## chatScheduledMessagesList

> ChatScheduledMessagesListSchema chatScheduledMessagesList(opts)



Returns a list of scheduled messages.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ChatScheduledMessagesApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `none`
  'channel': "channel_example", // String | The channel of the scheduled messages
  'latest': 3.4, // Number | A UNIX timestamp of the latest value in the time range
  'oldest': 3.4, // Number | A UNIX timestamp of the oldest value in the time range
  'limit': 56, // Number | Maximum number of original entries to return.
  'cursor': "cursor_example" // String | For pagination purposes, this is the `cursor` value returned from a previous call to `chat.scheduledmessages.list` indicating where you want to start this call from.
};
apiInstance.chatScheduledMessagesList(opts, (error, data, response) => {
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
 **channel** | **String**| The channel of the scheduled messages | [optional] 
 **latest** | **Number**| A UNIX timestamp of the latest value in the time range | [optional] 
 **oldest** | **Number**| A UNIX timestamp of the oldest value in the time range | [optional] 
 **limit** | **Number**| Maximum number of original entries to return. | [optional] 
 **cursor** | **String**| For pagination purposes, this is the &#x60;cursor&#x60; value returned from a previous call to &#x60;chat.scheduledmessages.list&#x60; indicating where you want to start this call from. | [optional] 

### Return type

[**ChatScheduledMessagesListSchema**](ChatScheduledMessagesListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

