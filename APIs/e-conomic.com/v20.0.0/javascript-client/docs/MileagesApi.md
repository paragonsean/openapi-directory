# VismaEConomicOpenApi.MileagesApi

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approveMileageEntries**](MileagesApi.md#approveMileageEntries) | **POST** /mileages/approve | Approve a list of Mileage entries



## approveMileageEntries

> approveMileageEntries(opts)

Approve a list of Mileage entries

Use this endpoint to approve a list of Mileage entries.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.MileagesApi();
let opts = {
  'mileageNumbersCollection': new VismaEConomicOpenApi.MileageNumbersCollection() // MileageNumbersCollection | 
};
apiInstance.approveMileageEntries(opts, (error, data, response) => {
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
 **mileageNumbersCollection** | [**MileageNumbersCollection**](MileageNumbersCollection.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json

