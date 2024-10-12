# AutomataMarketIntelligenceApi.ContentproSimilarTextApi

All URIs are relative to *https://api.byautomata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentproSimilarTextPost**](ContentproSimilarTextApi.md#contentproSimilarTextPost) | **POST** /contentpro-similar-text | The /contentpro-similar-text endpoint accepts and arbitrary piece of text and returns similar articles and blogs written by companies.



## contentproSimilarTextPost

> ContentproSearchGet200Response contentproSimilarTextPost(contentproSimilarTextPostRequest)

The /contentpro-similar-text endpoint accepts and arbitrary piece of text and returns similar articles and blogs written by companies.

### Example

```javascript
import AutomataMarketIntelligenceApi from 'automata_market_intelligence_api';

let apiInstance = new AutomataMarketIntelligenceApi.ContentproSimilarTextApi();
let contentproSimilarTextPostRequest = new AutomataMarketIntelligenceApi.ContentproSimilarTextPostRequest(); // ContentproSimilarTextPostRequest | We'll provide information about related companies and articles based on the text you provide.
apiInstance.contentproSimilarTextPost(contentproSimilarTextPostRequest, (error, data, response) => {
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
 **contentproSimilarTextPostRequest** | [**ContentproSimilarTextPostRequest**](ContentproSimilarTextPostRequest.md)| We&#39;ll provide information about related companies and articles based on the text you provide. | 

### Return type

[**ContentproSearchGet200Response**](ContentproSearchGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

