# ForemApiV1.VideosApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**videos**](VideosApi.md#videos) | **GET** /api/videos | Articles with a video



## videos

> [VideoArticle] videos(opts)

Articles with a video

This endpoint allows the client to retrieve a list of articles that are uploaded with a video.  It will only return published video articles ordered by descending popularity.  It supports pagination, each page will contain 24 articles by default.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.VideosApi();
let opts = {
  'page': 1, // Number | Pagination page
  'perPage': 24 // Number | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
};
apiInstance.videos(opts, (error, data, response) => {
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
 **perPage** | **Number**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 24]

### Return type

[**[VideoArticle]**](VideoArticle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

