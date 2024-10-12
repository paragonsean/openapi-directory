# CoreApiV2.JournalsApi

All URIs are relative to *http://core.ac.uk/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJournalByIssn**](JournalsApi.md#getJournalByIssn) | **GET** /journals/get/{issn} | Find journal by ISSN
[**getJournalByIssnBatch**](JournalsApi.md#getJournalByIssnBatch) | **POST** /journals/get | Batch operation for retrieving journals by ISSN
[**journalsSearchPost**](JournalsApi.md#journalsSearchPost) | **POST** /journals/search | Batch operation for search through journals
[**journalsSearchQueryGet**](JournalsApi.md#journalsSearchQueryGet) | **GET** /journals/search/{query} | Search through journals



## getJournalByIssn

> JournalResponse getJournalByIssn(issn)

Find journal by ISSN

Returns a journal with given ISSN identifier.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.JournalsApi();
let issn = "issn_example"; // String | ISSN identifier of journal that needs to be fetched.
apiInstance.getJournalByIssn(issn, (error, data, response) => {
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
 **issn** | **String**| ISSN identifier of journal that needs to be fetched. | 

### Return type

[**JournalResponse**](JournalResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJournalByIssnBatch

> [JournalResponse] getJournalByIssnBatch(body)

Batch operation for retrieving journals by ISSN

Method accepts a JSON array of ISSNs and retrieves a list of journals.

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.JournalsApi();
let body = ["null"]; // [String] | JSON array with ISSNs of journals that need to be fetched
apiInstance.getJournalByIssnBatch(body, (error, data, response) => {
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
 **body** | [**[String]**](String.md)| JSON array with ISSNs of journals that need to be fetched | 

### Return type

[**[JournalResponse]**](JournalResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## journalsSearchPost

> [JournalResponse] journalsSearchPost(body)

Batch operation for search through journals

Method accepts a JSON array of search queries and parameters. It then searches through all journals and returns a JSON array of search results for each of the queries. Method searches through all journal fields (title, identifiers, subjects, language, rights and publisher).

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.JournalsApi();
let body = [new CoreApiV2.SearchRequest()]; // [SearchRequest] | JSON array with search queries and parameters. One request can contain up to 100 queries.
apiInstance.journalsSearchPost(body, (error, data, response) => {
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
 **body** | [**[SearchRequest]**](SearchRequest.md)| JSON array with search queries and parameters. One request can contain up to 100 queries. | 

### Return type

[**[JournalResponse]**](JournalResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## journalsSearchQueryGet

> JournalSearchResponse journalsSearchQueryGet(query, opts)

Search through journals

Searches through all journals and returns a JSON array of search results. Method searches through all journal fields (title, identifiers, subjects, language, rights and publisher).

### Example

```javascript
import CoreApiV2 from 'core_api_v2';
let defaultClient = CoreApiV2.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new CoreApiV2.JournalsApi();
let query = "query_example"; // String | Search query
let opts = {
  'page': 1, // Number | Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
  'pageSize': 10 // Number | The number of results to return per page. Can be any number between 10 and 100, default is 10.
};
apiInstance.journalsSearchQueryGet(query, opts, (error, data, response) => {
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
 **query** | **String**| Search query | 
 **page** | **Number**| Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page). | [optional] [default to 1]
 **pageSize** | **Number**| The number of results to return per page. Can be any number between 10 and 100, default is 10. | [optional] [default to 10]

### Return type

[**JournalSearchResponse**](JournalSearchResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

