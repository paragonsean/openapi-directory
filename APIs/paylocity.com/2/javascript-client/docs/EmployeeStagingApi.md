# PaylocityApi.EmployeeStagingApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addNewEmployeeToWebLink**](EmployeeStagingApi.md#addNewEmployeeToWebLink) | **POST** /v2/weblinkstaging/companies/{companyId}/employees/newemployees | Add new employee to Web Link



## addNewEmployeeToWebLink

> [TrackingNumberResponse] addNewEmployeeToWebLink(companyId, stagedEmployee)

Add new employee to Web Link

Add new employee to Web Link will send partially completed or potentially erroneous new hire record to Web Link, where it can be corrected and competed by company administrator or authorized Paylocity Service Bureau employee.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EmployeeStagingApi();
let companyId = "companyId_example"; // String | Company Id
let stagedEmployee = new PaylocityApi.StagedEmployee(); // StagedEmployee | StagedEmployee Model
apiInstance.addNewEmployeeToWebLink(companyId, stagedEmployee, (error, data, response) => {
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
 **stagedEmployee** | [**StagedEmployee**](StagedEmployee.md)| StagedEmployee Model | 

### Return type

[**[TrackingNumberResponse]**](TrackingNumberResponse.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

