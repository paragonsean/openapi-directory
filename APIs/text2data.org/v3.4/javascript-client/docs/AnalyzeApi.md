# TextAnalyticsSentimentAnalysisApiApiText2dataCom.AnalyzeApi

All URIs are relative to *http://api.text2data.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyzeGet**](AnalyzeApi.md#analyzeGet) | **GET** /v3/Analyze | Test api response without api key
[**analyzePost**](AnalyzeApi.md#analyzePost) | **POST** /v3/Analyze | Sentiment analysis service



## analyzeGet

> DocumentResult analyzeGet()

Test api response without api key

### Example

```javascript
import TextAnalyticsSentimentAnalysisApiApiText2dataCom from 'text_analytics__sentiment_analysis_api___api_text2data_com';

let apiInstance = new TextAnalyticsSentimentAnalysisApiApiText2dataCom.AnalyzeApi();
apiInstance.analyzeGet((error, data, response) => {
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


## analyzePost

> DocumentResult analyzePost(requestDoc)

Sentiment analysis service

Sample request:                    POST /Analyze      {         \&quot;DocumentText\&quot;: \&quot;Excellent location, opposite a very large mall with wide variety of shops, restaurants and more.\&quot;,         \&quot;PrivateKey\&quot;: \&quot;your_api_key\&quot;,         \&quot;Secret\&quot;: \&quot;\&quot;      }

### Example

```javascript
import TextAnalyticsSentimentAnalysisApiApiText2dataCom from 'text_analytics__sentiment_analysis_api___api_text2data_com';

let apiInstance = new TextAnalyticsSentimentAnalysisApiApiText2dataCom.AnalyzeApi();
let requestDoc = new TextAnalyticsSentimentAnalysisApiApiText2dataCom.Document(); // Document | 
apiInstance.analyzePost(requestDoc, (error, data, response) => {
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

