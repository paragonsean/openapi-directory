# CoreApiV2.AllApi

All URIs are relative to *http://core.ac.uk/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchPost**](AllApi.md#searchPost) | **POST** /search | Batch operation for search through all resources
[**searchQueryGet**](AllApi.md#searchQueryGet) | **GET** /search/{query} | Search through all resources



## searchPost

> [SearchAllResponse] searchPost(body)

Batch operation for search through all resources

Method accepts a JSON array of search queries. It searches through all resources and returns a JSON array with search results for each of the queries. Method searches through all resources and all fields. The results are ordered by relevance score and contain type of the relevant resource and its ID. Furthermore, the responses are oredered based on the order of the request items. The metadata of each resource need to be obtained through an appropriate method.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.AllApi();
let body = [new CoreApiV2.SearchRequest()]; // [SearchRequest] | JSON array with search queries and pagination parameters. One request can contain up to 100 queries
apiInstance.searchPost(body, (error, data, response) => {
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
 **body** | [**[SearchRequest]**](SearchRequest.md)| JSON array with search queries and pagination parameters. One request can contain up to 100 queries | 

### Return type

[**[SearchAllResponse]**](SearchAllResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchQueryGet

> SearchAllResponse searchQueryGet(query, opts)

Search through all resources

Searches through all resources and returns a JSON array with search results. Method searches through all resources and all fields. The results are ordered by relevance score and contain type of the relevant resource and its ID. The metadata of each resource need to be obtained through an appropriate method.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.AllApi();
let query = "query_example"; // String | The search query
let opts = {
  'page': 1, // Number | Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
  'pageSize': 10 // Number | The number of results to return per page. Can be any number between 10 and 100, default is 10.
};
apiInstance.searchQueryGet(query, opts, (error, data, response) => {
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
 **query** | **String**| The search query | 
 **page** | **Number**| Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page). | [optional] [default to 1]
 **pageSize** | **Number**| The number of results to return per page. Can be any number between 10 and 100, default is 10. | [optional] [default to 10]

### Return type

[**SearchAllResponse**](SearchAllResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

