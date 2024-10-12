# GiphyApi.GifsApi

All URIs are relative to *https://api.giphy.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGifById**](GifsApi.md#getGifById) | **GET** /gifs/{gifId} | Get GIF by Id
[**getGifsById**](GifsApi.md#getGifsById) | **GET** /gifs | Get GIFs by ID
[**randomGif**](GifsApi.md#randomGif) | **GET** /gifs/random | Random GIF
[**searchGifs**](GifsApi.md#searchGifs) | **GET** /gifs/search | Search GIFs
[**translateGif**](GifsApi.md#translateGif) | **GET** /gifs/translate | Translate phrase to GIF
[**trendingGifs**](GifsApi.md#trendingGifs) | **GET** /gifs/trending | Trending GIFs



## getGifById

> RandomGif200Response getGifById(gifId)

Get GIF by Id

Returns a GIF given that GIF&#39;s unique ID 

### Example

```javascript
import GiphyApi from 'giphy_api';
let defaultClient = GiphyApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GiphyApi.GifsApi();
let gifId = 56; // Number | Filters results by specified GIF ID.
apiInstance.getGifById(gifId, (error, data, response) => {
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
 **gifId** | **Number**| Filters results by specified GIF ID. | 

### Return type

[**RandomGif200Response**](RandomGif200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGifsById

> GetGifsById200Response getGifsById(opts)

Get GIFs by ID

A multiget version of the get GIF by ID endpoint. 

### Example

```javascript
import GiphyApi from 'giphy_api';
let defaultClient = GiphyApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GiphyApi.GifsApi();
let opts = {
  'ids': "ids_example" // String | Filters results by specified GIF IDs, separated by commas.
};
apiInstance.getGifsById(opts, (error, data, response) => {
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
 **ids** | **String**| Filters results by specified GIF IDs, separated by commas. | [optional] 

### Return type

[**GetGifsById200Response**](GetGifsById200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## randomGif

> RandomGif200Response randomGif(opts)

Random GIF

Returns a random GIF, limited by tag. Excluding the tag parameter will return a random GIF from the GIPHY catalog. 

### Example

```javascript
import GiphyApi from 'giphy_api';
let defaultClient = GiphyApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GiphyApi.GifsApi();
let opts = {
  'tag': "tag_example", // String | Filters results by specified tag.
  'rating': "rating_example" // String | Filters results by specified rating.
};
apiInstance.randomGif(opts, (error, data, response) => {
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
 **tag** | **String**| Filters results by specified tag. | [optional] 
 **rating** | **String**| Filters results by specified rating. | [optional] 

### Return type

[**RandomGif200Response**](RandomGif200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchGifs

> GetGifsById200Response searchGifs(q, opts)

Search GIFs

Search all GIPHY GIFs for a word or phrase. Punctuation will be stripped and ignored.  Use a plus or url encode for phrases. Example paul+rudd, ryan+gosling or american+psycho. 

### Example

```javascript
import GiphyApi from 'giphy_api';
let defaultClient = GiphyApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GiphyApi.GifsApi();
let q = "q_example"; // String | Search query term or prhase.
let opts = {
  'limit': 25, // Number | The maximum number of records to return.
  'offset': 0, // Number | An optional results offset.
  'rating': "rating_example", // String | Filters results by specified rating.
  'lang': "lang_example" // String | Specify default language for regional content; use a 2-letter ISO 639-1 language code.
};
apiInstance.searchGifs(q, opts, (error, data, response) => {
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
 **q** | **String**| Search query term or prhase. | 
 **limit** | **Number**| The maximum number of records to return. | [optional] [default to 25]
 **offset** | **Number**| An optional results offset. | [optional] [default to 0]
 **rating** | **String**| Filters results by specified rating. | [optional] 
 **lang** | **String**| Specify default language for regional content; use a 2-letter ISO 639-1 language code. | [optional] 

### Return type

[**GetGifsById200Response**](GetGifsById200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## translateGif

> RandomGif200Response translateGif(s)

Translate phrase to GIF

The translate API draws on search, but uses the GIPHY &#x60;special sauce&#x60; to handle translating from one vocabulary to another. In this case, words and phrases to GIF 

### Example

```javascript
import GiphyApi from 'giphy_api';
let defaultClient = GiphyApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GiphyApi.GifsApi();
let s = "s_example"; // String | Search term.
apiInstance.translateGif(s, (error, data, response) => {
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
 **s** | **String**| Search term. | 

### Return type

[**RandomGif200Response**](RandomGif200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trendingGifs

> GetGifsById200Response trendingGifs(opts)

Trending GIFs

Fetch GIFs currently trending online. Hand curated by the GIPHY editorial team.  The data returned mirrors the GIFs showcased on the GIPHY homepage. Returns 25 results by default. 

### Example

```javascript
import GiphyApi from 'giphy_api';
let defaultClient = GiphyApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GiphyApi.GifsApi();
let opts = {
  'limit': 25, // Number | The maximum number of records to return.
  'offset': 0, // Number | An optional results offset.
  'rating': "rating_example" // String | Filters results by specified rating.
};
apiInstance.trendingGifs(opts, (error, data, response) => {
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
 **limit** | **Number**| The maximum number of records to return. | [optional] [default to 25]
 **offset** | **Number**| An optional results offset. | [optional] [default to 0]
 **rating** | **String**| Filters results by specified rating. | [optional] 

### Return type

[**GetGifsById200Response**](GetGifsById200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

