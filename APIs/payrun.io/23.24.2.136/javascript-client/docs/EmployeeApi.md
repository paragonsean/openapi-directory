# PayRunIo.EmployeeApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteEmployee**](EmployeeApi.md#deleteEmployee) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId} | Delete an Employee
[**deleteEmployeeRevision**](EmployeeApi.md#deleteEmployeeRevision) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId}/{EffectiveDate} | Delete an Employee revision matching the specified revision date.
[**deleteEmployeeRevisionByNumber**](EmployeeApi.md#deleteEmployeeRevisionByNumber) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId}/Revision/{RevisionNumber} | Delete an Employee revision matching the specified revision number.
[**deleteEmployeeSecret**](EmployeeApi.md#deleteEmployeeSecret) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId}/Secret/{SecretId} | Deletes employee secret
[**getAEAssessmentFromEmployee_0**](EmployeeApi.md#getAEAssessmentFromEmployee_0) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessment/{AEAssessmentId} | Get the auto enrolment assessment
[**getAEAssessmentsFromEmployee_0**](EmployeeApi.md#getAEAssessmentsFromEmployee_0) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessments | Get the auto enrolment assessments
[**getAllEmployeeTags_0**](EmployeeApi.md#getAllEmployeeTags_0) | **GET** /Employer/{EmployerId}/Employees/Tags | Get all employee tags
[**getCommentariesFromEmployee**](EmployeeApi.md#getCommentariesFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Commentaries | Get links to all commentaries for the specified employee
[**getCommentaryFromEmployee**](EmployeeApi.md#getCommentaryFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Commentary/{CommentaryId} | Get commentary from employee
[**getCommentaryFromPayRunByEmployee**](EmployeeApi.md#getCommentaryFromPayRunByEmployee) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId}/Employee/{EmployeeId}/Commentary | Get commentary from payrun by specified employee.
[**getEmployeeByEffectiveDate**](EmployeeApi.md#getEmployeeByEffectiveDate) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/{EffectiveDate} | Get employee by effective date.
[**getEmployeeFromEmployer**](EmployeeApi.md#getEmployeeFromEmployer) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId} | Get employee from employer
[**getEmployeeRevisionByNumber**](EmployeeApi.md#getEmployeeRevisionByNumber) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Revision/{RevisionNumber} | Gets the employee by revision number
[**getEmployeeRevisionSummaries**](EmployeeApi.md#getEmployeeRevisionSummaries) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Revisions/Summary | Get all employee revision summaries
[**getEmployeeRevisionSummaryByNumber**](EmployeeApi.md#getEmployeeRevisionSummaryByNumber) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Revision/{RevisionNumber}/Summary | Gets the employee summary by revision number
[**getEmployeeRevisions**](EmployeeApi.md#getEmployeeRevisions) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Revisions | Get all employee revisions
[**getEmployeeSecret**](EmployeeApi.md#getEmployeeSecret) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Secret/{SecretId} | Get employee secret
[**getEmployeeSecrets**](EmployeeApi.md#getEmployeeSecrets) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Secrets | Get all employee secret links
[**getEmployeeSummariesByEffectiveDate**](EmployeeApi.md#getEmployeeSummariesByEffectiveDate) | **GET** /Employer/{EmployerId}/Employees/{EffectiveDate}/Summary | Get employee summaries from employer at a given effective date.
[**getEmployeeSummariesFromEmployer**](EmployeeApi.md#getEmployeeSummariesFromEmployer) | **GET** /Employer/{EmployerId}/Employees/Summary | Get employee summaries from employer.
[**getEmployeeSummaryByEffectiveDate**](EmployeeApi.md#getEmployeeSummaryByEffectiveDate) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/{EffectiveDate}/Summary | Get employee summary by effective date.
[**getEmployeeSummaryFromEmployer**](EmployeeApi.md#getEmployeeSummaryFromEmployer) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Summary | Get employee summary from employer
[**getEmployeesByEffectiveDate**](EmployeeApi.md#getEmployeesByEffectiveDate) | **GET** /Employer/{EmployerId}/Employees/{EffectiveDate} | Get employees from employer at a given effective date.
[**getEmployeesFromEmployer**](EmployeeApi.md#getEmployeesFromEmployer) | **GET** /Employer/{EmployerId}/Employees | Get employees from employer.
[**getEmployeesFromPayRun**](EmployeeApi.md#getEmployeesFromPayRun) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId}/Employees | Get employees from the pay run
[**getEmployeesFromPaySchedule**](EmployeeApi.md#getEmployeesFromPaySchedule) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/Employees | Get all employees revisions from a pay schedule.
[**getEmployeesFromPayScheduleOnEffectiveDate**](EmployeeApi.md#getEmployeesFromPayScheduleOnEffectiveDate) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/Employees/{EffectiveDate} | Get employees from a pay schedule on effective date.
[**getEmployeesWithTag_0**](EmployeeApi.md#getEmployeesWithTag_0) | **GET** /Employer/{EmployerId}/Employees/Tag/{TagId} | Get employees with tag
[**getPayRunsFromEmployee_0**](EmployeeApi.md#getPayRunsFromEmployee_0) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayRuns | Gets the pay runs from the employee
[**patchEmployee**](EmployeeApi.md#patchEmployee) | **PATCH** /Employer/{EmployerId}/Employee/{EmployeeId} | Patches the employee
[**postEmployeeIntoEmployer**](EmployeeApi.md#postEmployeeIntoEmployer) | **POST** /Employer/{EmployerId}/Employees | Create a new Employee
[**postEmployeeSecret**](EmployeeApi.md#postEmployeeSecret) | **POST** /Employer/{EmployerId}/Employee/{EmployeeId}/Secrets | Create a new employee secret
[**putEmployeeIntoEmployer**](EmployeeApi.md#putEmployeeIntoEmployer) | **PUT** /Employer/{EmployerId}/Employee/{EmployeeId} | Updates the Employee
[**putEmployeeSecret**](EmployeeApi.md#putEmployeeSecret) | **PUT** /Employer/{EmployerId}/Employee/{EmployeeId}/Secret/{SecretId} | Create a new employee secret



## deleteEmployee

> deleteEmployee(employerId, employeeId, authorization, apiVersion)

Delete an Employee

Delete the specified employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteEmployee(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEmployeeRevision

> deleteEmployeeRevision(employerId, employeeId, effectiveDate, authorization, apiVersion)

Delete an Employee revision matching the specified revision date.

Deletes the specified employee revision for the matching revision date

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteEmployeeRevision(employerId, employeeId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **effectiveDate** | **Date**| The effective date to be applied. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEmployeeRevisionByNumber

> deleteEmployeeRevisionByNumber(employerId, employeeId, revisionNumber, authorization, apiVersion)

Delete an Employee revision matching the specified revision number.

Deletes the specified employee revision for the matching revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteEmployeeRevisionByNumber(employerId, employeeId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **revisionNumber** | **String**| The revision number. E.g. 1 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEmployeeSecret

> deleteEmployeeSecret(employerId, employeeId, secretId, authorization, apiVersion)

Deletes employee secret

Deletes an employee secret from the given resource location

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let secretId = "secretId_example"; // String | The secret unique identifier. E.g ERSEC001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteEmployeeSecret(employerId, employeeId, secretId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **secretId** | **String**| The secret unique identifier. E.g ERSEC001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAEAssessmentFromEmployee_0

> AEAssessment getAEAssessmentFromEmployee_0(employerId, employeeId, aEAssessmentId, authorization, apiVersion)

Get the auto enrolment assessment

Gets the auto enrolment assessment from the specified employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let aEAssessmentId = "aEAssessmentId_example"; // String | The auto enrolment assessment unique identifier. E.g. AE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAEAssessmentFromEmployee_0(employerId, employeeId, aEAssessmentId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **aEAssessmentId** | **String**| The auto enrolment assessment unique identifier. E.g. AE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**AEAssessment**](AEAssessment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAEAssessmentsFromEmployee_0

> LinkCollection getAEAssessmentsFromEmployee_0(employerId, employeeId, authorization, apiVersion)

Get the auto enrolment assessments

Gets all auto enrolment assessments from the specified employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAEAssessmentsFromEmployee_0(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllEmployeeTags_0

> LinkCollection getAllEmployeeTags_0(employerId, authorization, apiVersion)

Get all employee tags

Gets all the employee tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllEmployeeTags_0(employerId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCommentariesFromEmployee

> LinkCollection getCommentariesFromEmployee(employerId, employeeId, authorization, apiVersion)

Get links to all commentaries for the specified employee

Get links to all commentaries for the specified employee.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCommentariesFromEmployee(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCommentaryFromEmployee

> Commentary getCommentaryFromEmployee(employerId, employeeId, commentaryId, authorization, apiVersion)

Get commentary from employee

Gets the specified commentary report from the employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let commentaryId = "commentaryId_example"; // String | The commentary unique identifier. E.g. C001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCommentaryFromEmployee(employerId, employeeId, commentaryId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **commentaryId** | **String**| The commentary unique identifier. E.g. C001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Commentary**](Commentary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCommentaryFromPayRunByEmployee

> Commentary getCommentaryFromPayRunByEmployee(employerId, payScheduleId, payRunId, employeeId, authorization, apiVersion)

Get commentary from payrun by specified employee.

Get commentary from payrun by specified employee.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCommentaryFromPayRunByEmployee(employerId, payScheduleId, payRunId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **payScheduleId** | **String**| The pay schedules&#39; unique identifier. E.g SCH001 | 
 **payRunId** | **String**| The pay runs&#39; unique identifier. E.g. PR001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Commentary**](Commentary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeByEffectiveDate

> Employee getEmployeeByEffectiveDate(employerId, employeeId, effectiveDate, authorization, apiVersion)

Get employee by effective date.

Returns the employee&#39;s state at the specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeByEffectiveDate(employerId, employeeId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **effectiveDate** | **Date**| The effective date to be applied. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeFromEmployer

> Employee getEmployeeFromEmployer(employerId, employeeId, authorization, apiVersion)

Get employee from employer

Gets the specified employee from employer by employee code.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeFromEmployer(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeRevisionByNumber

> Employee getEmployeeRevisionByNumber(employerId, employeeId, revisionNumber, authorization, apiVersion)

Gets the employee by revision number

Get the employee revision matching the specified revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeRevisionByNumber(employerId, employeeId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **revisionNumber** | **String**| The revision number. E.g. 1 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeRevisionSummaries

> LinkCollection getEmployeeRevisionSummaries(employerId, employeeId, authorization, apiVersion)

Get all employee revision summaries

Gets links to all employee revision summaries

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeRevisionSummaries(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeRevisionSummaryByNumber

> EmployeeSummary getEmployeeRevisionSummaryByNumber(employerId, employeeId, revisionNumber, authorization, apiVersion)

Gets the employee summary by revision number

Get the employee revision summary matching the specified revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeRevisionSummaryByNumber(employerId, employeeId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **revisionNumber** | **String**| The revision number. E.g. 1 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**EmployeeSummary**](EmployeeSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeRevisions

> LinkCollection getEmployeeRevisions(employerId, employeeId, authorization, apiVersion)

Get all employee revisions

Gets links to all employee revisions

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeRevisions(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeSecret

> EmployeeSecret getEmployeeSecret(employerId, employeeId, secretId, authorization, apiVersion)

Get employee secret

Get the public visible employee secret object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let secretId = "secretId_example"; // String | The secret unique identifier. E.g ERSEC001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeSecret(employerId, employeeId, secretId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **secretId** | **String**| The secret unique identifier. E.g ERSEC001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**EmployeeSecret**](EmployeeSecret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeSecrets

> LinkCollection getEmployeeSecrets(employerId, employeeId, authorization, apiVersion)

Get all employee secret links

Get all the employee secret links

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeSecrets(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeSummariesByEffectiveDate

> LinkCollection getEmployeeSummariesByEffectiveDate(employerId, effectiveDate, authorization, apiVersion)

Get employee summaries from employer at a given effective date.

Get links to all employee summaries for the employer on specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeSummariesByEffectiveDate(employerId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **effectiveDate** | **Date**| The effective date to be applied. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeSummariesFromEmployer

> LinkCollection getEmployeeSummariesFromEmployer(employerId, authorization, apiVersion)

Get employee summaries from employer.

Get links to all employee summaries for the specified employer.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeSummariesFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeSummaryByEffectiveDate

> EmployeeSummary getEmployeeSummaryByEffectiveDate(employerId, employeeId, effectiveDate, authorization, apiVersion)

Get employee summary by effective date.

Gets the employee summary for the specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeSummaryByEffectiveDate(employerId, employeeId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **effectiveDate** | **Date**| The effective date to be applied. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**EmployeeSummary**](EmployeeSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeeSummaryFromEmployer

> EmployeeSummary getEmployeeSummaryFromEmployer(employerId, employeeId, authorization, apiVersion)

Get employee summary from employer

Gets the specified employee summary data from employer by employee code.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeeSummaryFromEmployer(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**EmployeeSummary**](EmployeeSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeesByEffectiveDate

> LinkCollection getEmployeesByEffectiveDate(employerId, effectiveDate, authorization, apiVersion)

Get employees from employer at a given effective date.

Get links to all employees for the employer on specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeesByEffectiveDate(employerId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **effectiveDate** | **Date**| The effective date to be applied. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeesFromEmployer

> LinkCollection getEmployeesFromEmployer(employerId, authorization, apiVersion)

Get employees from employer.

Get links to all employees for the specified employer.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeesFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeesFromPayRun

> LinkCollection getEmployeesFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion)

Get employees from the pay run

Gets links to all employees included in the specified pay run.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeesFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **payScheduleId** | **String**| The pay schedules&#39; unique identifier. E.g SCH001 | 
 **payRunId** | **String**| The pay runs&#39; unique identifier. E.g. PR001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeesFromPaySchedule

> LinkCollection getEmployeesFromPaySchedule(employerId, payScheduleId, authorization, apiVersion)

Get all employees revisions from a pay schedule.

Gets links to all employee revisions that have ever existed in the specified pay schedule.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeesFromPaySchedule(employerId, payScheduleId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **payScheduleId** | **String**| The pay schedules&#39; unique identifier. E.g SCH001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeesFromPayScheduleOnEffectiveDate

> LinkCollection getEmployeesFromPayScheduleOnEffectiveDate(employerId, payScheduleId, effectiveDate, authorization, apiVersion)

Get employees from a pay schedule on effective date.

Gets links to all employee revisions in the specified pay schedule for the given effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeesFromPayScheduleOnEffectiveDate(employerId, payScheduleId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **payScheduleId** | **String**| The pay schedules&#39; unique identifier. E.g SCH001 | 
 **effectiveDate** | **Date**| The effective date to be applied. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployeesWithTag_0

> LinkCollection getEmployeesWithTag_0(employerId, tagId, authorization, apiVersion)

Get employees with tag

Gets the employees with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeesWithTag_0(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayRunsFromEmployee_0

> LinkCollection getPayRunsFromEmployee_0(employerId, employeeId, authorization, apiVersion)

Gets the pay runs from the employee

Get links to all pay runs for the specified employee.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayRunsFromEmployee_0(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchEmployee

> Employee patchEmployee(employerId, employeeId, authorization, apiVersion, employee)

Patches the employee

Patches the specified employee with the supplied values

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let employee = new PayRunIo.Employee(); // Employee | The employee object.
apiInstance.patchEmployee(employerId, employeeId, authorization, apiVersion, employee, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **employee** | [**Employee**](Employee.md)| The employee object. | 

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postEmployeeIntoEmployer

> Link postEmployeeIntoEmployer(employerId, authorization, apiVersion, employee)

Create a new Employee

Create a new employee object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let employee = new PayRunIo.Employee(); // Employee | The employee object.
apiInstance.postEmployeeIntoEmployer(employerId, authorization, apiVersion, employee, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **employee** | [**Employee**](Employee.md)| The employee object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postEmployeeSecret

> Link postEmployeeSecret(employerId, employeeId, authorization, apiVersion)

Create a new employee secret

Create new employee secret using auto generated resource location key

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.postEmployeeSecret(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putEmployeeIntoEmployer

> Employee putEmployeeIntoEmployer(employerId, employeeId, authorization, apiVersion, employee)

Updates the Employee

Updates the existing specified employee object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let employee = new PayRunIo.Employee(); // Employee | The employee object.
apiInstance.putEmployeeIntoEmployer(employerId, employeeId, authorization, apiVersion, employee, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **employee** | [**Employee**](Employee.md)| The employee object. | 

### Return type

[**Employee**](Employee.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putEmployeeSecret

> EmployeeSecret putEmployeeSecret(employerId, employeeId, secretId, authorization, apiVersion)

Create a new employee secret

Create / update an employee secret at the given resource location

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployeeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let secretId = "secretId_example"; // String | The secret unique identifier. E.g ERSEC001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putEmployeeSecret(employerId, employeeId, secretId, authorization, apiVersion, (error, data, response) => {
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
 **employerId** | **String**| The employers&#39; unique identifier. E.g ER001 | 
 **employeeId** | **String**| The employees&#39; unique identifier. E.g EE001 | 
 **secretId** | **String**| The secret unique identifier. E.g ERSEC001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**EmployeeSecret**](EmployeeSecret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

