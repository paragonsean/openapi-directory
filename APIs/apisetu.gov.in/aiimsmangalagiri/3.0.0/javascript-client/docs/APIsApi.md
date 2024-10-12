# AiimsMangalagiri.APIsApi

All URIs are relative to *https://apisetu.gov.in/aiimsmangalagiri/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**labrp**](APIsApi.md#labrp) | **POST** /labrp/certificate | Clinical Laboratory Report



## labrp

> labrp(opts)

Clinical Laboratory Report

API to verify Clinical Laboratory Report.

### Example

```javascript
import AiimsMangalagiri from 'aiims_mangalagiri';
let defaultClient = AiimsMangalagiri.ApiClient.instance;
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

let apiInstance = new AiimsMangalagiri.APIsApi();
let opts = {
  'labrpRequest': new AiimsMangalagiri.LabrpRequest() // LabrpRequest | Request format
};
apiInstance.labrp(opts, (error, data, response) => {
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
 **labrpRequest** | [**LabrpRequest**](LabrpRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

