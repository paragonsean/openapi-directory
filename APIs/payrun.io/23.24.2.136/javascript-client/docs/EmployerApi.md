# PayRunIo.EmployerApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteEmployer**](EmployerApi.md#deleteEmployer) | **DELETE** /Employer/{EmployerId} | Delete an Employer
[**deleteEmployerRevision**](EmployerApi.md#deleteEmployerRevision) | **DELETE** /Employer/{EmployerId}/{EffectiveDate} | Delete an Employer revision matching the specified revision date.
[**deleteEmployerRevisionByNumber**](EmployerApi.md#deleteEmployerRevisionByNumber) | **DELETE** /Employer/{EmployerId}/Revision/{RevisionNumber} | Delete an Employer revision matching the specified revision number.
[**deleteEmployerSecret**](EmployerApi.md#deleteEmployerSecret) | **DELETE** /Employer/{EmployerId}/Secret/{SecretId} | Deletes employer secret
[**getAllEmployerTags_0**](EmployerApi.md#getAllEmployerTags_0) | **GET** /Employers/Tags | Get all employer tags
[**getEmployer**](EmployerApi.md#getEmployer) | **GET** /Employer/{EmployerId} | Gets the employer
[**getEmployerByEffectiveDate**](EmployerApi.md#getEmployerByEffectiveDate) | **GET** /Employer/{EmployerId}/{EffectiveDate} | Gets the employer at the specified effective
[**getEmployerRevisionByNumber**](EmployerApi.md#getEmployerRevisionByNumber) | **GET** /Employer/{EmployerId}/Revision/{RevisionNumber} | Gets the employer by revision number
[**getEmployerRevisionSummaries**](EmployerApi.md#getEmployerRevisionSummaries) | **GET** /Employer/{EmployerId}/Revisions/Summary | Get all employer revision summaries
[**getEmployerRevisionSummaryByNumber**](EmployerApi.md#getEmployerRevisionSummaryByNumber) | **GET** /Employer/{EmployerId}/Revision/{RevisionNumber}/Summary | Gets the employer summary by revision number
[**getEmployerRevisions**](EmployerApi.md#getEmployerRevisions) | **GET** /Employer/{EmployerId}/Revisions | Gets the employer revisions
[**getEmployerSecret**](EmployerApi.md#getEmployerSecret) | **GET** /Employer/{EmployerId}/Secret/{SecretId} | Get employer secret
[**getEmployerSecrets**](EmployerApi.md#getEmployerSecrets) | **GET** /Employer/{EmployerId}/Secrets | Get all employer secret links
[**getEmployerSummaries**](EmployerApi.md#getEmployerSummaries) | **GET** /Employers/Summary | Get employer summaries.
[**getEmployerSummariesByEffectiveDate**](EmployerApi.md#getEmployerSummariesByEffectiveDate) | **GET** /Employers/{EffectiveDate}/Summary | Get employer summaries at a given effective date.
[**getEmployerSummary**](EmployerApi.md#getEmployerSummary) | **GET** /Employer/{EmployerId}/Summary | Get employer summary
[**getEmployerSummaryByEffectiveDate**](EmployerApi.md#getEmployerSummaryByEffectiveDate) | **GET** /Employer/{EmployerId}/{EffectiveDate}/Summary | Get employer summary by effective date.
[**getEmployers**](EmployerApi.md#getEmployers) | **GET** /Employers | Gets all employers
[**getEmployersByEffectiveDate**](EmployerApi.md#getEmployersByEffectiveDate) | **GET** /Employers/{EffectiveDate} | Gets all employers at the specified effective date
[**getEmployersWithTag_0**](EmployerApi.md#getEmployersWithTag_0) | **GET** /Employers/Tag/{TagId} | Get employers with tag
[**patchEmployer**](EmployerApi.md#patchEmployer) | **PATCH** /Employer/{EmployerId} | Patches the employer
[**postEmployer**](EmployerApi.md#postEmployer) | **POST** /Employers | Create a new Employer
[**postEmployerSecret**](EmployerApi.md#postEmployerSecret) | **POST** /Employer/{EmployerId}/Secrets | Create a new employer secret
[**putEmployer**](EmployerApi.md#putEmployer) | **PUT** /Employer/{EmployerId} | Updates the Employer
[**putEmployerSecret**](EmployerApi.md#putEmployerSecret) | **PUT** /Employer/{EmployerId}/Secret/{SecretId} | Create a new employer secret



## deleteEmployer

> deleteEmployer(employerId, authorization, apiVersion)

Delete an Employer

Delete the specified employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEmployerRevision

> deleteEmployerRevision(employerId, effectiveDate, authorization, apiVersion)

Delete an Employer revision matching the specified revision date.

Deletes the specified employer revision for the matching revision date

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteEmployerRevision(employerId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## deleteEmployerRevisionByNumber

> deleteEmployerRevisionByNumber(employerId, revisionNumber, authorization, apiVersion)

Delete an Employer revision matching the specified revision number.

Deletes the specified employer revision for the matching revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteEmployerRevisionByNumber(employerId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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


## deleteEmployerSecret

> deleteEmployerSecret(employerId, secretId, authorization, apiVersion)

Deletes employer secret

Deletes an employer secret from the given resource location

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let secretId = "secretId_example"; // String | The secret unique identifier. E.g ERSEC001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteEmployerSecret(employerId, secretId, authorization, apiVersion, (error, data, response) => {
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


## getAllEmployerTags_0

> LinkCollection getAllEmployerTags_0(authorization, apiVersion)

Get all employer tags

Gets all the employer tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllEmployerTags_0(authorization, apiVersion, (error, data, response) => {
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


## getEmployer

> Employer getEmployer(employerId, authorization, apiVersion)

Gets the employer

Get the specified employer object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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

[**Employer**](Employer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployerByEffectiveDate

> Employer getEmployerByEffectiveDate(employerId, effectiveDate, authorization, apiVersion)

Gets the employer at the specified effective

Returns the employer&#39;s state at the specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerByEffectiveDate(employerId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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

[**Employer**](Employer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployerRevisionByNumber

> Employer getEmployerRevisionByNumber(employerId, revisionNumber, authorization, apiVersion)

Gets the employer by revision number

Get the employer revision matching the specified revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerRevisionByNumber(employerId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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
 **revisionNumber** | **String**| The revision number. E.g. 1 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Employer**](Employer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployerRevisionSummaries

> LinkCollection getEmployerRevisionSummaries(employerId, authorization, apiVersion)

Get all employer revision summaries

Gets links to all employer revision summaries

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerRevisionSummaries(employerId, authorization, apiVersion, (error, data, response) => {
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


## getEmployerRevisionSummaryByNumber

> EmployerSummary getEmployerRevisionSummaryByNumber(employerId, revisionNumber, authorization, apiVersion)

Gets the employer summary by revision number

Get the employer revision summary matching the specified revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerRevisionSummaryByNumber(employerId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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
 **revisionNumber** | **String**| The revision number. E.g. 1 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**EmployerSummary**](EmployerSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployerRevisions

> LinkCollection getEmployerRevisions(employerId, authorization, apiVersion)

Gets the employer revisions

Gets links to all the employer revisions

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerRevisions(employerId, authorization, apiVersion, (error, data, response) => {
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


## getEmployerSecret

> EmployerSecret getEmployerSecret(employerId, secretId, authorization, apiVersion)

Get employer secret

Get the public visible employer secret object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let secretId = "secretId_example"; // String | The secret unique identifier. E.g ERSEC001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerSecret(employerId, secretId, authorization, apiVersion, (error, data, response) => {
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
 **secretId** | **String**| The secret unique identifier. E.g ERSEC001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**EmployerSecret**](EmployerSecret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployerSecrets

> LinkCollection getEmployerSecrets(employerId, authorization, apiVersion)

Get all employer secret links

Get all the employer secret links

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerSecrets(employerId, authorization, apiVersion, (error, data, response) => {
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


## getEmployerSummaries

> LinkCollection getEmployerSummaries(authorization, apiVersion)

Get employer summaries.

Get links to all employer summaries.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerSummaries(authorization, apiVersion, (error, data, response) => {
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


## getEmployerSummariesByEffectiveDate

> LinkCollection getEmployerSummariesByEffectiveDate(effectiveDate, authorization, apiVersion)

Get employer summaries at a given effective date.

Get links to all employer summaries on specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerSummariesByEffectiveDate(effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getEmployerSummary

> EmployerSummary getEmployerSummary(employerId, authorization, apiVersion)

Get employer summary

Gets the specified employer summary data.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerSummary(employerId, authorization, apiVersion, (error, data, response) => {
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

[**EmployerSummary**](EmployerSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployerSummaryByEffectiveDate

> EmployerSummary getEmployerSummaryByEffectiveDate(employerId, effectiveDate, authorization, apiVersion)

Get employer summary by effective date.

Gets the employer summary for the specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployerSummaryByEffectiveDate(employerId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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

[**EmployerSummary**](EmployerSummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmployers

> LinkCollection getEmployers(authorization, apiVersion)

Gets all employers

Gets links to all employers contained under the authorised application scope

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployers(authorization, apiVersion, (error, data, response) => {
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


## getEmployersByEffectiveDate

> LinkCollection getEmployersByEffectiveDate(effectiveDate, authorization, apiVersion)

Gets all employers at the specified effective date

Gets links to all employers contained under the authorised application scope for the specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployersByEffectiveDate(effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getEmployersWithTag_0

> LinkCollection getEmployersWithTag_0(tagId, authorization, apiVersion)

Get employers with tag

Gets the employers with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getEmployersWithTag_0(tagId, authorization, apiVersion, (error, data, response) => {
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


## patchEmployer

> Employer patchEmployer(employerId, authorization, apiVersion, employer)

Patches the employer

Patches the specified employer with the supplied values

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let employer = new PayRunIo.Employer(); // Employer | The employer object.
apiInstance.patchEmployer(employerId, authorization, apiVersion, employer, (error, data, response) => {
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
 **employer** | [**Employer**](Employer.md)| The employer object. | 

### Return type

[**Employer**](Employer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postEmployer

> Link postEmployer(authorization, apiVersion, employer)

Create a new Employer

Create a new employer object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let employer = new PayRunIo.Employer(); // Employer | The employer object.
apiInstance.postEmployer(authorization, apiVersion, employer, (error, data, response) => {
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
 **employer** | [**Employer**](Employer.md)| The employer object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postEmployerSecret

> Link postEmployerSecret(employerId, authorization, apiVersion)

Create a new employer secret

Create new employer secret using auto generated resource location key

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.postEmployerSecret(employerId, authorization, apiVersion, (error, data, response) => {
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


## putEmployer

> Employer putEmployer(employerId, authorization, apiVersion, employer)

Updates the Employer

Updates the existing specified employer object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let employer = new PayRunIo.Employer(); // Employer | The employer object.
apiInstance.putEmployer(employerId, authorization, apiVersion, employer, (error, data, response) => {
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
 **employer** | [**Employer**](Employer.md)| The employer object. | 

### Return type

[**Employer**](Employer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putEmployerSecret

> EmployerSecret putEmployerSecret(employerId, secretId, authorization, apiVersion)

Create a new employer secret

Create / update an employer secret at the given resource location

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.EmployerApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let secretId = "secretId_example"; // String | The secret unique identifier. E.g ERSEC001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putEmployerSecret(employerId, secretId, authorization, apiVersion, (error, data, response) => {
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
 **secretId** | **String**| The secret unique identifier. E.g ERSEC001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**EmployerSecret**](EmployerSecret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

