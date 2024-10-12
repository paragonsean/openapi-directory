# PaylocityApi.PrimaryStateTaxApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOrUpdatePrimaryStateTax**](PrimaryStateTaxApi.md#addOrUpdatePrimaryStateTax) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/primaryStateTax | Add/update primary state tax



## addOrUpdatePrimaryStateTax

> addOrUpdatePrimaryStateTax(companyId, employeeId, stateTax)

Add/update primary state tax

Sends new or updated employee primary state tax information directly to Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.PrimaryStateTaxApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let stateTax = new PaylocityApi.StateTax(); // StateTax | Primary State Tax Model
apiInstance.addOrUpdatePrimaryStateTax(companyId, employeeId, stateTax, (error, data, response) => {
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
 **stateTax** | [**StateTax**](StateTax.md)| Primary State Tax Model | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

