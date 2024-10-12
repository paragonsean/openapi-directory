# DevCommunity.DefaultApi

All URIs are relative to *https://dev.to*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getArticles**](DefaultApi.md#getArticles) | **GET** /api/articles/search | Get a list of filtered articles



## getArticles

> GetArticlesResponse getArticles(opts)

Get a list of filtered articles

### Example

```javascript
import DevCommunity from 'dev_community';

let apiInstance = new DevCommunity.DefaultApi();
let opts = {
  'q': "q_example", // String | Accepts keywords to use as a search query.
  'page': 0, // Number | Pagination Page
  'perPage': 60, // Number | Page size (the number of items to return per page).
  'top': "top_example" // String | Returns the most popular articles in the last N days. 'top' indicates the number of days since publication of the articles returned. This param can be used in conjuction with q or tag.
};
apiInstance.getArticles(opts, (error, data, response) => {
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
 **q** | **String**| Accepts keywords to use as a search query. | [optional] 
 **page** | **Number**| Pagination Page | [optional] [default to 0]
 **perPage** | **Number**| Page size (the number of items to return per page). | [optional] [default to 60]
 **top** | **String**| Returns the most popular articles in the last N days. &#39;top&#39; indicates the number of days since publication of the articles returned. This param can be used in conjuction with q or tag. | [optional] 

### Return type

[**GetArticlesResponse**](GetArticlesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.forem.api-v1+json

