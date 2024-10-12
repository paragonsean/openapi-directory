# WhatsAppBusinessApi.MediaApi

All URIs are relative to *http://whatsapp.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMedia**](MediaApi.md#deleteMedia) | **DELETE** /media/{MediaId} | Delete-Media
[**downloadMedia**](MediaApi.md#downloadMedia) | **GET** /media/{MediaId} | Download-Media
[**uploadMedia**](MediaApi.md#uploadMedia) | **POST** /media | Upload-Media



## deleteMedia

> deleteMedia(mediaId)

Delete-Media

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.MediaApi();
let mediaId = "mediaId_example"; // String | 
apiInstance.deleteMedia(mediaId, (error, data, response) => {
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
 **mediaId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## downloadMedia

> downloadMedia(mediaId)

Download-Media

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.MediaApi();
let mediaId = "mediaId_example"; // String | 
apiInstance.downloadMedia(mediaId, (error, data, response) => {
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
 **mediaId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadMedia

> UploadMediaResponse uploadMedia(body)

Upload-Media

### Example

```javascript
import WhatsAppBusinessApi from 'whats_app_business_api';
let defaultClient = WhatsAppBusinessApi.ApiClient.instance;
// Configure Bearer (token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new WhatsAppBusinessApi.MediaApi();
let body = "/path/to/file"; // File | 
apiInstance.uploadMedia(body, (error, data, response) => {
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
 **body** | **File**|  | 

### Return type

[**UploadMediaResponse**](UploadMediaResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/msword, application/pdf, application/vnd.ms-excel, application/vnd.ms-powerpoint, audio/acc, audio/amr, audio/mp4, audio/mpeg, audio/ogg, codecs=opus, image/jpeg, image/png, text/plain, video/mp4
- **Accept**: application/json

