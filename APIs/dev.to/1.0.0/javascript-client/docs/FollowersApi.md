# ForemApiV1.FollowersApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFollowers**](FollowersApi.md#getFollowers) | **GET** /api/followers/users | Followers



## getFollowers

> [GetFollowers200ResponseInner] getFollowers(opts)

Followers

This endpoint allows the client to retrieve a list of the followers they have.         \&quot;Followers\&quot; are users that are following other users on the website.         It supports pagination, each page will contain 80 followers by default.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.FollowersApi();
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 30, // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
  'sort': "created_at" // String | Default is 'created_at'. Specifies the sort order for the created_at param of the follow                                 relationship. To sort by newest followers first (descending order) specify                                 ?sort=-created_at.
};
apiInstance.getFollowers(opts, (error, data, response) => {
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
 **perPage** | **Number**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30]
 **sort** | **String**| Default is &#39;created_at&#39;. Specifies the sort order for the created_at param of the follow                                 relationship. To sort by newest followers first (descending order) specify                                 ?sort&#x3D;-created_at. | [optional] 

### Return type

[**[GetFollowers200ResponseInner]**](GetFollowers200ResponseInner.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

