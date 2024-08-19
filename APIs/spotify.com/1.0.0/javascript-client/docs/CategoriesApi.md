# SpotifyWebApi.CategoriesApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getACategoriesPlaylists_0**](CategoriesApi.md#getACategoriesPlaylists_0) | **GET** /browse/categories/{category_id}/playlists | Get Category&#39;s Playlists 
[**getACategory**](CategoriesApi.md#getACategory) | **GET** /browse/categories/{category_id} | Get Single Browse Category 
[**getCategories**](CategoriesApi.md#getCategories) | **GET** /browse/categories | Get Several Browse Categories 



## getACategoriesPlaylists_0

> PagingFeaturedPlaylistObject getACategoriesPlaylists_0(categoryId, opts)

Get Category&#39;s Playlists 

Get a list of Spotify playlists tagged with a particular category. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.CategoriesApi();
let categoryId = "dinner"; // String | 
let opts = {
  'country': "SE", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getACategoriesPlaylists_0(categoryId, opts, (error, data, response) => {
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
 **categoryId** | **String**|  | 
 **country** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingFeaturedPlaylistObject**](PagingFeaturedPlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getACategory

> CategoryObject getACategory(categoryId, opts)

Get Single Browse Category 

Get a single category used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab). 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.CategoriesApi();
let categoryId = "dinner"; // String | 
let opts = {
  'country': "SE", // String | 
  'locale': "sv_SE" // String | 
};
apiInstance.getACategory(categoryId, opts, (error, data, response) => {
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
 **categoryId** | **String**|  | 
 **country** | **String**|  | [optional] 
 **locale** | **String**|  | [optional] 

### Return type

[**CategoryObject**](CategoryObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCategories

> GetCategories200Response getCategories(opts)

Get Several Browse Categories 

Get a list of categories used to tag items in Spotify (on, for example, the Spotify player’s “Browse” tab). 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.CategoriesApi();
let opts = {
  'country': "SE", // String | 
  'locale': "sv_SE", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getCategories(opts, (error, data, response) => {
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
 **country** | **String**|  | [optional] 
 **locale** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**GetCategories200Response**](GetCategories200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

