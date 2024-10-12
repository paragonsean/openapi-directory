# Contribly.MediaApi

All URIs are relative to *https://api.contribly.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaPost**](MediaApi.md#mediaPost) | **POST** /media | Submit a new media file



## mediaPost

> Media mediaPost(body)

Submit a new media file

### Example

```javascript
import Contribly from 'contribly';
let defaultClient = Contribly.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Contribly.MediaApi();
let body = null; // Blob | Binary media file
apiInstance.mediaPost(body, (error, data, response) => {
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
 **body** | **Blob**| Binary media file | 

### Return type

[**Media**](Media.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

