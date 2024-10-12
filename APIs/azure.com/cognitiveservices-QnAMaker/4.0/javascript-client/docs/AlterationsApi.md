# QnAMakerClient.AlterationsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alterationsGet**](AlterationsApi.md#alterationsGet) | **GET** /alterations | Download alterations from runtime.
[**alterationsReplace**](AlterationsApi.md#alterationsReplace) | **PUT** /alterations | Replace alterations data.



## alterationsGet

> WordAlterationsDTO alterationsGet()

Download alterations from runtime.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.AlterationsApi();
apiInstance.alterationsGet((error, data, response) => {
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

[**WordAlterationsDTO**](WordAlterationsDTO.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alterationsReplace

> alterationsReplace(wordAlterations)

Replace alterations data.

### Example

```javascript
import QnAMakerClient from 'qn_a_maker_client';
let defaultClient = QnAMakerClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new QnAMakerClient.AlterationsApi();
let wordAlterations = new QnAMakerClient.WordAlterationsDTO(); // WordAlterationsDTO | New alterations data.
apiInstance.alterationsReplace(wordAlterations, (error, data, response) => {
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
 **wordAlterations** | [**WordAlterationsDTO**](WordAlterationsDTO.md)| New alterations data. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

