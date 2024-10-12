# RegressionAnalysisApi.DefaultApi

All URIs are relative to *https://services.scideas.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regressionApiPost**](DefaultApi.md#regressionApiPost) | **POST** /regression/api | Returns regression analysis.



## regressionApiPost

> InlineResponse200 regressionApiPost(regressionApiBody)

Returns regression analysis.

### Example

```javascript
import RegressionAnalysisApi from 'regression_analysis_api';

let apiInstance = new RegressionAnalysisApi.DefaultApi();
let regressionApiBody = new RegressionAnalysisApi.RegressionApiBody(); // RegressionApiBody | 
apiInstance.regressionApiPost(regressionApiBody, (error, data, response) => {
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
 **regressionApiBody** | [**RegressionApiBody**](RegressionApiBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

