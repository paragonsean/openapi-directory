# MeilisearchV11.SearchApi

All URIs are relative to *http://localhost:7700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchInIndex**](SearchApi.md#searchInIndex) | **GET** /indexes/books/search | Search in index
[**searchInIndex1**](SearchApi.md#searchInIndex1) | **POST** /indexes/books/search | Search in index



## searchInIndex

> searchInIndex(opts)

Search in index

Search in index

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SearchApi();
let opts = {
  'q': "prinec", // String | 
  'offset': "0", // String | 
  'limit': "1", // String | 
  'attributesToRetrieve': "title,author", // String | 
  'attributesToCrop': "title", // String | 
  'attributesToHighlight': "*", // String | 
  'cropLength': "5", // String | 
  'cropMarker': "[...]", // String | 
  'filter': "genre=\"fantasy\"", // String | 
  'showMatchesPosition': "true", // String | 
  'facets': "genre", // String | 
  'sort': "price", // String | 
  'highlightPreTag': "<mark>", // String | 
  'highlightPostTag': "</mark>", // String | 
  'matchingStrategy': "all", // String | 
  'page': "2", // String | 
  'hitsPerPage': "50" // String | 
};
apiInstance.searchInIndex(opts, (error, data, response) => {
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
 **q** | **String**|  | [optional] 
 **offset** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 
 **attributesToRetrieve** | **String**|  | [optional] 
 **attributesToCrop** | **String**|  | [optional] 
 **attributesToHighlight** | **String**|  | [optional] 
 **cropLength** | **String**|  | [optional] 
 **cropMarker** | **String**|  | [optional] 
 **filter** | **String**|  | [optional] 
 **showMatchesPosition** | **String**|  | [optional] 
 **facets** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **highlightPreTag** | **String**|  | [optional] 
 **highlightPostTag** | **String**|  | [optional] 
 **matchingStrategy** | **String**|  | [optional] 
 **page** | **String**|  | [optional] 
 **hitsPerPage** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## searchInIndex1

> searchInIndex1(opts)

Search in index

Search in index

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.SearchApi();
let opts = {
  'searchInIndex1Request': {"attributesToHighlight":["title"],"q":""} // SearchInIndex1Request | 
};
apiInstance.searchInIndex1(opts, (error, data, response) => {
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
 **searchInIndex1Request** | [**SearchInIndex1Request**](SearchInIndex1Request.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

