# MuxApi.DirectUploadsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelDirectUpload**](DirectUploadsApi.md#cancelDirectUpload) | **PUT** /video/v1/uploads/{UPLOAD_ID}/cancel | Cancel a direct upload
[**createDirectUpload**](DirectUploadsApi.md#createDirectUpload) | **POST** /video/v1/uploads | Create a new direct upload URL
[**getDirectUpload**](DirectUploadsApi.md#getDirectUpload) | **GET** /video/v1/uploads/{UPLOAD_ID} | Retrieve a single direct upload&#39;s info
[**listDirectUploads**](DirectUploadsApi.md#listDirectUploads) | **GET** /video/v1/uploads | List direct uploads



## cancelDirectUpload

> UploadResponse cancelDirectUpload(UPLOAD_ID)

Cancel a direct upload

Cancels a direct upload and marks it as cancelled. If a pending upload finishes after this request, no asset will be created. This request will only succeed if the upload is still in the &#x60;waiting&#x60; state. 

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.DirectUploadsApi();
let UPLOAD_ID = "abcd1234"; // String | ID of the Upload
apiInstance.cancelDirectUpload(UPLOAD_ID, (error, data, response) => {
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
 **UPLOAD_ID** | **String**| ID of the Upload | 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createDirectUpload

> UploadResponse createDirectUpload(createUploadRequest)

Create a new direct upload URL

Creates a new direct upload, through which video content can be uploaded for ingest to Mux.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.DirectUploadsApi();
let createUploadRequest = {"cors_origin":"https://example.com/","new_asset_settings":{"mp4_support":"standard","playback_policy":["public"]}}; // CreateUploadRequest | 
apiInstance.createDirectUpload(createUploadRequest, (error, data, response) => {
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
 **createUploadRequest** | [**CreateUploadRequest**](CreateUploadRequest.md)|  | 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDirectUpload

> UploadResponse getDirectUpload(UPLOAD_ID)

Retrieve a single direct upload&#39;s info

Fetches information about a single direct upload in the current environment.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.DirectUploadsApi();
let UPLOAD_ID = "abcd1234"; // String | ID of the Upload
apiInstance.getDirectUpload(UPLOAD_ID, (error, data, response) => {
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
 **UPLOAD_ID** | **String**| ID of the Upload | 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDirectUploads

> ListUploadsResponse listDirectUploads(opts)

List direct uploads

Lists direct uploads in the current environment.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.DirectUploadsApi();
let opts = {
  'limit': 25, // Number | Number of items to include in the response
  'page': 1 // Number | Offset by this many pages, of the size of `limit`
};
apiInstance.listDirectUploads(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 25]
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListUploadsResponse**](ListUploadsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

