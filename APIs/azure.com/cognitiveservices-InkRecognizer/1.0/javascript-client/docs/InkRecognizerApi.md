# InkRecognizerClient.InkRecognizerApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inkRecognizerRecognize**](InkRecognizerApi.md#inkRecognizerRecognize) | **PUT** /recognize | 



## inkRecognizerRecognize

> AnalysisResponse inkRecognizerRecognize(body, opts)



Ink Recognition operation is used to perform ink layout and recognition of written words and shapes. It allows passing the ink strokes to the service to get the recognition results in the response.

### Example

```javascript
import InkRecognizerClient from 'ink_recognizer_client';
let defaultClient = InkRecognizerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new InkRecognizerClient.InkRecognizerApi();
let body = new InkRecognizerClient.AnalysisRequest(); // AnalysisRequest | The collection of stroke objects to send for analysis
let opts = {
  'xMsClientRequestId': "xMsClientRequestId_example" // String | The request id used to uniquely identify each request during troubleshooting. This is an optional parameter useful for correlating logs and other artifacts.
};
apiInstance.inkRecognizerRecognize(body, opts, (error, data, response) => {
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
 **body** | [**AnalysisRequest**](AnalysisRequest.md)| The collection of stroke objects to send for analysis | 
 **xMsClientRequestId** | **String**| The request id used to uniquely identify each request during troubleshooting. This is an optional parameter useful for correlating logs and other artifacts. | [optional] 

### Return type

[**AnalysisResponse**](AnalysisResponse.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

