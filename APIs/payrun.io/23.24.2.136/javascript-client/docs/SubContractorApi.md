# PayRunIo.SubContractorApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSubContractor**](SubContractorApi.md#deleteSubContractor) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId} | Delete an sub contractor
[**deleteSubContractorRevision**](SubContractorApi.md#deleteSubContractorRevision) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/{EffectiveDate} | Delete an sub contractor revision matching the specified revision date.
[**deleteSubContractorRevisionByNumber**](SubContractorApi.md#deleteSubContractorRevisionByNumber) | **DELETE** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Revision/{RevisionNumber} | Delete an SubContractor revision matching the specified revision number.
[**getSubContractorByEffectiveDate**](SubContractorApi.md#getSubContractorByEffectiveDate) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/{EffectiveDate} | Get sub contractor by effective date.
[**getSubContractorFromEmployer**](SubContractorApi.md#getSubContractorFromEmployer) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId} | Get sub contractor from employer
[**getSubContractorRevisionByNumber**](SubContractorApi.md#getSubContractorRevisionByNumber) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Revision/{RevisionNumber} | Gets the sub contractor by revision number
[**getSubContractorRevisions**](SubContractorApi.md#getSubContractorRevisions) | **GET** /Employer/{EmployerId}/SubContractor/{SubContractorId}/Revisions | Get all sub contractor revisions
[**getSubContractorsByEffectiveDate**](SubContractorApi.md#getSubContractorsByEffectiveDate) | **GET** /Employer/{EmployerId}/SubContractors/{EffectiveDate} | Get sub contractors from employer at a given effective date.
[**getSubContractorsFromEmployer**](SubContractorApi.md#getSubContractorsFromEmployer) | **GET** /Employer/{EmployerId}/SubContractors | Get sub contractors from employer.
[**patchSubContractor**](SubContractorApi.md#patchSubContractor) | **PATCH** /Employer/{EmployerId}/SubContractor/{SubContractorId} | Patches the sub contractor
[**postSubContractorIntoEmployer**](SubContractorApi.md#postSubContractorIntoEmployer) | **POST** /Employer/{EmployerId}/SubContractors | Create a new sub contractor
[**putSubContractorIntoEmployer**](SubContractorApi.md#putSubContractorIntoEmployer) | **PUT** /Employer/{EmployerId}/SubContractor/{SubContractorId} | Updates the sub contractor



## deleteSubContractor

> deleteSubContractor(employerId, subContractorId, authorization, apiVersion)

Delete an sub contractor

Delete the specified sub contractor

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteSubContractor(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSubContractorRevision

> deleteSubContractorRevision(employerId, subContractorId, effectiveDate, authorization, apiVersion)

Delete an sub contractor revision matching the specified revision date.

Deletes the specified sub contractor revision for the matching revision date

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteSubContractorRevision(employerId, subContractorId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## deleteSubContractorRevisionByNumber

> deleteSubContractorRevisionByNumber(employerId, subContractorId, revisionNumber, authorization, apiVersion)

Delete an SubContractor revision matching the specified revision number.

Deletes the specified sub contractor revision for the matching revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteSubContractorRevisionByNumber(employerId, subContractorId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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


## getSubContractorByEffectiveDate

> SubContractor getSubContractorByEffectiveDate(employerId, subContractorId, effectiveDate, authorization, apiVersion)

Get sub contractor by effective date.

Returns the sub contractor&#39;s state at the specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getSubContractorByEffectiveDate(employerId, subContractorId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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

[**SubContractor**](SubContractor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubContractorFromEmployer

> SubContractor getSubContractorFromEmployer(employerId, subContractorId, authorization, apiVersion)

Get sub contractor from employer

Gets the specified sub contractor from employer.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getSubContractorFromEmployer(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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

[**SubContractor**](SubContractor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubContractorRevisionByNumber

> SubContractor getSubContractorRevisionByNumber(employerId, subContractorId, revisionNumber, authorization, apiVersion)

Gets the sub contractor by revision number

Get the sub contractor revision matching the specified revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getSubContractorRevisionByNumber(employerId, subContractorId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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
 **revisionNumber** | **String**| The revision number. E.g. 1 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**SubContractor**](SubContractor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubContractorRevisions

> LinkCollection getSubContractorRevisions(employerId, subContractorId, authorization, apiVersion)

Get all sub contractor revisions

Gets links to all the sub contractor revisions

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getSubContractorRevisions(employerId, subContractorId, authorization, apiVersion, (error, data, response) => {
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


## getSubContractorsByEffectiveDate

> LinkCollection getSubContractorsByEffectiveDate(employerId, effectiveDate, authorization, apiVersion)

Get sub contractors from employer at a given effective date.

Get links to all sub contractors for the employer on specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getSubContractorsByEffectiveDate(employerId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getSubContractorsFromEmployer

> LinkCollection getSubContractorsFromEmployer(employerId, authorization, apiVersion)

Get sub contractors from employer.

Get links to all sub contractors for the specified employer.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getSubContractorsFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## patchSubContractor

> SubContractor patchSubContractor(employerId, subContractorId, authorization, apiVersion, subContractor)

Patches the sub contractor

Patches the specified sub contractor with the supplied values

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let subContractor = new PayRunIo.SubContractor(); // SubContractor | The sub contractor object.
apiInstance.patchSubContractor(employerId, subContractorId, authorization, apiVersion, subContractor, (error, data, response) => {
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
 **subContractor** | [**SubContractor**](SubContractor.md)| The sub contractor object. | 

### Return type

[**SubContractor**](SubContractor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postSubContractorIntoEmployer

> Link postSubContractorIntoEmployer(employerId, authorization, apiVersion, subContractor)

Create a new sub contractor

Create a new sub contractor object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let subContractor = new PayRunIo.SubContractor(); // SubContractor | The sub contractor object.
apiInstance.postSubContractorIntoEmployer(employerId, authorization, apiVersion, subContractor, (error, data, response) => {
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
 **subContractor** | [**SubContractor**](SubContractor.md)| The sub contractor object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putSubContractorIntoEmployer

> SubContractor putSubContractorIntoEmployer(employerId, subContractorId, authorization, apiVersion, subContractor)

Updates the sub contractor

Updates the existing specified sub contractor object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.SubContractorApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let subContractorId = "subContractorId_example"; // String | The sub contractors' unique identifier. E.g SUB001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let subContractor = new PayRunIo.SubContractor(); // SubContractor | The sub contractor object.
apiInstance.putSubContractorIntoEmployer(employerId, subContractorId, authorization, apiVersion, subContractor, (error, data, response) => {
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
 **subContractor** | [**SubContractor**](SubContractor.md)| The sub contractor object. | 

### Return type

[**SubContractor**](SubContractor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

