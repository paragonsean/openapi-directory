# CoreApiV2.RepositoriesApi

All URIs are relative to *http://core.ac.uk/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRepositoryById**](RepositoriesApi.md#getRepositoryById) | **GET** /repositories/get/{repositoryId} | Get repository by CORE repository ID
[**getRepositoryByIdBatch**](RepositoriesApi.md#getRepositoryByIdBatch) | **POST** /repositories/get | Batch operation for retrieving repositories by CORE repository ID
[**repositoriesSearchPost**](RepositoriesApi.md#repositoriesSearchPost) | **POST** /repositories/search | Batch operation for searching through repositories
[**repositoriesSearchQueryGet**](RepositoriesApi.md#repositoriesSearchQueryGet) | **GET** /repositories/search/{query} | Search through all repositories



## getRepositoryById

> RepositoryResponse getRepositoryById(repositoryId, opts)

Get repository by CORE repository ID

Method will retrieve a repository based on given CORE repository ID.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.RepositoriesApi();
let repositoryId = 56; // Number | CORE repository ID of the article that needs to be fetched.
let opts = {
  'stats': false, // Boolean | Whether to retrieve statistics about the repository. The default value is false
  'depositHistory': false, // Boolean | Returns deposit history over time
  'depositHistoryCumulative': false // Boolean | Returns deposit history over time
};
apiInstance.getRepositoryById(repositoryId, opts, (error, data, response) => {
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
 **repositoryId** | **Number**| CORE repository ID of the article that needs to be fetched. | 
 **stats** | **Boolean**| Whether to retrieve statistics about the repository. The default value is false | [optional] [default to false]
 **depositHistory** | **Boolean**| Returns deposit history over time | [optional] [default to false]
 **depositHistoryCumulative** | **Boolean**| Returns deposit history over time | [optional] [default to false]

### Return type

[**RepositoryResponse**](RepositoryResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryByIdBatch

> [RepositoryResponse] getRepositoryByIdBatch(body, opts)

Batch operation for retrieving repositories by CORE repository ID

Method accepts a JSON array of CORE repository IDs and retrieves a list of repositories. The response array is ordered based on the order of the IDs in the request array. The maximum number of IDs in request is 100.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.RepositoriesApi();
let body = [null]; // [Number] | JSON array with CORE repository IDs of repositories that need to be fetched
let opts = {
  'stats': false, // Boolean | Whether to retrieve statistics about the repository. The default value is false
  'depositHistory': false, // Boolean | Returns deposit history over time
  'depositHistoryCumulative': false // Boolean | Returns deposit history over time
};
apiInstance.getRepositoryByIdBatch(body, opts, (error, data, response) => {
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
 **body** | [**[Number]**](Number.md)| JSON array with CORE repository IDs of repositories that need to be fetched | 
 **stats** | **Boolean**| Whether to retrieve statistics about the repository. The default value is false | [optional] [default to false]
 **depositHistory** | **Boolean**| Returns deposit history over time | [optional] [default to false]
 **depositHistoryCumulative** | **Boolean**| Returns deposit history over time | [optional] [default to false]

### Return type

[**[RepositoryResponse]**](RepositoryResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesSearchPost

> RepositorySearchResponse repositoriesSearchPost(body, opts)

Batch operation for searching through repositories

Method accepts a JSON array of search queries and parameters. It then searches through all repositories and returns a JSON array of search results for each of the queries. Method searches through all repository fields.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.RepositoriesApi();
let body = [new CoreApiV2.SearchRequest()]; // [SearchRequest] | JSON array with search queries and parameters. One request can contain up to 100 queries
let opts = {
  'stats': false, // Boolean | Whether to retrieve statistics about the repository. The default value is false
  'depositHistory': false, // Boolean | Returns deposit history over time
  'depositHistoryCumulative': false // Boolean | Returns deposit history over time
};
apiInstance.repositoriesSearchPost(body, opts, (error, data, response) => {
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
 **body** | [**[SearchRequest]**](SearchRequest.md)| JSON array with search queries and parameters. One request can contain up to 100 queries | 
 **stats** | **Boolean**| Whether to retrieve statistics about the repository. The default value is false | [optional] [default to false]
 **depositHistory** | **Boolean**| Returns deposit history over time | [optional] [default to false]
 **depositHistoryCumulative** | **Boolean**| Returns deposit history over time | [optional] [default to false]

### Return type

[**RepositorySearchResponse**](RepositorySearchResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoriesSearchQueryGet

> RepositorySearchResponse repositoriesSearchQueryGet(query, opts)

Search through all repositories

Searches through all repositories and returns a JSON array with search results. Method searches through all repository fields.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.RepositoriesApi();
let query = "query_example"; // String | The search query
let opts = {
  'page': 1, // Number | Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
  'pageSize': 10, // Number | The number of results to return per page. Can be any number between 10 and 100, default is 10.
  'stats': false, // Boolean | Whether to retrieve statistics about the repository. The default value is false
  'depositHistory': false, // Boolean | Returns deposit history over time
  'depositHistoryCumulative': false // Boolean | Returns deposit history over time
};
apiInstance.repositoriesSearchQueryGet(query, opts, (error, data, response) => {
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
 **stats** | **Boolean**| Whether to retrieve statistics about the repository. The default value is false | [optional] [default to false]
 **depositHistory** | **Boolean**| Returns deposit history over time | [optional] [default to false]
 **depositHistoryCumulative** | **Boolean**| Returns deposit history over time | [optional] [default to false]

### Return type

[**RepositorySearchResponse**](RepositorySearchResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

