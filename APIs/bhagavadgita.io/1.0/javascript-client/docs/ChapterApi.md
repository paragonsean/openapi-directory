# BhagavadGitaApi.ChapterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1ChaptersChapterNumberGet**](ChapterApi.md#apiV1ChaptersChapterNumberGet) | **GET** /api/v1/chapters/{chapter_number} | Get a specific chapter from the Bhagavad Gita.
[**apiV1ChaptersGet**](ChapterApi.md#apiV1ChaptersGet) | **GET** /api/v1/chapters | Get all the 18 Chapters of the Bhagavad Gita.



## apiV1ChaptersChapterNumberGet

> ChapterSchema apiV1ChaptersChapterNumberGet(accessToken, chapterNumber, opts)

Get a specific chapter from the Bhagavad Gita.

Get information about a specific chapter from the Bhagavad Gita.&lt;br/&gt;

### Example

```javascript
import BhagavadGitaApi from 'bhagavad_gita_api';

let apiInstance = new BhagavadGitaApi.ChapterApi();
let accessToken = "accessToken_example"; // String | Your app's access token.
let chapterNumber = 1; // Number | Which Chapter Number to filter?
let opts = {
  'language': "language_example" // String | Language to query. Leave blank for english.
};
apiInstance.apiV1ChaptersChapterNumberGet(accessToken, chapterNumber, opts, (error, data, response) => {
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
 **accessToken** | **String**| Your app&#39;s access token. | 
 **chapterNumber** | **Number**| Which Chapter Number to filter? | [default to 1]
 **language** | **String**| Language to query. Leave blank for english. | [optional] 

### Return type

[**ChapterSchema**](ChapterSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1ChaptersGet

> ChapterSchema apiV1ChaptersGet(accessToken, opts)

Get all the 18 Chapters of the Bhagavad Gita.

Get a list of all the 18 Chapters of the Bhagavad Gita.&lt;br/&gt;

### Example

```javascript
import BhagavadGitaApi from 'bhagavad_gita_api';

let apiInstance = new BhagavadGitaApi.ChapterApi();
let accessToken = "accessToken_example"; // String | Your app's access token.
let opts = {
  'language': "language_example" // String | Language to query. Leave blank for english.
};
apiInstance.apiV1ChaptersGet(accessToken, opts, (error, data, response) => {
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
 **accessToken** | **String**| Your app&#39;s access token. | 
 **language** | **String**| Language to query. Leave blank for english. | [optional] 

### Return type

[**ChapterSchema**](ChapterSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

