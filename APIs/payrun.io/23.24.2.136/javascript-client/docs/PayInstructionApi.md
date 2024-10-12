# PayRunIo.PayInstructionApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePayInstruction**](PayInstructionApi.md#deletePayInstruction) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId} | Deletes a pay instruction
[**getAllPayInstructionTags_0**](PayInstructionApi.md#getAllPayInstructionTags_0) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstructions/Tags | Get all pay instruction tags
[**getPayInstructionFromEmployee**](PayInstructionApi.md#getPayInstructionFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId} | Gets the specified pay instruction from the employee
[**getPayInstructionsFromEmployee**](PayInstructionApi.md#getPayInstructionsFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstructions | Gets the pay instructions from the specified employee
[**getPayInstructionsWithTag_0**](PayInstructionApi.md#getPayInstructionsWithTag_0) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstructions/Tag/{TagId} | Get pay instructions with tag
[**patchPayInstruction**](PayInstructionApi.md#patchPayInstruction) | **PATCH** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId} | Sparse Update of a Pay Instruction
[**postPayInstruction**](PayInstructionApi.md#postPayInstruction) | **POST** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstructions | Creates a new Pay Instruction
[**putPayInstruction**](PayInstructionApi.md#putPayInstruction) | **PUT** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId} | Update a Pay Instruction



## deletePayInstruction

> deletePayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion)

Deletes a pay instruction

Delete the specified pay instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **payInstructionId** | **String**| The pay instruction unique identifier. E.g. SAL001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPayInstructionTags_0

> LinkCollection getAllPayInstructionTags_0(employerId, employeeId, authorization, apiVersion)

Get all pay instruction tags

Gets all the pay instruction tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPayInstructionTags_0(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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


## getPayInstructionFromEmployee

> PayInstruction getPayInstructionFromEmployee(employerId, employeeId, payInstructionId, authorization, apiVersion)

Gets the specified pay instruction from the employee

Returns the specified pay instruction from employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayInstructionFromEmployee(employerId, employeeId, payInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **payInstructionId** | **String**| The pay instruction unique identifier. E.g. SAL001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**PayInstruction**](PayInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayInstructionsFromEmployee

> LinkCollection getPayInstructionsFromEmployee(employerId, employeeId, authorization, apiVersion)

Gets the pay instructions from the specified employee

Get links to all pay instructions for the specified employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayInstructionsFromEmployee(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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


## getPayInstructionsWithTag_0

> LinkCollection getPayInstructionsWithTag_0(employerId, employeeId, tagId, authorization, apiVersion)

Get pay instructions with tag

Gets the pay instructions with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayInstructionsWithTag_0(employerId, employeeId, tagId, authorization, apiVersion, (error, data, response) => {
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


## patchPayInstruction

> PayInstruction patchPayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion, payInstruction)

Sparse Update of a Pay Instruction

Patches the specified pay instruction with the supplied values

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let payInstruction = new PayRunIo.PayInstruction(); // PayInstruction | The pay instruction object.
apiInstance.patchPayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion, payInstruction, (error, data, response) => {
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
 **payInstructionId** | **String**| The pay instruction unique identifier. E.g. SAL001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **payInstruction** | [**PayInstruction**](PayInstruction.md)| The pay instruction object. | 

### Return type

[**PayInstruction**](PayInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPayInstruction

> Link postPayInstruction(employerId, employeeId, authorization, apiVersion, payInstruction)

Creates a new Pay Instruction

Creates a new pay instruction object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let payInstruction = new PayRunIo.PayInstruction(); // PayInstruction | The pay instruction object.
apiInstance.postPayInstruction(employerId, employeeId, authorization, apiVersion, payInstruction, (error, data, response) => {
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
 **payInstruction** | [**PayInstruction**](PayInstruction.md)| The pay instruction object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPayInstruction

> PayInstruction putPayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion, payInstruction)

Update a Pay Instruction

Updates the existing specified pay instruction object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayInstructionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let payInstruction = new PayRunIo.PayInstruction(); // PayInstruction | The pay instruction object.
apiInstance.putPayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion, payInstruction, (error, data, response) => {
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
 **payInstructionId** | **String**| The pay instruction unique identifier. E.g. SAL001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **payInstruction** | [**PayInstruction**](PayInstruction.md)| The pay instruction object. | 

### Return type

[**PayInstruction**](PayInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

