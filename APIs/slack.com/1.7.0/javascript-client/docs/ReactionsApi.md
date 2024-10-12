# SlackWebApi.ReactionsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reactionsAdd**](ReactionsApi.md#reactionsAdd) | **POST** /reactions.add | 
[**reactionsGet**](ReactionsApi.md#reactionsGet) | **GET** /reactions.get | 
[**reactionsList**](ReactionsApi.md#reactionsList) | **GET** /reactions.list | 
[**reactionsRemove**](ReactionsApi.md#reactionsRemove) | **POST** /reactions.remove | 



## reactionsAdd

> ReactionsAddSchema reactionsAdd(token, channel, name, timestamp)



Adds a reaction to an item.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ReactionsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `reactions:write`
let channel = "channel_example"; // String | Channel where the message to add reaction to was posted.
let name = "name_example"; // String | Reaction (emoji) name.
let timestamp = "timestamp_example"; // String | Timestamp of the message to add reaction to.
apiInstance.reactionsAdd(token, channel, name, timestamp, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;reactions:write&#x60; | 
 **channel** | **String**| Channel where the message to add reaction to was posted. | 
 **name** | **String**| Reaction (emoji) name. | 
 **timestamp** | **String**| Timestamp of the message to add reaction to. | 

### Return type

[**ReactionsAddSchema**](ReactionsAddSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## reactionsGet

> [ReactionsGetSuccessSchemaInner] reactionsGet(token, opts)



Gets reactions for an item.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ReactionsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `reactions:read`
let opts = {
  'channel': "channel_example", // String | Channel where the message to get reactions for was posted.
  'file': "file_example", // String | File to get reactions for.
  'fileComment': "fileComment_example", // String | File comment to get reactions for.
  'full': true, // Boolean | If true always return the complete reaction list.
  'timestamp': "timestamp_example" // String | Timestamp of the message to get reactions for.
};
apiInstance.reactionsGet(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;reactions:read&#x60; | 
 **channel** | **String**| Channel where the message to get reactions for was posted. | [optional] 
 **file** | **String**| File to get reactions for. | [optional] 
 **fileComment** | **String**| File comment to get reactions for. | [optional] 
 **full** | **Boolean**| If true always return the complete reaction list. | [optional] 
 **timestamp** | **String**| Timestamp of the message to get reactions for. | [optional] 

### Return type

[**[ReactionsGetSuccessSchemaInner]**](ReactionsGetSuccessSchemaInner.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reactionsList

> ReactionsListSchema reactionsList(token, opts)



Lists reactions made by a user.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ReactionsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `reactions:read`
let opts = {
  'user': "user_example", // String | Show reactions made by this user. Defaults to the authed user.
  'full': true, // Boolean | If true always return the complete reaction list.
  'count': 56, // Number | 
  'page': 56, // Number | 
  'cursor': "cursor_example", // String | Parameter for pagination. Set `cursor` equal to the `next_cursor` attribute returned by the previous request's `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more details.
  'limit': 56 // Number | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.
};
apiInstance.reactionsList(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;reactions:read&#x60; | 
 **user** | **String**| Show reactions made by this user. Defaults to the authed user. | [optional] 
 **full** | **Boolean**| If true always return the complete reaction list. | [optional] 
 **count** | **Number**|  | [optional] 
 **page** | **Number**|  | [optional] 
 **cursor** | **String**| Parameter for pagination. Set &#x60;cursor&#x60; equal to the &#x60;next_cursor&#x60; attribute returned by the previous request&#39;s &#x60;response_metadata&#x60;. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more details. | [optional] 
 **limit** | **Number**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. | [optional] 

### Return type

[**ReactionsListSchema**](ReactionsListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reactionsRemove

> ReactionsRemoveSchema reactionsRemove(token, name, opts)



Removes a reaction from an item.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ReactionsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `reactions:write`
let name = "name_example"; // String | Reaction (emoji) name.
let opts = {
  'channel': "channel_example", // String | Channel where the message to remove reaction from was posted.
  'file': "file_example", // String | File to remove reaction from.
  'fileComment': "fileComment_example", // String | File comment to remove reaction from.
  'timestamp': "timestamp_example" // String | Timestamp of the message to remove reaction from.
};
apiInstance.reactionsRemove(token, name, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;reactions:write&#x60; | 
 **name** | **String**| Reaction (emoji) name. | 
 **channel** | **String**| Channel where the message to remove reaction from was posted. | [optional] 
 **file** | **String**| File to remove reaction from. | [optional] 
 **fileComment** | **String**| File comment to remove reaction from. | [optional] 
 **timestamp** | **String**| Timestamp of the message to remove reaction from. | [optional] 

### Return type

[**ReactionsRemoveSchema**](ReactionsRemoveSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

