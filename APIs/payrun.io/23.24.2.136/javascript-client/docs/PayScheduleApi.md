# PayRunIo.PayScheduleApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePaySchedule**](PayScheduleApi.md#deletePaySchedule) | **DELETE** /Employer/{EmployerId}/PaySchedule/{PayScheduleId} | Deletes a pay schedule
[**getAllPayScheduleTags_0**](PayScheduleApi.md#getAllPayScheduleTags_0) | **GET** /Employer/{EmployerId}/PaySchedules/Tags | Get all pay schedule tags
[**getEmployeesFromPayScheduleOnEffectiveDate_0**](PayScheduleApi.md#getEmployeesFromPayScheduleOnEffectiveDate_0) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/Employees/{EffectiveDate} | Get employees from a pay schedule on effective date.
[**getEmployeesFromPaySchedule_0**](PayScheduleApi.md#getEmployeesFromPaySchedule_0) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/Employees | Get all employees revisions from a pay schedule.
[**getPayRunFromPaySchedule_0**](PayScheduleApi.md#getPayRunFromPaySchedule_0) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId} | Gets the pay run from the pay schedule
[**getPayRunsFromPaySchedule_0**](PayScheduleApi.md#getPayRunsFromPaySchedule_0) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRuns | Gets the pay runs from the pay schedule
[**getPayScheduleFromEmployer**](PayScheduleApi.md#getPayScheduleFromEmployer) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId} | Gets the specified pay schedule from the employer
[**getPaySchedulesFromEmployer**](PayScheduleApi.md#getPaySchedulesFromEmployer) | **GET** /Employer/{EmployerId}/PaySchedules | Gets the pay schedule from the specified employer
[**getPaySchedulesWithTag_0**](PayScheduleApi.md#getPaySchedulesWithTag_0) | **GET** /Employer/{EmployerId}/PaySchedules/Tag/{TagId} | Get pay schedule with tag
[**postPaySchedule**](PayScheduleApi.md#postPaySchedule) | **POST** /Employer/{EmployerId}/PaySchedules | Create a new pay schedule
[**putPaySchedule**](PayScheduleApi.md#putPaySchedule) | **PUT** /Employer/{EmployerId}/PaySchedule/{PayScheduleId} | Updates a pay schedule



## deletePaySchedule

> deletePaySchedule(employerId, payScheduleId, authorization, apiVersion)

Deletes a pay schedule

Delete the specified pay schedule

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePaySchedule(employerId, payScheduleId, authorization, apiVersion, (error, data, response) => {
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
 **payScheduleId** | **String**| The pay schedules&#39; unique identifier. E.g SCH001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPayScheduleTags_0

> LinkCollection getAllPayScheduleTags_0(employerId, authorization, apiVersion)

Get all pay schedule tags

Gets all the pay schedule tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPayScheduleTags_0(employerId, authorization, apiVersion, (error, data, response) => {
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


## getEmployeesFromPayScheduleOnEffectiveDate_0

> LinkCollection getEmployeesFromPayScheduleOnEffectiveDate_0(employerId, payScheduleId, effectiveDate, authorization, apiVersion)

Get employees from a pay schedule on effective date.

Gets links to all employee revisions in the specified pay schedule for the given effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeesFromPayScheduleOnEffectiveDate_0(employerId, payScheduleId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getEmployeesFromPaySchedule_0

> LinkCollection getEmployeesFromPaySchedule_0(employerId, payScheduleId, authorization, apiVersion)

Get all employees revisions from a pay schedule.

Gets links to all employee revisions that have ever existed in the specified pay schedule.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeesFromPaySchedule_0(employerId, payScheduleId, authorization, apiVersion, (error, data, response) => {
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


## getPayRunFromPaySchedule_0

> PayRun getPayRunFromPaySchedule_0(employerId, payScheduleId, payRunId, authorization, apiVersion)

Gets the pay run from the pay schedule

Returns the pay run from the pay schedule

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayRunFromPaySchedule_0(employerId, payScheduleId, payRunId, authorization, apiVersion, (error, data, response) => {
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

[**PayRun**](PayRun.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayRunsFromPaySchedule_0

> LinkCollection getPayRunsFromPaySchedule_0(employerId, payScheduleId, authorization, apiVersion)

Gets the pay runs from the pay schedule

Get links to all pay runs for the specified pay schedule

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayRunsFromPaySchedule_0(employerId, payScheduleId, authorization, apiVersion, (error, data, response) => {
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


## getPayScheduleFromEmployer

> PaySchedule getPayScheduleFromEmployer(employerId, payScheduleId, authorization, apiVersion)

Gets the specified pay schedule from the employer

Returns the specified pay schedule object from employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayScheduleFromEmployer(employerId, payScheduleId, authorization, apiVersion, (error, data, response) => {
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

[**PaySchedule**](PaySchedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPaySchedulesFromEmployer

> LinkCollection getPaySchedulesFromEmployer(employerId, authorization, apiVersion)

Gets the pay schedule from the specified employer

Get links to all pay schedules for the specified employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPaySchedulesFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## getPaySchedulesWithTag_0

> LinkCollection getPaySchedulesWithTag_0(employerId, tagId, authorization, apiVersion)

Get pay schedule with tag

Gets the pay schedules with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPaySchedulesWithTag_0(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## postPaySchedule

> Link postPaySchedule(employerId, authorization, apiVersion, paySchedule)

Create a new pay schedule

Create a new pay schedule object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let paySchedule = new PayRunIo.PaySchedule(); // PaySchedule | The pay schedule object.
apiInstance.postPaySchedule(employerId, authorization, apiVersion, paySchedule, (error, data, response) => {
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
 **paySchedule** | [**PaySchedule**](PaySchedule.md)| The pay schedule object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPaySchedule

> PaySchedule putPaySchedule(employerId, payScheduleId, authorization, apiVersion, paySchedule)

Updates a pay schedule

Updates the existing specified pay schedule object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayScheduleApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let paySchedule = new PayRunIo.PaySchedule(); // PaySchedule | The pay schedule object.
apiInstance.putPaySchedule(employerId, payScheduleId, authorization, apiVersion, paySchedule, (error, data, response) => {
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
 **paySchedule** | [**PaySchedule**](PaySchedule.md)| The pay schedule object. | 

### Return type

[**PaySchedule**](PaySchedule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

