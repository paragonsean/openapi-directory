# InfermedicaApi.RedFlagsApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**computeRedFlags**](RedFlagsApi.md#computeRedFlags) | **POST** /red_flags | Query the diagnostic engine for possible red flag symptoms



## computeRedFlags

> [SuggestResult] computeRedFlags(body, opts)

Query the diagnostic engine for possible red flag symptoms

Suggests possible red flag symptoms based on provided patient information.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.RedFlagsApi();
let body = new InfermedicaApi.DiagnosisRequest(); // DiagnosisRequest | 
let opts = {
  'maxResults': 8 // Number | maximum number of results
};
apiInstance.computeRedFlags(body, opts, (error, data, response) => {
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
 **body** | [**DiagnosisRequest**](DiagnosisRequest.md)|  | 
 **maxResults** | **Number**| maximum number of results | [optional] [default to 8]

### Return type

[**[SuggestResult]**](SuggestResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

