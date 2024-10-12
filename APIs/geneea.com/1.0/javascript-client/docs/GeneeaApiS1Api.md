# GeneeaNaturalLanguageProcessing.GeneeaApiS1Api

All URIs are relative to *https://api.geneea.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**correctionGet**](GeneeaApiS1Api.md#correctionGet) | **GET** /s1/correction | Performs text correction (diacritization) on the given document
[**correctionPost**](GeneeaApiS1Api.md#correctionPost) | **POST** /s1/correction | Performs text correction (diacritization) on the given document
[**entitiesGet**](GeneeaApiS1Api.md#entitiesGet) | **GET** /s1/entities | Performs named-entity recognition on the given document
[**entitiesPost**](GeneeaApiS1Api.md#entitiesPost) | **POST** /s1/entities | Performs named-entity recognition on the given document
[**lemmatizeGet**](GeneeaApiS1Api.md#lemmatizeGet) | **GET** /s1/lemmatize | Performs lemmatization on the given document
[**lemmatizePost**](GeneeaApiS1Api.md#lemmatizePost) | **POST** /s1/lemmatize | Performs lemmatization on the given document
[**sentimentGet**](GeneeaApiS1Api.md#sentimentGet) | **GET** /s1/sentiment | Performs sentiment analysis on the given document
[**sentimentPost**](GeneeaApiS1Api.md#sentimentPost) | **POST** /s1/sentiment | Performs sentiment analysis on the given document
[**topicGet**](GeneeaApiS1Api.md#topicGet) | **GET** /s1/topic | Performs topic detection on the given document
[**topicPost**](GeneeaApiS1Api.md#topicPost) | **POST** /s1/topic | Performs topic detection on the given document



## correctionGet

> Object correctionGet(opts)

Performs text correction (diacritization) on the given document

&lt;br/&gt;&lt;strong&gt;Possible options:&lt;/strong&gt;&lt;p class&#x3D;\&quot;markdown\&quot;&gt;An optional parameter &lt;code&gt;diacritize&lt;/code&gt; with values &lt;code&gt;yes&lt;/code&gt;, &lt;code&gt;no&lt;/code&gt; or &lt;code&gt;auto&lt;/code&gt; indicate whether the text diacritization will be performed. The default value is &lt;code&gt;auto&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.GeneeaApiS1Api();
let opts = {
  'id': "id_example", // String | document ID
  'text': "text_example", // String | raw document text
  'url': "url_example", // String | document URL
  'extractor': "extractor_example", // String | document extractor
  'language': "language_example", // String | document language
  'returnTextInfo': true // Boolean | 
};
apiInstance.correctionGet(opts, (error, data, response) => {
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
 **id** | **String**| document ID | [optional] 
 **text** | **String**| raw document text | [optional] 
 **url** | **String**| document URL | [optional] 
 **extractor** | **String**| document extractor | [optional] 
 **language** | **String**| document language | [optional] 
 **returnTextInfo** | **Boolean**|  | [optional] 

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## correctionPost

> Object correctionPost(opts)

Performs text correction (diacritization) on the given document

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;br/&gt;&lt;strong&gt;Possible options:&lt;/strong&gt;&lt;p class&#x3D;\&quot;markdown\&quot;&gt;An optional parameter &lt;code&gt;diacritize&lt;/code&gt; with values &lt;code&gt;yes&lt;/code&gt;, &lt;code&gt;no&lt;/code&gt; or &lt;code&gt;auto&lt;/code&gt; indicate whether the text diacritization will be performed. The default value is &lt;code&gt;auto&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.GeneeaApiS1Api();
let opts = {
  'body': new GeneeaNaturalLanguageProcessing.Request() // Request | request
};
apiInstance.correctionPost(opts, (error, data, response) => {
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
 **body** | [**Request**](Request.md)| request | [optional] 

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## entitiesGet

> EntitiesResponse entitiesGet(opts)

Performs named-entity recognition on the given document

entitiesGet

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.GeneeaApiS1Api();
let opts = {
  'id': "id_example", // String | document ID
  'text': "text_example", // String | raw document text
  'url': "url_example", // String | document URL
  'extractor': "extractor_example", // String | document extractor
  'language': "language_example", // String | document language
  'returnTextInfo': true // Boolean | 
};
apiInstance.entitiesGet(opts, (error, data, response) => {
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
 **id** | **String**| document ID | [optional] 
 **text** | **String**| raw document text | [optional] 
 **url** | **String**| document URL | [optional] 
 **extractor** | **String**| document extractor | [optional] 
 **language** | **String**| document language | [optional] 
 **returnTextInfo** | **Boolean**|  | [optional] 

### Return type

[**EntitiesResponse**](EntitiesResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## entitiesPost

> EntitiesResponse entitiesPost(opts)

Performs named-entity recognition on the given document

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.GeneeaApiS1Api();
let opts = {
  'body': new GeneeaNaturalLanguageProcessing.Request() // Request | request
};
apiInstance.entitiesPost(opts, (error, data, response) => {
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
 **body** | [**Request**](Request.md)| request | [optional] 

### Return type

[**EntitiesResponse**](EntitiesResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## lemmatizeGet

> LemmatizeResponse lemmatizeGet(opts)

Performs lemmatization on the given document

lemmatizeGet

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.GeneeaApiS1Api();
let opts = {
  'id': "id_example", // String | document ID
  'text': "text_example", // String | raw document text
  'url': "url_example", // String | document URL
  'extractor': "extractor_example", // String | document extractor
  'language': "language_example", // String | document language
  'returnTextInfo': true // Boolean | 
};
apiInstance.lemmatizeGet(opts, (error, data, response) => {
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
 **id** | **String**| document ID | [optional] 
 **text** | **String**| raw document text | [optional] 
 **url** | **String**| document URL | [optional] 
 **extractor** | **String**| document extractor | [optional] 
 **language** | **String**| document language | [optional] 
 **returnTextInfo** | **Boolean**|  | [optional] 

### Return type

[**LemmatizeResponse**](LemmatizeResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lemmatizePost

> LemmatizeResponse lemmatizePost(opts)

Performs lemmatization on the given document

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.GeneeaApiS1Api();
let opts = {
  'body': new GeneeaNaturalLanguageProcessing.Request() // Request | request
};
apiInstance.lemmatizePost(opts, (error, data, response) => {
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
 **body** | [**Request**](Request.md)| request | [optional] 

### Return type

[**LemmatizeResponse**](LemmatizeResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sentimentGet

> SentimentResponse sentimentGet(opts)

Performs sentiment analysis on the given document

sentimentGet

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.GeneeaApiS1Api();
let opts = {
  'id': "id_example", // String | document ID
  'text': "text_example", // String | raw document text
  'url': "url_example", // String | document URL
  'extractor': "extractor_example", // String | document extractor
  'language': "language_example", // String | document language
  'returnTextInfo': true // Boolean | 
};
apiInstance.sentimentGet(opts, (error, data, response) => {
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
 **id** | **String**| document ID | [optional] 
 **text** | **String**| raw document text | [optional] 
 **url** | **String**| document URL | [optional] 
 **extractor** | **String**| document extractor | [optional] 
 **language** | **String**| document language | [optional] 
 **returnTextInfo** | **Boolean**|  | [optional] 

### Return type

[**SentimentResponse**](SentimentResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sentimentPost

> SentimentResponse sentimentPost(opts)

Performs sentiment analysis on the given document

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.GeneeaApiS1Api();
let opts = {
  'body': new GeneeaNaturalLanguageProcessing.Request() // Request | request
};
apiInstance.sentimentPost(opts, (error, data, response) => {
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
 **body** | [**Request**](Request.md)| request | [optional] 

### Return type

[**SentimentResponse**](SentimentResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## topicGet

> TopicResponse topicGet(opts)

Performs topic detection on the given document

topicGet

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.GeneeaApiS1Api();
let opts = {
  'id': "id_example", // String | document ID
  'text': "text_example", // String | raw document text
  'url': "url_example", // String | document URL
  'extractor': "extractor_example", // String | document extractor
  'language': "language_example", // String | document language
  'returnTextInfo': true // Boolean | 
};
apiInstance.topicGet(opts, (error, data, response) => {
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
 **id** | **String**| document ID | [optional] 
 **text** | **String**| raw document text | [optional] 
 **url** | **String**| document URL | [optional] 
 **extractor** | **String**| document extractor | [optional] 
 **language** | **String**| document language | [optional] 
 **returnTextInfo** | **Boolean**|  | [optional] 

### Return type

[**TopicResponse**](TopicResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topicPost

> TopicResponse topicPost(opts)

Performs topic detection on the given document

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.GeneeaApiS1Api();
let opts = {
  'body': new GeneeaNaturalLanguageProcessing.Request() // Request | request
};
apiInstance.topicPost(opts, (error, data, response) => {
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
 **body** | [**Request**](Request.md)| request | [optional] 

### Return type

[**TopicResponse**](TopicResponse.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

