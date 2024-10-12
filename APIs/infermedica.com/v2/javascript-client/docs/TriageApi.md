# InfermedicaApi.TriageApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**computeTriage**](TriageApi.md#computeTriage) | **POST** /triage | Query diagnostic engine for triage level



## computeTriage

> TriageResponse computeTriage(body)

Query diagnostic engine for triage level

Estimates triage level based on provided patient information.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.TriageApi();
let body = new InfermedicaApi.DiagnosisRequest(); // DiagnosisRequest | 
apiInstance.computeTriage(body, (error, data, response) => {
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

[**TriageResponse**](TriageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

