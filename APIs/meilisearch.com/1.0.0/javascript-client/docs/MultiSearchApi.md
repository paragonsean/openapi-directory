# MeilisearchV11.MultiSearchApi

All URIs are relative to *http://localhost:7700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchOneOrMoreIndexes**](MultiSearchApi.md#searchOneOrMoreIndexes) | **POST** /multi-search | Search one or more indexes



## searchOneOrMoreIndexes

> searchOneOrMoreIndexes(opts)

Search one or more indexes

Search one or more indexes

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.MultiSearchApi();
let opts = {
  'searchOneOrMoreIndexesRequest': {"queries":[{"indexUid":"books","q":"Pride and Prejudice"},{"attributesToHighlight":["title"],"indexUid":"books","q":"Alice In Wonderland"}]} // SearchOneOrMoreIndexesRequest | 
};
apiInstance.searchOneOrMoreIndexes(opts, (error, data, response) => {
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
 **searchOneOrMoreIndexesRequest** | [**SearchOneOrMoreIndexesRequest**](SearchOneOrMoreIndexesRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

