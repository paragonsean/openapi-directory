# Vimeo.AlbumsEssentialsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAlbum**](AlbumsEssentialsApi.md#createAlbum) | **POST** /users/{user_id}/albums | Create an album
[**createAlbumAlt1**](AlbumsEssentialsApi.md#createAlbumAlt1) | **POST** /me/albums | Create an album
[**deleteAlbum**](AlbumsEssentialsApi.md#deleteAlbum) | **DELETE** /users/{user_id}/albums/{album_id} | Delete an album
[**deleteAlbumAlt1**](AlbumsEssentialsApi.md#deleteAlbumAlt1) | **DELETE** /me/albums/{album_id} | Delete an album
[**editAlbum**](AlbumsEssentialsApi.md#editAlbum) | **PATCH** /users/{user_id}/albums/{album_id} | Edit an album
[**editAlbumAlt1**](AlbumsEssentialsApi.md#editAlbumAlt1) | **PATCH** /me/albums/{album_id} | Edit an album
[**getAlbum**](AlbumsEssentialsApi.md#getAlbum) | **GET** /users/{user_id}/albums/{album_id} | Get a specific album
[**getAlbumAlt1**](AlbumsEssentialsApi.md#getAlbumAlt1) | **GET** /me/albums/{album_id} | Get a specific album
[**getAlbums**](AlbumsEssentialsApi.md#getAlbums) | **GET** /users/{user_id}/albums | Get all the albums that belong to a user
[**getAlbumsAlt1**](AlbumsEssentialsApi.md#getAlbumsAlt1) | **GET** /me/albums | Get all the albums that belong to a user



## createAlbum

> Album createAlbum(userId, createAlbumAlt1Request)

Create an album

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

let apiInstance = new Vimeo.AlbumsEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let createAlbumAlt1Request = new Vimeo.CreateAlbumAlt1Request(); // CreateAlbumAlt1Request | 
apiInstance.createAlbum(userId, createAlbumAlt1Request, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **createAlbumAlt1Request** | [**CreateAlbumAlt1Request**](CreateAlbumAlt1Request.md)|  | 

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.album+json
- **Accept**: application/vnd.vimeo.album+json


## createAlbumAlt1

> Album createAlbumAlt1(createAlbumAlt1Request)

Create an album

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

let apiInstance = new Vimeo.AlbumsEssentialsApi();
let createAlbumAlt1Request = new Vimeo.CreateAlbumAlt1Request(); // CreateAlbumAlt1Request | 
apiInstance.createAlbumAlt1(createAlbumAlt1Request, (error, data, response) => {
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
 **createAlbumAlt1Request** | [**CreateAlbumAlt1Request**](CreateAlbumAlt1Request.md)|  | 

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.album+json
- **Accept**: application/vnd.vimeo.album+json


## deleteAlbum

> deleteAlbum(albumId, userId)

Delete an album

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

let apiInstance = new Vimeo.AlbumsEssentialsApi();
let albumId = 3706071; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
apiInstance.deleteAlbum(albumId, userId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteAlbumAlt1

> deleteAlbumAlt1(albumId)

Delete an album

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

let apiInstance = new Vimeo.AlbumsEssentialsApi();
let albumId = 3706071; // Number | The ID of the album.
apiInstance.deleteAlbumAlt1(albumId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editAlbum

> Album editAlbum(albumId, userId, opts)

Edit an album

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

let apiInstance = new Vimeo.AlbumsEssentialsApi();
let albumId = 3706071; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'editAlbumAlt1Request': new Vimeo.EditAlbumAlt1Request() // EditAlbumAlt1Request | 
};
apiInstance.editAlbum(albumId, userId, opts, (error, data, response) => {
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
 **editAlbumAlt1Request** | [**EditAlbumAlt1Request**](EditAlbumAlt1Request.md)|  | [optional] 

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.album+json
- **Accept**: application/vnd.vimeo.album+json


## editAlbumAlt1

> Album editAlbumAlt1(albumId, opts)

Edit an album

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

let apiInstance = new Vimeo.AlbumsEssentialsApi();
let albumId = 3706071; // Number | The ID of the album.
let opts = {
  'editAlbumAlt1Request': new Vimeo.EditAlbumAlt1Request() // EditAlbumAlt1Request | 
};
apiInstance.editAlbumAlt1(albumId, opts, (error, data, response) => {
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
 **editAlbumAlt1Request** | [**EditAlbumAlt1Request**](EditAlbumAlt1Request.md)|  | [optional] 

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.album+json
- **Accept**: application/vnd.vimeo.album+json


## getAlbum

> Album getAlbum(albumId, userId)

Get a specific album

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

let apiInstance = new Vimeo.AlbumsEssentialsApi();
let albumId = 3706071; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
apiInstance.getAlbum(albumId, userId, (error, data, response) => {
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

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.album+json


## getAlbumAlt1

> Album getAlbumAlt1(albumId)

Get a specific album

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

let apiInstance = new Vimeo.AlbumsEssentialsApi();
let albumId = 3706071; // Number | The ID of the album.
apiInstance.getAlbumAlt1(albumId, (error, data, response) => {
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

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.album+json


## getAlbums

> [Album] getAlbums(userId, opts)

Get all the albums that belong to a user

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

let apiInstance = new Vimeo.AlbumsEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getAlbums(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Album]**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAlbumsAlt1

> [Album] getAlbumsAlt1(opts)

Get all the albums that belong to a user

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

let apiInstance = new Vimeo.AlbumsEssentialsApi();
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getAlbumsAlt1(opts, (error, data, response) => {
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
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Album]**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

