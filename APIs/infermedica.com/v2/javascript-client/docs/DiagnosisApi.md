# InfermedicaApi.DiagnosisApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**computeDiagnosis**](DiagnosisApi.md#computeDiagnosis) | **POST** /diagnosis | Query diagnostic engine



## computeDiagnosis

> DiagnosisResponsePublic computeDiagnosis(body)

Query diagnostic engine

Suggests possible diagnoses and relevant observations based on provided patient information.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.DiagnosisApi();
let body = new InfermedicaApi.DiagnosisRequest(); // DiagnosisRequest | 
apiInstance.computeDiagnosis(body, (error, data, response) => {
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

### Return type

[**DiagnosisResponsePublic**](DiagnosisResponsePublic.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

