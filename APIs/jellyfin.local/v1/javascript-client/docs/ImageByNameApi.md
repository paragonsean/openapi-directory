# JellyfinApi.ImageByNameApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGeneralImage**](ImageByNameApi.md#getGeneralImage) | **GET** /Images/General/{name}/{type} | Get General Image.
[**getGeneralImages**](ImageByNameApi.md#getGeneralImages) | **GET** /Images/General | Get all general images.
[**getMediaInfoImage**](ImageByNameApi.md#getMediaInfoImage) | **GET** /Images/MediaInfo/{theme}/{name} | Get media info image.
[**getMediaInfoImages**](ImageByNameApi.md#getMediaInfoImages) | **GET** /Images/MediaInfo | Get all media info images.
[**getRatingImage**](ImageByNameApi.md#getRatingImage) | **GET** /Images/Ratings/{theme}/{name} | Get rating image.
[**getRatingImages**](ImageByNameApi.md#getRatingImages) | **GET** /Images/Ratings | Get all general images.



## getGeneralImage

> File getGeneralImage(name, type)

Get General Image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageByNameApi();
let name = "name_example"; // String | The name of the image.
let type = "type_example"; // String | Image Type (primary, backdrop, logo, etc).
apiInstance.getGeneralImage(name, type, (error, data, response) => {
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
 **name** | **String**| The name of the image. | 
 **type** | **String**| Image Type (primary, backdrop, logo, etc). | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase, application/octet-stream


## getGeneralImages

> [ImageByNameInfo] getGeneralImages()

Get all general images.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageByNameApi();
apiInstance.getGeneralImages((error, data, response) => {
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

[**[ImageByNameInfo]**](ImageByNameInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getMediaInfoImage

> File getMediaInfoImage(theme, name)

Get media info image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageByNameApi();
let theme = "theme_example"; // String | The theme to get the image from.
let name = "name_example"; // String | The name of the image.
apiInstance.getMediaInfoImage(theme, name, (error, data, response) => {
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
 **theme** | **String**| The theme to get the image from. | 
 **name** | **String**| The name of the image. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase, application/octet-stream


## getMediaInfoImages

> [ImageByNameInfo] getMediaInfoImages()

Get all media info images.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageByNameApi();
apiInstance.getMediaInfoImages((error, data, response) => {
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

[**[ImageByNameInfo]**](ImageByNameInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRatingImage

> File getRatingImage(theme, name)

Get rating image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.ImageByNameApi();
let theme = "theme_example"; // String | The theme to get the image from.
let name = "name_example"; // String | The name of the image.
apiInstance.getRatingImage(theme, name, (error, data, response) => {
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
 **theme** | **String**| The theme to get the image from. | 
 **name** | **String**| The name of the image. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase, application/octet-stream


## getRatingImages

> [ImageByNameInfo] getRatingImages()

Get all general images.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ImageByNameApi();
apiInstance.getRatingImages((error, data, response) => {
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

[**[ImageByNameInfo]**](ImageByNameInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

