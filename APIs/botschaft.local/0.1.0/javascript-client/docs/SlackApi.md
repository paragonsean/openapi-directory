# FastApi.SlackApi

All URIs are relative to *http://botschaft.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slackGetSlackGet**](SlackApi.md#slackGetSlackGet) | **GET** /slack | Slack Get
[**slackPostSlackPost**](SlackApi.md#slackPostSlackPost) | **POST** /slack | Slack Post



## slackGetSlackGet

> Object slackGetSlackGet(channel, opts)

Slack Get

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.SlackApi();
let channel = "channel_example"; // String | 
let opts = {
  'message': "message_example", // String | 
  'base64Message': "base64Message_example", // String | 
  'authorization': "authorization_example" // String | 
};
apiInstance.slackGetSlackGet(channel, opts, (error, data, response) => {
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
 **channel** | **String**|  | 
 **message** | **String**|  | [optional] 
 **base64Message** | **String**|  | [optional] 
 **authorization** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## slackPostSlackPost

> Object slackPostSlackPost(slackMessageRequest, opts)

Slack Post

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.SlackApi();
let slackMessageRequest = new FastApi.SlackMessageRequest(); // SlackMessageRequest | 
let opts = {
  'authorization': "authorization_example" // String | 
};
apiInstance.slackPostSlackPost(slackMessageRequest, opts, (error, data, response) => {
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
 **slackMessageRequest** | [**SlackMessageRequest**](SlackMessageRequest.md)|  | 
 **authorization** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

