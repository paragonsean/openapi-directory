# ShakespeareApi.TranslationApi

All URIs are relative to *http://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shakespeareTranslateGet**](TranslationApi.md#shakespeareTranslateGet) | **GET** /shakespeare/translate | 



## shakespeareTranslateGet

> shakespeareTranslateGet(text)



Translate from English to Shakespeare English.

### Example

```javascript
import ShakespeareApi from 'shakespeare_api';
let defaultClient = ShakespeareApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new ShakespeareApi.TranslationApi();
let text = "text_example"; // String | Text to translate to Shakespeare English.
apiInstance.shakespeareTranslateGet(text, (error, data, response) => {
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
 **text** | **String**| Text to translate to Shakespeare English. | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

