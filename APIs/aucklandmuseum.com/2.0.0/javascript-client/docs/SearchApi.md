# AucklandMuseumApi.SearchApi

All URIs are relative to *http://api.aucklandmuseum.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSearch**](SearchApi.md#getSearch) | **GET** /search/{index}/{operation} | Perform simple search queries over Auckland Museum Collections and Cenotaph data
[**postSearch**](SearchApi.md#postSearch) | **POST** /search/{index}/{operation} | Perform complex search queries over Auckland Museum Collections and Cenotaph data



## getSearch

> getSearch(index, operation, opts)

Perform simple search queries over Auckland Museum Collections and Cenotaph data

Use this endpoint to perform simple search queries for finding information and subjects you may be interested in  Searches performed via this endpoint run against an [Elastic](www.elastic.co) server. This endpoint mirrors the Elastic search API documented [here](https://www.elastic.co/guide/en/elasticsearch/reference/1.5/search-search.html)  Use the   - &#x60;collectionsonline&#x60; index to perform searches over other all Collections data   - &#x60;cenotaph&#x60; index to perform searches over Cenotaph data 

### Example

```javascript
import AucklandMuseumApi from 'auckland_museum_api';

let apiInstance = new AucklandMuseumApi.SearchApi();
let index = "index_example"; // String | search index name Possible values: * `collectionsonline` * `cenotaph` 
let operation = "operation_example"; // String | One of the supported elasticsearch operations like `_search` or `_suggest`
let opts = {
  'q': "q_example" // String | One of the supported elasticsearch query parameter values for key `q`
};
apiInstance.getSearch(index, operation, opts, (error, data, response) => {
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
 **index** | **String**| search index name Possible values: * &#x60;collectionsonline&#x60; * &#x60;cenotaph&#x60;  | 
 **operation** | **String**| One of the supported elasticsearch operations like &#x60;_search&#x60; or &#x60;_suggest&#x60; | 
 **q** | **String**| One of the supported elasticsearch query parameter values for key &#x60;q&#x60; | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postSearch

> postSearch(index, operation, opts)

Perform complex search queries over Auckland Museum Collections and Cenotaph data

Searches performed via this endpoint run against an [Elastic](www.elastic.co) server. This endpoint mirrors the Elastic search API documented [here](https://www.elastic.co/guide/en/elasticsearch/reference/1.5/search-search.html)  Use the   - &#x60;collectionsonline&#x60; index to perform searches over other all Collections data   - &#x60;cenotaph&#x60; index to perform searches over Cenotaph data 

### Example

```javascript
import AucklandMuseumApi from 'auckland_museum_api';

let apiInstance = new AucklandMuseumApi.SearchApi();
let index = "index_example"; // String | search index name Possible values: * `collectionsonline` * `cenotaph` 
let operation = "operation_example"; // String | One of the supported elasticsearch operations like `_search` or `_suggest`
let opts = {
  'body': {key: null} // Object | body
};
apiInstance.postSearch(index, operation, opts, (error, data, response) => {
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
 **index** | **String**| search index name Possible values: * &#x60;collectionsonline&#x60; * &#x60;cenotaph&#x60;  | 
 **operation** | **String**| One of the supported elasticsearch operations like &#x60;_search&#x60; or &#x60;_suggest&#x60; | 
 **body** | **Object**| body | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

