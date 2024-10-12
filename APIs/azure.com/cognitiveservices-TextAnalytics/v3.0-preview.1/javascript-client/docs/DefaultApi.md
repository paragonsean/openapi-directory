# TextAnalyticsClient.DefaultApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entitiesLinking**](DefaultApi.md#entitiesLinking) | **POST** /entities/linking | Linked entities from a well-known knowledge base
[**entitiesRecognitionGeneral**](DefaultApi.md#entitiesRecognitionGeneral) | **POST** /entities/recognition/general | Named Entity Recognition
[**entitiesRecognitionPii**](DefaultApi.md#entitiesRecognitionPii) | **POST** /entities/recognition/pii | Entities containing personal information
[**keyPhrases**](DefaultApi.md#keyPhrases) | **POST** /keyPhrases | Key Phrases
[**languages**](DefaultApi.md#languages) | **POST** /languages | Detect Language
[**sentiment**](DefaultApi.md#sentiment) | **POST** /sentiment | Sentiment



## entitiesLinking

> EntityLinkingResult entitiesLinking(input, opts)

Linked entities from a well-known knowledge base

The API returns a list of recognized entities with links to a well-known knowledge base. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example

```javascript
import TextAnalyticsClient from 'text_analytics_client';
let defaultClient = TextAnalyticsClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new TextAnalyticsClient.DefaultApi();
let input = new TextAnalyticsClient.MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze.
let opts = {
  'modelVersion': "modelVersion_example", // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
  'showStats': true // Boolean | (Optional) if set to true, response will contain input and document level statistics.
};
apiInstance.entitiesLinking(input, opts, (error, data, response) => {
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
 **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. | 
 **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] 
 **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] 

### Return type

[**EntityLinkingResult**](EntityLinkingResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## entitiesRecognitionGeneral

> EntitiesResult entitiesRecognitionGeneral(input, opts)

Named Entity Recognition

The API returns a list of general named entities in a given document. For the list of supported entity types, check &lt;a href&#x3D;\&quot;https://aka.ms/taner\&quot;&gt;Supported Entity Types in Text Analytics API&lt;/a&gt;. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example

```javascript
import TextAnalyticsClient from 'text_analytics_client';
let defaultClient = TextAnalyticsClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new TextAnalyticsClient.DefaultApi();
let input = new TextAnalyticsClient.MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze.
let opts = {
  'modelVersion': "modelVersion_example", // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
  'showStats': true // Boolean | (Optional) if set to true, response will contain input and document level statistics.
};
apiInstance.entitiesRecognitionGeneral(input, opts, (error, data, response) => {
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
 **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. | 
 **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] 
 **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] 

### Return type

[**EntitiesResult**](EntitiesResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## entitiesRecognitionPii

> EntitiesResult entitiesRecognitionPii(input, opts)

Entities containing personal information

The API returns a list of entities with personal information (\\\&quot;SSN\\\&quot;, \\\&quot;Bank Account\\\&quot; etc) in the document. For the list of supported entity types, check &lt;a href&#x3D;\&quot;https://aka.ms/tanerpii\&quot;&gt;Supported Entity Types in Text Analytics API&lt;/a&gt;. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages. 

### Example

```javascript
import TextAnalyticsClient from 'text_analytics_client';
let defaultClient = TextAnalyticsClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new TextAnalyticsClient.DefaultApi();
let input = new TextAnalyticsClient.MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze.
let opts = {
  'modelVersion': "modelVersion_example", // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
  'showStats': true // Boolean | (Optional) if set to true, response will contain input and document level statistics.
};
apiInstance.entitiesRecognitionPii(input, opts, (error, data, response) => {
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
 **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. | 
 **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] 
 **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] 

### Return type

[**EntitiesResult**](EntitiesResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## keyPhrases

> KeyPhraseResult keyPhrases(input, opts)

Key Phrases

The API returns a list of strings denoting the key phrases in the input text. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example

```javascript
import TextAnalyticsClient from 'text_analytics_client';
let defaultClient = TextAnalyticsClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new TextAnalyticsClient.DefaultApi();
let input = new TextAnalyticsClient.MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze. Documents can now contain a language field to indicate the text language
let opts = {
  'modelVersion': "modelVersion_example", // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
  'showStats': true // Boolean | (Optional) if set to true, response will contain input and document level statistics.
};
apiInstance.keyPhrases(input, opts, (error, data, response) => {
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
 **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] 
 **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] 

### Return type

[**KeyPhraseResult**](KeyPhraseResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## languages

> LanguageResult languages(input, opts)

Detect Language

The API returns the detected language and a numeric score between 0 and 1. Scores close to 1 indicate 100% certainty that the identified language is true. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example

```javascript
import TextAnalyticsClient from 'text_analytics_client';
let defaultClient = TextAnalyticsClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new TextAnalyticsClient.DefaultApi();
let input = new TextAnalyticsClient.LanguageBatchInput(); // LanguageBatchInput | Collection of documents to analyze.
let opts = {
  'modelVersion': "modelVersion_example", // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
  'showStats': true // Boolean | (Optional) if set to true, response will contain input and document level statistics.
};
apiInstance.languages(input, opts, (error, data, response) => {
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
 **input** | [**LanguageBatchInput**](LanguageBatchInput.md)| Collection of documents to analyze. | 
 **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] 
 **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] 

### Return type

[**LanguageResult**](LanguageResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## sentiment

> SentimentResponse sentiment(input, opts)

Sentiment

The API returns a sentiment prediction, as well as sentiment scores for each sentiment class (Positive, Negative, and Neutral) for the document and each sentence within it. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example

```javascript
import TextAnalyticsClient from 'text_analytics_client';
let defaultClient = TextAnalyticsClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new TextAnalyticsClient.DefaultApi();
let input = new TextAnalyticsClient.MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze.
let opts = {
  'modelVersion': "modelVersion_example", // String | (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
  'showStats': true // Boolean | (Optional) if set to true, response will contain input and document level statistics.
};
apiInstance.sentiment(input, opts, (error, data, response) => {
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
 **input** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. | 
 **modelVersion** | **String**| (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version.  | [optional] 
 **showStats** | **Boolean**| (Optional) if set to true, response will contain input and document level statistics. | [optional] 

### Return type

[**SentimentResponse**](SentimentResponse.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

