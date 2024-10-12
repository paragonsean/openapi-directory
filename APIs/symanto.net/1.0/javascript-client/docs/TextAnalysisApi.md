# PsycholinguisticTextAnalytics.TextAnalysisApi

All URIs are relative to *https://api.symanto.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**communication**](TextAnalysisApi.md#communication) | **POST** /communication | Communication &amp; Tonality
[**ekmanEmotion**](TextAnalysisApi.md#ekmanEmotion) | **POST** /ekman-emotion | Emotion Analysis
[**emotion**](TextAnalysisApi.md#emotion) | **POST** /emotion | Emotion Analysis
[**languageDetection**](TextAnalysisApi.md#languageDetection) | **POST** /language-detection | Language Detection
[**personality**](TextAnalysisApi.md#personality) | **POST** /personality | Personality Traits
[**sentiment**](TextAnalysisApi.md#sentiment) | **POST** /sentiment | Sentiment Analysis
[**topicSentiment**](TextAnalysisApi.md#topicSentiment) | **POST** /topic-sentiment | Extracts topics and sentiments and relates them.



## communication

> [PostPredicted] communication(opts)

Communication &amp; Tonality

Identify the purpose and writing style of a written text.  Supported Languages: [&#x60;ar&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;it&#x60;, &#x60;nl&#x60;, &#x60;pt&#x60;, &#x60;ru&#x60;, &#x60;tr&#x60;, &#x60;zh&#x60;]  Returned labels: * action-seeking * fact-oriented * information-seeking * self-revealing

### Example

```javascript
import PsycholinguisticTextAnalytics from 'psycholinguistic_text_analytics';
let defaultClient = PsycholinguisticTextAnalytics.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new PsycholinguisticTextAnalytics.TextAnalysisApi();
let opts = {
  'all': false, // Boolean | 
  'post': [new PsycholinguisticTextAnalytics.Post()] // [Post] | 
};
apiInstance.communication(opts, (error, data, response) => {
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
 **all** | **Boolean**|  | [optional] [default to false]
 **post** | [**[Post]**](Post.md)|  | [optional] 

### Return type

[**[PostPredicted]**](PostPredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ekmanEmotion

> [PostPredicted] ekmanEmotion(opts)

Emotion Analysis

Detect the emotions of the text based on Ekman.  Supported Langauges: [&#x60;en&#x60;, &#x60;de&#x60;, &#x60;es&#x60;]  Returned labels: * anger * disgust * fear * joy * sadness * surprise * no-emotion

### Example

```javascript
import PsycholinguisticTextAnalytics from 'psycholinguistic_text_analytics';
let defaultClient = PsycholinguisticTextAnalytics.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new PsycholinguisticTextAnalytics.TextAnalysisApi();
let opts = {
  'all': false, // Boolean | 
  'post': [new PsycholinguisticTextAnalytics.Post()] // [Post] | 
};
apiInstance.ekmanEmotion(opts, (error, data, response) => {
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
 **all** | **Boolean**|  | [optional] [default to false]
 **post** | [**[Post]**](Post.md)|  | [optional] 

### Return type

[**[PostPredicted]**](PostPredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## emotion

> [PostPredicted] emotion(opts)

Emotion Analysis

Detect the emotions of the text.  Supported Langauges: [&#x60;en&#x60;, &#x60;de&#x60;, &#x60;es&#x60;]  Returned labels: * anger * joy * love * sadness * surprise * uncategorized

### Example

```javascript
import PsycholinguisticTextAnalytics from 'psycholinguistic_text_analytics';
let defaultClient = PsycholinguisticTextAnalytics.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new PsycholinguisticTextAnalytics.TextAnalysisApi();
let opts = {
  'all': false, // Boolean | 
  'post': [new PsycholinguisticTextAnalytics.Post()] // [Post] | 
};
apiInstance.emotion(opts, (error, data, response) => {
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
 **all** | **Boolean**|  | [optional] [default to false]
 **post** | [**[Post]**](Post.md)|  | [optional] 

### Return type

[**[PostPredicted]**](PostPredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## languageDetection

> [LanguagePredicted] languageDetection(opts)

Language Detection

Identifies what language a text is written in. Only languages that our API supports can be analyzed.  Returned labels: * language_code of the detected language

### Example

```javascript
import PsycholinguisticTextAnalytics from 'psycholinguistic_text_analytics';
let defaultClient = PsycholinguisticTextAnalytics.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new PsycholinguisticTextAnalytics.TextAnalysisApi();
let opts = {
  'languageDetection': [new PsycholinguisticTextAnalytics.LanguageDetection()] // [LanguageDetection] | 
};
apiInstance.languageDetection(opts, (error, data, response) => {
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
 **languageDetection** | [**[LanguageDetection]**](LanguageDetection.md)|  | [optional] 

### Return type

[**[LanguagePredicted]**](LanguagePredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## personality

> [PostPredicted] personality(opts)

Personality Traits

Predict the personality trait of author of any written text.  Supported Languages: [&#x60;ar&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;it&#x60;, &#x60;nl&#x60;, &#x60;pt&#x60;, &#x60;ru&#x60;, &#x60;tr&#x60;, &#x60;zh&#x60;]  Returned labels:  * emotional * rational

### Example

```javascript
import PsycholinguisticTextAnalytics from 'psycholinguistic_text_analytics';
let defaultClient = PsycholinguisticTextAnalytics.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new PsycholinguisticTextAnalytics.TextAnalysisApi();
let opts = {
  'all': false, // Boolean | 
  'post': [new PsycholinguisticTextAnalytics.Post()] // [Post] | 
};
apiInstance.personality(opts, (error, data, response) => {
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
 **all** | **Boolean**|  | [optional] [default to false]
 **post** | [**[Post]**](Post.md)|  | [optional] 

### Return type

[**[PostPredicted]**](PostPredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sentiment

> [PostPredicted] sentiment(opts)

Sentiment Analysis

Evaluate the overall tonality of the text.  Supported Languages: [&#x60;en&#x60;, &#x60;de&#x60;, &#x60;es&#x60;]  Returned labels: * positive * negative

### Example

```javascript
import PsycholinguisticTextAnalytics from 'psycholinguistic_text_analytics';
let defaultClient = PsycholinguisticTextAnalytics.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new PsycholinguisticTextAnalytics.TextAnalysisApi();
let opts = {
  'all': false, // Boolean | 
  'post': [new PsycholinguisticTextAnalytics.Post()] // [Post] | 
};
apiInstance.sentiment(opts, (error, data, response) => {
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
 **all** | **Boolean**|  | [optional] [default to false]
 **post** | [**[Post]**](Post.md)|  | [optional] 

### Return type

[**[PostPredicted]**](PostPredicted.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## topicSentiment

> [TopicSentimentOutput] topicSentiment(opts)

Extracts topics and sentiments and relates them.

### Example

```javascript
import PsycholinguisticTextAnalytics from 'psycholinguistic_text_analytics';
let defaultClient = PsycholinguisticTextAnalytics.ApiClient.instance;
// Configure API key authorization: apiKeyHeader
let apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix = 'Token';

let apiInstance = new PsycholinguisticTextAnalytics.TextAnalysisApi();
let opts = {
  'domain': "domain_example", // String | Provide analysis domain for better extraction (optional)
  'post': [new PsycholinguisticTextAnalytics.Post()] // [Post] | 
};
apiInstance.topicSentiment(opts, (error, data, response) => {
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
 **domain** | **String**| Provide analysis domain for better extraction (optional) | [optional] 
 **post** | [**[Post]**](Post.md)|  | [optional] 

### Return type

[**[TopicSentimentOutput]**](TopicSentimentOutput.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

