# AmazonPolly.DefaultApi

All URIs are relative to *http://polly.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteLexicon**](DefaultApi.md#deleteLexicon) | **DELETE** /v1/lexicons/{LexiconName} | 
[**describeVoices**](DefaultApi.md#describeVoices) | **GET** /v1/voices | 
[**getLexicon**](DefaultApi.md#getLexicon) | **GET** /v1/lexicons/{LexiconName} | 
[**getSpeechSynthesisTask**](DefaultApi.md#getSpeechSynthesisTask) | **GET** /v1/synthesisTasks/{TaskId} | 
[**listLexicons**](DefaultApi.md#listLexicons) | **GET** /v1/lexicons | 
[**listSpeechSynthesisTasks**](DefaultApi.md#listSpeechSynthesisTasks) | **GET** /v1/synthesisTasks | 
[**putLexicon**](DefaultApi.md#putLexicon) | **PUT** /v1/lexicons/{LexiconName} | 
[**startSpeechSynthesisTask**](DefaultApi.md#startSpeechSynthesisTask) | **POST** /v1/synthesisTasks | 
[**synthesizeSpeech**](DefaultApi.md#synthesizeSpeech) | **POST** /v1/speech | 



## deleteLexicon

> Object deleteLexicon(lexiconName, opts)



&lt;p&gt;Deletes the specified pronunciation lexicon stored in an Amazon Web Services Region. A lexicon which has been deleted is not available for speech synthesis, nor is it possible to retrieve it using either the &lt;code&gt;GetLexicon&lt;/code&gt; or &lt;code&gt;ListLexicon&lt;/code&gt; APIs.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\&quot;&gt;Managing Lexicons&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonPolly from 'amazon_polly';
let defaultClient = AmazonPolly.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPolly.DefaultApi();
let lexiconName = "lexiconName_example"; // String | The name of the lexicon to delete. Must be an existing lexicon in the region.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteLexicon(lexiconName, opts, (error, data, response) => {
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
 **lexiconName** | **String**| The name of the lexicon to delete. Must be an existing lexicon in the region. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeVoices

> DescribeVoicesOutput describeVoices(opts)



&lt;p&gt;Returns the list of voices that are available for use when requesting speech synthesis. Each voice speaks a specified language, is either male or female, and is identified by an ID, which is the ASCII version of the voice name. &lt;/p&gt; &lt;p&gt;When synthesizing speech ( &lt;code&gt;SynthesizeSpeech&lt;/code&gt; ), you provide the voice ID for the voice you want from the list of voices returned by &lt;code&gt;DescribeVoices&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For example, you want your news reader application to read news in a specific language, but giving a user the option to choose the voice. Using the &lt;code&gt;DescribeVoices&lt;/code&gt; operation you can provide the user with a list of available voices to select from.&lt;/p&gt; &lt;p&gt; You can optionally specify a language code to filter the available voices. For example, if you specify &lt;code&gt;en-US&lt;/code&gt;, the operation returns a list of all available US English voices. &lt;/p&gt; &lt;p&gt;This operation requires permissions to perform the &lt;code&gt;polly:DescribeVoices&lt;/code&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonPolly from 'amazon_polly';
let defaultClient = AmazonPolly.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPolly.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'engine': "engine_example", // String | Specifies the engine (<code>standard</code> or <code>neural</code>) used by Amazon Polly when processing input text for speech synthesis. 
  'languageCode': "languageCode_example", // String |  The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don't specify this optional parameter, all available voices are returned. 
  'includeAdditionalLanguageCodes': true, // Boolean | Boolean value indicating whether to return any bilingual voices that use the specified language as an additional language. For instance, if you request all languages that use US English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US English, that voice will be included if you specify <code>yes</code> but not if you specify <code>no</code>.
  'nextToken': "nextToken_example" // String | An opaque pagination token returned from the previous <code>DescribeVoices</code> operation. If present, this indicates where to continue the listing.
};
apiInstance.describeVoices(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **engine** | **String**| Specifies the engine (&lt;code&gt;standard&lt;/code&gt; or &lt;code&gt;neural&lt;/code&gt;) used by Amazon Polly when processing input text for speech synthesis.  | [optional] 
 **languageCode** | **String**|  The language identification tag (ISO 639 code for the language name-ISO 3166 country code) for filtering the list of voices returned. If you don&#39;t specify this optional parameter, all available voices are returned.  | [optional] 
 **includeAdditionalLanguageCodes** | **Boolean**| Boolean value indicating whether to return any bilingual voices that use the specified language as an additional language. For instance, if you request all languages that use US English (es-US), and there is an Italian voice that speaks both Italian (it-IT) and US English, that voice will be included if you specify &lt;code&gt;yes&lt;/code&gt; but not if you specify &lt;code&gt;no&lt;/code&gt;. | [optional] 
 **nextToken** | **String**| An opaque pagination token returned from the previous &lt;code&gt;DescribeVoices&lt;/code&gt; operation. If present, this indicates where to continue the listing. | [optional] 

### Return type

[**DescribeVoicesOutput**](DescribeVoicesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLexicon

> GetLexiconOutput getLexicon(lexiconName, opts)



Returns the content of the specified pronunciation lexicon stored in an Amazon Web Services Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\&quot;&gt;Managing Lexicons&lt;/a&gt;.

### Example

```javascript
import AmazonPolly from 'amazon_polly';
let defaultClient = AmazonPolly.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPolly.DefaultApi();
let lexiconName = "lexiconName_example"; // String | Name of the lexicon.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getLexicon(lexiconName, opts, (error, data, response) => {
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
 **lexiconName** | **String**| Name of the lexicon. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetLexiconOutput**](GetLexiconOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSpeechSynthesisTask

> GetSpeechSynthesisTaskOutput getSpeechSynthesisTask(taskId, opts)



Retrieves a specific SpeechSynthesisTask object based on its TaskID. This object contains information about the given speech synthesis task, including the status of the task, and a link to the S3 bucket containing the output of the task.

### Example

```javascript
import AmazonPolly from 'amazon_polly';
let defaultClient = AmazonPolly.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPolly.DefaultApi();
let taskId = "taskId_example"; // String | The Amazon Polly generated identifier for a speech synthesis task.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSpeechSynthesisTask(taskId, opts, (error, data, response) => {
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
 **taskId** | **String**| The Amazon Polly generated identifier for a speech synthesis task. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSpeechSynthesisTaskOutput**](GetSpeechSynthesisTaskOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLexicons

> ListLexiconsOutput listLexicons(opts)



Returns a list of pronunciation lexicons stored in an Amazon Web Services Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\&quot;&gt;Managing Lexicons&lt;/a&gt;.

### Example

```javascript
import AmazonPolly from 'amazon_polly';
let defaultClient = AmazonPolly.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPolly.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | An opaque pagination token returned from previous <code>ListLexicons</code> operation. If present, indicates where to continue the list of lexicons.
};
apiInstance.listLexicons(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| An opaque pagination token returned from previous &lt;code&gt;ListLexicons&lt;/code&gt; operation. If present, indicates where to continue the list of lexicons. | [optional] 

### Return type

[**ListLexiconsOutput**](ListLexiconsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSpeechSynthesisTasks

> ListSpeechSynthesisTasksOutput listSpeechSynthesisTasks(opts)



Returns a list of SpeechSynthesisTask objects ordered by their creation date. This operation can filter the tasks by their status, for example, allowing users to list only tasks that are completed.

### Example

```javascript
import AmazonPolly from 'amazon_polly';
let defaultClient = AmazonPolly.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPolly.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | Maximum number of speech synthesis tasks returned in a List operation.
  'nextToken': "nextToken_example", // String | The pagination token to use in the next request to continue the listing of speech synthesis tasks. 
  'status': "status_example" // String | Status of the speech synthesis tasks returned in a List operation
};
apiInstance.listSpeechSynthesisTasks(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| Maximum number of speech synthesis tasks returned in a List operation. | [optional] 
 **nextToken** | **String**| The pagination token to use in the next request to continue the listing of speech synthesis tasks.  | [optional] 
 **status** | **String**| Status of the speech synthesis tasks returned in a List operation | [optional] 

### Return type

[**ListSpeechSynthesisTasksOutput**](ListSpeechSynthesisTasksOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putLexicon

> Object putLexicon(lexiconName, putLexiconRequest, opts)



&lt;p&gt;Stores a pronunciation lexicon in an Amazon Web Services Region. If a lexicon with the same name already exists in the region, it is overwritten by the new lexicon. Lexicon operations have eventual consistency, therefore, it might take some time before the lexicon is available to the SynthesizeSpeech operation.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html\&quot;&gt;Managing Lexicons&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonPolly from 'amazon_polly';
let defaultClient = AmazonPolly.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPolly.DefaultApi();
let lexiconName = "lexiconName_example"; // String | Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long. 
let putLexiconRequest = new AmazonPolly.PutLexiconRequest(); // PutLexiconRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putLexicon(lexiconName, putLexiconRequest, opts, (error, data, response) => {
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
 **lexiconName** | **String**| Name of the lexicon. The name must follow the regular express format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive alphanumeric string up to 20 characters long.  | 
 **putLexiconRequest** | [**PutLexiconRequest**](PutLexiconRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startSpeechSynthesisTask

> StartSpeechSynthesisTaskOutput startSpeechSynthesisTask(startSpeechSynthesisTaskRequest, opts)



Allows the creation of an asynchronous synthesis task, by starting a new &lt;code&gt;SpeechSynthesisTask&lt;/code&gt;. This operation requires all the standard information needed for speech synthesis, plus the name of an Amazon S3 bucket for the service to store the output of the synthesis task and two optional parameters (&lt;code&gt;OutputS3KeyPrefix&lt;/code&gt; and &lt;code&gt;SnsTopicArn&lt;/code&gt;). Once the synthesis task is created, this operation will return a &lt;code&gt;SpeechSynthesisTask&lt;/code&gt; object, which will include an identifier of this task as well as the current status. The &lt;code&gt;SpeechSynthesisTask&lt;/code&gt; object is available for 72 hours after starting the asynchronous synthesis task.

### Example

```javascript
import AmazonPolly from 'amazon_polly';
let defaultClient = AmazonPolly.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPolly.DefaultApi();
let startSpeechSynthesisTaskRequest = new AmazonPolly.StartSpeechSynthesisTaskRequest(); // StartSpeechSynthesisTaskRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startSpeechSynthesisTask(startSpeechSynthesisTaskRequest, opts, (error, data, response) => {
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
 **startSpeechSynthesisTaskRequest** | [**StartSpeechSynthesisTaskRequest**](StartSpeechSynthesisTaskRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartSpeechSynthesisTaskOutput**](StartSpeechSynthesisTaskOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## synthesizeSpeech

> SynthesizeSpeechOutput synthesizeSpeech(synthesizeSpeechRequest, opts)



Synthesizes UTF-8 input, plain text or SSML, to a stream of bytes. SSML input must be valid, well-formed SSML. Some alphabets might not be available with all the voices (for example, Cyrillic might not be read at all by English voices) unless phoneme mapping is used. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/polly/latest/dg/how-text-to-speech-works.html\&quot;&gt;How it Works&lt;/a&gt;.

### Example

```javascript
import AmazonPolly from 'amazon_polly';
let defaultClient = AmazonPolly.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPolly.DefaultApi();
let synthesizeSpeechRequest = new AmazonPolly.SynthesizeSpeechRequest(); // SynthesizeSpeechRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.synthesizeSpeech(synthesizeSpeechRequest, opts, (error, data, response) => {
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
 **synthesizeSpeechRequest** | [**SynthesizeSpeechRequest**](SynthesizeSpeechRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SynthesizeSpeechOutput**](SynthesizeSpeechOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

