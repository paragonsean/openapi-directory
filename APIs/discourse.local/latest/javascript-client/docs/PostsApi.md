# DiscourseApiDocumentation.PostsApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTopicPostPM**](PostsApi.md#createTopicPostPM) | **POST** /posts.json | Creates a new topic, a new post, or a private message
[**deletePost**](PostsApi.md#deletePost) | **DELETE** /posts/{id}.json | delete a single post
[**getPost**](PostsApi.md#getPost) | **GET** /posts/{id}.json | Retrieve a single post
[**listPosts**](PostsApi.md#listPosts) | **GET** /posts.json | List latest posts across topics
[**lockPost**](PostsApi.md#lockPost) | **PUT** /posts/{id}/locked.json | Lock a post from being edited
[**performPostAction**](PostsApi.md#performPostAction) | **POST** /post_actions.json | Like a post and other actions
[**postReplies**](PostsApi.md#postReplies) | **GET** /posts/{id}/replies.json | List replies to a post
[**updatePost**](PostsApi.md#updatePost) | **PUT** /posts/{id}.json | Update a single post



## createTopicPostPM

> CreateTopicPostPM200Response createTopicPostPM(opts)

Creates a new topic, a new post, or a private message

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PostsApi();
let opts = {
  'createTopicPostPMRequest': new DiscourseApiDocumentation.CreateTopicPostPMRequest() // CreateTopicPostPMRequest | 
};
apiInstance.createTopicPostPM(opts, (error, data, response) => {
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


## deletePost

> deletePost(id, opts)

delete a single post

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PostsApi();
let id = 56; // Number | 
let opts = {
  'deletePostRequest': new DiscourseApiDocumentation.DeletePostRequest() // DeletePostRequest | 
};
apiInstance.deletePost(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**|  | 
 **deletePostRequest** | [**DeletePostRequest**](DeletePostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getPost

> GetPost200Response getPost(id)

Retrieve a single post

This endpoint can be used to get the number of likes on a post using the &#x60;actions_summary&#x60; property in the response. &#x60;actions_summary&#x60; responses with the id of &#x60;2&#x60; signify a &#x60;like&#x60;. If there are no &#x60;actions_summary&#x60; items with the id of &#x60;2&#x60;, that means there are 0 likes. Other ids likely refer to various different flag types. 

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PostsApi();
let id = "id_example"; // String | 
apiInstance.getPost(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**GetPost200Response**](GetPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPosts

> ListPosts200Response listPosts(apiKey, apiUsername, opts)

List latest posts across topics

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PostsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let opts = {
  'before': "before_example" // String | Load posts with an id lower than this value. Useful for pagination.
};
apiInstance.listPosts(apiKey, apiUsername, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **before** | **String**| Load posts with an id lower than this value. Useful for pagination. | [optional] 

### Return type

[**ListPosts200Response**](ListPosts200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lockPost

> LockPost200Response lockPost(apiKey, apiUsername, id, opts)

Lock a post from being edited

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PostsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'lockPostRequest': new DiscourseApiDocumentation.LockPostRequest() // LockPostRequest | 
};
apiInstance.lockPost(apiKey, apiUsername, id, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 
 **lockPostRequest** | [**LockPostRequest**](LockPostRequest.md)|  | [optional] 

### Return type

[**LockPost200Response**](LockPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## performPostAction

> PerformPostAction200Response performPostAction(apiKey, apiUsername, opts)

Like a post and other actions

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PostsApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let opts = {
  'performPostActionRequest': new DiscourseApiDocumentation.PerformPostActionRequest() // PerformPostActionRequest | 
};
apiInstance.performPostAction(apiKey, apiUsername, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **performPostActionRequest** | [**PerformPostActionRequest**](PerformPostActionRequest.md)|  | [optional] 

### Return type

[**PerformPostAction200Response**](PerformPostAction200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postReplies

> [PostReplies200ResponseInner] postReplies(id)

List replies to a post

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PostsApi();
let id = "id_example"; // String | 
apiInstance.postReplies(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**[PostReplies200ResponseInner]**](PostReplies200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePost

> UpdatePost200Response updatePost(id, opts)

Update a single post

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.PostsApi();
let id = "id_example"; // String | 
let opts = {
  'updatePostRequest': new DiscourseApiDocumentation.UpdatePostRequest() // UpdatePostRequest | 
};
apiInstance.updatePost(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **updatePostRequest** | [**UpdatePostRequest**](UpdatePostRequest.md)|  | [optional] 

### Return type

[**UpdatePost200Response**](UpdatePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

