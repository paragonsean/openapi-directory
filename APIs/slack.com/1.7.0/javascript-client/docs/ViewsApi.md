# SlackWebApi.ViewsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**viewsOpen**](ViewsApi.md#viewsOpen) | **GET** /views.open | 
[**viewsPublish**](ViewsApi.md#viewsPublish) | **GET** /views.publish | 
[**viewsPush**](ViewsApi.md#viewsPush) | **GET** /views.push | 
[**viewsUpdate**](ViewsApi.md#viewsUpdate) | **GET** /views.update | 



## viewsOpen

> DefaultSuccessTemplate viewsOpen(token, triggerId, view)



Open a view for a user.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ViewsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let triggerId = "triggerId_example"; // String | Exchange a trigger to post to the user.
let view = "view_example"; // String | A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.
apiInstance.viewsOpen(token, triggerId, view, (error, data, response) => {
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
 **triggerId** | **String**| Exchange a trigger to post to the user. | 
 **view** | **String**| A [view payload](/reference/surfaces/views). This must be a JSON-encoded string. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## viewsPublish

> DefaultSuccessTemplate viewsPublish(token, userId, view, opts)



Publish a static view for a User.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ViewsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let userId = "userId_example"; // String | `id` of the user you want publish a view to.
let view = "view_example"; // String | A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.
let opts = {
  'hash': "hash_example" // String | A string that represents view state to protect against possible race conditions.
};
apiInstance.viewsPublish(token, userId, view, opts, (error, data, response) => {
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
 **userId** | **String**| &#x60;id&#x60; of the user you want publish a view to. | 
 **view** | **String**| A [view payload](/reference/surfaces/views). This must be a JSON-encoded string. | 
 **hash** | **String**| A string that represents view state to protect against possible race conditions. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## viewsPush

> DefaultSuccessTemplate viewsPush(token, triggerId, view)



Push a view onto the stack of a root view.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ViewsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let triggerId = "triggerId_example"; // String | Exchange a trigger to post to the user.
let view = "view_example"; // String | A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.
apiInstance.viewsPush(token, triggerId, view, (error, data, response) => {
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
 **triggerId** | **String**| Exchange a trigger to post to the user. | 
 **view** | **String**| A [view payload](/reference/surfaces/views). This must be a JSON-encoded string. | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## viewsUpdate

> DefaultSuccessTemplate viewsUpdate(token, opts)



Update an existing view.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ViewsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `none`
let opts = {
  'viewId': "viewId_example", // String | A unique identifier of the view to be updated. Either `view_id` or `external_id` is required.
  'externalId': "externalId_example", // String | A unique identifier of the view set by the developer. Must be unique for all views on a team. Max length of 255 characters. Either `view_id` or `external_id` is required.
  'view': "view_example", // String | A [view object](/reference/surfaces/views). This must be a JSON-encoded string.
  'hash': "hash_example" // String | A string that represents view state to protect against possible race conditions.
};
apiInstance.viewsUpdate(token, opts, (error, data, response) => {
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
 **viewId** | **String**| A unique identifier of the view to be updated. Either &#x60;view_id&#x60; or &#x60;external_id&#x60; is required. | [optional] 
 **externalId** | **String**| A unique identifier of the view set by the developer. Must be unique for all views on a team. Max length of 255 characters. Either &#x60;view_id&#x60; or &#x60;external_id&#x60; is required. | [optional] 
 **view** | **String**| A [view object](/reference/surfaces/views). This must be a JSON-encoded string. | [optional] 
 **hash** | **String**| A string that represents view state to protect against possible race conditions. | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

