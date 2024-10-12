# ForemApiV1.TagsApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFollowedTags_0**](TagsApi.md#getFollowedTags_0) | **GET** /api/follows/tags | Followed Tags
[**getTags**](TagsApi.md#getTags) | **GET** /api/tags | Tags



## getFollowedTags_0

> [FollowedTag] getFollowedTags_0()

Followed Tags

This endpoint allows the client to retrieve a list of the tags they follow.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.TagsApi();
apiInstance.getFollowedTags_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[FollowedTag]**](FollowedTag.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTags

> [Tag] getTags(opts)

Tags

This endpoint allows the client to retrieve a list of tags that can be used to tag articles.  It will return tags ordered by popularity.  It supports pagination, each page will contain 10 tags by default.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.TagsApi();
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 10 // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
};
apiInstance.getTags(opts, (error, data, response) => {
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
 **page** | **Number**| Pagination page | [optional] [default to 1]
 **perPage** | **Number**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 10]

### Return type

[**[Tag]**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

