# PayRunIo.ReportLineInstructionApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteReportingInstruction**](ReportLineInstructionApi.md#deleteReportingInstruction) | **DELETE** /Employer/{EmployerId}/ReportingInstruction/{ReportingInstructionId} | Deletes a reporting instruction
[**getReportingInstructionFromEmployer**](ReportLineInstructionApi.md#getReportingInstructionFromEmployer) | **GET** /Employer/{EmployerId}/ReportingInstruction/{ReportingInstructionId} | Gets the specified reporting instruction from the employer
[**getReportingInstructionsFromEmployer**](ReportLineInstructionApi.md#getReportingInstructionsFromEmployer) | **GET** /Employer/{EmployerId}/ReportingInstructions | Gets the reporting instructions from the specified employer
[**postReportingInstruction**](ReportLineInstructionApi.md#postReportingInstruction) | **POST** /Employer/{EmployerId}/ReportingInstructions | Creates a new Reporting Instruction
[**putReportingInstruction**](ReportLineInstructionApi.md#putReportingInstruction) | **PUT** /Employer/{EmployerId}/ReportingInstruction/{ReportingInstructionId} | Update a reporting Instruction



## deleteReportingInstruction

> deleteReportingInstruction(employerId, reportingInstructionId, authorization, apiVersion)

Deletes a reporting instruction

Delete the specified reporting instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportLineInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let reportingInstructionId = "reportingInstructionId_example"; // String | The reporting instruction unique identifier. E.g. SERRPT001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteReportingInstruction(employerId, reportingInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **reportingInstructionId** | **String**| The reporting instruction unique identifier. E.g. SERRPT001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportingInstructionFromEmployer

> ReportingInstruction getReportingInstructionFromEmployer(employerId, reportingInstructionId, authorization, apiVersion)

Gets the specified reporting instruction from the employer

Returns the specified pay instruction from employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportLineInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let reportingInstructionId = "reportingInstructionId_example"; // String | The reporting instruction unique identifier. E.g. SERRPT001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getReportingInstructionFromEmployer(employerId, reportingInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **reportingInstructionId** | **String**| The reporting instruction unique identifier. E.g. SERRPT001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**ReportingInstruction**](ReportingInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getReportingInstructionsFromEmployer

> LinkCollection getReportingInstructionsFromEmployer(employerId, authorization, apiVersion)

Gets the reporting instructions from the specified employer

Get links to all pay instructions for the specified employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportLineInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getReportingInstructionsFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## postReportingInstruction

> Link postReportingInstruction(employerId, authorization, apiVersion, reportingInstruction)

Creates a new Reporting Instruction

Creates a new reporting instruction object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportLineInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let reportingInstruction = new PayRunIo.ReportingInstruction(); // ReportingInstruction | The reporting instruction object.
apiInstance.postReportingInstruction(employerId, authorization, apiVersion, reportingInstruction, (error, data, response) => {
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
 **reportingInstruction** | [**ReportingInstruction**](ReportingInstruction.md)| The reporting instruction object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putReportingInstruction

> ReportingInstruction putReportingInstruction(employerId, reportingInstructionId, authorization, apiVersion, reportingInstruction)

Update a reporting Instruction

Updates the existing specified reporting instruction object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReportLineInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let reportingInstructionId = "reportingInstructionId_example"; // String | The reporting instruction unique identifier. E.g. SERRPT001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let reportingInstruction = new PayRunIo.ReportingInstruction(); // ReportingInstruction | The reporting instruction object.
apiInstance.putReportingInstruction(employerId, reportingInstructionId, authorization, apiVersion, reportingInstruction, (error, data, response) => {
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
 **reportingInstructionId** | **String**| The reporting instruction unique identifier. E.g. SERRPT001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **reportingInstruction** | [**ReportingInstruction**](ReportingInstruction.md)| The reporting instruction object. | 

### Return type

[**ReportingInstruction**](ReportingInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

