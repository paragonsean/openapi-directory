# SpotifyWebApi.GenresApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRecommendationGenres**](GenresApi.md#getRecommendationGenres) | **GET** /recommendations/available-genre-seeds | Get Available Genre Seeds 



## getRecommendationGenres

> GetRecommendationGenres200Response getRecommendationGenres()

Get Available Genre Seeds 

Retrieve a list of available genres seed parameter values for [recommendations](/documentation/web-api/reference/get-recommendations). 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.GenresApi();
apiInstance.getRecommendationGenres((error, data, response) => {
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

[**GetRecommendationGenres200Response**](GetRecommendationGenres200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

