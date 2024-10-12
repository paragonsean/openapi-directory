# FunTranslationsApi.InternetFADApi

All URIs are relative to *http://api.funtranslations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translateErmahgerdGet**](InternetFADApi.md#translateErmahgerdGet) | **GET** /translate/ermahgerd | 



## translateErmahgerdGet

> translateErmahgerdGet(text)



Translate from English to ERMAHGERD.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.InternetFADApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateErmahgerdGet(text, (error, data, response) => {
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
 **text** | **String**| Text to translate | 

### Return type

null (empty response body)

### Authorization

[X-Funtranslations-Api-Secret](../README.md#X-Funtranslations-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

