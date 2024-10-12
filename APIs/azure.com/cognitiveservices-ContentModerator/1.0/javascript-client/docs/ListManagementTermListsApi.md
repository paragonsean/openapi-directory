# ContentModeratorClient.ListManagementTermListsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listManagementTermListsCreate**](ListManagementTermListsApi.md#listManagementTermListsCreate) | **POST** /contentmoderator/lists/v1.0/termlists | 
[**listManagementTermListsDelete**](ListManagementTermListsApi.md#listManagementTermListsDelete) | **DELETE** /contentmoderator/lists/v1.0/termlists/{listId} | 
[**listManagementTermListsGetAllTermLists**](ListManagementTermListsApi.md#listManagementTermListsGetAllTermLists) | **GET** /contentmoderator/lists/v1.0/termlists | 
[**listManagementTermListsGetDetails**](ListManagementTermListsApi.md#listManagementTermListsGetDetails) | **GET** /contentmoderator/lists/v1.0/termlists/{listId} | 
[**listManagementTermListsRefreshIndex**](ListManagementTermListsApi.md#listManagementTermListsRefreshIndex) | **POST** /contentmoderator/lists/v1.0/termlists/{listId}/RefreshIndex | 
[**listManagementTermListsUpdate**](ListManagementTermListsApi.md#listManagementTermListsUpdate) | **PUT** /contentmoderator/lists/v1.0/termlists/{listId} | 



## listManagementTermListsCreate

> TermList listManagementTermListsCreate(contentType, body)



Creates a Term List

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementTermListsApi();
let contentType = "contentType_example"; // String | The content type.
let body = new ContentModeratorClient.ListManagementImageListsCreateRequest(); // ListManagementImageListsCreateRequest | Schema of the body.
apiInstance.listManagementTermListsCreate(contentType, body, (error, data, response) => {
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
 **contentType** | **String**| The content type. | 
 **body** | [**ListManagementImageListsCreateRequest**](ListManagementImageListsCreateRequest.md)| Schema of the body. | 

### Return type

[**TermList**](TermList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listManagementTermListsDelete

> String listManagementTermListsDelete(listId)



Deletes term list with the list Id equal to list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementTermListsApi();
let listId = "listId_example"; // String | List Id of the image list.
apiInstance.listManagementTermListsDelete(listId, (error, data, response) => {
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

### Return type

**String**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementTermListsGetAllTermLists

> [TermList] listManagementTermListsGetAllTermLists()



gets all the Term Lists

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementTermListsApi();
apiInstance.listManagementTermListsGetAllTermLists((error, data, response) => {
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

[**[TermList]**](TermList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementTermListsGetDetails

> TermList listManagementTermListsGetDetails(listId)



Returns list Id details of the term list with list Id equal to list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementTermListsApi();
let listId = "listId_example"; // String | List Id of the image list.
apiInstance.listManagementTermListsGetDetails(listId, (error, data, response) => {
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

### Return type

[**TermList**](TermList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementTermListsRefreshIndex

> RefreshIndex listManagementTermListsRefreshIndex(listId, language)



Refreshes the index of the list with list Id equal to list ID passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementTermListsApi();
let listId = "listId_example"; // String | List Id of the image list.
let language = "language_example"; // String | Language of the terms.
apiInstance.listManagementTermListsRefreshIndex(listId, language, (error, data, response) => {
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

[**RefreshIndex**](RefreshIndex.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementTermListsUpdate

> TermList listManagementTermListsUpdate(listId, contentType, body)



Updates an Term List.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementTermListsApi();
let listId = "listId_example"; // String | List Id of the image list.
let contentType = "contentType_example"; // String | The content type.
let body = new ContentModeratorClient.ListManagementImageListsCreateRequest(); // ListManagementImageListsCreateRequest | Schema of the body.
apiInstance.listManagementTermListsUpdate(listId, contentType, body, (error, data, response) => {
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
 **contentType** | **String**| The content type. | 
 **body** | [**ListManagementImageListsCreateRequest**](ListManagementImageListsCreateRequest.md)| Schema of the body. | 

### Return type

[**TermList**](TermList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

