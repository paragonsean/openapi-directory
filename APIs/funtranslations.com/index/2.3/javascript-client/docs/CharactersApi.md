# FunTranslationsApi.CharactersApi

All URIs are relative to *http://api.funtranslations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translateChefGet**](CharactersApi.md#translateChefGet) | **GET** /translate/chef | 
[**translateDolanGet**](CharactersApi.md#translateDolanGet) | **GET** /translate/dolan | 
[**translateFerblatinGet**](CharactersApi.md#translateFerblatinGet) | **GET** /translate/ferblatin | 
[**translateFuddGet**](CharactersApi.md#translateFuddGet) | **GET** /translate/fudd | 
[**translateMinionGet**](CharactersApi.md#translateMinionGet) | **GET** /translate/minion | 
[**translatePirateGet**](CharactersApi.md#translatePirateGet) | **GET** /translate/pirate | 



## translateChefGet

> translateChefGet(text)



Translate from English to Swedish Chef speak.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.CharactersApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateChefGet(text, (error, data, response) => {
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


## translateDolanGet

> translateDolanGet(text)



Translate from English to Dolan Speak.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.CharactersApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateDolanGet(text, (error, data, response) => {
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


## translateFerblatinGet

> translateFerblatinGet(text)



Translate from English to Ferb Latin.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.CharactersApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateFerblatinGet(text, (error, data, response) => {
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


## translateFuddGet

> translateFuddGet(text)



Translate from English to Fudd Speak.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.CharactersApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateFuddGet(text, (error, data, response) => {
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


## translateMinionGet

> translateMinionGet(text)



Translate from English to Minion Speak.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.CharactersApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateMinionGet(text, (error, data, response) => {
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


## translatePirateGet

> translatePirateGet(text)



Translate from English to Pirate Speak.

### Example

```javascript
import FunTranslationsApi from 'fun_translations_api';
let defaultClient = FunTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new FunTranslationsApi.CharactersApi();
let text = "text_example"; // String | Text to translate
apiInstance.translatePirateGet(text, (error, data, response) => {
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

