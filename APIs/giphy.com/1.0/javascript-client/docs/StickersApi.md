# GiphyApi.StickersApi

All URIs are relative to *https://api.giphy.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**randomSticker**](StickersApi.md#randomSticker) | **GET** /stickers/random | Random Sticker
[**searchStickers**](StickersApi.md#searchStickers) | **GET** /stickers/search | Search Stickers
[**translateSticker**](StickersApi.md#translateSticker) | **GET** /stickers/translate | Translate phrase to Sticker
[**trendingStickers**](StickersApi.md#trendingStickers) | **GET** /stickers/trending | Trending Stickers



## randomSticker

> RandomGif200Response randomSticker(opts)

Random Sticker

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

let apiInstance = new GiphyApi.StickersApi();
let opts = {
  'tag': "tag_example", // String | Filters results by specified tag.
  'rating': "rating_example" // String | Filters results by specified rating.
};
apiInstance.randomSticker(opts, (error, data, response) => {
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


## searchStickers

> GetGifsById200Response searchStickers(q, opts)

Search Stickers

Replicates the functionality and requirements of the classic GIPHY search, but returns animated stickers rather than GIFs. 

### Example

```javascript
import GiphyApi from 'giphy_api';
let defaultClient = GiphyApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GiphyApi.StickersApi();
let q = "q_example"; // String | Search query term or prhase.
let opts = {
  'limit': 25, // Number | The maximum number of records to return.
  'offset': 0, // Number | An optional results offset.
  'rating': "rating_example", // String | Filters results by specified rating.
  'lang': "lang_example" // String | Specify default language for regional content; use a 2-letter ISO 639-1 language code.
};
apiInstance.searchStickers(q, opts, (error, data, response) => {
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


## translateSticker

> RandomGif200Response translateSticker(s)

Translate phrase to Sticker

The translate API draws on search, but uses the GIPHY &#x60;special sauce&#x60; to handle translating from one vocabulary to another. In this case, words and phrases to GIFs. 

### Example

```javascript
import GiphyApi from 'giphy_api';
let defaultClient = GiphyApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GiphyApi.StickersApi();
let s = "s_example"; // String | Search term.
apiInstance.translateSticker(s, (error, data, response) => {
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


## trendingStickers

> GetGifsById200Response trendingStickers(opts)

Trending Stickers

Fetch Stickers currently trending online. Hand curated by the GIPHY editorial team. Returns 25 results by default. 

### Example

```javascript
import GiphyApi from 'giphy_api';
let defaultClient = GiphyApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GiphyApi.StickersApi();
let opts = {
  'limit': 25, // Number | The maximum number of records to return.
  'offset': 0, // Number | An optional results offset.
  'rating': "rating_example" // String | Filters results by specified rating.
};
apiInstance.trendingStickers(opts, (error, data, response) => {
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

