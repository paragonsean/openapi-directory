# ContentModeratorClient.ListManagementImageApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listManagementImageAddImage**](ListManagementImageApi.md#listManagementImageAddImage) | **POST** /contentmoderator/lists/v1.0/imagelists/{listId}/images | 
[**listManagementImageDeleteAllImages**](ListManagementImageApi.md#listManagementImageDeleteAllImages) | **DELETE** /contentmoderator/lists/v1.0/imagelists/{listId}/images | 
[**listManagementImageDeleteImage**](ListManagementImageApi.md#listManagementImageDeleteImage) | **DELETE** /contentmoderator/lists/v1.0/imagelists/{listId}/images/{ImageId} | 
[**listManagementImageGetAllImageIds**](ListManagementImageApi.md#listManagementImageGetAllImageIds) | **GET** /contentmoderator/lists/v1.0/imagelists/{listId}/images | 



## listManagementImageAddImage

> Image listManagementImageAddImage(listId, opts)



Add an image to the list with list Id equal to list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementImageApi();
let listId = "listId_example"; // String | List Id of the image list.
let opts = {
  'tag': 56, // Number | Tag for the image.
  'label': "label_example" // String | The image label.
};
apiInstance.listManagementImageAddImage(listId, opts, (error, data, response) => {
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
 **tag** | **Number**| Tag for the image. | [optional] 
 **label** | **String**| The image label. | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementImageDeleteAllImages

> String listManagementImageDeleteAllImages(listId)



Deletes all images from the list with list Id equal to list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementImageApi();
let listId = "listId_example"; // String | List Id of the image list.
apiInstance.listManagementImageDeleteAllImages(listId, (error, data, response) => {
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


## listManagementImageDeleteImage

> String listManagementImageDeleteImage(listId, imageId)



Deletes an image from the list with list Id and image Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementImageApi();
let listId = "listId_example"; // String | List Id of the image list.
let imageId = "imageId_example"; // String | Id of the image.
apiInstance.listManagementImageDeleteImage(listId, imageId, (error, data, response) => {
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
 **imageId** | **String**| Id of the image. | 

### Return type

**String**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagementImageGetAllImageIds

> ImageIds listManagementImageGetAllImageIds(listId)



Gets all image Ids from the list with list Id equal to list Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ListManagementImageApi();
let listId = "listId_example"; // String | List Id of the image list.
apiInstance.listManagementImageGetAllImageIds(listId, (error, data, response) => {
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

[**ImageIds**](ImageIds.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

