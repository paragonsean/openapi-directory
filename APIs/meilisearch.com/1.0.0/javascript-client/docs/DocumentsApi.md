# MeilisearchV11.DocumentsApi

All URIs are relative to *http://localhost:7700*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOrReplaceDocuments**](DocumentsApi.md#addOrReplaceDocuments) | **POST** /indexes/books/documents | Add or replace documents
[**addOrUpdateDocuments**](DocumentsApi.md#addOrUpdateDocuments) | **PUT** /indexes/books/documents | Add or update documents
[**deleteAllDocuments**](DocumentsApi.md#deleteAllDocuments) | **DELETE** /indexes/books/documents | Delete all documents
[**deleteDocuments**](DocumentsApi.md#deleteDocuments) | **POST** /indexes/books/documents/delete-batch | Delete documents
[**deleteOneDocument**](DocumentsApi.md#deleteOneDocument) | **DELETE** /indexes/books/documents/1 | Delete one document
[**getDocuments**](DocumentsApi.md#getDocuments) | **GET** /indexes/books/documents | Get documents
[**getOneDocument**](DocumentsApi.md#getOneDocument) | **GET** /indexes/books/documents/2 | Get one document



## addOrReplaceDocuments

> addOrReplaceDocuments(opts)

Add or replace documents

Add or replace documents

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.DocumentsApi();
let opts = {
  'primaryKey': "id", // String | 
  'csvDelimiter': ";", // String | 
  'addOrReplaceDocumentsRequestInner': [{"author":"Jane Austen","genre":"romance","id":2,"price":3.5,"title":"Pride and Prejudice"},{"author":"Antoine de Saint-Exupéry","genre":"adventure","id":456,"price":10,"title":"Le Petit Prince"},{"author":"Lewis Carroll","genre":"fantasy","id":1,"price":25.99,"title":"Alice In Wonderland"},{"author":"J. R. R. Tolkien","genre":"fantasy","id":1344,"title":"The Hobbit"},{"author":"J. K. Rowling","genre":"fantasy","id":4,"title":"Harry Potter and the Half-Blood Prince"},{"author":"Douglas Adams","id":42,"title":"The Hitchhiker's Guide to the Galaxy"}] // [AddOrReplaceDocumentsRequestInner] | 
};
apiInstance.addOrReplaceDocuments(opts, (error, data, response) => {
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
 **primaryKey** | **String**|  | [optional] 
 **csvDelimiter** | **String**|  | [optional] 
 **addOrReplaceDocumentsRequestInner** | [**[AddOrReplaceDocumentsRequestInner]**](AddOrReplaceDocumentsRequestInner.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addOrUpdateDocuments

> addOrUpdateDocuments(opts)

Add or update documents

Add or update documents

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.DocumentsApi();
let opts = {
  'primaryKey': "id", // String | 
  'csvDelimiter': ";", // String | 
  'addOrUpdateDocumentsRequestInner': [{"author":"J. Austen","date":"1813","id":2}] // [AddOrUpdateDocumentsRequestInner] | 
};
apiInstance.addOrUpdateDocuments(opts, (error, data, response) => {
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
 **primaryKey** | **String**|  | [optional] 
 **csvDelimiter** | **String**|  | [optional] 
 **addOrUpdateDocumentsRequestInner** | [**[AddOrUpdateDocumentsRequestInner]**](AddOrUpdateDocumentsRequestInner.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteAllDocuments

> deleteAllDocuments()

Delete all documents

Delete all documents

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.DocumentsApi();
apiInstance.deleteAllDocuments((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDocuments

> deleteDocuments(opts)

Delete documents

Delete documents

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.DocumentsApi();
let opts = {
  'requestBody': [1,2] // [Number] | 
};
apiInstance.deleteDocuments(opts, (error, data, response) => {
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
 **requestBody** | [**[Number]**](Number.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteOneDocument

> deleteOneDocument()

Delete one document

Delete one document

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.DocumentsApi();
apiInstance.deleteOneDocument((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: Not defined


## getDocuments

> getDocuments(opts)

Get documents

Get documents

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.DocumentsApi();
let opts = {
  'limit': "1", // String | 
  'offset': "10", // String | 
  'fields': "id" // String | 
};
apiInstance.getDocuments(opts, (error, data, response) => {
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
 **limit** | **String**|  | [optional] 
 **offset** | **String**|  | [optional] 
 **fields** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getOneDocument

> getOneDocument(opts)

Get one document

Get one document

### Example

```javascript
import MeilisearchV11 from 'meilisearch_v1_1';

let apiInstance = new MeilisearchV11.DocumentsApi();
let opts = {
  'fields': "id" // String | 
};
apiInstance.getOneDocument(opts, (error, data, response) => {
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
 **fields** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

