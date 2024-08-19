# SpotifyWebApi.AudiobooksApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkUsersSavedAudiobooks**](AudiobooksApi.md#checkUsersSavedAudiobooks) | **GET** /me/audiobooks/contains | Check User&#39;s Saved Audiobooks 
[**getAnAudiobook**](AudiobooksApi.md#getAnAudiobook) | **GET** /audiobooks/{id} | Get an Audiobook 
[**getAudiobookChapters**](AudiobooksApi.md#getAudiobookChapters) | **GET** /audiobooks/{id}/chapters | Get Audiobook Chapters 
[**getMultipleAudiobooks**](AudiobooksApi.md#getMultipleAudiobooks) | **GET** /audiobooks | Get Several Audiobooks 
[**getUsersSavedAudiobooks**](AudiobooksApi.md#getUsersSavedAudiobooks) | **GET** /me/audiobooks | Get User&#39;s Saved Audiobooks 
[**removeAudiobooksUser**](AudiobooksApi.md#removeAudiobooksUser) | **DELETE** /me/audiobooks | Remove User&#39;s Saved Audiobooks 
[**saveAudiobooksUser**](AudiobooksApi.md#saveAudiobooksUser) | **PUT** /me/audiobooks | Save Audiobooks for Current User 



## checkUsersSavedAudiobooks

> [Boolean] checkUsersSavedAudiobooks(ids)

Check User&#39;s Saved Audiobooks 

Check if one or more audiobooks are already saved in the current Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.AudiobooksApi();
let ids = "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"; // String | 
apiInstance.checkUsersSavedAudiobooks(ids, (error, data, response) => {
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
 **ids** | **String**|  | 

### Return type

**[Boolean]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnAudiobook

> AudiobookObject getAnAudiobook(id, opts)

Get an Audiobook 

Get Spotify catalog information for a single audiobook.&lt;br /&gt; **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.AudiobooksApi();
let id = "7iHfbu1YPACw6oZPAFJtqe"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getAnAudiobook(id, opts, (error, data, response) => {
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
 **market** | **String**|  | [optional] 

### Return type

[**AudiobookObject**](AudiobookObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAudiobookChapters

> PagingSimplifiedChapterObject getAudiobookChapters(id, opts)

Get Audiobook Chapters 

Get Spotify catalog information about an audiobook&#39;s chapters.&lt;br /&gt; **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.AudiobooksApi();
let id = "7iHfbu1YPACw6oZPAFJtqe"; // String | 
let opts = {
  'market': "ES", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getAudiobookChapters(id, opts, (error, data, response) => {
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
 **market** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingSimplifiedChapterObject**](PagingSimplifiedChapterObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMultipleAudiobooks

> GetMultipleAudiobooks200Response getMultipleAudiobooks(ids, opts)

Get Several Audiobooks 

Get Spotify catalog information for several audiobooks identified by their Spotify IDs.&lt;br /&gt; **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.AudiobooksApi();
let ids = "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getMultipleAudiobooks(ids, opts, (error, data, response) => {
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
 **ids** | **String**|  | 
 **market** | **String**|  | [optional] 

### Return type

[**GetMultipleAudiobooks200Response**](GetMultipleAudiobooks200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersSavedAudiobooks

> PagingSimplifiedAudiobookObject getUsersSavedAudiobooks(opts)

Get User&#39;s Saved Audiobooks 

Get a list of the audiobooks saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.AudiobooksApi();
let opts = {
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersSavedAudiobooks(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingSimplifiedAudiobookObject**](PagingSimplifiedAudiobookObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeAudiobooksUser

> removeAudiobooksUser(ids)

Remove User&#39;s Saved Audiobooks 

Remove one or more audiobooks from the Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.AudiobooksApi();
let ids = "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"; // String | 
apiInstance.removeAudiobooksUser(ids, (error, data, response) => {
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
 **ids** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveAudiobooksUser

> saveAudiobooksUser(ids)

Save Audiobooks for Current User 

Save one or more audiobooks to the current Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.AudiobooksApi();
let ids = "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"; // String | 
apiInstance.saveAudiobooksUser(ids, (error, data, response) => {
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
 **ids** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

