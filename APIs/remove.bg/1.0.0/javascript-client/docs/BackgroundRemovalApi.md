# BackgroundRemovalApi.BackgroundRemovalApi

All URIs are relative to *https://api.remove.bg/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**removebgPost**](BackgroundRemovalApi.md#removebgPost) | **POST** /removebg | Remove the background of an image



## removebgPost

> RemoveBgJsonResponse removebgPost(removeBgJson)

Remove the background of an image

Removes the background of a JPG/PNG image.  * File size: up to 12 MB * Image source: File upload (binary or as base64 encoded string) or download from URL * Image Content: Any photo with a foreground [(e.g. people, products, animals, cars, etc.)](/supported-images) * Output resolutions available: Preview (up to 0.25 megapixels), Full (up to 25 megapixels)  Requires either an API Key to be provided in the &#x60;X-API-Key&#x60; request header or an OAuth 2.0 access token to be provided in the &#x60;Authorization&#x60; request header. 

### Example

```javascript
import BackgroundRemovalApi from 'background_removal_api';
let defaultClient = BackgroundRemovalApi.ApiClient.instance;
// Configure API key authorization: APIKeyHeader
let APIKeyHeader = defaultClient.authentications['APIKeyHeader'];
APIKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new BackgroundRemovalApi.BackgroundRemovalApi();
let removeBgJson = new BackgroundRemovalApi.RemoveBgJson(); // RemoveBgJson | 
apiInstance.removebgPost(removeBgJson, (error, data, response) => {
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
 **removeBgJson** | [**RemoveBgJson**](RemoveBgJson.md)|  | 

### Return type

[**RemoveBgJsonResponse**](RemoveBgJsonResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json, image/*, */*

