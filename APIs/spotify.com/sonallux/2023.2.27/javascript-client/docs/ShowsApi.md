# SpotifyWebApiWithFixesAndImprovementsFromSonallux.ShowsApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkUsersSavedShows**](ShowsApi.md#checkUsersSavedShows) | **GET** /me/shows/contains | Check User&#39;s Saved Shows 
[**getAShow**](ShowsApi.md#getAShow) | **GET** /shows/{id} | Get Show 
[**getAShowsEpisodes**](ShowsApi.md#getAShowsEpisodes) | **GET** /shows/{id}/episodes | Get Show Episodes 
[**getMultipleShows**](ShowsApi.md#getMultipleShows) | **GET** /shows | Get Several Shows 
[**getUsersSavedShows**](ShowsApi.md#getUsersSavedShows) | **GET** /me/shows | Get User&#39;s Saved Shows 
[**removeShowsUser**](ShowsApi.md#removeShowsUser) | **DELETE** /me/shows | Remove User&#39;s Saved Shows 
[**saveShowsUser**](ShowsApi.md#saveShowsUser) | **PUT** /me/shows | Save Shows for Current User 



## checkUsersSavedShows

> [Boolean] checkUsersSavedShows(ids)

Check User&#39;s Saved Shows 

Check if one or more shows is already saved in the current Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ShowsApi();
let ids = "5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ"; // String | 
apiInstance.checkUsersSavedShows(ids, (error, data, response) => {
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


## getAShow

> ShowObject getAShow(id, opts)

Get Show 

Get Spotify catalog information for a single show identified by its unique Spotify ID. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ShowsApi();
let id = "38bS44xjbVVZ3No3ByF1dJ"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getAShow(id, opts, (error, data, response) => {
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

[**ShowObject**](ShowObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAShowsEpisodes

> PagingSimplifiedEpisodeObject getAShowsEpisodes(id, opts)

Get Show Episodes 

Get Spotify catalog information about an show’s episodes. Optional parameters can be used to limit the number of episodes returned. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ShowsApi();
let id = "38bS44xjbVVZ3No3ByF1dJ"; // String | 
let opts = {
  'market': "ES", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getAShowsEpisodes(id, opts, (error, data, response) => {
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

[**PagingSimplifiedEpisodeObject**](PagingSimplifiedEpisodeObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMultipleShows

> GetMultipleShows200Response getMultipleShows(ids, opts)

Get Several Shows 

Get Spotify catalog information for several shows based on their Spotify IDs. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ShowsApi();
let ids = "5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getMultipleShows(ids, opts, (error, data, response) => {
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

[**GetMultipleShows200Response**](GetMultipleShows200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersSavedShows

> PagingSavedShowObject getUsersSavedShows(opts)

Get User&#39;s Saved Shows 

Get a list of shows saved in the current Spotify user&#39;s library. Optional parameters can be used to limit the number of shows returned. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ShowsApi();
let opts = {
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersSavedShows(opts, (error, data, response) => {
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

[**PagingSavedShowObject**](PagingSavedShowObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeShowsUser

> removeShowsUser(ids, opts)

Remove User&#39;s Saved Shows 

Delete one or more shows from current Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ShowsApi();
let ids = "5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ"; // String | 
let opts = {
  'market': "ES", // String | 
  'saveShowsUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveShowsUserRequest() // SaveShowsUserRequest | 
};
apiInstance.removeShowsUser(ids, opts, (error, data, response) => {
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
 **market** | **String**|  | [optional] 
 **saveShowsUserRequest** | [**SaveShowsUserRequest**](SaveShowsUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveShowsUser

> saveShowsUser(ids, opts)

Save Shows for Current User 

Save one or more shows to current Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ShowsApi();
let ids = "5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ"; // String | 
let opts = {
  'saveShowsUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveShowsUserRequest() // SaveShowsUserRequest | 
};
apiInstance.saveShowsUser(ids, opts, (error, data, response) => {
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
 **saveShowsUserRequest** | [**SaveShowsUserRequest**](SaveShowsUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

