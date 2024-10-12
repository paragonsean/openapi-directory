# DiscourseApiDocumentation.PrivateMessagesApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTopicPostPM_1**](PrivateMessagesApi.md#createTopicPostPM_1) | **POST** /posts.json | Creates a new topic, a new post, or a private message
[**getUserSentPrivateMessages**](PrivateMessagesApi.md#getUserSentPrivateMessages) | **GET** /topics/private-messages-sent/{username}.json | Get a list of private messages sent for a user
[**listUserPrivateMessages**](PrivateMessagesApi.md#listUserPrivateMessages) | **GET** /topics/private-messages/{username}.json | Get a list of private messages for a user



## createTopicPostPM_1

> CreateTopicPostPM200Response createTopicPostPM_1(opts)

Creates a new topic, a new post, or a private message

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PrivateMessagesApi();
let opts = {
  'createTopicPostPMRequest': new DiscourseApiDocumentation.CreateTopicPostPMRequest() // CreateTopicPostPMRequest | 
};
apiInstance.createTopicPostPM_1(opts, (error, data, response) => {
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
 **createTopicPostPMRequest** | [**CreateTopicPostPMRequest**](CreateTopicPostPMRequest.md)|  | [optional] 

### Return type

[**CreateTopicPostPM200Response**](CreateTopicPostPM200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getUserSentPrivateMessages

> GetUserSentPrivateMessages200Response getUserSentPrivateMessages(username)

Get a list of private messages sent for a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PrivateMessagesApi();
let username = "username_example"; // String | 
apiInstance.getUserSentPrivateMessages(username, (error, data, response) => {
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
 **username** | **String**|  | 

### Return type

[**GetUserSentPrivateMessages200Response**](GetUserSentPrivateMessages200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUserPrivateMessages

> ListUserPrivateMessages200Response listUserPrivateMessages(username)

Get a list of private messages for a user

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PrivateMessagesApi();
let username = "username_example"; // String | 
apiInstance.listUserPrivateMessages(username, (error, data, response) => {
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
 **username** | **String**|  | 

### Return type

[**ListUserPrivateMessages200Response**](ListUserPrivateMessages200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

