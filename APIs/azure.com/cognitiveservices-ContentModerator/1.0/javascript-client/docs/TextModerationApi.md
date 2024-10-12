# ContentModeratorClient.TextModerationApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**textModerationDetectLanguage**](TextModerationApi.md#textModerationDetectLanguage) | **POST** /contentmoderator/moderate/v1.0/ProcessText/DetectLanguage | 
[**textModerationScreenText**](TextModerationApi.md#textModerationScreenText) | **POST** /contentmoderator/moderate/v1.0/ProcessText/Screen/ | Detect profanity and match against custom and shared blacklists



## textModerationDetectLanguage

> DetectedLanguage textModerationDetectLanguage(contentType, textContent)



This operation will detect the language of given input content. Returns the &lt;a href&#x3D;\&quot;http://www-01.sil.org/iso639-3/codes.asp\&quot;&gt;ISO 639-3 code&lt;/a&gt; for the predominant language comprising the submitted text. Over 110 languages supported.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.TextModerationApi();
let contentType = "contentType_example"; // String | The content type.
let textContent = {key: null}; // Object | Content to screen.
apiInstance.textModerationDetectLanguage(contentType, textContent, (error, data, response) => {
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
 **contentType** | **String**| The content type. | 
 **textContent** | **Object**| Content to screen. | 

### Return type

[**DetectedLanguage**](DetectedLanguage.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: text/plain, text/html, text/xml, text/markdown
- **Accept**: application/json


## textModerationScreenText

> Screen textModerationScreenText(contentType, textContent, opts)

Detect profanity and match against custom and shared blacklists

Detects profanity in more than 100 languages and match against custom and shared blacklists.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.TextModerationApi();
let contentType = "contentType_example"; // String | The content type.
let textContent = {key: null}; // Object | Content to screen.
let opts = {
  'language': "language_example", // String | Language of the text.
  'autocorrect': false, // Boolean | Autocorrect text.
  'PII': false, // Boolean | Detect personal identifiable information.
  'listId': "listId_example", // String | The list Id.
  'classify': false // Boolean | Classify input.
};
apiInstance.textModerationScreenText(contentType, textContent, opts, (error, data, response) => {
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
 **contentType** | **String**| The content type. | 
 **textContent** | **Object**| Content to screen. | 
 **language** | **String**| Language of the text. | [optional] 
 **autocorrect** | **Boolean**| Autocorrect text. | [optional] [default to false]
 **PII** | **Boolean**| Detect personal identifiable information. | [optional] [default to false]
 **listId** | **String**| The list Id. | [optional] 
 **classify** | **Boolean**| Classify input. | [optional] [default to false]

### Return type

[**Screen**](Screen.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: text/plain, text/html, text/xml, text/markdown
- **Accept**: application/json

