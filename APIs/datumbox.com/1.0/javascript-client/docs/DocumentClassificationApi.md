# ApiDatumboxCom.DocumentClassificationApi

All URIs are relative to *http://api.datumbox.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adultContentDetection**](DocumentClassificationApi.md#adultContentDetection) | **POST** /1.0/AdultContentDetection.json | Classifies the Document as adult or noadult
[**commercialDetection**](DocumentClassificationApi.md#commercialDetection) | **POST** /1.0/CommercialDetection.json | Classifies the Document as commercial or nocommercial
[**educationalDetection**](DocumentClassificationApi.md#educationalDetection) | **POST** /1.0/EducationalDetection.json | Classifies the Document as educational or noeducational
[**genderDetection**](DocumentClassificationApi.md#genderDetection) | **POST** /1.0/GenderDetection.json | Gender Detection Service
[**languageDetection**](DocumentClassificationApi.md#languageDetection) | **POST** /1.0/LanguageDetection.json | Identifies the Language of the Document
[**readabilityAssessment**](DocumentClassificationApi.md#readabilityAssessment) | **POST** /1.0/ReadabilityAssessment.json | Evaluates the Readability of the Document
[**sentimentAnalysis**](DocumentClassificationApi.md#sentimentAnalysis) | **POST** /1.0/SentimentAnalysis.json | Identifies the Sentiment of the Document
[**spamDetection**](DocumentClassificationApi.md#spamDetection) | **POST** /1.0/SpamDetection.json | Classifies the Document as spam or nospam
[**subjectivityAnalysis**](DocumentClassificationApi.md#subjectivityAnalysis) | **POST** /1.0/SubjectivityAnalysis.json | Classifies Document as Subjective or Objective
[**topicClassification**](DocumentClassificationApi.md#topicClassification) | **POST** /1.0/TopicClassification.json | Identifies the Topic of the Document
[**twitterSentimentAnalysis**](DocumentClassificationApi.md#twitterSentimentAnalysis) | **POST** /1.0/TwitterSentimentAnalysis.json | Identifies the Sentiment of Twitter Messages



## adultContentDetection

> adultContentDetection(apiKey, opts)

Classifies the Document as adult or noadult

The Adult Content Detection function classifies the documents as adult or noadult based on their context. It can be used to detect whether a document contains content unsuitable for minors.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.adultContentDetection(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## commercialDetection

> commercialDetection(apiKey, opts)

Classifies the Document as commercial or nocommercial

The Commercial Detection function labels the documents as commercial or non-commercial based on their keywords and expressions. It can be used to detect whether a website is commercial or not.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.commercialDetection(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## educationalDetection

> educationalDetection(apiKey, opts)

Classifies the Document as educational or noeducational

The Educational Detection function classifies the documents as educational or non-educational based on their context. It can be used to detect whether a website is educational or not.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.educationalDetection(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## genderDetection

> genderDetection(apiKey, opts)

Gender Detection Service

The Gender Detection function identifies if a particular document is written-by or targets-to a man or a woman based on the context, the words and the idioms found in the text.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.genderDetection(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## languageDetection

> languageDetection(apiKey, opts)

Identifies the Language of the Document

The Language Detection function identifies the natural language of the given document based on its words and context. This classifier is able to detect 96 different languages.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.languageDetection(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## readabilityAssessment

> readabilityAssessment(apiKey, opts)

Evaluates the Readability of the Document

The Readability Assessment function determines the degree of readability of a document based on its terms and idioms. The texts are classified as basic, intermediate and advanced depending their difficulty.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.readabilityAssessment(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## sentimentAnalysis

> sentimentAnalysis(apiKey, opts)

Identifies the Sentiment of the Document

The Sentiment Analysis function classifies documents as positive, negative or neutral (lack of sentiment) depending on whether they express a positive, negative or neutral opinion.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.sentimentAnalysis(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## spamDetection

> spamDetection(apiKey, opts)

Classifies the Document as spam or nospam

The Spam Detection function labels documents as spam or nospam by taking into account their context. It can be used to filter out spam emails and comments.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.spamDetection(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## subjectivityAnalysis

> subjectivityAnalysis(apiKey, opts)

Classifies Document as Subjective or Objective

The Subjectivity Analysis function categorizes documents as subjective or objective based on their writing style. Texts that express personal opinions are labeled as subjective and the others as objective.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.subjectivityAnalysis(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## topicClassification

> topicClassification(apiKey, opts)

Identifies the Topic of the Document

The Topic Classification function assigns documents in 12 thematic categories based on their keywords, idioms and jargon. It can be used to identify the topic of the texts.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text that you want to analyze. It should not contain HTML tags.
};
apiInstance.topicClassification(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text that you want to analyze. It should not contain HTML tags. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## twitterSentimentAnalysis

> twitterSentimentAnalysis(apiKey, opts)

Identifies the Sentiment of Twitter Messages

The Twitter Sentiment Analysis function allows you to perform Sentiment Analysis on Twitter. It classifies the tweets as positive, negative or neutral depending on their context.

### Example

```javascript
import ApiDatumboxCom from 'api_datumbox_com';

let apiInstance = new ApiDatumboxCom.DocumentClassificationApi();
let apiKey = "apiKey_example"; // String | Your API Key
let opts = {
  'text': "text_example" // String | The text of the tweet that we evaluate.
};
apiInstance.twitterSentimentAnalysis(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**| Your API Key | 
 **text** | **String**| The text of the tweet that we evaluate. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

