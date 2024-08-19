# BhagavadGitaApi.VerseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1ChaptersChapterNumberVersesGet**](VerseApi.md#apiV1ChaptersChapterNumberVersesGet) | **GET** /api/v1/chapters/{chapter_number}/verses | Get all the Verses from a Chapter.
[**apiV1ChaptersChapterNumberVersesVerseNumberGet**](VerseApi.md#apiV1ChaptersChapterNumberVersesVerseNumberGet) | **GET** /api/v1/chapters/{chapter_number}/verses/{verse_number} | Get a particular verse from a chapter.
[**apiV1VersesGet**](VerseApi.md#apiV1VersesGet) | **GET** /api/v1/verses | Get all the Verses.



## apiV1ChaptersChapterNumberVersesGet

> VerseSchema apiV1ChaptersChapterNumberVersesGet(accessToken, chapterNumber, opts)

Get all the Verses from a Chapter.

Get a list of all Verses from a particular Chapter.&lt;br/&gt;

### Example

```javascript
import BhagavadGitaApi from 'bhagavad_gita_api';

let apiInstance = new BhagavadGitaApi.VerseApi();
let accessToken = "accessToken_example"; // String | Your app's access token.
let chapterNumber = 1; // Number | Which Chapter Number to filter?
let opts = {
  'language': "language_example" // String | Language to query. Leave blank for english.
};
apiInstance.apiV1ChaptersChapterNumberVersesGet(accessToken, chapterNumber, opts, (error, data, response) => {
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

[**VerseSchema**](VerseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1ChaptersChapterNumberVersesVerseNumberGet

> VerseSchema apiV1ChaptersChapterNumberVersesVerseNumberGet(accessToken, chapterNumber, verseNumber, opts)

Get a particular verse from a chapter.

Get a specific verse from a specific chapter.&lt;br/&gt;

### Example

```javascript
import BhagavadGitaApi from 'bhagavad_gita_api';

let apiInstance = new BhagavadGitaApi.VerseApi();
let accessToken = "accessToken_example"; // String | Your app's access token.
let chapterNumber = 1; // Number | Which Chapter Number to filter?
let verseNumber = "'1'"; // String | Which Verse Number to filter?
let opts = {
  'language': "language_example" // String | Language to query. Leave blank for english.
};
apiInstance.apiV1ChaptersChapterNumberVersesVerseNumberGet(accessToken, chapterNumber, verseNumber, opts, (error, data, response) => {
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
 **verseNumber** | **String**| Which Verse Number to filter? | [default to &#39;1&#39;]
 **language** | **String**| Language to query. Leave blank for english. | [optional] 

### Return type

[**VerseSchema**](VerseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1VersesGet

> VerseSchema apiV1VersesGet(accessToken, opts)

Get all the Verses.

Get a list of all Verses.&lt;br/&gt;

### Example

```javascript
import BhagavadGitaApi from 'bhagavad_gita_api';

let apiInstance = new BhagavadGitaApi.VerseApi();
let accessToken = "accessToken_example"; // String | Your app's access token.
let opts = {
  'language': "language_example" // String | Language to query. Leave blank for english.
};
apiInstance.apiV1VersesGet(accessToken, opts, (error, data, response) => {
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

[**VerseSchema**](VerseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

