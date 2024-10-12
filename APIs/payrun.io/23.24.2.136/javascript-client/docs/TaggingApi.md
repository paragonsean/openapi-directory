# PayRunIo.TaggingApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteCisInstructionTag**](TaggingApi.md#deleteCisInstructionTag) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tag/{TagId} | Delete CIS instruction tag
[**deleteCisLineTag**](TaggingApi.md#deleteCisLineTag) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tag/{TagId} | Delete CIS line tag
[**deleteCisLineTypeTag**](TaggingApi.md#deleteCisLineTypeTag) | **DELETE** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tag/{TagId} | Delete CIS line type tag
[**deleteEmployeeTag**](TaggingApi.md#deleteEmployeeTag) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId}/Tag/{TagId} | Delete employee tag
[**deleteEmployerTag**](TaggingApi.md#deleteEmployerTag) | **DELETE** /Employer/{EmployerId}/Tag/{TagId} | Delete employer tag
[**deleteHolidaySchemeTag**](TaggingApi.md#deleteHolidaySchemeTag) | **DELETE** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId} | Delete holiday scheme tag
[**deleteJournalLineTag**](TaggingApi.md#deleteJournalLineTag) | **DELETE** /Employer/{EmployerId}/JournalLine/{JournalLineId}/Tag/{TagId} | Delete journal line tag
[**deletePayCodeTag**](TaggingApi.md#deletePayCodeTag) | **DELETE** /Employer/{EmployerId}/PayCode/{PayCodeId}/Tag/{TagId} | Delete pay code tag
[**deletePayInstructionTag**](TaggingApi.md#deletePayInstructionTag) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId}/Tag/{TagId} | Delete pay instruction tag
[**deletePayLineTag**](TaggingApi.md#deletePayLineTag) | **DELETE** /Employer/{EmployerId}/Employee/{EmployeeId}/PayLine/{PayLineId}/Tag/{TagId} | Delete pay line tag
[**deletePayRunTag**](TaggingApi.md#deletePayRunTag) | **DELETE** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId}/Tag/{TagId} | Delete pay run tag
[**deletePayScheduleTag**](TaggingApi.md#deletePayScheduleTag) | **DELETE** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/Tag/{TagId} | Delete pay schedule tag
[**deletePermissionTag**](TaggingApi.md#deletePermissionTag) | **DELETE** /Permission/{PermissionId}/Tag/{TagId} | Delete Permission tag
[**deleteRtiTransactionTag**](TaggingApi.md#deleteRtiTransactionTag) | **DELETE** /Employer/{EmployerId}/RtiTransaction/{RtiTransactionId}/Tag/{TagId} | Delete RTI transaction tag
[**deleteSubContractorTag**](TaggingApi.md#deleteSubContractorTag) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId} | Delete sub contractor tag
[**deleteThirdPartyTransactionTag**](TaggingApi.md#deleteThirdPartyTransactionTag) | **DELETE** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId}/Tag/{TagId} | Delete third party transaction tag
[**deleteUserTag**](TaggingApi.md#deleteUserTag) | **DELETE** /User/{UserId}/Tag/{TagId} | Delete user tag
[**getAllCisInstructionTags**](TaggingApi.md#getAllCisInstructionTags) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstructions/Tags | Get all CIS instruction tags
[**getAllCisLineTags**](TaggingApi.md#getAllCisLineTags) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLines/Tags | Get all CIS line tags
[**getAllCisLineTypeTags**](TaggingApi.md#getAllCisLineTypeTags) | **GET** /Employer/{EmployerId}/CisLineTypes/Tags | Get all CIS line type tags
[**getAllEmployeeTags**](TaggingApi.md#getAllEmployeeTags) | **GET** /Employer/{EmployerId}/Employees/Tags | Get all employee tags
[**getAllEmployerTags**](TaggingApi.md#getAllEmployerTags) | **GET** /Employers/Tags | Get all employer tags
[**getAllHolidaySchemeTags**](TaggingApi.md#getAllHolidaySchemeTags) | **GET** /Employer/{EmployerId}/HolidaySchemes/Tags | Get all holiday scheme tags
[**getAllJournalLineTags**](TaggingApi.md#getAllJournalLineTags) | **GET** /Employer/{EmployerId}/JournalLines/Tags | Get all journal line tags
[**getAllJournalLinesWithTag**](TaggingApi.md#getAllJournalLinesWithTag) | **GET** /Employer/{EmployerId}/JournalLines/Tag/{TagId} | Get links to tagged journal lines
[**getAllPayCodeTags**](TaggingApi.md#getAllPayCodeTags) | **GET** /Employer/{EmployerId}/PayCodes/Tags | Get all pay code tags
[**getAllPayInstructionTags**](TaggingApi.md#getAllPayInstructionTags) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstructions/Tags | Get all pay instruction tags
[**getAllPayLineTags**](TaggingApi.md#getAllPayLineTags) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayLines/Tags | Get all pay line tags
[**getAllPayRunTags**](TaggingApi.md#getAllPayRunTags) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRuns/Tags | Get all pay run tags
[**getAllPayScheduleTags**](TaggingApi.md#getAllPayScheduleTags) | **GET** /Employer/{EmployerId}/PaySchedules/Tags | Get all pay schedule tags
[**getAllPermissionTags**](TaggingApi.md#getAllPermissionTags) | **GET** /Permissions/Tags | Get all Permission tags
[**getAllPermissionsWithTag**](TaggingApi.md#getAllPermissionsWithTag) | **GET** /Permissions/Tag/{TagId} | Get links to tagged Permissions
[**getAllRtiTransactionTags**](TaggingApi.md#getAllRtiTransactionTags) | **GET** /Employer/{EmployerId}/RtiTransactions/Tags | Get all RTI transaction tags
[**getAllSubContractorTags**](TaggingApi.md#getAllSubContractorTags) | **GET** /Employer/{EmployerId}/SubContractors/Tags | Get all sub contractor tags
[**getAllThirdPartyTransactionTags**](TaggingApi.md#getAllThirdPartyTransactionTags) | **GET** /Employer/{EmployerId}/ThirdPartyTransactions/Tags | Get all third party transaction tags
[**getAllThirdPartyTransactionsWithTag**](TaggingApi.md#getAllThirdPartyTransactionsWithTag) | **GET** /Employer/{EmployerId}/ThirdPartyTransactions/Tag/{TagId} | Get links to tagged third party transactions
[**getAllUserTags**](TaggingApi.md#getAllUserTags) | **GET** /Users/Tags | Get all user tags
[**getAllUsersWithTag**](TaggingApi.md#getAllUsersWithTag) | **GET** /Users/Tag/{TagId} | Get links to tagged users
[**getCisInstructionsWithTag**](TaggingApi.md#getCisInstructionsWithTag) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstructions/Tag/{TagId} | Get CIS instructions with tag
[**getCisLineTypesWithTag**](TaggingApi.md#getCisLineTypesWithTag) | **GET** /Employer/{EmployerId}/CisLineTypes/Tag/{TagId} | Get CIS line types with tag
[**getCisLinesWithTag**](TaggingApi.md#getCisLinesWithTag) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLines/Tag/{TagId} | Get CIS lines with tag
[**getEmployeesWithTag**](TaggingApi.md#getEmployeesWithTag) | **GET** /Employer/{EmployerId}/Employees/Tag/{TagId} | Get employees with tag
[**getEmployersWithTag**](TaggingApi.md#getEmployersWithTag) | **GET** /Employers/Tag/{TagId} | Get employers with tag
[**getHolidaySchemesWithTag**](TaggingApi.md#getHolidaySchemesWithTag) | **GET** /Employer/{EmployerId}/HolidaySchemes/Tag/{TagId} | Get holiday schemes with tag
[**getPayCodesWithTag**](TaggingApi.md#getPayCodesWithTag) | **GET** /Employer/{EmployerId}/PayCodes/Tag/{TagId} | Get pay codes with tag
[**getPayInstructionsWithTag**](TaggingApi.md#getPayInstructionsWithTag) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstructions/Tag/{TagId} | Get pay instructions with tag
[**getPayLinesWithTag**](TaggingApi.md#getPayLinesWithTag) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayLines/Tag/{TagId} | Get pay lines with tag
[**getPayRunsWithTag**](TaggingApi.md#getPayRunsWithTag) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRuns/Tag/{TagId} | Get pay runs with tag
[**getPaySchedulesWithTag**](TaggingApi.md#getPaySchedulesWithTag) | **GET** /Employer/{EmployerId}/PaySchedules/Tag/{TagId} | Get pay schedule with tag
[**getRtiTransactionsWithTag**](TaggingApi.md#getRtiTransactionsWithTag) | **GET** /Employer/{EmployerId}/RtiTransactions/Tag/{TagId} | Get RTI transactions with tag
[**getSubContractorsWithTag**](TaggingApi.md#getSubContractorsWithTag) | **GET** /Employer/{EmployerId}/SubContractors/Tag/{TagId} | Get sub contractors with tag
[**getTagFromCisInstruction**](TaggingApi.md#getTagFromCisInstruction) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tag/{TagId} | Get CIS instruction tag
[**getTagFromCisLine**](TaggingApi.md#getTagFromCisLine) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tag/{TagId} | Get CIS line tag
[**getTagFromCisLineType**](TaggingApi.md#getTagFromCisLineType) | **GET** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tag/{TagId} | Get CIS line type tag
[**getTagFromEmployee**](TaggingApi.md#getTagFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Tag/{TagId} | Get employee tag
[**getTagFromEmployeeRevision**](TaggingApi.md#getTagFromEmployeeRevision) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Tag/{TagId}/{EffectiveDate} | Get employee revision tag
[**getTagFromEmployer**](TaggingApi.md#getTagFromEmployer) | **GET** /Employer/{EmployerId}/Tag/{TagId} | Get employer tag
[**getTagFromEmployerRevision**](TaggingApi.md#getTagFromEmployerRevision) | **GET** /Employer/{EmployerId}/Tag/{TagId}/{EffectiveDate} | Get employer revision tag
[**getTagFromHolidayScheme**](TaggingApi.md#getTagFromHolidayScheme) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId} | Get holiday scheme tag
[**getTagFromHolidaySchemeRevision**](TaggingApi.md#getTagFromHolidaySchemeRevision) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId}/{EffectiveDate} | Get holiday scheme revision tag
[**getTagFromJournalLine**](TaggingApi.md#getTagFromJournalLine) | **GET** /Employer/{EmployerId}/JournalLine/{JournalLineId}/Tag/{TagId} | Get journal line tag
[**getTagFromPayCode**](TaggingApi.md#getTagFromPayCode) | **GET** /Employer/{EmployerId}/PayCode/{PayCodeId}/Tag/{TagId} | Get pay code tag
[**getTagFromPayInstruction**](TaggingApi.md#getTagFromPayInstruction) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId}/Tag/{TagId} | Get pay instruction tag
[**getTagFromPayLine**](TaggingApi.md#getTagFromPayLine) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayLine/{PayLineId}/Tag/{TagId} | Get pay line tag
[**getTagFromPayRun**](TaggingApi.md#getTagFromPayRun) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId}/Tag/{TagId} | Get pay run tag
[**getTagFromPaySchedule**](TaggingApi.md#getTagFromPaySchedule) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/Tag/{TagId} | Get pay schedule tag
[**getTagFromPermission**](TaggingApi.md#getTagFromPermission) | **GET** /Permission/{PermissionId}/Tag/{TagId} | Get Permission tag
[**getTagFromRtiTransaction**](TaggingApi.md#getTagFromRtiTransaction) | **GET** /Employer/{EmployerId}/RtiTransaction/{RtiTransactionId}/Tag/{TagId} | Get RTI transaction tag
[**getTagFromSubContractor**](TaggingApi.md#getTagFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId} | Get sub contractor tag
[**getTagFromSubContractorRevision**](TaggingApi.md#getTagFromSubContractorRevision) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId}/{EffectiveDate} | Get sub contractor revision tag
[**getTagFromThirdPartyTransaction**](TaggingApi.md#getTagFromThirdPartyTransaction) | **GET** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId}/Tag/{TagId} | Get third party transaction tag
[**getTagFromUser**](TaggingApi.md#getTagFromUser) | **GET** /User/{UserId}/Tag/{TagId} | Get user tag
[**getTagsFromCisInstruction**](TaggingApi.md#getTagsFromCisInstruction) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tags | Get all tags from the CIS instruction
[**getTagsFromCisLine**](TaggingApi.md#getTagsFromCisLine) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tags | Get all tags from the CIS line
[**getTagsFromCisLineType**](TaggingApi.md#getTagsFromCisLineType) | **GET** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tags | Get all tags from the CIS line type
[**getTagsFromEmployee**](TaggingApi.md#getTagsFromEmployee) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Tags | Get all employee tags
[**getTagsFromEmployeeRevision**](TaggingApi.md#getTagsFromEmployeeRevision) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/Tags/{EffectiveDate} | Get all employee revision tags
[**getTagsFromEmployer**](TaggingApi.md#getTagsFromEmployer) | **GET** /Employer/{EmployerId}/Tags | Get all employer tags
[**getTagsFromEmployerRevision**](TaggingApi.md#getTagsFromEmployerRevision) | **GET** /Employer/{EmployerId}/Tags/{EffectiveDate} | Get all employer revision tags
[**getTagsFromHolidayScheme**](TaggingApi.md#getTagsFromHolidayScheme) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tags | Get all tags from the holiday scheme
[**getTagsFromHolidaySchemeRevision**](TaggingApi.md#getTagsFromHolidaySchemeRevision) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tags/{EffectiveDate} | Get all holiday scheme revision tags
[**getTagsFromJournalLine**](TaggingApi.md#getTagsFromJournalLine) | **GET** /Employer/{EmployerId}/JournalLine/{JournalLineId}/Tags | Get tags from journal line
[**getTagsFromPayCode**](TaggingApi.md#getTagsFromPayCode) | **GET** /Employer/{EmployerId}/PayCode/{PayCodeId}/Tags | Get all pay code tags
[**getTagsFromPayInstruction**](TaggingApi.md#getTagsFromPayInstruction) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId}/Tags | Get all tags from the pay instruction
[**getTagsFromPayLine**](TaggingApi.md#getTagsFromPayLine) | **GET** /Employer/{EmployerId}/Employee/{EmployeeId}/PayLine/{PayLineId}/Tags | Get all tags from the pay line
[**getTagsFromPayRun**](TaggingApi.md#getTagsFromPayRun) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId}/Tags | Get all pay run tags
[**getTagsFromPaySchedule**](TaggingApi.md#getTagsFromPaySchedule) | **GET** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/Tags | Get all pay schedule tags
[**getTagsFromPermission**](TaggingApi.md#getTagsFromPermission) | **GET** /Permission/{PermissionId}/Tags | Get tags from Permission
[**getTagsFromRtiTransaction**](TaggingApi.md#getTagsFromRtiTransaction) | **GET** /Employer/{EmployerId}/RtiTransaction/{RtiTransactionId}/Tags | Get all tags from RTI transaction
[**getTagsFromSubContractor**](TaggingApi.md#getTagsFromSubContractor) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tags | Get all tags from the sub contractor
[**getTagsFromSubContractorRevision**](TaggingApi.md#getTagsFromSubContractorRevision) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tags/{EffectiveDate} | Get all sub contractor revision tags
[**getTagsFromThirdPartyTransaction**](TaggingApi.md#getTagsFromThirdPartyTransaction) | **GET** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId}/Tags | Get tags from third party transaction
[**getTagsFromUser**](TaggingApi.md#getTagsFromUser) | **GET** /User/{UserId}/Tags | Get tags from user
[**putCisInstructionTag**](TaggingApi.md#putCisInstructionTag) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisInstruction/{CisInstructionId}/Tag/{TagId} | Insert CIS instruction tag
[**putCisLineTag**](TaggingApi.md#putCisLineTag) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/CisLine/{CisLineId}/Tag/{TagId} | Insert CIS line tag
[**putCisLineTypeTag**](TaggingApi.md#putCisLineTypeTag) | **PUT** /Employer/{EmployerId}/CisLineType/{CisLineTypeId}/Tag/{TagId} | Insert CIS line type tag
[**putEmployeeTag**](TaggingApi.md#putEmployeeTag) | **PUT** /Employer/{EmployerId}/Employee/{EmployeeId}/Tag/{TagId} | Insert employee tag
[**putEmployerTag**](TaggingApi.md#putEmployerTag) | **PUT** /Employer/{EmployerId}/Tag/{TagId} | Insert employer tag
[**putHolidaySchemeTag**](TaggingApi.md#putHolidaySchemeTag) | **PUT** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId} | Insert holiday scheme tag
[**putJournalLineTag**](TaggingApi.md#putJournalLineTag) | **PUT** /Employer/{EmployerId}/JournalLine/{JournalLineId}/Tag/{TagId} | Insert journal line tag
[**putPayCodeTag**](TaggingApi.md#putPayCodeTag) | **PUT** /Employer/{EmployerId}/PayCode/{PayCodeId}/Tag/{TagId} | Insert pay code tag
[**putPayInstructionTag**](TaggingApi.md#putPayInstructionTag) | **PUT** /Employer/{EmployerId}/Employee/{EmployeeId}/PayInstruction/{PayInstructionId}/Tag/{TagId} | Insert pay instruction tag
[**putPayLineTag**](TaggingApi.md#putPayLineTag) | **PUT** /Employer/{EmployerId}/Employee/{EmployeeId}/PayLine/{PayLineId}/Tag/{TagId} | Insert pay line tag
[**putPayRunTag**](TaggingApi.md#putPayRunTag) | **PUT** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/PayRun/{PayRunId}/Tag/{TagId} | Insert pay run tag
[**putPayScheduleTag**](TaggingApi.md#putPayScheduleTag) | **PUT** /Employer/{EmployerId}/PaySchedule/{PayScheduleId}/Tag/{TagId} | Insert pay schedule tag
[**putPermissionTag**](TaggingApi.md#putPermissionTag) | **PUT** /Permission/{PermissionId}/Tag/{TagId} | Insert Permission tag
[**putRtiTransactionTag**](TaggingApi.md#putRtiTransactionTag) | **PUT** /Employer/{EmployerId}/RtiTransaction/{RtiTransactionId}/Tag/{TagId} | Insert RTI transaction tag
[**putSubContractorTag**](TaggingApi.md#putSubContractorTag) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Tag/{TagId} | Insert sub contractor tag
[**putThirdPartyTransactionTag**](TaggingApi.md#putThirdPartyTransactionTag) | **PUT** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId}/Tag/{TagId} | insert third party transaction tag
[**putUserTag**](TaggingApi.md#putUserTag) | **PUT** /User/{UserId}/Tag/{TagId} | Insert user tag



## deleteCisInstructionTag

> deleteCisInstructionTag(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion)

Delete CIS instruction tag

Deletes a tag from the CIS instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisInstructionTag(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion, (error, data, response) => {
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


## deleteCisLineTag

> deleteCisLineTag(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion)

Delete CIS line tag

Deletes a tag from the CIS line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisLineTag(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion, (error, data, response) => {
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


## deleteCisLineTypeTag

> deleteCisLineTypeTag(employerId, cisLineTypeId, tagId, authorization, apiVersion)

Delete CIS line type tag

Deletes a tag from the CIS line type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteCisLineTypeTag(employerId, cisLineTypeId, tagId, authorization, apiVersion, (error, data, response) => {
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


## deleteEmployeeTag

> deleteEmployeeTag(employerId, employeeId, tagId, authorization, apiVersion)

Delete employee tag

Deletes a tag from the employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteEmployeeTag(employerId, employeeId, tagId, authorization, apiVersion, (error, data, response) => {
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


## deleteEmployerTag

> deleteEmployerTag(employerId, tagId, authorization, apiVersion)

Delete employer tag

Deletes a tag from the employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteEmployerTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## deleteHolidaySchemeTag

> deleteHolidaySchemeTag(employerId, holidaySchemeId, tagId, authorization, apiVersion)

Delete holiday scheme tag

Deletes a tag from the holiday scheme

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteHolidaySchemeTag(employerId, holidaySchemeId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | 
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


## deleteJournalLineTag

> deleteJournalLineTag(employerId, journalLineId, tagId, authorization, apiVersion)

Delete journal line tag

Deletes a tag from the journal line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalLineId = "journalLineId_example"; // String | The journal line unique identifier. E.g JL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteJournalLineTag(employerId, journalLineId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **journalLineId** | **String**| The journal line unique identifier. E.g JL001 | 
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


## deletePayCodeTag

> deletePayCodeTag(employerId, payCodeId, tagId, authorization, apiVersion)

Delete pay code tag

Deletes a tag from the pay code

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePayCodeTag(employerId, payCodeId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **payCodeId** | **String**| The pay code unique identifier. E.g. BASIC | 
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


## deletePayInstructionTag

> deletePayInstructionTag(employerId, employeeId, payInstructionId, tagId, authorization, apiVersion)

Delete pay instruction tag

Deletes a tag from the pay instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePayInstructionTag(employerId, employeeId, payInstructionId, tagId, authorization, apiVersion, (error, data, response) => {
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


## deletePayLineTag

> deletePayLineTag(employerId, employeeId, payLineId, tagId, authorization, apiVersion)

Delete pay line tag

Deletes a tag from the pay line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payLineId = "payLineId_example"; // String | The pay line unique identifier. E.g. PL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePayLineTag(employerId, employeeId, payLineId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **payLineId** | **String**| The pay line unique identifier. E.g. PL001 | 
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


## deletePayRunTag

> deletePayRunTag(employerId, payScheduleId, payRunId, tagId, authorization, apiVersion)

Delete pay run tag

Deletes a tag from the pay run

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePayRunTag(employerId, payScheduleId, payRunId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **payRunId** | **String**| The pay runs&#39; unique identifier. E.g. PR001 | 
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


## deletePayScheduleTag

> deletePayScheduleTag(employerId, payScheduleId, tagId, authorization, apiVersion)

Delete pay schedule tag

Deletes a tag from the pay schedule

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePayScheduleTag(employerId, payScheduleId, tagId, authorization, apiVersion, (error, data, response) => {
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


## deletePermissionTag

> deletePermissionTag(permissionId, tagId, authorization, apiVersion)

Delete Permission tag

Deletes a tag from the Permission

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePermissionTag(permissionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
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


## deleteRtiTransactionTag

> deleteRtiTransactionTag(employerId, rtiTransactionId, tagId, authorization, apiVersion)

Delete RTI transaction tag

Deletes a tag from the RTI transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let rtiTransactionId = "rtiTransactionId_example"; // String | The RTI transaction unique identifier. E.g. FPS001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteRtiTransactionTag(employerId, rtiTransactionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **rtiTransactionId** | **String**| The RTI transaction unique identifier. E.g. FPS001 | 
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


## deleteSubContractorTag

> deleteSubContractorTag(employerId, subContractorId, tagId, authorization, apiVersion)

Delete sub contractor tag

Deletes a tag from the sub contractor

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteSubContractorTag(employerId, subContractorId, tagId, authorization, apiVersion, (error, data, response) => {
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


## deleteThirdPartyTransactionTag

> deleteThirdPartyTransactionTag(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion)

Delete third party transaction tag

Deletes a tag from the third party transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteThirdPartyTransactionTag(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **thirdPartyTransactionId** | **String**| The third party transaction unique identifier. E.g TP001 | 
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


## deleteUserTag

> deleteUserTag(userId, tagId, authorization, apiVersion)

Delete user tag

Deletes a tag from the user

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let userId = "userId_example"; // String | The user unique identifier. E.g USER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteUserTag(userId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **userId** | **String**| The user unique identifier. E.g USER001 | 
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


## getAllCisInstructionTags

> LinkCollection getAllCisInstructionTags(employerId, subContractorId, authorization, apiVersion)

Get all CIS instruction tags

Gets all the CIS instruction tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllCisInstructionTags(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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


## getAllCisLineTags

> LinkCollection getAllCisLineTags(employerId, subContractorId, authorization, apiVersion)

Get all CIS line tags

Gets all the CIS line tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllCisLineTags(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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


## getAllCisLineTypeTags

> LinkCollection getAllCisLineTypeTags(employerId, authorization, apiVersion)

Get all CIS line type tags

Gets all the CIS line type tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllCisLineTypeTags(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllEmployeeTags

> LinkCollection getAllEmployeeTags(employerId, authorization, apiVersion)

Get all employee tags

Gets all the employee tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllEmployeeTags(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllEmployerTags

> LinkCollection getAllEmployerTags(authorization, apiVersion)

Get all employer tags

Gets all the employer tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllEmployerTags(authorization, apiVersion, (error, data, response) => {
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


## getAllHolidaySchemeTags

> LinkCollection getAllHolidaySchemeTags(employerId, authorization, apiVersion)

Get all holiday scheme tags

Gets all the holiday scheme tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllHolidaySchemeTags(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllJournalLineTags

> LinkCollection getAllJournalLineTags(employerId, authorization, apiVersion)

Get all journal line tags

Gets all the journal line tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllJournalLineTags(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllJournalLinesWithTag

> LinkCollection getAllJournalLinesWithTag(employerId, tagId, authorization, apiVersion)

Get links to tagged journal lines

Gets the journal lines with the specified tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllJournalLinesWithTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getAllPayCodeTags

> LinkCollection getAllPayCodeTags(employerId, authorization, apiVersion)

Get all pay code tags

Gets all the pay code tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPayCodeTags(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllPayInstructionTags

> LinkCollection getAllPayInstructionTags(employerId, employeeId, authorization, apiVersion)

Get all pay instruction tags

Gets all the pay instruction tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPayInstructionTags(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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


## getAllPayLineTags

> LinkCollection getAllPayLineTags(employerId, employeeId, authorization, apiVersion)

Get all pay line tags

Gets all the pay line tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPayLineTags(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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


## getAllPayRunTags

> LinkCollection getAllPayRunTags(employerId, payScheduleId, authorization, apiVersion)

Get all pay run tags

Gets all the pay run tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPayRunTags(employerId, payScheduleId, authorization, apiVersion, (error, data, response) => {
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


## getAllPayScheduleTags

> LinkCollection getAllPayScheduleTags(employerId, authorization, apiVersion)

Get all pay schedule tags

Gets all the pay schedule tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPayScheduleTags(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllPermissionTags

> LinkCollection getAllPermissionTags(authorization, apiVersion)

Get all Permission tags

Get all tags from all Permissions

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPermissionTags(authorization, apiVersion, (error, data, response) => {
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


## getAllPermissionsWithTag

> LinkCollection getAllPermissionsWithTag(tagId, authorization, apiVersion)

Get links to tagged Permissions

Gets the Permissions with the specified tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPermissionsWithTag(tagId, authorization, apiVersion, (error, data, response) => {
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


## getAllRtiTransactionTags

> LinkCollection getAllRtiTransactionTags(employerId, authorization, apiVersion)

Get all RTI transaction tags

Gets all the RTI transaction tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllRtiTransactionTags(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllSubContractorTags

> LinkCollection getAllSubContractorTags(employerId, authorization, apiVersion)

Get all sub contractor tags

Gets all the sub contractor tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllSubContractorTags(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllThirdPartyTransactionTags

> LinkCollection getAllThirdPartyTransactionTags(employerId, authorization, apiVersion)

Get all third party transaction tags

Gets all the third party transaction tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllThirdPartyTransactionTags(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllThirdPartyTransactionsWithTag

> LinkCollection getAllThirdPartyTransactionsWithTag(employerId, tagId, authorization, apiVersion)

Get links to tagged third party transactions

Gets the third party transactions with the specified tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllThirdPartyTransactionsWithTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getAllUserTags

> LinkCollection getAllUserTags(authorization, apiVersion)

Get all user tags

Get all tags from all users

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllUserTags(authorization, apiVersion, (error, data, response) => {
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


## getAllUsersWithTag

> LinkCollection getAllUsersWithTag(tagId, authorization, apiVersion)

Get links to tagged users

Gets the users with the specified tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllUsersWithTag(tagId, authorization, apiVersion, (error, data, response) => {
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


## getCisInstructionsWithTag

> LinkCollection getCisInstructionsWithTag(employerId, subContractorId, tagId, authorization, apiVersion)

Get CIS instructions with tag

Gets the CIS instruction with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisInstructionsWithTag(employerId, subContractorId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getCisLineTypesWithTag

> LinkCollection getCisLineTypesWithTag(employerId, tagId, authorization, apiVersion)

Get CIS line types with tag

Gets the CIS line type with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisLineTypesWithTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getCisLinesWithTag

> LinkCollection getCisLinesWithTag(employerId, subContractorId, tagId, authorization, apiVersion)

Get CIS lines with tag

Gets the CIS line with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getCisLinesWithTag(employerId, subContractorId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getEmployeesWithTag

> LinkCollection getEmployeesWithTag(employerId, tagId, authorization, apiVersion)

Get employees with tag

Gets the employees with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployeesWithTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getEmployersWithTag

> LinkCollection getEmployersWithTag(tagId, authorization, apiVersion)

Get employers with tag

Gets the employers with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployersWithTag(tagId, authorization, apiVersion, (error, data, response) => {
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


## getHolidaySchemesWithTag

> LinkCollection getHolidaySchemesWithTag(employerId, tagId, authorization, apiVersion)

Get holiday schemes with tag

Gets the holiday scheme with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getHolidaySchemesWithTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getPayCodesWithTag

> LinkCollection getPayCodesWithTag(employerId, tagId, authorization, apiVersion)

Get pay codes with tag

Gets the pay codes with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayCodesWithTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getPayInstructionsWithTag

> LinkCollection getPayInstructionsWithTag(employerId, employeeId, tagId, authorization, apiVersion)

Get pay instructions with tag

Gets the pay instructions with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayInstructionsWithTag(employerId, employeeId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getPayLinesWithTag

> LinkCollection getPayLinesWithTag(employerId, employeeId, tagId, authorization, apiVersion)

Get pay lines with tag

Gets the pay line with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayLinesWithTag(employerId, employeeId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getPayRunsWithTag

> LinkCollection getPayRunsWithTag(employerId, payScheduleId, tagId, authorization, apiVersion)

Get pay runs with tag

Gets the pay runs with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayRunsWithTag(employerId, payScheduleId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getPaySchedulesWithTag

> LinkCollection getPaySchedulesWithTag(employerId, tagId, authorization, apiVersion)

Get pay schedule with tag

Gets the pay schedules with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPaySchedulesWithTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getRtiTransactionsWithTag

> LinkCollection getRtiTransactionsWithTag(employerId, tagId, authorization, apiVersion)

Get RTI transactions with tag

Gets the RTI transactions with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getRtiTransactionsWithTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getSubContractorsWithTag

> LinkCollection getSubContractorsWithTag(employerId, tagId, authorization, apiVersion)

Get sub contractors with tag

Gets the sub contractor with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getSubContractorsWithTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromCisInstruction

> Tag getTagFromCisInstruction(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion)

Get CIS instruction tag

Gets the tag from the CIS instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromCisInstruction(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromCisLine

> Tag getTagFromCisLine(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion)

Get CIS line tag

Gets the tag from the CIS line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromCisLine(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromCisLineType

> Tag getTagFromCisLineType(employerId, cisLineTypeId, tagId, authorization, apiVersion)

Get CIS line type tag

Gets the tag from the CIS line type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromCisLineType(employerId, cisLineTypeId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromEmployee

> Tag getTagFromEmployee(employerId, employeeId, tagId, authorization, apiVersion)

Get employee tag

Gets the tag from the employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromEmployee(employerId, employeeId, tagId, authorization, apiVersion, (error, data, response) => {
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

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagFromEmployeeRevision

> Tag getTagFromEmployeeRevision(employerId, employeeId, tagId, effectiveDate, authorization, apiVersion)

Get employee revision tag

Gets the tag from the employee revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromEmployeeRevision(employerId, employeeId, tagId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getTagFromEmployer

> Tag getTagFromEmployer(employerId, tagId, authorization, apiVersion)

Get employer tag

Gets the tag from the employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromEmployer(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagFromEmployerRevision

> Tag getTagFromEmployerRevision(employerId, tagId, effectiveDate, authorization, apiVersion)

Get employer revision tag

Gets the tag from the employer revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromEmployerRevision(employerId, tagId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getTagFromHolidayScheme

> Tag getTagFromHolidayScheme(employerId, holidaySchemeId, tagId, authorization, apiVersion)

Get holiday scheme tag

Gets the tag from the holiday scheme

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromHolidayScheme(employerId, holidaySchemeId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | 
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


## getTagFromHolidaySchemeRevision

> Tag getTagFromHolidaySchemeRevision(employerId, holidaySchemeId, tagId, effectiveDate, authorization, apiVersion)

Get holiday scheme revision tag

Gets the tag from the holiday scheme revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromHolidaySchemeRevision(employerId, holidaySchemeId, tagId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | 
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


## getTagFromJournalLine

> Tag getTagFromJournalLine(employerId, journalLineId, tagId, authorization, apiVersion)

Get journal line tag

Gets a tag from the journal line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalLineId = "journalLineId_example"; // String | The journal line unique identifier. E.g JL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromJournalLine(employerId, journalLineId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromPayCode

> Tag getTagFromPayCode(employerId, payCodeId, tagId, authorization, apiVersion)

Get pay code tag

Gets the tag from the pay code

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromPayCode(employerId, payCodeId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **payCodeId** | **String**| The pay code unique identifier. E.g. BASIC | 
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


## getTagFromPayInstruction

> Tag getTagFromPayInstruction(employerId, employeeId, payInstructionId, tagId, authorization, apiVersion)

Get pay instruction tag

Gets the tag from the pay instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromPayInstruction(employerId, employeeId, payInstructionId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromPayLine

> Tag getTagFromPayLine(employerId, employeeId, payLineId, tagId, authorization, apiVersion)

Get pay line tag

Gets the tag from the pay line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payLineId = "payLineId_example"; // String | The pay line unique identifier. E.g. PL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromPayLine(employerId, employeeId, payLineId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **payLineId** | **String**| The pay line unique identifier. E.g. PL001 | 
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


## getTagFromPayRun

> Tag getTagFromPayRun(employerId, payScheduleId, payRunId, tagId, authorization, apiVersion)

Get pay run tag

Gets the tag from the pay run

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromPayRun(employerId, payScheduleId, payRunId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromPaySchedule

> Tag getTagFromPaySchedule(employerId, payScheduleId, tagId, authorization, apiVersion)

Get pay schedule tag

Gets the tag from the pay schedule

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromPaySchedule(employerId, payScheduleId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromPermission

> Tag getTagFromPermission(permissionId, tagId, authorization, apiVersion)

Get Permission tag

Gets a tag from the Permission

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromPermission(permissionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
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


## getTagFromRtiTransaction

> Tag getTagFromRtiTransaction(employerId, rtiTransactionId, tagId, authorization, apiVersion)

Get RTI transaction tag

Gets the tag from the RTI transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let rtiTransactionId = "rtiTransactionId_example"; // String | The RTI transaction unique identifier. E.g. FPS001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromRtiTransaction(employerId, rtiTransactionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **rtiTransactionId** | **String**| The RTI transaction unique identifier. E.g. FPS001 | 
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


## getTagFromSubContractor

> Tag getTagFromSubContractor(employerId, subContractorId, tagId, authorization, apiVersion)

Get sub contractor tag

Gets the tag from the sub contractor

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromSubContractor(employerId, subContractorId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromSubContractorRevision

> Tag getTagFromSubContractorRevision(employerId, subContractorId, tagId, effectiveDate, authorization, apiVersion)

Get sub contractor revision tag

Gets the tag from the sub contractor revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromSubContractorRevision(employerId, subContractorId, tagId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getTagFromThirdPartyTransaction

> Tag getTagFromThirdPartyTransaction(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion)

Get third party transaction tag

Gets a tag from the third party transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromThirdPartyTransaction(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **thirdPartyTransactionId** | **String**| The third party transaction unique identifier. E.g TP001 | 
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


## getTagFromUser

> Tag getTagFromUser(userId, tagId, authorization, apiVersion)

Get user tag

Gets a tag from the user

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let userId = "userId_example"; // String | The user unique identifier. E.g USER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromUser(userId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **userId** | **String**| The user unique identifier. E.g USER001 | 
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


## getTagsFromCisInstruction

> LinkCollection getTagsFromCisInstruction(employerId, subContractorId, cisInstructionId, authorization, apiVersion)

Get all tags from the CIS instruction

Gets all the tags from the CIS instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromCisInstruction(employerId, subContractorId, cisInstructionId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromCisLine

> LinkCollection getTagsFromCisLine(employerId, subContractorId, cisLineId, authorization, apiVersion)

Get all tags from the CIS line

Gets all the tags from the CIS line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromCisLine(employerId, subContractorId, cisLineId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromCisLineType

> LinkCollection getTagsFromCisLineType(employerId, cisLineTypeId, authorization, apiVersion)

Get all tags from the CIS line type

Gets all the tags from the CIS line type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromCisLineType(employerId, cisLineTypeId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromEmployee

> LinkCollection getTagsFromEmployee(employerId, employeeId, authorization, apiVersion)

Get all employee tags

Gets all the tags from the employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromEmployee(employerId, employeeId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromEmployeeRevision

> LinkCollection getTagsFromEmployeeRevision(employerId, employeeId, effectiveDate, authorization, apiVersion)

Get all employee revision tags

Gets all the tags from the employee revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromEmployeeRevision(employerId, employeeId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromEmployer

> LinkCollection getTagsFromEmployer(employerId, authorization, apiVersion)

Get all employer tags

Gets all the tags from the employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromEmployerRevision

> LinkCollection getTagsFromEmployerRevision(employerId, effectiveDate, authorization, apiVersion)

Get all employer revision tags

Gets all the tags from the employer revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromEmployerRevision(employerId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromHolidayScheme

> LinkCollection getTagsFromHolidayScheme(employerId, holidaySchemeId, authorization, apiVersion)

Get all tags from the holiday scheme

Gets all the tags from the holiday scheme

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromHolidayScheme(employerId, holidaySchemeId, authorization, apiVersion, (error, data, response) => {
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
 **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromHolidaySchemeRevision

> LinkCollection getTagsFromHolidaySchemeRevision(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion)

Get all holiday scheme revision tags

Gets all the tags from the holiday scheme revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromHolidaySchemeRevision(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | 
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


## getTagsFromJournalLine

> LinkCollection getTagsFromJournalLine(employerId, journalLineId, authorization, apiVersion)

Get tags from journal line

Gets all tags from the journal line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalLineId = "journalLineId_example"; // String | The journal line unique identifier. E.g JL001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromJournalLine(employerId, journalLineId, authorization, apiVersion, (error, data, response) => {
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

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromPayCode

> LinkCollection getTagsFromPayCode(employerId, payCodeId, authorization, apiVersion)

Get all pay code tags

Gets all the tags from the pay code

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromPayCode(employerId, payCodeId, authorization, apiVersion, (error, data, response) => {
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
 **payCodeId** | **String**| The pay code unique identifier. E.g. BASIC | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromPayInstruction

> LinkCollection getTagsFromPayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion)

Get all tags from the pay instruction

Gets all the tags from the pay instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromPayInstruction(employerId, employeeId, payInstructionId, authorization, apiVersion, (error, data, response) => {
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

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromPayLine

> LinkCollection getTagsFromPayLine(employerId, employeeId, payLineId, authorization, apiVersion)

Get all tags from the pay line

Gets all the tags from the pay line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payLineId = "payLineId_example"; // String | The pay line unique identifier. E.g. PL001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromPayLine(employerId, employeeId, payLineId, authorization, apiVersion, (error, data, response) => {
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
 **payLineId** | **String**| The pay line unique identifier. E.g. PL001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromPayRun

> LinkCollection getTagsFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion)

Get all pay run tags

Gets all the tags from the pay run

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromPayRun(employerId, payScheduleId, payRunId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromPaySchedule

> LinkCollection getTagsFromPaySchedule(employerId, payScheduleId, authorization, apiVersion)

Get all pay schedule tags

Gets all the tags from the pay schedule

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromPaySchedule(employerId, payScheduleId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromPermission

> LinkCollection getTagsFromPermission(permissionId, authorization, apiVersion)

Get tags from Permission

Gets all tags from the Permission

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromPermission(permissionId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromRtiTransaction

> LinkCollection getTagsFromRtiTransaction(employerId, rtiTransactionId, authorization, apiVersion)

Get all tags from RTI transaction

Gets all the tags from the RTI transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let rtiTransactionId = "rtiTransactionId_example"; // String | The RTI transaction unique identifier. E.g. FPS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromRtiTransaction(employerId, rtiTransactionId, authorization, apiVersion, (error, data, response) => {
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
 **rtiTransactionId** | **String**| The RTI transaction unique identifier. E.g. FPS001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromSubContractor

> LinkCollection getTagsFromSubContractor(employerId, subContractorId, authorization, apiVersion)

Get all tags from the sub contractor

Gets all the tags from the sub contractor

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromSubContractor(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromSubContractorRevision

> LinkCollection getTagsFromSubContractorRevision(employerId, subContractorId, effectiveDate, authorization, apiVersion)

Get all sub contractor revision tags

Gets all the tags from the sub contractor revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromSubContractorRevision(employerId, subContractorId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromThirdPartyTransaction

> LinkCollection getTagsFromThirdPartyTransaction(employerId, thirdPartyTransactionId, authorization, apiVersion)

Get tags from third party transaction

Gets all tags from the third party transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromThirdPartyTransaction(employerId, thirdPartyTransactionId, authorization, apiVersion, (error, data, response) => {
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
 **thirdPartyTransactionId** | **String**| The third party transaction unique identifier. E.g TP001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTagsFromUser

> LinkCollection getTagsFromUser(userId, authorization, apiVersion)

Get tags from user

Gets all tags from the user

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let userId = "userId_example"; // String | The user unique identifier. E.g USER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromUser(userId, authorization, apiVersion, (error, data, response) => {
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
 **userId** | **String**| The user unique identifier. E.g USER001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putCisInstructionTag

> Tag putCisInstructionTag(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion)

Insert CIS instruction tag

Inserts a new tag on the CIS instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisInstructionId = "cisInstructionId_example"; // String | The CIS instruction unique identifier. E.g. CIS001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putCisInstructionTag(employerId, subContractorId, cisInstructionId, tagId, authorization, apiVersion, (error, data, response) => {
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


## putCisLineTag

> Tag putCisLineTag(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion)

Insert CIS line tag

Inserts a new tag on the CIS line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let cisLineId = "cisLineId_example"; // String | The CIS line unique identifier. E.g. CISLN001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putCisLineTag(employerId, subContractorId, cisLineId, tagId, authorization, apiVersion, (error, data, response) => {
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


## putCisLineTypeTag

> Tag putCisLineTypeTag(employerId, cisLineTypeId, tagId, authorization, apiVersion)

Insert CIS line type tag

Inserts a new tag on the CIS line type

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let cisLineTypeId = "cisLineTypeId_example"; // String | The CIS line type unique identifier. E.g. TYPEA
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putCisLineTypeTag(employerId, cisLineTypeId, tagId, authorization, apiVersion, (error, data, response) => {
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


## putEmployeeTag

> Tag putEmployeeTag(employerId, employeeId, tagId, authorization, apiVersion)

Insert employee tag

Inserts a new tag on the employee

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putEmployeeTag(employerId, employeeId, tagId, authorization, apiVersion, (error, data, response) => {
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

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putEmployerTag

> Tag putEmployerTag(employerId, tagId, authorization, apiVersion)

Insert employer tag

Inserts a new tag on the employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putEmployerTag(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putHolidaySchemeTag

> Tag putHolidaySchemeTag(employerId, holidaySchemeId, tagId, authorization, apiVersion)

Insert holiday scheme tag

Inserts a new tag on the holiday scheme

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putHolidaySchemeTag(employerId, holidaySchemeId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **holidaySchemeId** | **String**| The holiday schemes&#39; unique identifier. E.g HOLSCH001 | 
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


## putJournalLineTag

> Tag putJournalLineTag(employerId, journalLineId, tagId, authorization, apiVersion)

Insert journal line tag

Inserts a tag on the journal line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalLineId = "journalLineId_example"; // String | The journal line unique identifier. E.g JL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putJournalLineTag(employerId, journalLineId, tagId, authorization, apiVersion, (error, data, response) => {
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


## putPayCodeTag

> Tag putPayCodeTag(employerId, payCodeId, tagId, authorization, apiVersion)

Insert pay code tag

Inserts a new tag on the pay code

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putPayCodeTag(employerId, payCodeId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **payCodeId** | **String**| The pay code unique identifier. E.g. BASIC | 
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


## putPayInstructionTag

> Tag putPayInstructionTag(employerId, employeeId, payInstructionId, tagId, authorization, apiVersion)

Insert pay instruction tag

Inserts a new tag on the pay instruction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payInstructionId = "payInstructionId_example"; // String | The pay instruction unique identifier. E.g. SAL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putPayInstructionTag(employerId, employeeId, payInstructionId, tagId, authorization, apiVersion, (error, data, response) => {
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


## putPayLineTag

> Tag putPayLineTag(employerId, employeeId, payLineId, tagId, authorization, apiVersion)

Insert pay line tag

Inserts a new tag on the pay line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let employeeId = "employeeId_example"; // String | The employees' unique identifier. E.g EE001
let payLineId = "payLineId_example"; // String | The pay line unique identifier. E.g. PL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putPayLineTag(employerId, employeeId, payLineId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **payLineId** | **String**| The pay line unique identifier. E.g. PL001 | 
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


## putPayRunTag

> Tag putPayRunTag(employerId, payScheduleId, payRunId, tagId, authorization, apiVersion)

Insert pay run tag

Inserts a new tag on the pay run

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let payRunId = "payRunId_example"; // String | The pay runs' unique identifier. E.g. PR001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putPayRunTag(employerId, payScheduleId, payRunId, tagId, authorization, apiVersion, (error, data, response) => {
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


## putPayScheduleTag

> Tag putPayScheduleTag(employerId, payScheduleId, tagId, authorization, apiVersion)

Insert pay schedule tag

Inserts a new tag on the pay schedule

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payScheduleId = "payScheduleId_example"; // String | The pay schedules' unique identifier. E.g SCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putPayScheduleTag(employerId, payScheduleId, tagId, authorization, apiVersion, (error, data, response) => {
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


## putPermissionTag

> Tag putPermissionTag(permissionId, tagId, authorization, apiVersion)

Insert Permission tag

Inserts a tag on the Permission

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let permissionId = "permissionId_example"; // String | The permission unique identifier. E.g PERM001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putPermissionTag(permissionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **permissionId** | **String**| The permission unique identifier. E.g PERM001 | 
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


## putRtiTransactionTag

> Tag putRtiTransactionTag(employerId, rtiTransactionId, tagId, authorization, apiVersion)

Insert RTI transaction tag

Inserts a new tag on the RTI transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let rtiTransactionId = "rtiTransactionId_example"; // String | The RTI transaction unique identifier. E.g. FPS001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putRtiTransactionTag(employerId, rtiTransactionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **rtiTransactionId** | **String**| The RTI transaction unique identifier. E.g. FPS001 | 
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


## putSubContractorTag

> Tag putSubContractorTag(employerId, subContractorId, tagId, authorization, apiVersion)

Insert sub contractor tag

Inserts a new tag on the sub contractor

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putSubContractorTag(employerId, subContractorId, tagId, authorization, apiVersion, (error, data, response) => {
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


## putThirdPartyTransactionTag

> Tag putThirdPartyTransactionTag(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion)

insert third party transaction tag

Inserts a tag on the third party transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putThirdPartyTransactionTag(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **thirdPartyTransactionId** | **String**| The third party transaction unique identifier. E.g TP001 | 
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


## putUserTag

> Tag putUserTag(userId, tagId, authorization, apiVersion)

Insert user tag

Inserts a tag on the user

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.TaggingApi();
let userId = "userId_example"; // String | The user unique identifier. E.g USER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putUserTag(userId, tagId, authorization, apiVersion, (error, data, response) => {
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
 **userId** | **String**| The user unique identifier. E.g USER001 | 
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

