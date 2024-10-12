# ErskineMayApi.ChapterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiChapterChapterNumberGet**](ChapterApi.md#apiChapterChapterNumberGet) | **GET** /api/Chapter/{chapterNumber} | Returns a single chapter overview by chapter number.



## apiChapterChapterNumberGet

> ErskineMayChapterOverview apiChapterChapterNumberGet(chapterNumber)

Returns a single chapter overview by chapter number.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.ChapterApi();
let chapterNumber = 56; // Number | Chapter overview with the chapter number specified
apiInstance.apiChapterChapterNumberGet(chapterNumber, (error, data, response) => {
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
 **chapterNumber** | **Number**| Chapter overview with the chapter number specified | 

### Return type

[**ErskineMayChapterOverview**](ErskineMayChapterOverview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

