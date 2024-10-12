# FunTranslationsApi.MorseApi

All URIs are relative to *http://api.funtranslations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translateMorse2englishGet**](MorseApi.md#translateMorse2englishGet) | **GET** /translate/morse2english | 
[**translateMorseAudioGet**](MorseApi.md#translateMorseAudioGet) | **GET** /translate/morse/audio | 
[**translateMorseGet**](MorseApi.md#translateMorseGet) | **GET** /translate/morse | 



## translateMorse2englishGet

> translateMorse2englishGet(text)



Translate from Morse code to English.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.MorseApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateMorse2englishGet(text, (error, data, response) => {
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


## translateMorseAudioGet

> translateMorseAudioGet(text, speed, tone)



Translate from English to morse code and get the result as an audio file.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.MorseApi();
let text = "text_example"; // String | Text to translate
let speed = 56; // Number | Audio Speed (Words/Minute)
let tone = 56; // Number | Audio Tone Frequency(Hz)
apiInstance.translateMorseAudioGet(text, speed, tone, (error, data, response) => {
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
 **speed** | **Number**| Audio Speed (Words/Minute) | 
 **tone** | **Number**| Audio Tone Frequency(Hz) | 

### Return type

null (empty response body)

### Authorization

[X-Funtranslations-Api-Secret](../README.md#X-Funtranslations-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## translateMorseGet

> translateMorseGet(text)



Translate from English to morse code.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.MorseApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateMorseGet(text, (error, data, response) => {
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

