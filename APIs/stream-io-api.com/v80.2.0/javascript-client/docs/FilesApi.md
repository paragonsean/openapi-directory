# StreamChatApi.FilesApi

All URIs are relative to *https://chat.stream-io-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteFile_0**](FilesApi.md#deleteFile_0) | **DELETE** /channels/{type}/{id}/file | Delete file
[**deleteImage_0**](FilesApi.md#deleteImage_0) | **DELETE** /channels/{type}/{id}/image | Delete image
[**uploadFile_0**](FilesApi.md#uploadFile_0) | **POST** /channels/{type}/{id}/file | Upload file
[**uploadImage_0**](FilesApi.md#uploadImage_0) | **POST** /channels/{type}/{id}/image | Upload image



## deleteFile_0

> FileDeleteResponse deleteFile_0(type, id, opts)

Delete file

Deletes previously uploaded file  Required permissions: - DeleteAttachment 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.FilesApi();
let type = "type_example"; // String | Automatically added
let id = "id_example"; // String | Automatically added
let opts = {
  'url': "url_example" // String | 
};
apiInstance.deleteFile_0(type, id, opts, (error, data, response) => {
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
 **type** | **String**| Automatically added | 
 **id** | **String**| Automatically added | 
 **url** | **String**|  | [optional] 

### Return type

[**FileDeleteResponse**](FileDeleteResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteImage_0

> FileDeleteResponse deleteImage_0(type, id, opts)

Delete image

Deletes previously uploaded image  Required permissions: - DeleteAttachment 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.FilesApi();
let type = "type_example"; // String | Automatically added
let id = "id_example"; // String | Automatically added
let opts = {
  'url': "url_example" // String | 
};
apiInstance.deleteImage_0(type, id, opts, (error, data, response) => {
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
 **type** | **String**| Automatically added | 
 **id** | **String**| Automatically added | 
 **url** | **String**|  | [optional] 

### Return type

[**FileDeleteResponse**](FileDeleteResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadFile_0

> FileUploadResponse uploadFile_0(type, id, opts)

Upload file

Uploads file  Required permissions: - UploadAttachment 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.FilesApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'file': "file_example", // String | file field
  'user': new StreamChatApi.OnlyUserIDRequest() // OnlyUserIDRequest | 
};
apiInstance.uploadFile_0(type, id, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **file** | **String**| file field | [optional] 
 **user** | [**OnlyUserIDRequest**](OnlyUserIDRequest.md)|  | [optional] 

### Return type

[**FileUploadResponse**](FileUploadResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## uploadImage_0

> ImageUploadResponse uploadImage_0(type, id, opts)

Upload image

Uploads image  Required permissions: - UploadAttachment 

### Example

```javascript
import StreamChatApi from 'stream_chat_api';
let defaultClient = StreamChatApi.ApiClient.instance;
// Configure API key authorization: stream-auth-type
let stream-auth-type = defaultClient.authentications['stream-auth-type'];
stream-auth-type.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//stream-auth-type.apiKeyPrefix = 'Token';
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';

let apiInstance = new StreamChatApi.FilesApi();
let type = "type_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'file': "file_example", // String | 
  'uploadSizes': [new StreamChatApi.ImageSizeRequest()], // [ImageSizeRequest] | field with JSON-encoded array of image size configurations
  'user': new StreamChatApi.OnlyUserIDRequest() // OnlyUserIDRequest | 
};
apiInstance.uploadImage_0(type, id, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **id** | **String**|  | 
 **file** | **String**|  | [optional] 
 **uploadSizes** | [**[ImageSizeRequest]**](ImageSizeRequest.md)| field with JSON-encoded array of image size configurations | [optional] 
 **user** | [**OnlyUserIDRequest**](OnlyUserIDRequest.md)|  | [optional] 

### Return type

[**ImageUploadResponse**](ImageUploadResponse.md)

### Authorization

[stream-auth-type](../README.md#stream-auth-type), [api_key](../README.md#api_key), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

