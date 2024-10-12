# MotaWordApi.SearchApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkDocumentsReindex**](SearchApi.md#checkDocumentsReindex) | **GET** /search/documents/reindex/status | Check reindex status of the client source and translation documents.
[**reindexDocuments**](SearchApi.md#reindexDocuments) | **POST** /search/documents/reindex | Reindex for search all of the client source and translation documents.
[**searchEverywhere**](SearchApi.md#searchEverywhere) | **GET** /search | Search everything in your account



## checkDocumentsReindex

> AsyncOperationStatus checkDocumentsReindex(asyncRequestKey)

Check reindex status of the client source and translation documents.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.SearchApi();
let asyncRequestKey = "f0db2468-6b77-41a4-bafe-70157bc166ad"; // String | Async operation key
apiInstance.checkDocumentsReindex(asyncRequestKey, (error, data, response) => {
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
 **asyncRequestKey** | **String**| Async operation key | 

### Return type

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reindexDocuments

> AsyncOperationStatus reindexDocuments()

Reindex for search all of the client source and translation documents.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.SearchApi();
apiInstance.reindexDocuments((error, data, response) => {
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

[**AsyncOperationStatus**](AsyncOperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchEverywhere

> SearchEverywhereResult searchEverywhere(query, opts)

Search everything in your account

Search through everything in your account, from projects to documents, from source strings to translations...

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.SearchApi();
let query = "en-US"; // String | Search query term
let opts = {
  'include': ["null"], // [String] | Search in these entities. Current oprions are projects, documents, strings. Can be multiple. When not provided, we'll search through all entities.
  'page': 1, // Number | 
  'perPage': 10 // Number | 
};
apiInstance.searchEverywhere(query, opts, (error, data, response) => {
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
 **query** | **String**| Search query term | 
 **include** | [**[String]**](String.md)| Search in these entities. Current oprions are projects, documents, strings. Can be multiple. When not provided, we&#39;ll search through all entities. | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 10]

### Return type

[**SearchEverywhereResult**](SearchEverywhereResult.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

