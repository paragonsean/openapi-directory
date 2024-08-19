# PaylocityApi.EmployeeApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addEmployee**](EmployeeApi.md#addEmployee) | **POST** /v2/companies/{companyId}/employees | Add new employee
[**getAllEmployees**](EmployeeApi.md#getAllEmployees) | **GET** /v2/companies/{companyId}/employees/ | Get all employees
[**getEmployee**](EmployeeApi.md#getEmployee) | **GET** /v2/companies/{companyId}/employees/{employeeId} | Get employee
[**updateEmployee**](EmployeeApi.md#updateEmployee) | **PATCH** /v2/companies/{companyId}/employees/{employeeId} | Update employee



## addEmployee

> EmployeeIdResponse addEmployee(companyId, employee)

Add new employee

New Employee API sends new employee data directly to Web Pay. Companies who use the New Hire Template in Web Pay may require additional fields when hiring employees. New Employee API Requests will honor these required fields.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EmployeeApi();
let companyId = "companyId_example"; // String | Company Id
let employee = new PaylocityApi.Employee(); // Employee | Employee Model
apiInstance.addEmployee(companyId, employee, (error, data, response) => {
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
 **employee** | [**Employee**](Employee.md)| Employee Model | 

### Return type

[**EmployeeIdResponse**](EmployeeIdResponse.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAllEmployees

> [EmployeeInfo] getAllEmployees(companyId, opts)

Get all employees

Get All Employees API will return employee data currently available in Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EmployeeApi();
let companyId = "companyId_example"; // String | Company Id
let opts = {
  'pagesize': 56, // Number | Number of records per page. Default value is 25.
  'pagenumber': 56, // Number | Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber=0). Default value is 0.
  'includetotalcount': true // Boolean | Whether to include the total record count in the header's X-Pcty-Total-Count property. Default value is true.
};
apiInstance.getAllEmployees(companyId, opts, (error, data, response) => {
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
 **pagesize** | **Number**| Number of records per page. Default value is 25. | [optional] 
 **pagenumber** | **Number**| Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0. | [optional] 
 **includetotalcount** | **Boolean**| Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true. | [optional] 

### Return type

[**[EmployeeInfo]**](EmployeeInfo.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployee

> Employee getEmployee(companyId, employeeId)

Get employee

Get Employee API will return employee data currently available in Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EmployeeApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
apiInstance.getEmployee(companyId, employeeId, (error, data, response) => {
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

[**Employee**](Employee.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateEmployee

> updateEmployee(companyId, employeeId, employee)

Update employee

Update Employee API will update existing employee data in WebPay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EmployeeApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let employee = new PaylocityApi.Employee(); // Employee | Employee Model
apiInstance.updateEmployee(companyId, employeeId, employee, (error, data, response) => {
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
 **employee** | [**Employee**](Employee.md)| Employee Model | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

