# TraktApi.RecommendationsApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMovieRecommendations**](RecommendationsApi.md#getMovieRecommendations) | **GET** /recommendations/movies | Get movie recommendations
[**getShowRecommendations**](RecommendationsApi.md#getShowRecommendations) | **GET** /recommendations/shows | Get show recommendations
[**hideAMovieRecommendation**](RecommendationsApi.md#hideAMovieRecommendation) | **DELETE** /recommendations/movies/{id} | Hide a movie recommendation
[**hideAShowRecommendation**](RecommendationsApi.md#hideAShowRecommendation) | **DELETE** /recommendations/shows/{id} | Hide a show recommendation



## getMovieRecommendations

> getMovieRecommendations(opts)

Get movie recommendations

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info  Movie recommendations for a user. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page. Set &#x60;ignore_collected&#x3D;true&#x60; to filter out movies the user has already collected or &#x60;ignore_watchlisted&#x3D;true&#x60; to filter out movies the user has already watchlisted.  The &#x60;recommended_by&#x60; array contains all users who recommended the item along with any notes they added.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.RecommendationsApi();
let opts = {
  'ignoreCollected': "false", // String | filter out collected movies
  'ignoreWatchlisted': "false", // String | filter out watchlisted movies
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getMovieRecommendations(opts, (error, data, response) => {
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
 **ignoreCollected** | **String**| filter out collected movies | [optional] 
 **ignoreWatchlisted** | **String**| filter out watchlisted movies | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShowRecommendations

> getShowRecommendations(opts)

Get show recommendations

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info  TV show recommendations for a user. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page. Set &#x60;ignore_collected&#x3D;true&#x60; to filter out shows the user has already collected or &#x60;ignore_watchlisted&#x3D;true&#x60; to filter out shows the user has already watchlisted.  The &#x60;recommended_by&#x60; array contains all users who recommended the item along with any notes they added.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.RecommendationsApi();
let opts = {
  'ignoreCollected': "false", // String | filter out collected shows
  'ignoreWatchlisted': "false", // String | filter out watchlisted movies
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getShowRecommendations(opts, (error, data, response) => {
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
 **ignoreCollected** | **String**| filter out collected shows | [optional] 
 **ignoreWatchlisted** | **String**| filter out watchlisted movies | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hideAMovieRecommendation

> hideAMovieRecommendation(id, opts)

Hide a movie recommendation

#### &amp;#128274; OAuth Required  Hide a movie from getting recommended anymore.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.RecommendationsApi();
let id = "922"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.hideAMovieRecommendation(id, opts, (error, data, response) => {
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
 **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## hideAShowRecommendation

> hideAShowRecommendation(id, opts)

Hide a show recommendation

#### &amp;#128274; OAuth Required  Hide a show from getting recommended anymore.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.RecommendationsApi();
let id = "922"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.hideAShowRecommendation(id, opts, (error, data, response) => {
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
 **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

