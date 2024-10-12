# TextAnalyticsClient.EntitiesApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entities**](EntitiesApi.md#entities) | **POST** /entities | The API returns a list of recognized entities in a given document.



## entities

> EntitiesBatchResult entities(opts)

The API returns a list of recognized entities in a given document.

To get even more information on each recognized entity we recommend using the Bing Entity Search API by querying for the recognized entities names. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/text-analytics-supported-languages\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

### Example

```javascript
import TextAnalyticsClient from 'text_analytics_client';
let defaultClient = TextAnalyticsClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new TextAnalyticsClient.EntitiesApi();
let opts = {
  'showStats': true, // Boolean | (optional) if set to true, response will contain input and document level statistics.
  'multiLanguageBatchInput': new TextAnalyticsClient.MultiLanguageBatchInput() // MultiLanguageBatchInput | Collection of documents to analyze.
};
apiInstance.entities(opts, (error, data, response) => {
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

[**EntitiesBatchResult**](EntitiesBatchResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

