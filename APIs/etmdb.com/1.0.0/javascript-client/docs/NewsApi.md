# EtMdbRestApiV1.NewsApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**newsSearchRead**](NewsApi.md#newsSearchRead) | **GET** /api/v1/news/search/{title} | Return news or article search result



## newsSearchRead

> newsSearchRead(title)

Return news or article search result

Return news or article search result  ### Response Class (Status 200)  * __{title}__: Used as a key word to search news and articles,  For more details on how news &amp; articles are listed [see here][ref]. [ref]: https://etmdb.com/en/news-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.NewsApi();
let title = "title_example"; // String | 
apiInstance.newsSearchRead(title, (error, data, response) => {
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
 **title** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

