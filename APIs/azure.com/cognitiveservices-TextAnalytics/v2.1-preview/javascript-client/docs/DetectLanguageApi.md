# TextAnalyticsClient.DetectLanguageApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detectLanguage**](DetectLanguageApi.md#detectLanguage) | **POST** /languages | The API returns the detected language and a numeric score between 0 and 1.



## detectLanguage

> LanguageBatchResult detectLanguage(input)

The API returns the detected language and a numeric score between 0 and 1.

Scores close to 1 indicate 100% certainty that the identified language is true. A total of 120 languages are supported.

### Example

```javascript
import TextAnalyticsClient from 'text_analytics_client';
let defaultClient = TextAnalyticsClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new TextAnalyticsClient.DetectLanguageApi();
let input = new TextAnalyticsClient.BatchInput(); // BatchInput | Collection of documents to analyze.
apiInstance.detectLanguage(input, (error, data, response) => {
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
 **input** | [**BatchInput**](BatchInput.md)| Collection of documents to analyze. | 

### Return type

[**LanguageBatchResult**](LanguageBatchResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

