# InfermedicaApi.ExplainApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**computeExplanation**](ExplainApi.md#computeExplanation) | **POST** /explain | Query diagnostic engine for explanation



## computeExplanation

> ExplanationResponse computeExplanation(body)

Query diagnostic engine for explanation

Explains which evidence impact probability of selected condition.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.ExplainApi();
let body = new InfermedicaApi.ExplanationRequest(); // ExplanationRequest | 
apiInstance.computeExplanation(body, (error, data, response) => {
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
 **body** | [**ExplanationRequest**](ExplanationRequest.md)|  | 

### Return type

[**ExplanationResponse**](ExplanationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

