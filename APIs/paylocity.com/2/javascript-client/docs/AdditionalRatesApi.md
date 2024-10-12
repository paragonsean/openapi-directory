# PaylocityApi.AdditionalRatesApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOrUpdateAdditionalRates**](AdditionalRatesApi.md#addOrUpdateAdditionalRates) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/additionalRates | Add/update additional rates



## addOrUpdateAdditionalRates

> addOrUpdateAdditionalRates(companyId, employeeId, additionalRate)

Add/update additional rates

Sends new or updated employee additional rates information directly to Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.AdditionalRatesApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let additionalRate = new PaylocityApi.AdditionalRate(); // AdditionalRate | Additional Rate Model
apiInstance.addOrUpdateAdditionalRates(companyId, employeeId, additionalRate, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **additionalRate** | [**AdditionalRate**](AdditionalRate.md)| Additional Rate Model | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

