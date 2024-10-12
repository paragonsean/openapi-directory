# Vimeo.AlbumsCustomAlbumLogosApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAlbumLogo**](AlbumsCustomAlbumLogosApi.md#createAlbumLogo) | **POST** /users/{user_id}/albums/{album_id}/logos | Add a custom album logo
[**deleteAlbumLogo**](AlbumsCustomAlbumLogosApi.md#deleteAlbumLogo) | **DELETE** /users/{user_id}/albums/{album_id}/logos/{logo_id} | Remove a custom album logo
[**getAlbumLogo**](AlbumsCustomAlbumLogosApi.md#getAlbumLogo) | **GET** /users/{user_id}/albums/{album_id}/logos/{logo_id} | Get a specific custom album logo
[**getAlbumLogos**](AlbumsCustomAlbumLogosApi.md#getAlbumLogos) | **GET** /users/{user_id}/albums/{album_id}/logos | Get all the custom logos of an album
[**replaceAlbumLogo**](AlbumsCustomAlbumLogosApi.md#replaceAlbumLogo) | **PATCH** /users/{user_id}/albums/{album_id}/logos/{logo_id} | Replace a custom album logo



## createAlbumLogo

> Picture createAlbumLogo(albumId, userId)

Add a custom album logo

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AlbumsCustomAlbumLogosApi();
let albumId = 3706071; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
apiInstance.createAlbumLogo(albumId, userId, (error, data, response) => {
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
 **albumId** | **Number**| The ID of the album. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## deleteAlbumLogo

> deleteAlbumLogo(albumId, logoId, userId)

Remove a custom album logo

This method removes a custom logo from the specified album.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AlbumsCustomAlbumLogosApi();
let albumId = 3706071; // Number | The ID of the album.
let logoId = 12345; // Number | The ID of the custom logo.
let userId = 152184; // Number | The ID of the user.
apiInstance.deleteAlbumLogo(albumId, logoId, userId, (error, data, response) => {
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
 **albumId** | **Number**| The ID of the album. | 
 **logoId** | **Number**| The ID of the custom logo. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getAlbumLogo

> Picture getAlbumLogo(albumId, logoId, userId)

Get a specific custom album logo

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AlbumsCustomAlbumLogosApi();
let albumId = 3706071; // Number | The ID of the album.
let logoId = 12345; // Number | The ID of the custom logo.
let userId = 152184; // Number | The ID of the user.
apiInstance.getAlbumLogo(albumId, logoId, userId, (error, data, response) => {
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
 **albumId** | **Number**| The ID of the album. | 
 **logoId** | **Number**| The ID of the custom logo. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getAlbumLogos

> [Picture] getAlbumLogos(albumId, userId, opts)

Get all the custom logos of an album

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AlbumsCustomAlbumLogosApi();
let albumId = 3706071; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getAlbumLogos(albumId, userId, opts, (error, data, response) => {
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
 **albumId** | **Number**| The ID of the album. | 
 **userId** | **Number**| The ID of the user. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Picture]**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## replaceAlbumLogo

> Picture replaceAlbumLogo(albumId, logoId, userId, opts)

Replace a custom album logo

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AlbumsCustomAlbumLogosApi();
let albumId = 3706071; // Number | The ID of the album.
let logoId = 12345; // Number | The ID of the custom logo.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'replaceAlbumLogoRequest': new Vimeo.ReplaceAlbumLogoRequest() // ReplaceAlbumLogoRequest | 
};
apiInstance.replaceAlbumLogo(albumId, logoId, userId, opts, (error, data, response) => {
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
 **albumId** | **Number**| The ID of the album. | 
 **logoId** | **Number**| The ID of the custom logo. | 
 **userId** | **Number**| The ID of the user. | 
 **replaceAlbumLogoRequest** | [**ReplaceAlbumLogoRequest**](ReplaceAlbumLogoRequest.md)|  | [optional] 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.picture+json
- **Accept**: application/vnd.vimeo.picture+json

