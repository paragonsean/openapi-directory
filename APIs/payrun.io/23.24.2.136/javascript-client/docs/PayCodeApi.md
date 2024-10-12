# PayRunIo.PayCodeApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePayCode**](PayCodeApi.md#deletePayCode) | **DELETE** /Employer/{EmployerId}/PayCode/{PayCodeId} | Deletes a pay code
[**deletePayCodeRevision**](PayCodeApi.md#deletePayCodeRevision) | **DELETE** /Employer/{EmployerId}/PayCode/{PayCodeId}/{EffectiveDate} | Deletes a pay code revision
[**deletePayCodeRevisionByNumber**](PayCodeApi.md#deletePayCodeRevisionByNumber) | **DELETE** /Employer/{EmployerId}/PayCode/{PayCodeId}/Revision/{RevisionNumber} | Delete an PayCode revision matching the specified revision number.
[**getAllPayCodeTags_0**](PayCodeApi.md#getAllPayCodeTags_0) | **GET** /Employer/{EmployerId}/PayCodes/Tags | Get all pay code tags
[**getPayCodeByEffectiveDate**](PayCodeApi.md#getPayCodeByEffectiveDate) | **GET** /Employer/{EmployerId}/PayCode/{PayCodeId}/{EffectiveDate} | Gets pay code for specified date
[**getPayCodeFromEmployer**](PayCodeApi.md#getPayCodeFromEmployer) | **GET** /Employer/{EmployerId}/PayCode/{PayCodeId} | Gets the specified pay code from the employer
[**getPayCodeRevisionByNumber**](PayCodeApi.md#getPayCodeRevisionByNumber) | **GET** /Employer/{EmployerId}/PayCode/{PayCodeId}/Revision/{RevisionNumber} | Gets the pay code by revision number
[**getPayCodeRevisions**](PayCodeApi.md#getPayCodeRevisions) | **GET** /Employer/{EmployerId}/PayCode/{PayCodeId}/Revisions | Get all revisions of the Pay Code
[**getPayCodesByEffectiveDate**](PayCodeApi.md#getPayCodesByEffectiveDate) | **GET** /Employer/{EmployerId}/PayCodes/{EffectiveDate} | Gets all pay codes for specified date
[**getPayCodesFromEmployer**](PayCodeApi.md#getPayCodesFromEmployer) | **GET** /Employer/{EmployerId}/PayCodes | Gets the pay codes from the employer
[**getPayCodesFromNominalCode**](PayCodeApi.md#getPayCodesFromNominalCode) | **GET** /Employer/{EmployerId}/NominalCode/{NominalCodeId}/PayCodes | Gets the pay codes by nominal code
[**getPayCodesWithTag_0**](PayCodeApi.md#getPayCodesWithTag_0) | **GET** /Employer/{EmployerId}/PayCodes/Tag/{TagId} | Get pay codes with tag
[**patchPayCode**](PayCodeApi.md#patchPayCode) | **PATCH** /Employer/{EmployerId}/PayCode/{PayCodeId} | Patches the pay code
[**postPayCode**](PayCodeApi.md#postPayCode) | **POST** /Employer/{EmployerId}/PayCodes | Create a new pay code
[**putPayCode**](PayCodeApi.md#putPayCode) | **PUT** /Employer/{EmployerId}/PayCode/{PayCodeId} | Updates a pay code



## deletePayCode

> deletePayCode(employerId, payCodeId, authorization, apiVersion)

Deletes a pay code

Delete the specified pay code

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePayCode(employerId, payCodeId, authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePayCodeRevision

> deletePayCodeRevision(employerId, payCodeId, effectiveDate, authorization, apiVersion)

Deletes a pay code revision

Delete the pay code revision for the specified date

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePayCodeRevision(employerId, payCodeId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## deletePayCodeRevisionByNumber

> deletePayCodeRevisionByNumber(employerId, payCodeId, revisionNumber, authorization, apiVersion)

Delete an PayCode revision matching the specified revision number.

Deletes the specified pay code revision for the matching revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePayCodeRevisionByNumber(employerId, payCodeId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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


## getAllPayCodeTags_0

> LinkCollection getAllPayCodeTags_0(employerId, authorization, apiVersion)

Get all pay code tags

Gets all the pay code tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllPayCodeTags_0(employerId, authorization, apiVersion, (error, data, response) => {
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


## getPayCodeByEffectiveDate

> PayCode getPayCodeByEffectiveDate(employerId, payCodeId, effectiveDate, authorization, apiVersion)

Gets pay code for specified date

Gets the pay code revision for the specified effective date

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayCodeByEffectiveDate(employerId, payCodeId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **effectiveDate** | **Date**| The effective date to be applied. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**PayCode**](PayCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayCodeFromEmployer

> PayCode getPayCodeFromEmployer(employerId, payCodeId, authorization, apiVersion)

Gets the specified pay code from the employer

Returns the specified pay code from the employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayCodeFromEmployer(employerId, payCodeId, authorization, apiVersion, (error, data, response) => {
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

[**PayCode**](PayCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayCodeRevisionByNumber

> PayCode getPayCodeRevisionByNumber(employerId, payCodeId, revisionNumber, authorization, apiVersion)

Gets the pay code by revision number

Get the pay code revision matching the specified revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayCodeRevisionByNumber(employerId, payCodeId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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
 **revisionNumber** | **String**| The revision number. E.g. 1 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**PayCode**](PayCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayCodeRevisions

> LinkCollection getPayCodeRevisions(employerId, payCodeId, authorization, apiVersion)

Get all revisions of the Pay Code

Returns links to all revisions of the pay code

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayCodeRevisions(employerId, payCodeId, authorization, apiVersion, (error, data, response) => {
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


## getPayCodesByEffectiveDate

> LinkCollection getPayCodesByEffectiveDate(employerId, effectiveDate, authorization, apiVersion)

Gets all pay codes for specified date

Gets the effective pay code revision for the specified date

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayCodesByEffectiveDate(employerId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getPayCodesFromEmployer

> LinkCollection getPayCodesFromEmployer(employerId, authorization, apiVersion)

Gets the pay codes from the employer

Get links to all the pay codes for the specified employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayCodesFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## getPayCodesFromNominalCode

> LinkCollection getPayCodesFromNominalCode(employerId, nominalCodeId, authorization, apiVersion)

Gets the pay codes by nominal code

Get the pay codes that share the specified nominal code

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let nominalCodeId = "nominalCodeId_example"; // String | The nominal code unique identifier. E.g. NOM001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayCodesFromNominalCode(employerId, nominalCodeId, authorization, apiVersion, (error, data, response) => {
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
 **nominalCodeId** | **String**| The nominal code unique identifier. E.g. NOM001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPayCodesWithTag_0

> LinkCollection getPayCodesWithTag_0(employerId, tagId, authorization, apiVersion)

Get pay codes with tag

Gets the pay codes with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPayCodesWithTag_0(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## patchPayCode

> PayCode patchPayCode(employerId, payCodeId, authorization, apiVersion, payCode)

Patches the pay code

Patches the specified pay code object with the supplied values

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let payCode = new PayRunIo.PayCode(); // PayCode | The pay code object.
apiInstance.patchPayCode(employerId, payCodeId, authorization, apiVersion, payCode, (error, data, response) => {
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
 **payCode** | [**PayCode**](PayCode.md)| The pay code object. | 

### Return type

[**PayCode**](PayCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPayCode

> Link postPayCode(employerId, authorization, apiVersion, payCode)

Create a new pay code

Create a new pay code object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let payCode = new PayRunIo.PayCode(); // PayCode | The pay code object.
apiInstance.postPayCode(employerId, authorization, apiVersion, payCode, (error, data, response) => {
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
 **payCode** | [**PayCode**](PayCode.md)| The pay code object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPayCode

> PayCode putPayCode(employerId, payCodeId, authorization, apiVersion, payCode)

Updates a pay code

Updates the existing specified pay code object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PayCodeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let payCodeId = "payCodeId_example"; // String | The pay code unique identifier. E.g. BASIC
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let payCode = new PayRunIo.PayCode(); // PayCode | The pay code object.
apiInstance.putPayCode(employerId, payCodeId, authorization, apiVersion, payCode, (error, data, response) => {
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
 **payCode** | [**PayCode**](PayCode.md)| The pay code object. | 

### Return type

[**PayCode**](PayCode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

