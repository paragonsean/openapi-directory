# ContentModeratorClient.ListManagementTermApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listManagementTermAddTerm**](ListManagementTermApi.md#listManagementTermAddTerm) | **POST** /contentmoderator/lists/v1.0/termlists/{listId}/terms/{term} | 
[**listManagementTermDeleteAllTerms**](ListManagementTermApi.md#listManagementTermDeleteAllTerms) | **DELETE** /contentmoderator/lists/v1.0/termlists/{listId}/terms | 
[**listManagementTermDeleteTerm**](ListManagementTermApi.md#listManagementTermDeleteTerm) | **DELETE** /contentmoderator/lists/v1.0/termlists/{listId}/terms/{term} | 
[**listManagementTermGetAllTerms**](ListManagementTermApi.md#listManagementTermGetAllTerms) | **GET** /contentmoderator/lists/v1.0/termlists/{listId}/terms | 



## listManagementTermAddTerm

> listManagementTermAddTerm(listId, term, language)



Add a term to the term list with list Id equal to list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementTermApi();
let listId = "listId_example"; // String | List Id of the image list.
let term = "term_example"; // String | Term to be deleted
let language = "language_example"; // String | Language of the terms.
apiInstance.listManagementTermAddTerm(listId, term, language, (error, data, response) => {
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
 **listId** | **String**| List Id of the image list. | 
 **term** | **String**| Term to be deleted | 
 **language** | **String**| Language of the terms. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementTermDeleteAllTerms

> String listManagementTermDeleteAllTerms(listId, language)



Deletes all terms from the list with list Id equal to the list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementTermApi();
let listId = "listId_example"; // String | List Id of the image list.
let language = "language_example"; // String | Language of the terms.
apiInstance.listManagementTermDeleteAllTerms(listId, language, (error, data, response) => {
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
 **listId** | **String**| List Id of the image list. | 
 **language** | **String**| Language of the terms. | 

### Return type

**String**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementTermDeleteTerm

> String listManagementTermDeleteTerm(listId, term, language)



Deletes a term from the list with list Id equal to the list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementTermApi();
let listId = "listId_example"; // String | List Id of the image list.
let term = "term_example"; // String | Term to be deleted
let language = "language_example"; // String | Language of the terms.
apiInstance.listManagementTermDeleteTerm(listId, term, language, (error, data, response) => {
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
 **listId** | **String**| List Id of the image list. | 
 **term** | **String**| Term to be deleted | 
 **language** | **String**| Language of the terms. | 

### Return type

**String**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementTermGetAllTerms

> Terms listManagementTermGetAllTerms(listId, language, opts)



Gets all terms from the list with list Id equal to the list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementTermApi();
let listId = "listId_example"; // String | List Id of the image list.
let language = "language_example"; // String | Language of the terms.
let opts = {
  'offset': 56, // Number | The pagination start index.
  'limit': 56 // Number | The max limit.
};
apiInstance.listManagementTermGetAllTerms(listId, language, opts, (error, data, response) => {
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
 **listId** | **String**| List Id of the image list. | 
 **language** | **String**| Language of the terms. | 
 **offset** | **Number**| The pagination start index. | [optional] 
 **limit** | **Number**| The max limit. | [optional] 

### Return type

[**Terms**](Terms.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

