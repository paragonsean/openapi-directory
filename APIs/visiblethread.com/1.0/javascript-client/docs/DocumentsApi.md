# VisibleThreadApi.DocumentsApi

All URIs are relative to *https://api.visiblethread.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dictionariesGet**](DocumentsApi.md#dictionariesGet) | **GET** /dictionaries | Get your list of dictionaries
[**documentsGet**](DocumentsApi.md#documentsGet) | **GET** /documents | Get your list of documents
[**getDocById**](DocumentsApi.md#getDocById) | **GET** /documents/{docId} | Get data from a previously submitted document
[**getSearchResults**](DocumentsApi.md#getSearchResults) | **GET** /searches/{docId}/{dictionaryId} | Gets search results for a particular document/dictionary
[**runSearch**](DocumentsApi.md#runSearch) | **POST** /searches | Run a search
[**searchesGet**](DocumentsApi.md#searchesGet) | **GET** /searches | Get your list of searches
[**uploadDictionary**](DocumentsApi.md#uploadDictionary) | **POST** /dictionaries | Upload a dictionary (CSV)
[**uploadDoc**](DocumentsApi.md#uploadDoc) | **POST** /documents | Upload a document



## dictionariesGet

> dictionariesGet()

Get your list of dictionaries

Get your list of dictionaries

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.DocumentsApi();
apiInstance.dictionariesGet((error, data, response) => {
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

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## documentsGet

> [DocumentListSummary] documentsGet()

Get your list of documents

Get your list of documents

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.DocumentsApi();
apiInstance.documentsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[DocumentListSummary]**](DocumentListSummary.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocById

> DocumentResponseDetailed getDocById(docId)

Get data from a previously submitted document

Get data from a previously submitted document identified by ***docId***

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.DocumentsApi();
let docId = 789; // Number | Id of document to fetch
apiInstance.getDocById(docId, (error, data, response) => {
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
 **docId** | **Number**| Id of document to fetch | 

### Return type

[**DocumentResponseDetailed**](DocumentResponseDetailed.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSearchResults

> getSearchResults(docId, dictionaryId, matchingOnly)

Gets search results for a particular document/dictionary

Get detailed results for a scan/url (readability, long sentence and passive language instances), identified by **scanId** &amp; **urlId**

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.DocumentsApi();
let docId = 789; // Number | Id of document
let dictionaryId = 789; // Number | Id of dictionary
let matchingOnly = true; // Boolean | Only returning paragraphs containing a match
apiInstance.getSearchResults(docId, dictionaryId, matchingOnly, (error, data, response) => {
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
 **docId** | **Number**| Id of document | 
 **dictionaryId** | **Number**| Id of dictionary | 
 **matchingOnly** | **Boolean**| Only returning paragraphs containing a match | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## runSearch

> Object runSearch(body)

Run a search

Run a search on document **docId** using dictionary **dictId** 

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.DocumentsApi();
let body = new VisibleThreadApi.Search(); // Search | Run a search on document **docId** using dictionary**dictId**
apiInstance.runSearch(body, (error, data, response) => {
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
 **body** | [**Search**](Search.md)| Run a search on document **docId** using dictionary**dictId** | 

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## searchesGet

> searchesGet()

Get your list of searches

Get your list of searches

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.DocumentsApi();
apiInstance.searchesGet((error, data, response) => {
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

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## uploadDictionary

> uploadDictionary(file)

Upload a dictionary (CSV)

Upload a dictionary (CSV format) to your VisibleThread account. 

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.DocumentsApi();
let file = "/path/to/file"; // File | The uploaded CSV dictionary
apiInstance.uploadDictionary(file, (error, data, response) => {
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
 **file** | **File**| The uploaded CSV dictionary | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## uploadDoc

> NewDocumentResponse uploadDoc(file, opts)

Upload a document

Upload a document to your VisibleThread account.  We return a JSON response that contains a \&quot;docId\&quot; that represents your document.         You can use this id in other requests to check on the analysis status for the document and run a dictionary search and retrieve search results. 

### Example

```javascript
import VisibleThreadApi from 'visible_thread_api';
let defaultClient = VisibleThreadApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new VisibleThreadApi.DocumentsApi();
let file = "/path/to/file"; // File | The uploaded file data
let opts = {
  'longSentenceWordCount': 56, // Number | Optional setting what constitutes a long sentence (default 25)
  'veryLongSentenceWordCount': 56 // Number | Optional setting what constitutes a very long sentence (default 30)
};
apiInstance.uploadDoc(file, opts, (error, data, response) => {
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
 **file** | **File**| The uploaded file data | 
 **longSentenceWordCount** | **Number**| Optional setting what constitutes a long sentence (default 25) | [optional] 
 **veryLongSentenceWordCount** | **Number**| Optional setting what constitutes a very long sentence (default 30) | [optional] 

### Return type

[**NewDocumentResponse**](NewDocumentResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

