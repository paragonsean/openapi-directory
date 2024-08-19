# SpotifyWebApiWithFixesAndImprovementsFromSonallux.ChaptersApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAChapter**](ChaptersApi.md#getAChapter) | **GET** /chapters/{id} | Get a Chapter 
[**getAudiobookChapters_0**](ChaptersApi.md#getAudiobookChapters_0) | **GET** /audiobooks/{id}/chapters | Get Audiobook Chapters 
[**getSeveralChapters**](ChaptersApi.md#getSeveralChapters) | **GET** /chapters | Get Several Chapters 



## getAChapter

> ChapterObject getAChapter(id, opts)

Get a Chapter 

Get Spotify catalog information for a single chapter.&lt;br /&gt; **Note: Chapters are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ChaptersApi();
let id = "0D5wENdkdwbqlrHoaJ9g29"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getAChapter(id, opts, (error, data, response) => {
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

[**ChapterObject**](ChapterObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAudiobookChapters_0

> PagingSimplifiedChapterObject getAudiobookChapters_0(id, opts)

Get Audiobook Chapters 

Get Spotify catalog information about an audiobook&#39;s chapters.&lt;br /&gt; **Note: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ChaptersApi();
let id = "7iHfbu1YPACw6oZPAFJtqe"; // String | 
let opts = {
  'market': "ES", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getAudiobookChapters_0(id, opts, (error, data, response) => {
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


## getSeveralChapters

> GetSeveralChapters200Response getSeveralChapters(ids, opts)

Get Several Chapters 

Get Spotify catalog information for several chapters identified by their Spotify IDs.&lt;br /&gt; **Note: Chapters are only available for the US, UK, Ireland, New Zealand and Australia markets.** 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ChaptersApi();
let ids = "0IsXVP0JmcB2adSE338GkK,3ZXb8FKZGU0EHALYX6uCzU,0D5wENdkdwbqlrHoaJ9g29"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getSeveralChapters(ids, opts, (error, data, response) => {
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

[**GetSeveralChapters200Response**](GetSeveralChapters200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

