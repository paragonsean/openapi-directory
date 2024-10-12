# ContentModeratorClient.ListManagementImageListsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listManagementImageListsCreate**](ListManagementImageListsApi.md#listManagementImageListsCreate) | **POST** /contentmoderator/lists/v1.0/imagelists | 
[**listManagementImageListsDelete**](ListManagementImageListsApi.md#listManagementImageListsDelete) | **DELETE** /contentmoderator/lists/v1.0/imagelists/{listId} | 
[**listManagementImageListsGetAllImageLists**](ListManagementImageListsApi.md#listManagementImageListsGetAllImageLists) | **GET** /contentmoderator/lists/v1.0/imagelists | 
[**listManagementImageListsGetDetails**](ListManagementImageListsApi.md#listManagementImageListsGetDetails) | **GET** /contentmoderator/lists/v1.0/imagelists/{listId} | 
[**listManagementImageListsRefreshIndex**](ListManagementImageListsApi.md#listManagementImageListsRefreshIndex) | **POST** /contentmoderator/lists/v1.0/imagelists/{listId}/RefreshIndex | 
[**listManagementImageListsUpdate**](ListManagementImageListsApi.md#listManagementImageListsUpdate) | **PUT** /contentmoderator/lists/v1.0/imagelists/{listId} | 



## listManagementImageListsCreate

> ImageList listManagementImageListsCreate(contentType, body)



Creates an image list.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementImageListsApi();
let contentType = "contentType_example"; // String | The content type.
let body = new ContentModeratorClient.ListManagementImageListsCreateRequest(); // ListManagementImageListsCreateRequest | Schema of the body.
apiInstance.listManagementImageListsCreate(contentType, body, (error, data, response) => {
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

[**ImageList**](ImageList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listManagementImageListsDelete

> String listManagementImageListsDelete(listId)



Deletes image list with the list Id equal to list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementImageListsApi();
let listId = "listId_example"; // String | List Id of the image list.
apiInstance.listManagementImageListsDelete(listId, (error, data, response) => {
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


## listManagementImageListsGetAllImageLists

> [ImageList] listManagementImageListsGetAllImageLists()



Gets all the Image Lists.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementImageListsApi();
apiInstance.listManagementImageListsGetAllImageLists((error, data, response) => {
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

[**[ImageList]**](ImageList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementImageListsGetDetails

> ImageList listManagementImageListsGetDetails(listId)



Returns the details of the image list with list Id equal to list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementImageListsApi();
let listId = "listId_example"; // String | List Id of the image list.
apiInstance.listManagementImageListsGetDetails(listId, (error, data, response) => {
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

[**ImageList**](ImageList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementImageListsRefreshIndex

> RefreshIndex listManagementImageListsRefreshIndex(listId)



Refreshes the index of the list with list Id equal to list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementImageListsApi();
let listId = "listId_example"; // String | List Id of the image list.
apiInstance.listManagementImageListsRefreshIndex(listId, (error, data, response) => {
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

[**RefreshIndex**](RefreshIndex.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementImageListsUpdate

> ImageList listManagementImageListsUpdate(listId, contentType, body)



Updates an image list with list Id equal to list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementImageListsApi();
let listId = "listId_example"; // String | List Id of the image list.
let contentType = "contentType_example"; // String | The content type.
let body = new ContentModeratorClient.ListManagementImageListsCreateRequest(); // ListManagementImageListsCreateRequest | Schema of the body.
apiInstance.listManagementImageListsUpdate(listId, contentType, body, (error, data, response) => {
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

[**ImageList**](ImageList.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

