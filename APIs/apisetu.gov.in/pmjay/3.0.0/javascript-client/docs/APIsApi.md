# NationalHealthAuthority.APIsApi

All URIs are relative to *https://apisetu.gov.in/pmjay/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pmjay**](APIsApi.md#pmjay) | **POST** /pmjay/certificate | Pradhan Mantri Jan Arogya Yojana



## pmjay

> pmjay(opts)

Pradhan Mantri Jan Arogya Yojana

API to verify Pradhan Mantri Jan Arogya Yojana.

### Example

```javascript
import NationalHealthAuthority from 'national_health_authority';
let defaultClient = NationalHealthAuthority.ApiClient.instance;
// Configure API key authorization: clientId
let clientId = defaultClient.authentications['clientId'];
clientId.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//clientId.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new NationalHealthAuthority.APIsApi();
let opts = {
  'pmjayRequest': new NationalHealthAuthority.PmjayRequest() // PmjayRequest | Request format
};
apiInstance.pmjay(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmjayRequest** | [**PmjayRequest**](PmjayRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

