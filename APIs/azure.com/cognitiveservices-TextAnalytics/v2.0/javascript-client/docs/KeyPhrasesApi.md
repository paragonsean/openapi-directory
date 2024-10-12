# TextAnalyticsClient.KeyPhrasesApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keyPhrases**](KeyPhrasesApi.md#keyPhrases) | **POST** /keyPhrases | The API returns a list of strings denoting the key talking points in the input text.



## keyPhrases

> KeyPhraseBatchResult keyPhrases(input)

The API returns a list of strings denoting the key talking points in the input text.

See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview#supported-languages\&quot;&gt;Text Analytics Documentation&lt;/a&gt; for details about the languages that are supported by key phrase extraction.

### Example

```javascript
import TextAnalyticsClient from 'text_analytics_client';
let defaultClient = TextAnalyticsClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new TextAnalyticsClient.KeyPhrasesApi();
let input = new TextAnalyticsClient.MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze. Documents can now contain a language field to indicate the text language
apiInstance.keyPhrases(input, (error, data, response) => {
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
 **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. Documents can now contain a language field to indicate the text language | 

### Return type

[**KeyPhraseBatchResult**](KeyPhraseBatchResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

