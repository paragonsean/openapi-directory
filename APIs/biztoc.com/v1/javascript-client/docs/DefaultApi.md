# BizToc.DefaultApi

All URIs are relative to *https://ai.biztoc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNews**](DefaultApi.md#getNews) | **GET** /ai/news | Retrieves the latest news whose content contains the query string.



## getNews

> getNews(opts)

Retrieves the latest news whose content contains the query string.

### Example

```javascript
import BizToc from 'biz_toc';

let apiInstance = new BizToc.DefaultApi();
let opts = {
  'query': "query_example" // String | Used to query news articles on their title and body. For example, ?query=apple will return news stories that have 'apple' in their title or body.
};
apiInstance.getNews(opts, (error, data, response) => {
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
 **query** | **String**| Used to query news articles on their title and body. For example, ?query&#x3D;apple will return news stories that have &#39;apple&#39; in their title or body. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

