# SlackWebApi.StarsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**starsAdd**](StarsApi.md#starsAdd) | **POST** /stars.add | 
[**starsList**](StarsApi.md#starsList) | **GET** /stars.list | 
[**starsRemove**](StarsApi.md#starsRemove) | **POST** /stars.remove | 



## starsAdd

> StarsAddSchema starsAdd(token, opts)



Adds a star to an item.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.StarsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `stars:write`
let opts = {
  'channel': "channel_example", // String | Channel to add star to, or channel where the message to add star to was posted (used with `timestamp`).
  'file': "file_example", // String | File to add star to.
  'fileComment': "fileComment_example", // String | File comment to add star to.
  'timestamp': "timestamp_example" // String | Timestamp of the message to add star to.
};
apiInstance.starsAdd(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;stars:write&#x60; | 
 **channel** | **String**| Channel to add star to, or channel where the message to add star to was posted (used with &#x60;timestamp&#x60;). | [optional] 
 **file** | **String**| File to add star to. | [optional] 
 **fileComment** | **String**| File comment to add star to. | [optional] 
 **timestamp** | **String**| Timestamp of the message to add star to. | [optional] 

### Return type

[**StarsAddSchema**](StarsAddSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## starsList

> StarsListSchema starsList(opts)



Lists stars for a user.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.StarsApi();
let opts = {
  'token': "token_example", // String | Authentication token. Requires scope: `stars:read`
  'count': "count_example", // String | 
  'page': "page_example", // String | 
  'cursor': "cursor_example", // String | Parameter for pagination. Set `cursor` equal to the `next_cursor` attribute returned by the previous request's `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more details.
  'limit': 56 // Number | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.
};
apiInstance.starsList(opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;stars:read&#x60; | [optional] 
 **count** | **String**|  | [optional] 
 **page** | **String**|  | [optional] 
 **cursor** | **String**| Parameter for pagination. Set &#x60;cursor&#x60; equal to the &#x60;next_cursor&#x60; attribute returned by the previous request&#39;s &#x60;response_metadata&#x60;. This parameter is optional, but pagination is mandatory: the default value simply fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more details. | [optional] 
 **limit** | **Number**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. | [optional] 

### Return type

[**StarsListSchema**](StarsListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## starsRemove

> StarsRemoveSchema starsRemove(token, opts)



Removes a star from an item.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.StarsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `stars:write`
let opts = {
  'channel': "channel_example", // String | Channel to remove star from, or channel where the message to remove star from was posted (used with `timestamp`).
  'file': "file_example", // String | File to remove star from.
  'fileComment': "fileComment_example", // String | File comment to remove star from.
  'timestamp': "timestamp_example" // String | Timestamp of the message to remove star from.
};
apiInstance.starsRemove(token, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;stars:write&#x60; | 
 **channel** | **String**| Channel to remove star from, or channel where the message to remove star from was posted (used with &#x60;timestamp&#x60;). | [optional] 
 **file** | **String**| File to remove star from. | [optional] 
 **fileComment** | **String**| File comment to remove star from. | [optional] 
 **timestamp** | **String**| Timestamp of the message to remove star from. | [optional] 

### Return type

[**StarsRemoveSchema**](StarsRemoveSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

