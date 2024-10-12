# LibreTranslate.TranslateApi

All URIs are relative to *http://libretranslate.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detectPost**](TranslateApi.md#detectPost) | **POST** /detect | Detect the language of a single text
[**languagesGet**](TranslateApi.md#languagesGet) | **GET** /languages | Retrieve list of supported languages
[**translateFilePost**](TranslateApi.md#translateFilePost) | **POST** /translate_file | Translate file from a language to another
[**translatePost**](TranslateApi.md#translatePost) | **POST** /translate | Translate text from a language to another



## detectPost

> [DetectionsInner] detectPost()

Detect the language of a single text



### Example

```javascript
import LibreTranslate from 'libre_translate';

let apiInstance = new LibreTranslate.TranslateApi();
apiInstance.detectPost((error, data, response) => {
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

[**[DetectionsInner]**](DetectionsInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## languagesGet

> [LanguagesInner] languagesGet()

Retrieve list of supported languages



### Example

```javascript
import LibreTranslate from 'libre_translate';

let apiInstance = new LibreTranslate.TranslateApi();
apiInstance.languagesGet((error, data, response) => {
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

[**[LanguagesInner]**](LanguagesInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## translateFilePost

> TranslateFile translateFilePost()

Translate file from a language to another



### Example

```javascript
import LibreTranslate from 'libre_translate';

let apiInstance = new LibreTranslate.TranslateApi();
apiInstance.translateFilePost((error, data, response) => {
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

[**TranslateFile**](TranslateFile.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## translatePost

> Translate translatePost()

Translate text from a language to another



### Example

```javascript
import LibreTranslate from 'libre_translate';

let apiInstance = new LibreTranslate.TranslateApi();
apiInstance.translatePost((error, data, response) => {
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

[**Translate**](Translate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

