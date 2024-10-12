# TextAnalyticsClient.EntitiesApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entities**](EntitiesApi.md#entities) | **POST** /entities | The API returns a list of recognized entities in a given document.



## entities

> EntitiesBatchResultV2dot1 entities(input)

The API returns a list of recognized entities in a given document.

The API returns a list of recognized entities in a given document. To get even more information on each recognized entity we recommend using the Bing Entity Search API by querying for the recognized entities names. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/text-analytics-supported-languages\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.The API returns a list of known entities and general named entities (\&quot;Person\&quot;, \&quot;Location\&quot;, \&quot;Organization\&quot; etc) in a given document. Known entities are returned with Wikipedia Id and Wikipedia link, and also Bing Id which can be used in Bing Entity Search API. General named entities are returned with entity types. If a general named entity is also a known entity, then all information regarding it (Wikipedia Id, Bing Id, entity type etc) will be returned. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-entity-linking#supported-types-for-named-entity-recognition\&quot;&gt;Supported Entity Types in Text Analytics API&lt;/a&gt; for the list of supported Entity Types. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/text-analytics-supported-languages\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

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
let input = new TextAnalyticsClient.MultiLanguageBatchInput(); // MultiLanguageBatchInput | Collection of documents to analyze.
apiInstance.entities(input, (error, data, response) => {
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

### Return type

[**EntitiesBatchResultV2dot1**](EntitiesBatchResultV2dot1.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

