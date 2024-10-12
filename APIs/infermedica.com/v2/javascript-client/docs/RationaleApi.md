# InfermedicaApi.RationaleApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**computeRationale**](RationaleApi.md#computeRationale) | **POST** /rationale | Query diagnostic engine for question rationale



## computeRationale

> RationaleResponse computeRationale(body)

Query diagnostic engine for question rationale

Returns rationale behind the question asked by the system.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.RationaleApi();
let body = new InfermedicaApi.RationaleRequest(); // RationaleRequest | 
apiInstance.computeRationale(body, (error, data, response) => {
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
 **body** | [**RationaleRequest**](RationaleRequest.md)|  | 

### Return type

[**RationaleResponse**](RationaleResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

