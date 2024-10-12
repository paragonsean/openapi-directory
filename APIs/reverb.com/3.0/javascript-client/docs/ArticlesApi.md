# Reverb.ArticlesApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**articlesCategoriesGet**](ArticlesApi.md#articlesCategoriesGet) | **GET** /articles/categories | List of all article categories
[**articlesGet**](ArticlesApi.md#articlesGet) | **GET** /articles | 



## articlesCategoriesGet

> articlesCategoriesGet()

List of all article categories

List of all article categories

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ArticlesApi();
apiInstance.articlesCategoriesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## articlesGet

> articlesGet(opts)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ArticlesApi();
let opts = {
  'page': 1, // Number | 
  'perPage': 24, // Number | 
  'offset': 56, // Number | 
  'query': "query_example", // String | What's being searched for
  'excludeFeatured': 56 // Number | Number of featured articles to exclude
};
apiInstance.articlesGet(opts, (error, data, response) => {
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
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 24]
 **offset** | **Number**|  | [optional] 
 **query** | **String**| What&#39;s being searched for | [optional] 
 **excludeFeatured** | **Number**| Number of featured articles to exclude | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

