# SpotifyWebApi.MarketsApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAvailableMarkets**](MarketsApi.md#getAvailableMarkets) | **GET** /markets | Get Available Markets 



## getAvailableMarkets

> GetAvailableMarkets200Response getAvailableMarkets()

Get Available Markets 

Get the list of markets where Spotify is available. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.MarketsApi();
apiInstance.getAvailableMarkets((error, data, response) => {
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

[**GetAvailableMarkets200Response**](GetAvailableMarkets200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

