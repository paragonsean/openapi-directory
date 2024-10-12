# OpenTrialsApi.SearchApi

All URIs are relative to *http://opentrials.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](SearchApi.md#autocomplete) | **GET** /search/autocomplete/{in} | 
[**searchFDADocuments**](SearchApi.md#searchFDADocuments) | **GET** /search/fda_documents | 



## autocomplete

> AutocompleteResults autocomplete(_in, opts)



Autocomplete search feature for supported database entities (&#x60;location&#x60;). It has the same options as a regular &#x60;search&#x60; operation, with an extra **required** &#x60;in&#x60; parameter indicating the entity type to search.

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.SearchApi();
let _in = "_in_example"; // String | The entity to search for
let opts = {
  'q': "q_example", // String | The search query
  'page': 1, // Number | The page number
  'perPage': 20 // Number | Number of items per page
};
apiInstance.autocomplete(_in, opts, (error, data, response) => {
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
 **_in** | **String**| The entity to search for | 
 **q** | **String**| The search query | [optional] 
 **page** | **Number**| The page number | [optional] [default to 1]
 **perPage** | **Number**| Number of items per page | [optional] [default to 20]

### Return type

[**AutocompleteResults**](AutocompleteResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchFDADocuments

> FDADocumentSearchResults searchFDADocuments(opts)



Search the FDA documents

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.SearchApi();
let opts = {
  'q': "q_example", // String | The search query (follows the [ElasticSearch Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) syntax)
  'text': "text_example", // String | Search query on the documents file's text (follows the [ElasticSearch Simple Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-simple-query-string-query.html#_simple_query_string_syntax) syntax)
  'page': 1, // Number | The page number
  'perPage': 20 // Number | Number of items per page
};
apiInstance.searchFDADocuments(opts, (error, data, response) => {
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
 **q** | **String**| The search query (follows the [ElasticSearch Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) syntax) | [optional] 
 **text** | **String**| Search query on the documents file&#39;s text (follows the [ElasticSearch Simple Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-simple-query-string-query.html#_simple_query_string_syntax) syntax) | [optional] 
 **page** | **Number**| The page number | [optional] [default to 1]
 **perPage** | **Number**| Number of items per page | [optional] [default to 20]

### Return type

[**FDADocumentSearchResults**](FDADocumentSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

