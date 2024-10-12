# PayRunIo.AEAssessmentApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAEAssessment**](AEAssessmentApi.md#deleteAEAssessment) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessment/{AEAssessmentId} | Delete auto enrolment assessment
[**getAEAssessmentFromEmployee**](AEAssessmentApi.md#getAEAssessmentFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessment/{AEAssessmentId} | Get the auto enrolment assessment
[**getAEAssessmentsFromEmployee**](AEAssessmentApi.md#getAEAssessmentsFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessments | Get the auto enrolment assessments
[**getAEAssessmentsFromPayRun**](AEAssessmentApi.md#getAEAssessmentsFromPayRun) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId}/AEAssessments | Get the auto enrolment assessments
[**postNewAEAssessment**](AEAssessmentApi.md#postNewAEAssessment) | **POST** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessments | Insert new auto enrolment assessment
[**putNewAEAssessment**](AEAssessmentApi.md#putNewAEAssessment) | **PUT** /Employer/{EmployerId}/Employee/{EmployeeId}/AEAssessment/{AEAssessmentId} | Insert new auto enrolment assessment



## deleteAEAssessment

> deleteAEAssessment(employerId, employeeId, aEAssessmentId, authorization, apiVersion)

Delete auto enrolment assessment

Deletes an existing auto enrolment assessment for the employee. Used to remove historical assessments

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.AEAssessmentApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let aEAssessmentId = "aEAssessmentId_example"; // String | The auto enrolment assessment unique identifier. E.g. AE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteAEAssessment(employerId, employeeId, aEAssessmentId, authorization, apiVersion, (error, data, response) => {
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
 **aEAssessmentId** | **String**| The auto enrolment assessment unique identifier. E.g. AE001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAEAssessmentFromEmployee

> AEAssessment getAEAssessmentFromEmployee(employerId, employeeId, aEAssessmentId, authorization, apiVersion)

Get the auto enrolment assessment

Gets the auto enrolment assessment from the specified employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.AEAssessmentApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let aEAssessmentId = "aEAssessmentId_example"; // String | The auto enrolment assessment unique identifier. E.g. AE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAEAssessmentFromEmployee(employerId, employeeId, aEAssessmentId, authorization, apiVersion, (error, data, response) => {
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


## getAEAssessmentsFromEmployee

> LinkCollection getAEAssessmentsFromEmployee(employerId, employeeId, authorization, apiVersion)

Get the auto enrolment assessments

Gets all auto enrolment assessments from the specified employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.AEAssessmentApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAEAssessmentsFromEmployee(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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


## getAEAssessmentsFromPayRun

> LinkCollection getAEAssessmentsFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion)

Get the auto enrolment assessments

Gets all auto enrolment assessments from the specified pay run

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.AEAssessmentApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAEAssessmentsFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion, (error, data, response) => {
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


## postNewAEAssessment

> Link postNewAEAssessment(employerId, employeeId, authorization, apiVersion, aEAssessment)

Insert new auto enrolment assessment

Creates a new auto enrolment assessment for the employee. Used to insert historical assessments

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.AEAssessmentApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let aEAssessment = new PayRunIo.AEAssessment(); // AEAssessment | The auto enrolment assessment object.
apiInstance.postNewAEAssessment(employerId, employeeId, authorization, apiVersion, aEAssessment, (error, data, response) => {
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
 **aEAssessment** | [**AEAssessment**](AEAssessment.md)| The auto enrolment assessment object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putNewAEAssessment

> AEAssessment putNewAEAssessment(employerId, employeeId, aEAssessmentId, authorization, apiVersion, aEAssessment)

Insert new auto enrolment assessment

Creates a new auto enrolment assessment for the employee. Used to insert historical assessments

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.AEAssessmentApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let aEAssessmentId = "aEAssessmentId_example"; // String | The auto enrolment assessment unique identifier. E.g. AE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let aEAssessment = new PayRunIo.AEAssessment(); // AEAssessment | The auto enrolment assessment object.
apiInstance.putNewAEAssessment(employerId, employeeId, aEAssessmentId, authorization, apiVersion, aEAssessment, (error, data, response) => {
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
 **aEAssessment** | [**AEAssessment**](AEAssessment.md)| The auto enrolment assessment object. | 

### Return type

[**AEAssessment**](AEAssessment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

