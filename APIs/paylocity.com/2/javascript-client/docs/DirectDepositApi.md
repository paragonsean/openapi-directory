# PaylocityApi.DirectDepositApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllDirectDeposit**](DirectDepositApi.md#getAllDirectDeposit) | **GET** /v2/companies/{companyId}/employees/{employeeId}/directDeposit | Get All Direct Deposit



## getAllDirectDeposit

> [DirectDeposit] getAllDirectDeposit(companyId, employeeId)

Get All Direct Deposit

Get All Direct Deposit returns main direct deposit and all additional direct depositsfor the selected employee.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.DirectDepositApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
apiInstance.getAllDirectDeposit(companyId, employeeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 

### Return type

[**[DirectDeposit]**](DirectDeposit.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

