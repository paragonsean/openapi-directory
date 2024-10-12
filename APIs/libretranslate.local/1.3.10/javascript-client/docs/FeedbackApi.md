# LibreTranslate.FeedbackApi

All URIs are relative to *http://libretranslate.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suggestPost**](FeedbackApi.md#suggestPost) | **POST** /suggest | Submit a suggestion to improve a translation



## suggestPost

> SuggestResponse suggestPost()

Submit a suggestion to improve a translation



### Example

```javascript
import LibreTranslate from 'libre_translate';

let apiInstance = new LibreTranslate.FeedbackApi();
apiInstance.suggestPost((error, data, response) => {
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

[**SuggestResponse**](SuggestResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

