# TextAnalyticsClient.SentimentApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sentiment**](SentimentApi.md#sentiment) | **POST** /sentiment | The API returns a numeric score between 0 and 1.



## sentiment

> SentimentBatchResult sentiment(opts)

The API returns a numeric score between 0 and 1.

Scores close to 1 indicate positive sentiment, while scores close to 0 indicate negative sentiment. A score of 0.5 indicates the lack of sentiment (e.g. a factoid statement). See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview#supported-languages\&quot;&gt;Text Analytics Documentation&lt;/a&gt; for details about the languages that are supported by sentiment analysis.

### Example

```javascript
import TextAnalyticsClient from 'text_analytics_client';
let defaultClient = TextAnalyticsClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new TextAnalyticsClient.SentimentApi();
let opts = {
  'showStats': true, // Boolean | (optional) if set to true, response will contain input and document level statistics.
  'multiLanguageBatchInput': new TextAnalyticsClient.MultiLanguageBatchInput() // MultiLanguageBatchInput | Collection of documents to analyze.
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
 **showStats** | **Boolean**| (optional) if set to true, response will contain input and document level statistics. | [optional] 
 **multiLanguageBatchInput** | [**MultiLanguageBatchInput**](MultiLanguageBatchInput.md)| Collection of documents to analyze. | [optional] 

### Return type

[**SentimentBatchResult**](SentimentBatchResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

