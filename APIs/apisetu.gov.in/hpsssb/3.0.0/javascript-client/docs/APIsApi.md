# HpStaffSelectionCommissionHpsscHimachalPradeshHimachalPradesh.APIsApi

All URIs are relative to *https://apisetu.gov.in/hpsssb/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adcrd**](APIsApi.md#adcrd) | **POST** /adcrd/certificate | Admit Card



## adcrd

> adcrd(opts)

Admit Card

API to verify Admit Card.

### Example

```javascript
import HpStaffSelectionCommissionHpsscHimachalPradeshHimachalPradesh from 'hp_staff_selection_commission_hpssc_himachal_pradesh_himachal_pradesh';
let defaultClient = HpStaffSelectionCommissionHpsscHimachalPradeshHimachalPradesh.ApiClient.instance;
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

let apiInstance = new HpStaffSelectionCommissionHpsscHimachalPradeshHimachalPradesh.APIsApi();
let opts = {
  'adcrdRequest': new HpStaffSelectionCommissionHpsscHimachalPradeshHimachalPradesh.AdcrdRequest() // AdcrdRequest | Request format
};
apiInstance.adcrd(opts, (error, data, response) => {
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
 **adcrdRequest** | [**AdcrdRequest**](AdcrdRequest.md)| Request format | [optional] 

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf, application/json

