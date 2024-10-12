# TranslationApi.LanguageApi

All URIs are relative to *https://api.ebay.com/commerce/translation/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translate**](LanguageApi.md#translate) | **POST** /translate | 



## translate

> TranslateResponse translate(translateRequest)



Translates input text inot a given language.

### Example

```javascript
import TranslationApi from 'translation_api';
let defaultClient = TranslationApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TranslationApi.LanguageApi();
let translateRequest = new TranslationApi.TranslateRequest(); // TranslateRequest | 
apiInstance.translate(translateRequest, (error, data, response) => {
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
 **translateRequest** | [**TranslateRequest**](TranslateRequest.md)|  | 

### Return type

[**TranslateResponse**](TranslateResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

