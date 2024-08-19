# PaylocityApi.NonPrimaryStateTaxApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOrUpdateNonPrimaryStateTax**](NonPrimaryStateTaxApi.md#addOrUpdateNonPrimaryStateTax) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/nonprimaryStateTax | Add/update non-primary state tax



## addOrUpdateNonPrimaryStateTax

> addOrUpdateNonPrimaryStateTax(companyId, employeeId, nonPrimaryStateTax)

Add/update non-primary state tax

Sends new or updated employee non-primary state tax information directly to Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.NonPrimaryStateTaxApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let nonPrimaryStateTax = new PaylocityApi.NonPrimaryStateTax(); // NonPrimaryStateTax | Non-Primary State Tax Model
apiInstance.addOrUpdateNonPrimaryStateTax(companyId, employeeId, nonPrimaryStateTax, (error, data, response) => {
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
 **nonPrimaryStateTax** | [**NonPrimaryStateTax**](NonPrimaryStateTax.md)| Non-Primary State Tax Model | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

