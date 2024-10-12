# JellyfinApi.ItemLookupApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applySearchCriteria**](ItemLookupApi.md#applySearchCriteria) | **POST** /Items/RemoteSearch/Apply/{itemId} | Applies search criteria to an item and refreshes metadata.
[**getBookRemoteSearchResults**](ItemLookupApi.md#getBookRemoteSearchResults) | **POST** /Items/RemoteSearch/Book | Get book remote search.
[**getBoxSetRemoteSearchResults**](ItemLookupApi.md#getBoxSetRemoteSearchResults) | **POST** /Items/RemoteSearch/BoxSet | Get box set remote search.
[**getExternalIdInfos**](ItemLookupApi.md#getExternalIdInfos) | **GET** /Items/{itemId}/ExternalIdInfos | Get the item&#39;s external id info.
[**getMovieRemoteSearchResults**](ItemLookupApi.md#getMovieRemoteSearchResults) | **POST** /Items/RemoteSearch/Movie | Get movie remote search.
[**getMusicAlbumRemoteSearchResults**](ItemLookupApi.md#getMusicAlbumRemoteSearchResults) | **POST** /Items/RemoteSearch/MusicAlbum | Get music album remote search.
[**getMusicArtistRemoteSearchResults**](ItemLookupApi.md#getMusicArtistRemoteSearchResults) | **POST** /Items/RemoteSearch/MusicArtist | Get music artist remote search.
[**getMusicVideoRemoteSearchResults**](ItemLookupApi.md#getMusicVideoRemoteSearchResults) | **POST** /Items/RemoteSearch/MusicVideo | Get music video remote search.
[**getPersonRemoteSearchResults**](ItemLookupApi.md#getPersonRemoteSearchResults) | **POST** /Items/RemoteSearch/Person | Get person remote search.
[**getRemoteSearchImage**](ItemLookupApi.md#getRemoteSearchImage) | **GET** /Items/RemoteSearch/Image | Gets a remote image.
[**getSeriesRemoteSearchResults**](ItemLookupApi.md#getSeriesRemoteSearchResults) | **POST** /Items/RemoteSearch/Series | Get series remote search.
[**getTrailerRemoteSearchResults**](ItemLookupApi.md#getTrailerRemoteSearchResults) | **POST** /Items/RemoteSearch/Trailer | Get trailer remote search.



## applySearchCriteria

> applySearchCriteria(itemId, remoteSearchResult, opts)

Applies search criteria to an item and refreshes metadata.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let itemId = "itemId_example"; // String | Item id.
let remoteSearchResult = new JellyfinApi.RemoteSearchResult(); // RemoteSearchResult | The remote search result.
let opts = {
  'replaceAllImages': true // Boolean | Optional. Whether or not to replace all images. Default: True.
};
apiInstance.applySearchCriteria(itemId, remoteSearchResult, opts, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 
 **remoteSearchResult** | [**RemoteSearchResult**](RemoteSearchResult.md)| The remote search result. | 
 **replaceAllImages** | **Boolean**| Optional. Whether or not to replace all images. Default: True. | [optional] [default to true]

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## getBookRemoteSearchResults

> [RemoteSearchResult] getBookRemoteSearchResults(bookInfoRemoteSearchQuery)

Get book remote search.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let bookInfoRemoteSearchQuery = new JellyfinApi.BookInfoRemoteSearchQuery(); // BookInfoRemoteSearchQuery | Remote search query.
apiInstance.getBookRemoteSearchResults(bookInfoRemoteSearchQuery, (error, data, response) => {
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
 **bookInfoRemoteSearchQuery** | [**BookInfoRemoteSearchQuery**](BookInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getBoxSetRemoteSearchResults

> [RemoteSearchResult] getBoxSetRemoteSearchResults(boxSetInfoRemoteSearchQuery)

Get box set remote search.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let boxSetInfoRemoteSearchQuery = new JellyfinApi.BoxSetInfoRemoteSearchQuery(); // BoxSetInfoRemoteSearchQuery | Remote search query.
apiInstance.getBoxSetRemoteSearchResults(boxSetInfoRemoteSearchQuery, (error, data, response) => {
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
 **boxSetInfoRemoteSearchQuery** | [**BoxSetInfoRemoteSearchQuery**](BoxSetInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getExternalIdInfos

> [ExternalIdInfo] getExternalIdInfos(itemId)

Get the item&#39;s external id info.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let itemId = "itemId_example"; // String | Item id.
apiInstance.getExternalIdInfos(itemId, (error, data, response) => {
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
 **itemId** | **String**| Item id. | 

### Return type

[**[ExternalIdInfo]**](ExternalIdInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getMovieRemoteSearchResults

> [RemoteSearchResult] getMovieRemoteSearchResults(movieInfoRemoteSearchQuery)

Get movie remote search.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let movieInfoRemoteSearchQuery = new JellyfinApi.MovieInfoRemoteSearchQuery(); // MovieInfoRemoteSearchQuery | Remote search query.
apiInstance.getMovieRemoteSearchResults(movieInfoRemoteSearchQuery, (error, data, response) => {
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
 **movieInfoRemoteSearchQuery** | [**MovieInfoRemoteSearchQuery**](MovieInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getMusicAlbumRemoteSearchResults

> [RemoteSearchResult] getMusicAlbumRemoteSearchResults(albumInfoRemoteSearchQuery)

Get music album remote search.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let albumInfoRemoteSearchQuery = new JellyfinApi.AlbumInfoRemoteSearchQuery(); // AlbumInfoRemoteSearchQuery | Remote search query.
apiInstance.getMusicAlbumRemoteSearchResults(albumInfoRemoteSearchQuery, (error, data, response) => {
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
 **albumInfoRemoteSearchQuery** | [**AlbumInfoRemoteSearchQuery**](AlbumInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getMusicArtistRemoteSearchResults

> [RemoteSearchResult] getMusicArtistRemoteSearchResults(artistInfoRemoteSearchQuery)

Get music artist remote search.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let artistInfoRemoteSearchQuery = new JellyfinApi.ArtistInfoRemoteSearchQuery(); // ArtistInfoRemoteSearchQuery | Remote search query.
apiInstance.getMusicArtistRemoteSearchResults(artistInfoRemoteSearchQuery, (error, data, response) => {
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
 **artistInfoRemoteSearchQuery** | [**ArtistInfoRemoteSearchQuery**](ArtistInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getMusicVideoRemoteSearchResults

> [RemoteSearchResult] getMusicVideoRemoteSearchResults(musicVideoInfoRemoteSearchQuery)

Get music video remote search.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let musicVideoInfoRemoteSearchQuery = new JellyfinApi.MusicVideoInfoRemoteSearchQuery(); // MusicVideoInfoRemoteSearchQuery | Remote search query.
apiInstance.getMusicVideoRemoteSearchResults(musicVideoInfoRemoteSearchQuery, (error, data, response) => {
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
 **musicVideoInfoRemoteSearchQuery** | [**MusicVideoInfoRemoteSearchQuery**](MusicVideoInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPersonRemoteSearchResults

> [RemoteSearchResult] getPersonRemoteSearchResults(personLookupInfoRemoteSearchQuery)

Get person remote search.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let personLookupInfoRemoteSearchQuery = new JellyfinApi.PersonLookupInfoRemoteSearchQuery(); // PersonLookupInfoRemoteSearchQuery | Remote search query.
apiInstance.getPersonRemoteSearchResults(personLookupInfoRemoteSearchQuery, (error, data, response) => {
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
 **personLookupInfoRemoteSearchQuery** | [**PersonLookupInfoRemoteSearchQuery**](PersonLookupInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRemoteSearchImage

> File getRemoteSearchImage(imageUrl, providerName)

Gets a remote image.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let imageUrl = "imageUrl_example"; // String | The image url.
let providerName = "providerName_example"; // String | The provider name.
apiInstance.getRemoteSearchImage(imageUrl, providerName, (error, data, response) => {
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
 **imageUrl** | **String**| The image url. | 
 **providerName** | **String**| The provider name. | 

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*


## getSeriesRemoteSearchResults

> [RemoteSearchResult] getSeriesRemoteSearchResults(seriesInfoRemoteSearchQuery)

Get series remote search.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let seriesInfoRemoteSearchQuery = new JellyfinApi.SeriesInfoRemoteSearchQuery(); // SeriesInfoRemoteSearchQuery | Remote search query.
apiInstance.getSeriesRemoteSearchResults(seriesInfoRemoteSearchQuery, (error, data, response) => {
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
 **seriesInfoRemoteSearchQuery** | [**SeriesInfoRemoteSearchQuery**](SeriesInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getTrailerRemoteSearchResults

> [RemoteSearchResult] getTrailerRemoteSearchResults(trailerInfoRemoteSearchQuery)

Get trailer remote search.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.ItemLookupApi();
let trailerInfoRemoteSearchQuery = new JellyfinApi.TrailerInfoRemoteSearchQuery(); // TrailerInfoRemoteSearchQuery | Remote search query.
apiInstance.getTrailerRemoteSearchResults(trailerInfoRemoteSearchQuery, (error, data, response) => {
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
 **trailerInfoRemoteSearchQuery** | [**TrailerInfoRemoteSearchQuery**](TrailerInfoRemoteSearchQuery.md)| Remote search query. | 

### Return type

[**[RemoteSearchResult]**](RemoteSearchResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

