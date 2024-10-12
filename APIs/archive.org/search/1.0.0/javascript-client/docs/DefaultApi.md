# SearchServices.DefaultApi

All URIs are relative to *https://api.archive.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchV1FieldsGet**](DefaultApi.md#searchV1FieldsGet) | **GET** /search/v1/fields | 
[**searchV1OrganicGet**](DefaultApi.md#searchV1OrganicGet) | **GET** /search/v1/organic | 
[**searchV1ScrapeGet**](DefaultApi.md#searchV1ScrapeGet) | **GET** /search/v1/scrape | 



## searchV1FieldsGet

> [String] searchV1FieldsGet(opts)



Fields that can be requested

### Example

```javascript
import SearchServices from 'search_services';

let apiInstance = new SearchServices.DefaultApi();
let opts = {
  'callback': "callback_example" // String | Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.
};
apiInstance.searchV1FieldsGet(opts, (error, data, response) => {
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
 **callback** | **String**| Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json


## searchV1OrganicGet

> OrganicResult searchV1OrganicGet(opts)



Return relevance-based results from search queries 

### Example

```javascript
import SearchServices from 'search_services';

let apiInstance = new SearchServices.DefaultApi();
let opts = {
  'q': "q_example", // String | Lucene-type search query
  'field': "'identifier'", // String | Metadata field
  'size': 1000, // Number | Number of query results to return
  'totalOnly': false, // Boolean | Request total only; do not return hits
  'callback': "callback_example" // String | Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.
};
apiInstance.searchV1OrganicGet(opts, (error, data, response) => {
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
 **q** | **String**| Lucene-type search query | [optional] 
 **field** | **String**| Metadata field | [optional] [default to &#39;identifier&#39;]
 **size** | **Number**| Number of query results to return | [optional] [default to 1000]
 **totalOnly** | **Boolean**| Request total only; do not return hits | [optional] [default to false]
 **callback** | **String**| Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. | [optional] 

### Return type

[**OrganicResult**](OrganicResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json


## searchV1ScrapeGet

> ScrapeResult searchV1ScrapeGet(opts)



Scrape search results from Internet Archive, allowing a scrolling cursor 

### Example

```javascript
import SearchServices from 'search_services';

let apiInstance = new SearchServices.DefaultApi();
let opts = {
  'q': "q_example", // String | Lucene-type search query
  'field': "'identifier'", // String | Metadata field
  'sort': "sort_example", // String | sort collations
  'size': 1000, // Number | Number of query results to return
  'cursor': "cursor_example", // String | Cursor for scrolling (used for subsequent calls)
  'totalOnly': false, // Boolean | Request total only; do not return hits
  'callback': "callback_example" // String | Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as `callback(data)`, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.
};
apiInstance.searchV1ScrapeGet(opts, (error, data, response) => {
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
 **q** | **String**| Lucene-type search query | [optional] 
 **field** | **String**| Metadata field | [optional] [default to &#39;identifier&#39;]
 **sort** | **String**| sort collations | [optional] 
 **size** | **Number**| Number of query results to return | [optional] [default to 1000]
 **cursor** | **String**| Cursor for scrolling (used for subsequent calls) | [optional] 
 **totalOnly** | **Boolean**| Request total only; do not return hits | [optional] [default to false]
 **callback** | **String**| Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. | [optional] 

### Return type

[**ScrapeResult**](ScrapeResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json

