# LanguageIdentificationPrediction.DefaultApi

All URIs are relative to *https://language-identification-prediction.p.rapidapi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recognizeLanguagePost**](DefaultApi.md#recognizeLanguagePost) | **POST** /recognize-language/ | Recognize Language



## recognizeLanguagePost

> recognizeLanguagePost(xRapidAPIHost, xRapidAPIKey, text)

Recognize Language

### Example

```javascript
import LanguageIdentificationPrediction from 'language_identification__prediction';

let apiInstance = new LanguageIdentificationPrediction.DefaultApi();
let xRapidAPIHost = "'language-identification-prediction.p.rapidapi.com'"; // String | 
let xRapidAPIKey = "xRapidAPIKey_example"; // String | 
let text = "text_example"; // String | text
apiInstance.recognizeLanguagePost(xRapidAPIHost, xRapidAPIKey, text, (error, data, response) => {
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
 **xRapidAPIHost** | **String**|  | [default to &#39;language-identification-prediction.p.rapidapi.com&#39;]
 **xRapidAPIKey** | **String**|  | 
 **text** | **String**| text | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
- **Accept**: Not defined

