# StarwarsTranslationsApi.StarwarsApi

All URIs are relative to *https://api.funtranslations.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**translateCheunhGet**](StarwarsApi.md#translateCheunhGet) | **GET** /translate/cheunh | 
[**translateGunganGet**](StarwarsApi.md#translateGunganGet) | **GET** /translate/gungan | 
[**translateHutteseGet**](StarwarsApi.md#translateHutteseGet) | **GET** /translate/huttese | 
[**translateMandalorianGet**](StarwarsApi.md#translateMandalorianGet) | **GET** /translate/mandalorian | 
[**translateSithGet**](StarwarsApi.md#translateSithGet) | **GET** /translate/sith | 
[**translateYodaGet**](StarwarsApi.md#translateYodaGet) | **GET** /translate/yoda | 



## translateCheunhGet

> translateCheunhGet(text)



Translate from English to Starwars cheunh.

### Example

```javascript
import StarwarsTranslationsApi from 'starwars_translations_api';
let defaultClient = StarwarsTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new StarwarsTranslationsApi.StarwarsApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateCheunhGet(text, (error, data, response) => {
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


## translateGunganGet

> translateGunganGet(text)



Translate from English to Starwars Gungan Language.

### Example

```javascript
import StarwarsTranslationsApi from 'starwars_translations_api';
let defaultClient = StarwarsTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new StarwarsTranslationsApi.StarwarsApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateGunganGet(text, (error, data, response) => {
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


## translateHutteseGet

> translateHutteseGet(text)



Translate from English to Starwars Huttese Language.

### Example

```javascript
import StarwarsTranslationsApi from 'starwars_translations_api';
let defaultClient = StarwarsTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new StarwarsTranslationsApi.StarwarsApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateHutteseGet(text, (error, data, response) => {
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


## translateMandalorianGet

> translateMandalorianGet(text)



Translate from English to Starwars Mandalorian Language.

### Example

```javascript
import StarwarsTranslationsApi from 'starwars_translations_api';
let defaultClient = StarwarsTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new StarwarsTranslationsApi.StarwarsApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateMandalorianGet(text, (error, data, response) => {
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


## translateSithGet

> translateSithGet(text)



Translate from English to Sith Speak.

### Example

```javascript
import StarwarsTranslationsApi from 'starwars_translations_api';
let defaultClient = StarwarsTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new StarwarsTranslationsApi.StarwarsApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateSithGet(text, (error, data, response) => {
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


## translateYodaGet

> translateYodaGet(text)



Translate from English to Yoda Speak.

### Example

```javascript
import StarwarsTranslationsApi from 'starwars_translations_api';
let defaultClient = StarwarsTranslationsApi.ApiClient.instance;
// Configure API key authorization: X-Funtranslations-Api-Secret
let X-Funtranslations-Api-Secret = defaultClient.authentications['X-Funtranslations-Api-Secret'];
X-Funtranslations-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Funtranslations-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new StarwarsTranslationsApi.StarwarsApi();
let text = "text_example"; // String | Text to translate
apiInstance.translateYodaGet(text, (error, data, response) => {
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

