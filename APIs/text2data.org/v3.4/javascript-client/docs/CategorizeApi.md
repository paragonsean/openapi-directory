# TextAnalyticsSentimentAnalysisApiApiText2dataCom.CategorizeApi

All URIs are relative to *http://api.text2data.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categorizeGet**](CategorizeApi.md#categorizeGet) | **GET** /v3/Categorize | Test api response without api key
[**categorizePost**](CategorizeApi.md#categorizePost) | **POST** /v3/Categorize | Document categorization service



## categorizeGet

> DocumentResult categorizeGet()

Test api response without api key

### Example

```javascript
import TextAnalyticsSentimentAnalysisApiApiText2dataCom from 'text_analytics__sentiment_analysis_api___api_text2data_com';

let apiInstance = new TextAnalyticsSentimentAnalysisApiApiText2dataCom.CategorizeApi();
apiInstance.categorizeGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**DocumentResult**](DocumentResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## categorizePost

> DocumentResult categorizePost(requestDoc)

Document categorization service

Sample request:                    POST /Categorize      {         \&quot;DocumentText\&quot;: \&quot;Excellent location, opposite a very large mall with wide variety of shops, restaurants and more.\&quot;,         \&quot;PrivateKey\&quot;: \&quot;your_api_key\&quot;,         \&quot;UserCategoryModelName\&quot;: \&quot;your_model_name\&quot;,         \&quot;Secret\&quot;: \&quot;\&quot;      }

### Example

```javascript
import TextAnalyticsSentimentAnalysisApiApiText2dataCom from 'text_analytics__sentiment_analysis_api___api_text2data_com';

let apiInstance = new TextAnalyticsSentimentAnalysisApiApiText2dataCom.CategorizeApi();
let requestDoc = new TextAnalyticsSentimentAnalysisApiApiText2dataCom.Document(); // Document | 
apiInstance.categorizePost(requestDoc, (error, data, response) => {
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
 **requestDoc** | [**Document**](Document.md)|  | 

### Return type

[**DocumentResult**](DocumentResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

