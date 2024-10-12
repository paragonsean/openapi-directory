# LinQr.ImageManagementApi

All URIs are relative to *https://run.byvalue.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**imageDeleteImagesIdDelete**](ImageManagementApi.md#imageDeleteImagesIdDelete) | **DELETE** /images/{id} | Delete image
[**imageListAllImagesGet**](ImageManagementApi.md#imageListAllImagesGet) | **GET** /images | List all images
[**imageListImagesIdGet**](ImageManagementApi.md#imageListImagesIdGet) | **GET** /images/{id} | List image
[**imageUploadImagesPost**](ImageManagementApi.md#imageUploadImagesPost) | **POST** /images | Upload image



## imageDeleteImagesIdDelete

> imageDeleteImagesIdDelete(id)

Delete image

This endpoint allows you to delete images hosted in the LinQR storage.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.ImageManagementApi();
let id = "id_example"; // String | 
apiInstance.imageDeleteImagesIdDelete(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## imageListAllImagesGet

> [ImageMetadata] imageListAllImagesGet()

List all images

This endpoint allows you to list images hosted in the LinQR storage. If there are no images hosted, an empty array is returned.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.ImageManagementApi();
apiInstance.imageListAllImagesGet((error, data, response) => {
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

[**[ImageMetadata]**](ImageMetadata.md)

### Authorization

[RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## imageListImagesIdGet

> ImageMetadata imageListImagesIdGet(id)

List image

This endpoint allows you to list single image hosted in the LinQR storage.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.ImageManagementApi();
let id = "id_example"; // String | 
apiInstance.imageListImagesIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**ImageMetadata**](ImageMetadata.md)

### Authorization

[RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain


## imageUploadImagesPost

> ImageMetadata imageUploadImagesPost(image)

Upload image

This endpoint allows you to upload images to LinQR storage. In the response, metadata of the submitted image is sent, including the identifier used by other endpoints from the &#x60;Image management&#x60; group for image identification.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.ImageManagementApi();
let image = "/path/to/file"; // File | Binary file to be uploaded into LinQR storage. Maximum single file size is 1MiB (1,048,576 bytes).
apiInstance.imageUploadImagesPost(image, (error, data, response) => {
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
 **image** | **File**| Binary file to be uploaded into LinQR storage. Maximum single file size is 1MiB (1,048,576 bytes). | 

### Return type

[**ImageMetadata**](ImageMetadata.md)

### Authorization

[RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, text/plain

