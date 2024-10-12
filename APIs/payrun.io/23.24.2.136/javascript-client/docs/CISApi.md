# PayRunIo.CISApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteCisInstruction**](CISApi.md#deleteCisInstruction) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId} | Delete a CIS instruction
[**deleteCisInstructionTag_0**](CISApi.md#deleteCisInstructionTag_0) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tag/{TagId} | Delete CIS instruction tag
[**deleteCisLine**](CISApi.md#deleteCisLine) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId} | Delete a CIS line
[**deleteCisLineTag_0**](CISApi.md#deleteCisLineTag_0) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tag/{TagId} | Delete CIS line tag
[**deleteCisLineType**](CISApi.md#deleteCisLineType) | **DELETE** /Employer/{EmployerId}/CisLineType/{CisLineTypeId} | Delete an CIS line type
[**deleteCisLineTypeTag_0**](CISApi.md#deleteCisLineTypeTag_0) | **DELETE** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tag/{TagId} | Delete CIS line type tag
[**deleteCisTransaction**](CISApi.md#deleteCisTransaction) | **DELETE** /Employer/{EmployerId}/CisTransaction/{CisTransactionId} | Delete the CIS transaction
[**deleteSubContractorTag_0**](CISApi.md#deleteSubContractorTag_0) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId} | Delete sub contractor tag
[**getAllCisInstructionTags_0**](CISApi.md#getAllCisInstructionTags_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstructions/Tags | Get all CIS instruction tags
[**getAllCisLineTags_0**](CISApi.md#getAllCisLineTags_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLines/Tags | Get all CIS line tags
[**getAllCisLineTypeTags_0**](CISApi.md#getAllCisLineTypeTags_0) | **GET** /Employer/{EmployerId}/CisLineTypes/Tags | Get all CIS line type tags
[**getAllSubContractorTags_0**](CISApi.md#getAllSubContractorTags_0) | **GET** /Employer/{EmployerId}/SubContractors/Tags | Get all sub contractor tags
[**getCisInstructionFromSubContractor**](CISApi.md#getCisInstructionFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId} | Get CIS instruction from sub contractor
[**getCisInstructionsFromSubContractor**](CISApi.md#getCisInstructionsFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstructions | Get CIS instructions from sub contractor.
[**getCisInstructionsWithTag_0**](CISApi.md#getCisInstructionsWithTag_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstructions/Tag/{TagId} | Get CIS instructions with tag
[**getCisLineFromSubContractor**](CISApi.md#getCisLineFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId} | Get CIS line from sub contractor
[**getCisLineTypeFromEmployer**](CISApi.md#getCisLineTypeFromEmployer) | **GET** /Employer/{EmployerId}/CisLineType/{CisLineTypeId} | Get CIS line type from employer
[**getCisLineTypesFromEmployer**](CISApi.md#getCisLineTypesFromEmployer) | **GET** /Employer/{EmployerId}/CisLineTypes | Get CIS line types from employer.
[**getCisLineTypesWithTag_0**](CISApi.md#getCisLineTypesWithTag_0) | **GET** /Employer/{EmployerId}/CisLineTypes/Tag/{TagId} | Get CIS line types with tag
[**getCisLinesFromSubContractor**](CISApi.md#getCisLinesFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLines | Get CIS lines from sub contractor.
[**getCisLinesWithTag_0**](CISApi.md#getCisLinesWithTag_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLines/Tag/{TagId} | Get CIS lines with tag
[**getCisTransactionFromEmployer**](CISApi.md#getCisTransactionFromEmployer) | **GET** /Employer/{EmployerId}/CisTransaction/{CisTransactionId} | Get the CIS transaction
[**getCisTransactionsFromEmployer**](CISApi.md#getCisTransactionsFromEmployer) | **GET** /Employer/{EmployerId}/CisTransactions | Get all CIS transactions for the employer
[**getSubContractorsWithTag_0**](CISApi.md#getSubContractorsWithTag_0) | **GET** /Employer/{EmployerId}/SubContractors/Tag/{TagId} | Get sub contractors with tag
[**getTagFromCisInstruction_0**](CISApi.md#getTagFromCisInstruction_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tag/{TagId} | Get CIS instruction tag
[**getTagFromCisLineType_0**](CISApi.md#getTagFromCisLineType_0) | **GET** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tag/{TagId} | Get CIS line type tag
[**getTagFromCisLine_0**](CISApi.md#getTagFromCisLine_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tag/{TagId} | Get CIS line tag
[**getTagFromSubContractorRevision_0**](CISApi.md#getTagFromSubContractorRevision_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId}/{EffectiveDate} | Get sub contractor revision tag
[**getTagFromSubContractor_0**](CISApi.md#getTagFromSubContractor_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId} | Get sub contractor tag
[**getTagsFromCisInstruction_0**](CISApi.md#getTagsFromCisInstruction_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tags | Get all tags from the CIS instruction
[**getTagsFromCisLineType_0**](CISApi.md#getTagsFromCisLineType_0) | **GET** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tags | Get all tags from the CIS line type
[**getTagsFromCisLine_0**](CISApi.md#getTagsFromCisLine_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tags | Get all tags from the CIS line
[**getTagsFromSubContractorRevision_0**](CISApi.md#getTagsFromSubContractorRevision_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tags/{EffectiveDate} | Get all sub contractor revision tags
[**getTagsFromSubContractor_0**](CISApi.md#getTagsFromSubContractor_0) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tags | Get all tags from the sub contractor
[**patchCisInstruction**](CISApi.md#patchCisInstruction) | **PATCH** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId} | Patches the CIS instruction
[**postCisInstructionIntoSubContractor**](CISApi.md#postCisInstructionIntoSubContractor) | **POST** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstructions | Create a new CIS instruction
[**postCisLineTypeIntoEmployer**](CISApi.md#postCisLineTypeIntoEmployer) | **POST** /Employer/{EmployerId}/CisLineTypes | Create a new CIS line type
[**putCisInstructionIntoSubContractor**](CISApi.md#putCisInstructionIntoSubContractor) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId} | Updates the CIS instruction
[**putCisInstructionTag_0**](CISApi.md#putCisInstructionTag_0) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tag/{TagId} | Insert CIS instruction tag
[**putCisLineTag_0**](CISApi.md#putCisLineTag_0) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tag/{TagId} | Insert CIS line tag
[**putCisLineTypeIntoEmployer**](CISApi.md#putCisLineTypeIntoEmployer) | **PUT** /Employer/{EmployerId}/CisLineType/{CisLineTypeId} | Updates the CIS line type
[**putCisLineTypeTag_0**](CISApi.md#putCisLineTypeTag_0) | **PUT** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tag/{TagId} | Insert CIS line type tag
[**putSubContractorTag_0**](CISApi.md#putSubContractorTag_0) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId} | Insert sub contractor tag



## deleteCisInstruction

> deleteCisInstruction(employerId, subContractorId, cisInstructionId, authorization, apiVersion)

Delete a CIS instruction

Delete the specified CIS instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisInstruction(employerId, subContractorId, cisInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **subContractorId** | **String**| The sub contractors&#39; unique identifier. E.g SUB001 | 
 **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCisInstructionTag_0

> deleteCisInstructionTag_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion)

Delete CIS instruction tag

Deletes a tag from the CIS instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisInstructionTag_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **subContractorId** | **String**| The sub contractors&#39; unique identifier. E.g SUB001 | 
 **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCisLine

> deleteCisLine(employerId, subContractorId, cisLineId, authorization, apiVersion)

Delete a CIS line

Delete the specified CIS line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisLine(employerId, subContractorId, cisLineId, authorization, apiVersion, (error, data, response) => {
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
 **subContractorId** | **String**| The sub contractors&#39; unique identifier. E.g SUB001 | 
 **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCisLineTag_0

> deleteCisLineTag_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion)

Delete CIS line tag

Deletes a tag from the CIS line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisLineTag_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **subContractorId** | **String**| The sub contractors&#39; unique identifier. E.g SUB001 | 
 **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCisLineType

> deleteCisLineType(employerId, cisLineTypeId, authorization, apiVersion)

Delete an CIS line type

Delete the specified CIS line type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisLineType(employerId, cisLineTypeId, authorization, apiVersion, (error, data, response) => {
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
 **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCisLineTypeTag_0

> deleteCisLineTypeTag_0(employerId, cisLineTypeId, tagId, authorization, apiVersion)

Delete CIS line type tag

Deletes a tag from the CIS line type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisLineTypeTag_0(employerId, cisLineTypeId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCisTransaction

> deleteCisTransaction(employerId, cisTransactionId, authorization, apiVersion)

Delete the CIS transaction

Deletes the specified CIS transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisTransactionId = "cisTransactionId_example"; // String | The CIS transaction unique identifier. E.g. CISTRAN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisTransaction(employerId, cisTransactionId, authorization, apiVersion, (error, data, response) => {
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
 **cisTransactionId** | **String**| The CIS transaction unique identifier. E.g. CISTRAN001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSubContractorTag_0

> deleteSubContractorTag_0(employerId, subContractorId, tagId, authorization, apiVersion)

Delete sub contractor tag

Deletes a tag from the sub contractor

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteSubContractorTag_0(employerId, subContractorId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **subContractorId** | **String**| The sub contractors&#39; unique identifier. E.g SUB001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllCisInstructionTags_0

> LinkCollection getAllCisInstructionTags_0(employerId, subContractorId, authorization, apiVersion)

Get all CIS instruction tags

Gets all the CIS instruction tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllCisInstructionTags_0(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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


## getAllCisLineTags_0

> LinkCollection getAllCisLineTags_0(employerId, subContractorId, authorization, apiVersion)

Get all CIS line tags

Gets all the CIS line tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllCisLineTags_0(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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


## getAllCisLineTypeTags_0

> LinkCollection getAllCisLineTypeTags_0(employerId, authorization, apiVersion)

Get all CIS line type tags

Gets all the CIS line type tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllCisLineTypeTags_0(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllSubContractorTags_0

> LinkCollection getAllSubContractorTags_0(employerId, authorization, apiVersion)

Get all sub contractor tags

Gets all the sub contractor tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllSubContractorTags_0(employerId, authorization, apiVersion, (error, data, response) => {
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


## getCisInstructionFromSubContractor

> CisInstruction getCisInstructionFromSubContractor(employerId, subContractorId, cisInstructionId, authorization, apiVersion)

Get CIS instruction from sub contractor

Gets the specified CIS instruction from sub contractor.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisInstructionFromSubContractor(employerId, subContractorId, cisInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**CisInstruction**](CisInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCisInstructionsFromSubContractor

> LinkCollection getCisInstructionsFromSubContractor(employerId, subContractorId, authorization, apiVersion)

Get CIS instructions from sub contractor.

Get links to all CIS instructions for the specified sub contractor.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisInstructionsFromSubContractor(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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


## getCisInstructionsWithTag_0

> LinkCollection getCisInstructionsWithTag_0(employerId, subContractorId, tagId, authorization, apiVersion)

Get CIS instructions with tag

Gets the CIS instruction with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisInstructionsWithTag_0(employerId, subContractorId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getCisLineFromSubContractor

> CisLine getCisLineFromSubContractor(employerId, subContractorId, cisLineId, authorization, apiVersion)

Get CIS line from sub contractor

Gets the specified CIS line from sub contractor.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisLineFromSubContractor(employerId, subContractorId, cisLineId, authorization, apiVersion, (error, data, response) => {
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
 **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**CisLine**](CisLine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCisLineTypeFromEmployer

> CisLineType getCisLineTypeFromEmployer(employerId, cisLineTypeId, authorization, apiVersion)

Get CIS line type from employer

Gets the specified CIS line type from employer.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisLineTypeFromEmployer(employerId, cisLineTypeId, authorization, apiVersion, (error, data, response) => {
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
 **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**CisLineType**](CisLineType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCisLineTypesFromEmployer

> LinkCollection getCisLineTypesFromEmployer(employerId, authorization, apiVersion)

Get CIS line types from employer.

Get links to all CIS line types for the specified employer.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisLineTypesFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## getCisLineTypesWithTag_0

> LinkCollection getCisLineTypesWithTag_0(employerId, tagId, authorization, apiVersion)

Get CIS line types with tag

Gets the CIS line type with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisLineTypesWithTag_0(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getCisLinesFromSubContractor

> LinkCollection getCisLinesFromSubContractor(employerId, subContractorId, authorization, apiVersion)

Get CIS lines from sub contractor.

Get links to all CIS lines for the specified sub contractor.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisLinesFromSubContractor(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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


## getCisLinesWithTag_0

> LinkCollection getCisLinesWithTag_0(employerId, subContractorId, tagId, authorization, apiVersion)

Get CIS lines with tag

Gets the CIS line with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisLinesWithTag_0(employerId, subContractorId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getCisTransactionFromEmployer

> CisTransaction getCisTransactionFromEmployer(employerId, cisTransactionId, authorization, apiVersion)

Get the CIS transaction

Returns the specified CIS transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisTransactionId = "cisTransactionId_example"; // String | The CIS transaction unique identifier. E.g. CISTRAN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisTransactionFromEmployer(employerId, cisTransactionId, authorization, apiVersion, (error, data, response) => {
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
 **cisTransactionId** | **String**| The CIS transaction unique identifier. E.g. CISTRAN001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**CisTransaction**](CisTransaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCisTransactionsFromEmployer

> LinkCollection getCisTransactionsFromEmployer(employerId, authorization, apiVersion)

Get all CIS transactions for the employer

Get links for all CIS transactions for the specified employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisTransactionsFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## getSubContractorsWithTag_0

> LinkCollection getSubContractorsWithTag_0(employerId, tagId, authorization, apiVersion)

Get sub contractors with tag

Gets the sub contractor with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getSubContractorsWithTag_0(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromCisInstruction_0

> Tag getTagFromCisInstruction_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion)

Get CIS instruction tag

Gets the tag from the CIS instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromCisInstruction_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagFromCisLineType_0

> Tag getTagFromCisLineType_0(employerId, cisLineTypeId, tagId, authorization, apiVersion)

Get CIS line type tag

Gets the tag from the CIS line type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromCisLineType_0(employerId, cisLineTypeId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagFromCisLine_0

> Tag getTagFromCisLine_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion)

Get CIS line tag

Gets the tag from the CIS line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromCisLine_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagFromSubContractorRevision_0

> Tag getTagFromSubContractorRevision_0(employerId, subContractorId, tagId, effectiveDate, authorization, apiVersion)

Get sub contractor revision tag

Gets the tag from the sub contractor revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromSubContractorRevision_0(employerId, subContractorId, tagId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **effectiveDate** | **Date**| The effective date to be applied. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagFromSubContractor_0

> Tag getTagFromSubContractor_0(employerId, subContractorId, tagId, authorization, apiVersion)

Get sub contractor tag

Gets the tag from the sub contractor

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromSubContractor_0(employerId, subContractorId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromCisInstruction_0

> LinkCollection getTagsFromCisInstruction_0(employerId, subContractorId, cisInstructionId, authorization, apiVersion)

Get all tags from the CIS instruction

Gets all the tags from the CIS instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromCisInstruction_0(employerId, subContractorId, cisInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromCisLineType_0

> LinkCollection getTagsFromCisLineType_0(employerId, cisLineTypeId, authorization, apiVersion)

Get all tags from the CIS line type

Gets all the tags from the CIS line type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromCisLineType_0(employerId, cisLineTypeId, authorization, apiVersion, (error, data, response) => {
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
 **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromCisLine_0

> LinkCollection getTagsFromCisLine_0(employerId, subContractorId, cisLineId, authorization, apiVersion)

Get all tags from the CIS line

Gets all the tags from the CIS line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromCisLine_0(employerId, subContractorId, cisLineId, authorization, apiVersion, (error, data, response) => {
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
 **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromSubContractorRevision_0

> LinkCollection getTagsFromSubContractorRevision_0(employerId, subContractorId, effectiveDate, authorization, apiVersion)

Get all sub contractor revision tags

Gets all the tags from the sub contractor revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromSubContractorRevision_0(employerId, subContractorId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromSubContractor_0

> LinkCollection getTagsFromSubContractor_0(employerId, subContractorId, authorization, apiVersion)

Get all tags from the sub contractor

Gets all the tags from the sub contractor

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromSubContractor_0(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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


## patchCisInstruction

> CisInstruction patchCisInstruction(employerId, subContractorId, cisInstructionId, authorization, apiVersion)

Patches the CIS instruction

Update an existing CIS instruction object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.patchCisInstruction(employerId, subContractorId, cisInstructionId, authorization, apiVersion, (error, data, response) => {
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
 **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**CisInstruction**](CisInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postCisInstructionIntoSubContractor

> Link postCisInstructionIntoSubContractor(employerId, subContractorId, authorization, apiVersion, cisInstruction)

Create a new CIS instruction

Create a new CIS instruction object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let cisInstruction = new PayRunIo.CisInstruction(); // CisInstruction | The CIS instruction object.
apiInstance.postCisInstructionIntoSubContractor(employerId, subContractorId, authorization, apiVersion, cisInstruction, (error, data, response) => {
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
 **cisInstruction** | [**CisInstruction**](CisInstruction.md)| The CIS instruction object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postCisLineTypeIntoEmployer

> Link postCisLineTypeIntoEmployer(employerId, authorization, apiVersion, cisLineType)

Create a new CIS line type

Create a new CIS line type object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let cisLineType = new PayRunIo.CisLineType(); // CisLineType | The CIS line type object.
apiInstance.postCisLineTypeIntoEmployer(employerId, authorization, apiVersion, cisLineType, (error, data, response) => {
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
 **cisLineType** | [**CisLineType**](CisLineType.md)| The CIS line type object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putCisInstructionIntoSubContractor

> CisInstruction putCisInstructionIntoSubContractor(employerId, subContractorId, cisInstructionId, authorization, apiVersion, cisInstruction)

Updates the CIS instruction

Insert or update existing CIS instruction object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let cisInstruction = new PayRunIo.CisInstruction(); // CisInstruction | The CIS instruction object.
apiInstance.putCisInstructionIntoSubContractor(employerId, subContractorId, cisInstructionId, authorization, apiVersion, cisInstruction, (error, data, response) => {
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
 **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **cisInstruction** | [**CisInstruction**](CisInstruction.md)| The CIS instruction object. | 

### Return type

[**CisInstruction**](CisInstruction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putCisInstructionTag_0

> Tag putCisInstructionTag_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion)

Insert CIS instruction tag

Inserts a new tag on the CIS instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putCisInstructionTag_0(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **cisInstructionId** | **String**| The CIS instruction unique identifier. E.g. CIS001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putCisLineTag_0

> Tag putCisLineTag_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion)

Insert CIS line tag

Inserts a new tag on the CIS line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putCisLineTag_0(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **cisLineId** | **String**| The CIS line unique identifier. E.g. CISLN001 | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putCisLineTypeIntoEmployer

> CisLineType putCisLineTypeIntoEmployer(employerId, cisLineTypeId, authorization, apiVersion, cisLineType)

Updates the CIS line type

Updates the existing specified CIS line type object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let cisLineType = new PayRunIo.CisLineType(); // CisLineType | The CIS line type object.
apiInstance.putCisLineTypeIntoEmployer(employerId, cisLineTypeId, authorization, apiVersion, cisLineType, (error, data, response) => {
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
 **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **cisLineType** | [**CisLineType**](CisLineType.md)| The CIS line type object. | 

### Return type

[**CisLineType**](CisLineType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putCisLineTypeTag_0

> Tag putCisLineTypeTag_0(employerId, cisLineTypeId, tagId, authorization, apiVersion)

Insert CIS line type tag

Inserts a new tag on the CIS line type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putCisLineTypeTag_0(employerId, cisLineTypeId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **cisLineTypeId** | **String**| The CIS line type unique identifier. E.g. TYPEA | 
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putSubContractorTag_0

> Tag putSubContractorTag_0(employerId, subContractorId, tagId, authorization, apiVersion)

Insert sub contractor tag

Inserts a new tag on the sub contractor

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.CISApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putSubContractorTag_0(employerId, subContractorId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **tagId** | **String**| The tag unique identifier. E.g. MyTag | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

