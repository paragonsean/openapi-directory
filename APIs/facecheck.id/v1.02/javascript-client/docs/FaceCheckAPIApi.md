# FacialRecognitionReverseImageFaceSearchApi.FaceCheckAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiDeletePicPost**](FaceCheckAPIApi.md#apiDeletePicPost) | **POST** /api/delete_pic | Remove an image from a search request
[**apiInfoPost**](FaceCheckAPIApi.md#apiInfoPost) | **POST** /api/info | Returns remaining search credits, search engine online status, and number of indexed faces
[**apiSearchPost**](FaceCheckAPIApi.md#apiSearchPost) | **POST** /api/search | 
[**apiUploadPicPost**](FaceCheckAPIApi.md#apiUploadPicPost) | **POST** /api/upload_pic | 



## apiDeletePicPost

> BrowserJsonResponse apiDeletePicPost(opts)

Remove an image from a search request

### Example

```javascript
import FacialRecognitionReverseImageFaceSearchApi from 'facial_recognition_reverse_image_face_search_api';
let defaultClient = FacialRecognitionReverseImageFaceSearchApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new FacialRecognitionReverseImageFaceSearchApi.FaceCheckAPIApi();
let opts = {
  'idSearch': "idSearch_example", // String | 
  'idPic': "idPic_example" // String | 
};
apiInstance.apiDeletePicPost(opts, (error, data, response) => {
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
 **idSearch** | **String**|  | [optional] 
 **idPic** | **String**|  | [optional] 

### Return type

[**BrowserJsonResponse**](BrowserJsonResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiInfoPost

> InfoResponse apiInfoPost()

Returns remaining search credits, search engine online status, and number of indexed faces

### Example

```javascript
import FacialRecognitionReverseImageFaceSearchApi from 'facial_recognition_reverse_image_face_search_api';
let defaultClient = FacialRecognitionReverseImageFaceSearchApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new FacialRecognitionReverseImageFaceSearchApi.FaceCheckAPIApi();
apiInstance.apiInfoPost((error, data, response) => {
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

[**InfoResponse**](InfoResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiSearchPost

> BrowserJsonResponse apiSearchPost(opts)



### Example

```javascript
import FacialRecognitionReverseImageFaceSearchApi from 'facial_recognition_reverse_image_face_search_api';
let defaultClient = FacialRecognitionReverseImageFaceSearchApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new FacialRecognitionReverseImageFaceSearchApi.FaceCheckAPIApi();
let opts = {
  'searchData': new FacialRecognitionReverseImageFaceSearchApi.SearchData() // SearchData | 
};
apiInstance.apiSearchPost(opts, (error, data, response) => {
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
 **searchData** | [**SearchData**](SearchData.md)|  | [optional] 

### Return type

[**BrowserJsonResponse**](BrowserJsonResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json


## apiUploadPicPost

> BrowserJsonResponse apiUploadPicPost(opts)



### Example

```javascript
import FacialRecognitionReverseImageFaceSearchApi from 'facial_recognition_reverse_image_face_search_api';
let defaultClient = FacialRecognitionReverseImageFaceSearchApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new FacialRecognitionReverseImageFaceSearchApi.FaceCheckAPIApi();
let opts = {
  'idSearch': "idSearch_example", // String | 
  'images': ["null"] // [File] | 
};
apiInstance.apiUploadPicPost(opts, (error, data, response) => {
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
 **idSearch** | **String**|  | [optional] 
 **images** | **[File]**|  | [optional] 

### Return type

[**BrowserJsonResponse**](BrowserJsonResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

