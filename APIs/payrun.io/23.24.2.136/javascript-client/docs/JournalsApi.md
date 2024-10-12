# PayRunIo.JournalsApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteJournalInstruction**](JournalsApi.md#deleteJournalInstruction) | **DELETE** /Employer/{EmployerId}/JournalInstruction/{JournalInstructionId} | Deletes a Journal instruction
[**deleteJournalInstructionTemplate**](JournalsApi.md#deleteJournalInstructionTemplate) | **DELETE** /JournalInstruction/{JournalInstructionId} | Deletes a Journal instruction template
[**getJournalInstructionFromEmployer**](JournalsApi.md#getJournalInstructionFromEmployer) | **GET** /Employer/{EmployerId}/JournalInstruction/{JournalInstructionId} | Gets the specified journal instruction from the employer
[**getJournalInstructionTemplate**](JournalsApi.md#getJournalInstructionTemplate) | **GET** /JournalInstruction/{JournalInstructionId} | Gets the Journal instructions template for the application
[**getJournalInstructionTemplates**](JournalsApi.md#getJournalInstructionTemplates) | **GET** /JournalInstructions | Gets the Journal instructions templates for the application
[**getJournalInstructionsFromEmployer**](JournalsApi.md#getJournalInstructionsFromEmployer) | **GET** /Employer/{EmployerId}/JournalInstructions | Gets the Journal instructions from the specified employer
[**getJournalLineFromEmployer**](JournalsApi.md#getJournalLineFromEmployer) | **GET** /Employer/{EmployerId}/JournalLine/{JournalLineId} | Gets the specified journal Line from the employer
[**getJournalLinesFromEmployee**](JournalsApi.md#getJournalLinesFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/JournalLines | Gets the journal Lines from the specified employee
[**getJournalLinesFromEmployer**](JournalsApi.md#getJournalLinesFromEmployer) | **GET** /Employer/{EmployerId}/JournalLines | Gets the Journal Lines from the specified employer
[**getJournalLinesFromPayRun**](JournalsApi.md#getJournalLinesFromPayRun) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId}/JournalLines | Gets the journal Lines from the specified pay run
[**getJournalLinesFromSubContractor**](JournalsApi.md#getJournalLinesFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/JournalLines | Gets the journal Lines from the specified sub contractor
[**postJournalInstruction**](JournalsApi.md#postJournalInstruction) | **POST** /Employer/{EmployerId}/JournalInstructions | Creates a new Journal Instruction
[**postJournalInstructionTemplate**](JournalsApi.md#postJournalInstructionTemplate) | **POST** /JournalInstructions | Creates a new Journal Instruction template
[**putJournalInstruction**](JournalsApi.md#putJournalInstruction) | **PUT** /Employer/{EmployerId}/JournalInstruction/{JournalInstructionId} | Update a Journal Instruction
[**putJournalInstructionTemplate**](JournalsApi.md#putJournalInstructionTemplate) | **PUT** /JournalInstruction/{JournalInstructionId} | Update a Journal Instruction template



## deleteJournalInstruction

> deleteJournalInstruction(employerId, journalInstructionId, authorization, apiVersion)

Deletes a Journal instruction

Delete the specified Journal instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteJournalInstruction(employerId, journalInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteJournalInstructionTemplate

> deleteJournalInstructionTemplate(journalInstructionId, authorization, apiVersion)

Deletes a Journal instruction template

Delete the specified Journal instruction template object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteJournalInstructionTemplate(journalInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJournalInstructionFromEmployer

> JournalInstruction getJournalInstructionFromEmployer(employerId, journalInstructionId, authorization, apiVersion)

Gets the specified journal instruction from the employer

Returns the specified journal instruction from employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getJournalInstructionFromEmployer(employerId, journalInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JournalInstruction**](JournalInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJournalInstructionTemplate

> JournalInstruction getJournalInstructionTemplate(journalInstructionId, authorization, apiVersion)

Gets the Journal instructions template for the application

Retrurns the specified journal instruction from the application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getJournalInstructionTemplate(journalInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JournalInstruction**](JournalInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJournalInstructionTemplates

> LinkCollection getJournalInstructionTemplates(authorization, apiVersion)

Gets the Journal instructions templates for the application

Get links to all journal instruction templates for the application

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getJournalInstructionTemplates(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJournalInstructionsFromEmployer

> LinkCollection getJournalInstructionsFromEmployer(employerId, authorization, apiVersion)

Gets the Journal instructions from the specified employer

Get links to all journal instructions for the specified employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getJournalInstructionsFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## getJournalLineFromEmployer

> JournalLine getJournalLineFromEmployer(employerId, journalLineId, authorization, apiVersion)

Gets the specified journal Line from the employer

Returns the specified journal Line from employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalLineId = "journalLineId_example"; // String | The journal line unique identifier. E.g JL001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getJournalLineFromEmployer(employerId, journalLineId, authorization, apiVersion, (error, data, response) => {
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
 **journalLineId** | **String**| The journal line unique identifier. E.g JL001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JournalLine**](JournalLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJournalLinesFromEmployee

> LinkCollection getJournalLinesFromEmployee(employerId, employeeId, authorization, apiVersion)

Gets the journal Lines from the specified employee

Get links to all journal lines for the specified employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getJournalLinesFromEmployee(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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


## getJournalLinesFromEmployer

> LinkCollection getJournalLinesFromEmployer(employerId, authorization, apiVersion)

Gets the Journal Lines from the specified employer

Get links to all journal Lines for the specified employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getJournalLinesFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## getJournalLinesFromPayRun

> LinkCollection getJournalLinesFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion)

Gets the journal Lines from the specified pay run

Get links to all journal lines for the specified pay run

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getJournalLinesFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion, (error, data, response) => {
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


## getJournalLinesFromSubContractor

> LinkCollection getJournalLinesFromSubContractor(employerId, subContractorId, authorization, apiVersion)

Gets the journal Lines from the specified sub contractor

Get links to all journal lines for the specified sub contractor

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getJournalLinesFromSubContractor(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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
 **subContractorId** | **String**| The sub contractors&#39; unique identifier. E.g SUB001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postJournalInstruction

> Link postJournalInstruction(employerId, authorization, apiVersion)

Creates a new Journal Instruction

Creates a new Journal instruction object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.postJournalInstruction(employerId, authorization, apiVersion, (error, data, response) => {
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

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postJournalInstructionTemplate

> Link postJournalInstructionTemplate(authorization, apiVersion)

Creates a new Journal Instruction template

Creates a new Journal instruction teamplte object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.postJournalInstructionTemplate(authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putJournalInstruction

> JournalInstruction putJournalInstruction(employerId, journalInstructionId, authorization, apiVersion)

Update a Journal Instruction

Updates the existing specified Journal instruction object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putJournalInstruction(employerId, journalInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JournalInstruction**](JournalInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putJournalInstructionTemplate

> JournalInstruction putJournalInstructionTemplate(journalInstructionId, authorization, apiVersion)

Update a Journal Instruction template

Updates the existing specified Journal instruction template object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalsApi();
let journalInstructionId = "journalInstructionId_example"; // String | The journal instruction unique identifier. E.g JI001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putJournalInstructionTemplate(journalInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **journalInstructionId** | **String**| The journal instruction unique identifier. E.g JI001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**JournalInstruction**](JournalInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

