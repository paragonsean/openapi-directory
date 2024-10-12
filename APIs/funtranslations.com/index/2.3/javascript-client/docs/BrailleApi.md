# FunTranslationsApi.BrailleApi

All URIs are relative to *http://api.funtranslations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translateBrailleDotsGet**](BrailleApi.md#translateBrailleDotsGet) | **GET** /translate/braille/dots | 
[**translateBrailleGet**](BrailleApi.md#translateBrailleGet) | **GET** /translate/braille | 
[**translateBrailleHtmlGet**](BrailleApi.md#translateBrailleHtmlGet) | **GET** /translate/braille/html | 
[**translateBrailleImageGet**](BrailleApi.md#translateBrailleImageGet) | **GET** /translate/braille/image | 
[**translateBrailleUnicodeGet**](BrailleApi.md#translateBrailleUnicodeGet) | **GET** /translate/braille/unicode | 



## translateBrailleDotsGet

> translateBrailleDotsGet(text)



Use this to see which dots are enabled for each Braille letters. This is highly educational (to see which dots are enabled) and can potentially drive a non braille display which works on individual dots.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.BrailleApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateBrailleDotsGet(text, (error, data, response) => {
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


## translateBrailleGet

> translateBrailleGet(text)



Translate from English to Braille. This is what you use if you have a braille display. This API translates the English text into characters that a braille display understands and you can feed the translated text directly to the display.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.BrailleApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateBrailleGet(text, (error, data, response) => {
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


## translateBrailleHtmlGet

> translateBrailleHtmlGet(text)



Translate from English to Braille Image characters. This is probably what you want to use if you are displaying braille in a browser.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.BrailleApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateBrailleHtmlGet(text, (error, data, response) => {
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


## translateBrailleImageGet

> translateBrailleImageGet(text)



Translate from English to Braille image characters. This is probably what you want to use if you are displaying braille in a browser.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.BrailleApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateBrailleImageGet(text, (error, data, response) => {
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


## translateBrailleUnicodeGet

> translateBrailleUnicodeGet(text)



Translate from English to Braille Unicode characters.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.BrailleApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateBrailleUnicodeGet(text, (error, data, response) => {
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

