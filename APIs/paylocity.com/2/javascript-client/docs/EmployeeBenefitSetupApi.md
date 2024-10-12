# PaylocityApi.EmployeeBenefitSetupApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateOrAddEmployeeBenefitSetup**](EmployeeBenefitSetupApi.md#updateOrAddEmployeeBenefitSetup) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/benefitSetup | Add/update employee&#39;s benefit setup



## updateOrAddEmployeeBenefitSetup

> updateOrAddEmployeeBenefitSetup(companyId, employeeId, benefitSetup)

Add/update employee&#39;s benefit setup

Sends new or updated employee benefit setup information directly to Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EmployeeBenefitSetupApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let benefitSetup = new PaylocityApi.BenefitSetup(); // BenefitSetup | BenefitSetup Model
apiInstance.updateOrAddEmployeeBenefitSetup(companyId, employeeId, benefitSetup, (error, data, response) => {
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
 **benefitSetup** | [**BenefitSetup**](BenefitSetup.md)| BenefitSetup Model | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

