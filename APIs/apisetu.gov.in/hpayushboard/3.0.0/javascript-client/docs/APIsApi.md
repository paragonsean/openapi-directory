# BoardOfAyurvedicAndUnaniSystemsOfMedicineHimachalPradeshHimachalPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/hpayushboard/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**phcer**](APIsApi.md#phcer) | **POST** /phcer/certificate | Pharmacist Registration Certificate
[**rpcer**](APIsApi.md#rpcer) | **POST** /rpcer/certificate | Pharmacist Renewal certificate



## phcer

> phcer(opts)

Pharmacist Registration Certificate

API to verify Pharmacist Registration Certificate.

### Example

```javascript
import BoardOfAyurvedicAndUnaniSystemsOfMedicineHimachalPradeshHimachalPradesh from 'board_of_ayurvedic_and_unani_systems_of_medicine_himachal_pradesh_himachal_pradesh';
let defaultClient = BoardOfAyurvedicAndUnaniSystemsOfMedicineHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new BoardOfAyurvedicAndUnaniSystemsOfMedicineHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'phcerRequest': new BoardOfAyurvedicAndUnaniSystemsOfMedicineHimachalPradeshHimachalPradesh.PhcerRequest() // PhcerRequest | Request format
};
apiInstance.phcer(opts, (error, data, response) => {
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
 **phcerRequest** | [**PhcerRequest**](PhcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json


## rpcer

> rpcer(opts)

Pharmacist Renewal certificate

API to verify Pharmacist Renewal certificate.

### Example

```javascript
import BoardOfAyurvedicAndUnaniSystemsOfMedicineHimachalPradeshHimachalPradesh from 'board_of_ayurvedic_and_unani_systems_of_medicine_himachal_pradesh_himachal_pradesh';
let defaultClient = BoardOfAyurvedicAndUnaniSystemsOfMedicineHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new BoardOfAyurvedicAndUnaniSystemsOfMedicineHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'rpcerRequest': new BoardOfAyurvedicAndUnaniSystemsOfMedicineHimachalPradeshHimachalPradesh.RpcerRequest() // RpcerRequest | Request format
};
apiInstance.rpcer(opts, (error, data, response) => {
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
 **rpcerRequest** | [**RpcerRequest**](RpcerRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

