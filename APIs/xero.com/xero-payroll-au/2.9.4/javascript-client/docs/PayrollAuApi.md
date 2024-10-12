# XeroPayrollAuApi.PayrollAuApi

All URIs are relative to *https://api.xero.com/payroll.xro/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEmployee**](PayrollAuApi.md#createEmployee) | **POST** /Employees | Creates a payroll employee
[**createLeaveApplication**](PayrollAuApi.md#createLeaveApplication) | **POST** /LeaveApplications | Creates a leave application
[**createPayItem**](PayrollAuApi.md#createPayItem) | **POST** /PayItems | Creates a pay item
[**createPayRun**](PayrollAuApi.md#createPayRun) | **POST** /PayRuns | Creates a pay run
[**createPayrollCalendar**](PayrollAuApi.md#createPayrollCalendar) | **POST** /PayrollCalendars | Creates a Payroll Calendar
[**createSuperfund**](PayrollAuApi.md#createSuperfund) | **POST** /Superfunds | Creates a superfund
[**createTimesheet**](PayrollAuApi.md#createTimesheet) | **POST** /Timesheets | Creates a timesheet
[**getEmployee**](PayrollAuApi.md#getEmployee) | **GET** /Employees/{EmployeeID} | Retrieves an employee&#39;s detail by unique employee id
[**getEmployees**](PayrollAuApi.md#getEmployees) | **GET** /Employees | Searches payroll employees
[**getLeaveApplication**](PayrollAuApi.md#getLeaveApplication) | **GET** /LeaveApplications/{LeaveApplicationID} | Retrieves a leave application by a unique leave application id
[**getLeaveApplications**](PayrollAuApi.md#getLeaveApplications) | **GET** /LeaveApplications | Retrieves leave applications
[**getPayItems**](PayrollAuApi.md#getPayItems) | **GET** /PayItems | Retrieves pay items
[**getPayRun**](PayrollAuApi.md#getPayRun) | **GET** /PayRuns/{PayRunID} | Retrieves a pay run by using a unique pay run id
[**getPayRuns**](PayrollAuApi.md#getPayRuns) | **GET** /PayRuns | Retrieves pay runs
[**getPayrollCalendar**](PayrollAuApi.md#getPayrollCalendar) | **GET** /PayrollCalendars/{PayrollCalendarID} | Retrieves payroll calendar by using a unique payroll calendar ID
[**getPayrollCalendars**](PayrollAuApi.md#getPayrollCalendars) | **GET** /PayrollCalendars | Retrieves payroll calendars
[**getPayslip**](PayrollAuApi.md#getPayslip) | **GET** /Payslip/{PayslipID} | Retrieves for a payslip by a unique payslip id
[**getSettings**](PayrollAuApi.md#getSettings) | **GET** /Settings | Retrieves payroll settings
[**getSuperfund**](PayrollAuApi.md#getSuperfund) | **GET** /Superfunds/{SuperFundID} | Retrieves a superfund by using a unique superfund ID
[**getSuperfundProducts**](PayrollAuApi.md#getSuperfundProducts) | **GET** /SuperfundProducts | Retrieves superfund products
[**getSuperfunds**](PayrollAuApi.md#getSuperfunds) | **GET** /Superfunds | Retrieves superfunds
[**getTimesheet**](PayrollAuApi.md#getTimesheet) | **GET** /Timesheets/{TimesheetID} | Retrieves a timesheet by using a unique timesheet id
[**getTimesheets**](PayrollAuApi.md#getTimesheets) | **GET** /Timesheets | Retrieves timesheets
[**updateEmployee**](PayrollAuApi.md#updateEmployee) | **POST** /Employees/{EmployeeID} | Updates an employee&#39;s detail
[**updateLeaveApplication**](PayrollAuApi.md#updateLeaveApplication) | **POST** /LeaveApplications/{LeaveApplicationID} | Updates a specific leave application
[**updatePayRun**](PayrollAuApi.md#updatePayRun) | **POST** /PayRuns/{PayRunID} | Updates a pay run
[**updatePayslip**](PayrollAuApi.md#updatePayslip) | **POST** /Payslip/{PayslipID} | Updates a payslip
[**updateSuperfund**](PayrollAuApi.md#updateSuperfund) | **POST** /Superfunds/{SuperFundID} | Updates a superfund
[**updateTimesheet**](PayrollAuApi.md#updateTimesheet) | **POST** /Timesheets/{TimesheetID} | Updates a timesheet



## createEmployee

> Employees createEmployee(xeroTenantId, employee)

Creates a payroll employee

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let employee = [ { "FirstName": "Albus", "LastName": "Dumbledore", "DateOfBirth": "/Date(321523200000+0000)/", "HomeAddress": { "AddressLine1": "101 Green St", "City": "Island Bay", "Region": "NSW", "PostalCode": "6023", "Country": "AUSTRALIA" }, "StartDate": "/Date(321523200000+0000)/", "MiddleNames": "Percival", "Email": "albus39608@hogwarts.edu", "Gender": "M", "Phone": "444-2323", "Mobile": "555-1212", "IsAuthorisedToApproveLeave": true, "IsAuthorisedToApproveTimesheets": true, "JobTitle": "Regional Manager", "Classification": "corporate", "OrdinaryEarningsRateID": "ab874dfb-ab09-4c91-954e-43acf6fc23b4", "Status": "ACTIVE" } ]; // [Employee] | 
apiInstance.createEmployee(xeroTenantId, employee, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **employee** | [**[Employee]**](Employee.md)|  | 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLeaveApplication

> LeaveApplications createLeaveApplication(xeroTenantId, leaveApplication)

Creates a leave application

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let leaveApplication = [ { "EmployeeID": "cdfb8371-0b21-4b8a-8903-1024df6c391e", "LeaveTypeID": "184ea8f7-d143-46dd-bef3-0c60e1aa6fca", "Title": "Hello World", "StartDate": "/Date(1572559200000+0000)/", "EndDate": "/Date(1572645600000+0000)/" } ]; // [LeaveApplication] | 
apiInstance.createLeaveApplication(xeroTenantId, leaveApplication, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **leaveApplication** | [**[LeaveApplication]**](LeaveApplication.md)|  | 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPayItem

> PayItems createPayItem(xeroTenantId, payItem)

Creates a pay item

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let payItem = { "EarningsRates": [ { "Name": "MyRate", "AccountCode": "400", "TypeOfUnits": "4.00", "IsExemptFromTax": true, "IsExemptFromSuper": true, "IsReportableAsW1": false, "EarningsType": "ORDINARYTIMEEARNINGS", "EarningsRateID": "1fa4e226-b711-46ba-a8a7-4344c9c5fb87", "RateType": "MULTIPLE", "RatePerUnit": "10.0", "Multiplier": 1.5, "Amount": 5, "EmploymentTerminationPaymentType": "O" } ] }; // PayItem | 
apiInstance.createPayItem(xeroTenantId, payItem, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **payItem** | [**PayItem**](PayItem.md)|  | 

### Return type

[**PayItems**](PayItems.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPayRun

> PayRuns createPayRun(xeroTenantId, payRun)

Creates a pay run

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let payRun = [ { "PayrollCalendarID": "78bb86b9-e1ea-47ac-b75d-f087a81931de", "PayRunPeriodStartDate": "/Date(1572566400000+0000)/", "PayRunPeriodEndDate": "/Date(1573084800000+0000)/", "PayRunStatus": "DRAFT", "PaymentDate": "/Date(1573171200000+0000)/" } ]; // [PayRun] | 
apiInstance.createPayRun(xeroTenantId, payRun, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **payRun** | [**[PayRun]**](PayRun.md)|  | 

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPayrollCalendar

> PayrollCalendars createPayrollCalendar(xeroTenantId, payrollCalendar)

Creates a Payroll Calendar

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let payrollCalendar = [ { "PayrollCalendarID":"78bb86b9-e1ea-47ac-b75d-f087a81931de", "PayRunPeriodStartDate":"/Date(1572566400000+0000)/", "PayRunPeriodEndDate":"/Date(1573084800000+0000)/", "PayRunStatus":"DRAFT", "PaymentDate":"/Date(1573171200000+0000)/" } ]; // [PayrollCalendar] | 
apiInstance.createPayrollCalendar(xeroTenantId, payrollCalendar, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **payrollCalendar** | [**[PayrollCalendar]**](PayrollCalendar.md)|  | 

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSuperfund

> SuperFunds createSuperfund(xeroTenantId, superFund)

Creates a superfund

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let superFund = [ { "usi":"PTC0133AU", "Type":"REGULATED", "Name":"Bar99359", "AccountNumber":"FB36350", "AccountName":"Foo38428", "USI":"PTC0133AU" } ]; // [SuperFund] | 
apiInstance.createSuperfund(xeroTenantId, superFund, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **superFund** | [**[SuperFund]**](SuperFund.md)|  | 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTimesheet

> Timesheets createTimesheet(xeroTenantId, timesheet)

Creates a timesheet

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let timesheet = [ { "EmployeeID":"b34e89ff-770d-4099-b7e5-f968767118bc", "StartDate":"/Date(1573171200000+0000)/", "EndDate":"/Date(1573689600000+0000)/", "Status":"DRAFT", "TimesheetLines":[ { "EarningsRateID":"ab874dfb-ab09-4c91-954e-43acf6fc23b4", "TrackingItemID":"af5e9ce2-2349-4136-be99-3561b189f473", "NumberOfUnits":[ 2.0, 10.0, 0.0, 0.0, 5.0, 0.0, 5.0 ] } ] } ]; // [Timesheet] | 
apiInstance.createTimesheet(xeroTenantId, timesheet, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **timesheet** | [**[Timesheet]**](Timesheet.md)|  | 

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getEmployee

> Employees getEmployee(xeroTenantId, employeeID)

Retrieves an employee&#39;s detail by unique employee id

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let employeeID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Employee id for single object
apiInstance.getEmployee(xeroTenantId, employeeID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **employeeID** | **String**| Employee id for single object | 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployees

> Employees getEmployees(xeroTenantId, opts)

Searches payroll employees

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': "ifModifiedSince_example", // String | Only records created or modified since this timestamp will be returned
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "EmailAddress%20DESC", // String | Order by an any element
  'page': 56 // Number | e.g. page=1 – Up to 100 employees will be returned in a single API call
};
apiInstance.getEmployees(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 employees will be returned in a single API call | [optional] 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLeaveApplication

> LeaveApplications getLeaveApplication(xeroTenantId, leaveApplicationID)

Retrieves a leave application by a unique leave application id

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let leaveApplicationID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Leave Application id for single object
apiInstance.getLeaveApplication(xeroTenantId, leaveApplicationID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **leaveApplicationID** | **String**| Leave Application id for single object | 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLeaveApplications

> LeaveApplications getLeaveApplications(xeroTenantId, opts)

Retrieves leave applications

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': "ifModifiedSince_example", // String | Only records created or modified since this timestamp will be returned
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "EmailAddress%20DESC", // String | Order by an any element
  'page': 56 // Number | e.g. page=1 – Up to 100 objects will be returned in a single API call
};
apiInstance.getLeaveApplications(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayItems

> PayItems getPayItems(xeroTenantId, opts)

Retrieves pay items

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': "ifModifiedSince_example", // String | Only records created or modified since this timestamp will be returned
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "EmailAddress%20DESC", // String | Order by an any element
  'page': 56 // Number | e.g. page=1 – Up to 100 objects will be returned in a single API call
};
apiInstance.getPayItems(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**PayItems**](PayItems.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayRun

> PayRuns getPayRun(xeroTenantId, payRunID)

Retrieves a pay run by using a unique pay run id

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let payRunID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | PayRun id for single object
apiInstance.getPayRun(xeroTenantId, payRunID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **payRunID** | **String**| PayRun id for single object | 

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayRuns

> PayRuns getPayRuns(xeroTenantId, opts)

Retrieves pay runs

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': "ifModifiedSince_example", // String | Only records created or modified since this timestamp will be returned
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "EmailAddress%20DESC", // String | Order by an any element
  'page': 56 // Number | e.g. page=1 – Up to 100 PayRuns will be returned in a single API call
};
apiInstance.getPayRuns(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 PayRuns will be returned in a single API call | [optional] 

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayrollCalendar

> PayrollCalendars getPayrollCalendar(xeroTenantId, payrollCalendarID)

Retrieves payroll calendar by using a unique payroll calendar ID

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let payrollCalendarID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Payroll Calendar id for single object
apiInstance.getPayrollCalendar(xeroTenantId, payrollCalendarID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **payrollCalendarID** | **String**| Payroll Calendar id for single object | 

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayrollCalendars

> PayrollCalendars getPayrollCalendars(xeroTenantId, opts)

Retrieves payroll calendars

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': "ifModifiedSince_example", // String | Only records created or modified since this timestamp will be returned
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "EmailAddress%20DESC", // String | Order by an any element
  'page': 56 // Number | e.g. page=1 – Up to 100 objects will be returned in a single API call
};
apiInstance.getPayrollCalendars(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call | [optional] 

### Return type

[**PayrollCalendars**](PayrollCalendars.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayslip

> PayslipObject getPayslip(xeroTenantId, payslipID)

Retrieves for a payslip by a unique payslip id

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let payslipID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Payslip id for single object
apiInstance.getPayslip(xeroTenantId, payslipID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **payslipID** | **String**| Payslip id for single object | 

### Return type

[**PayslipObject**](PayslipObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSettings

> SettingsObject getSettings(xeroTenantId)

Retrieves payroll settings

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
apiInstance.getSettings(xeroTenantId, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 

### Return type

[**SettingsObject**](SettingsObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSuperfund

> SuperFunds getSuperfund(xeroTenantId, superFundID)

Retrieves a superfund by using a unique superfund ID

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let superFundID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Superfund id for single object
apiInstance.getSuperfund(xeroTenantId, superFundID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **superFundID** | **String**| Superfund id for single object | 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSuperfundProducts

> SuperFundProducts getSuperfundProducts(xeroTenantId, opts)

Retrieves superfund products

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'ABN': "40022701955", // String | The ABN of the Regulated SuperFund
  'USI': "OSF0001AU" // String | The USI of the Regulated SuperFund
};
apiInstance.getSuperfundProducts(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ABN** | **String**| The ABN of the Regulated SuperFund | [optional] 
 **USI** | **String**| The USI of the Regulated SuperFund | [optional] 

### Return type

[**SuperFundProducts**](SuperFundProducts.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSuperfunds

> SuperFunds getSuperfunds(xeroTenantId, opts)

Retrieves superfunds

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': "ifModifiedSince_example", // String | Only records created or modified since this timestamp will be returned
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "EmailAddress%20DESC", // String | Order by an any element
  'page': 56 // Number | e.g. page=1 – Up to 100 SuperFunds will be returned in a single API call
};
apiInstance.getSuperfunds(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 SuperFunds will be returned in a single API call | [optional] 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTimesheet

> TimesheetObject getTimesheet(xeroTenantId, timesheetID)

Retrieves a timesheet by using a unique timesheet id

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let timesheetID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Timesheet id for single object
apiInstance.getTimesheet(xeroTenantId, timesheetID, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **timesheetID** | **String**| Timesheet id for single object | 

### Return type

[**TimesheetObject**](TimesheetObject.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTimesheets

> Timesheets getTimesheets(xeroTenantId, opts)

Retrieves timesheets

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let opts = {
  'ifModifiedSince': "ifModifiedSince_example", // String | Only records created or modified since this timestamp will be returned
  'where': "Status==\"ACTIVE\"", // String | Filter by an any element
  'order': "EmailAddress%20DESC", // String | Order by an any element
  'page': 56 // Number | e.g. page=1 – Up to 100 timesheets will be returned in a single API call
};
apiInstance.getTimesheets(xeroTenantId, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **ifModifiedSince** | **String**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **String**| Filter by an any element | [optional] 
 **order** | **String**| Order by an any element | [optional] 
 **page** | **Number**| e.g. page&#x3D;1 – Up to 100 timesheets will be returned in a single API call | [optional] 

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateEmployee

> Employees updateEmployee(xeroTenantId, employeeID, opts)

Updates an employee&#39;s detail

Update properties on a single employee

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let employeeID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Employee id for single object
let opts = {
  'employee': [ { "MiddleNames": "Frank" } ] // [Employee] | 
};
apiInstance.updateEmployee(xeroTenantId, employeeID, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **employeeID** | **String**| Employee id for single object | 
 **employee** | [**[Employee]**](Employee.md)|  | [optional] 

### Return type

[**Employees**](Employees.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateLeaveApplication

> LeaveApplications updateLeaveApplication(xeroTenantId, leaveApplicationID, leaveApplication)

Updates a specific leave application

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let leaveApplicationID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Leave Application id for single object
let leaveApplication = [ { "EmployeeID": "cdfb8371-0b21-4b8a-8903-1024df6c391e", "LeaveTypeID": "184ea8f7-d143-46dd-bef3-0c60e1aa6fca", "StartDate": "/Date(1572559200000+0000)/", "EndDate": "/Date(1572645600000+0000)/", "Description": "My updated Description" } ]; // [LeaveApplication] | 
apiInstance.updateLeaveApplication(xeroTenantId, leaveApplicationID, leaveApplication, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **leaveApplicationID** | **String**| Leave Application id for single object | 
 **leaveApplication** | [**[LeaveApplication]**](LeaveApplication.md)|  | 

### Return type

[**LeaveApplications**](LeaveApplications.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePayRun

> PayRuns updatePayRun(xeroTenantId, payRunID, opts)

Updates a pay run

Update properties on a single PayRun

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let payRunID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | PayRun id for single object
let opts = {
  'payRun': [new XeroPayrollAuApi.PayRun()] // [PayRun] | 
};
apiInstance.updatePayRun(xeroTenantId, payRunID, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **payRunID** | **String**| PayRun id for single object | 
 **payRun** | [**[PayRun]**](PayRun.md)|  | [optional] 

### Return type

[**PayRuns**](PayRuns.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePayslip

> Payslips updatePayslip(xeroTenantId, payslipID, opts)

Updates a payslip

Update lines on a single payslips

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let payslipID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Payslip id for single object
let opts = {
  'payslipLines': { "Payslip": { "EmployeeID": "cdfb8371-0b21-4b8a-8903-1024df6c391e", "DeductionLines": [ { "DeductionTypeID": "727af5e8-b347-4ae7-85fc-9b82266d0aec", "CalculationType": "FIXEDAMOUNT", "NumberOfUnits": 10 } ] } } // [PayslipLines] | 
};
apiInstance.updatePayslip(xeroTenantId, payslipID, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **payslipID** | **String**| Payslip id for single object | 
 **payslipLines** | [**[PayslipLines]**](PayslipLines.md)|  | [optional] 

### Return type

[**Payslips**](Payslips.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSuperfund

> SuperFunds updateSuperfund(xeroTenantId, superFundID, opts)

Updates a superfund

Update properties on a single Superfund

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let superFundID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Superfund id for single object
let opts = {
  'superFund':  [ { "Type":"REGULATED", "Name":"Nice23534" } ] // [SuperFund] | 
};
apiInstance.updateSuperfund(xeroTenantId, superFundID, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **superFundID** | **String**| Superfund id for single object | 
 **superFund** | [**[SuperFund]**](SuperFund.md)|  | [optional] 

### Return type

[**SuperFunds**](SuperFunds.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTimesheet

> Timesheets updateTimesheet(xeroTenantId, timesheetID, opts)

Updates a timesheet

Update properties on a single timesheet

### Example

```javascript
import XeroPayrollAuApi from 'xero_payroll_au_api';
let defaultClient = XeroPayrollAuApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new XeroPayrollAuApi.PayrollAuApi();
let xeroTenantId = "xeroTenantId_example"; // String | Xero identifier for Tenant
let timesheetID = "4ff1e5cc-9835-40d5-bb18-09fdb118db9c"; // String | Timesheet id for single object
let opts = {
  'timesheet': [ { "EmployeeID":"b34e89ff-770d-4099-b7e5-f968767118bc", "StartDate":"/Date(1573171200000+0000)/", "EndDate":"/Date(1573689600000+0000)/", "Status":"APPROVED", "Hours":22.0, "TimesheetID":"a7eb0a79-8511-4ee7-b473-3a25f28abcb9", "TimesheetLines":[ { "EarningsRateID":"ab874dfb-ab09-4c91-954e-43acf6fc23b4", "TrackingItemID":"af5e9ce2-2349-4136-be99-3561b189f473", "NumberOfUnits":[ 2.0, 10.0, 0.0, 0.0, 5.0, 0.0, 5.0 ], "UpdatedDateUTC":"/Date(1573516185127+0000)/" } ] } ] // [Timesheet] | 
};
apiInstance.updateTimesheet(xeroTenantId, timesheetID, opts, (error, data, response) => {
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
 **xeroTenantId** | **String**| Xero identifier for Tenant | 
 **timesheetID** | **String**| Timesheet id for single object | 
 **timesheet** | [**[Timesheet]**](Timesheet.md)|  | [optional] 

### Return type

[**Timesheets**](Timesheets.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

