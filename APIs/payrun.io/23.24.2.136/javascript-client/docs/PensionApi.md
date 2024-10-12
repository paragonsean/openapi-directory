# PayRunIo.PensionApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePension**](PensionApi.md#deletePension) | **DELETE** /Employer/{EmployerId}/Pension/{PensionId} | Delete a Pension
[**deletePensionRevision**](PensionApi.md#deletePensionRevision) | **DELETE** /Employer/{EmployerId}/Pension/{PensionId}/{EffectiveDate} | Delete an Pension revision matching the specified revision date.
[**deletePensionRevisionByNumber**](PensionApi.md#deletePensionRevisionByNumber) | **DELETE** /Employer/{EmployerId}/Pension/{PensionId}/Revision/{RevisionNumber} | Delete an Pension revision matching the specified revision number.
[**getPensionByEffectiveDate**](PensionApi.md#getPensionByEffectiveDate) | **GET** /Employer/{EmployerId}/Pension/{PensionId}/{EffectiveDate} | Get pension by effective date.
[**getPensionFromEmployer**](PensionApi.md#getPensionFromEmployer) | **GET** /Employer/{EmployerId}/Pension/{PensionId} | Get pension from employer
[**getPensionRevisionByNumber**](PensionApi.md#getPensionRevisionByNumber) | **GET** /Employer/{EmployerId}/Pension/{PensionId}/Revision/{RevisionNumber} | Gets the pension by revision number
[**getPensionRevisions**](PensionApi.md#getPensionRevisions) | **GET** /Employer/{EmployerId}/Pension/{PensionId}/Revisions | Get all pension revisions
[**getPensionsByEffectiveDate**](PensionApi.md#getPensionsByEffectiveDate) | **GET** /Employer/{EmployerId}/Pensions/{EffectiveDate} | Get pensions from employer at a given effective date.
[**getPensionsFromEmployer**](PensionApi.md#getPensionsFromEmployer) | **GET** /Employer/{EmployerId}/Pensions | Get pensions from employer.
[**patchPension**](PensionApi.md#patchPension) | **PATCH** /Employer/{EmployerId}/Pension/{PensionId} | Patches the pension
[**postPensionIntoEmployer**](PensionApi.md#postPensionIntoEmployer) | **POST** /Employer/{EmployerId}/Pensions | Create a new Pension
[**putPensionIntoEmployer**](PensionApi.md#putPensionIntoEmployer) | **PUT** /Employer/{EmployerId}/Pension/{PensionId} | Updates the Pension



## deletePension

> deletePension(employerId, pensionId, authorization, apiVersion)

Delete a Pension

Delete the specified ppension

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let pensionId = "pensionId_example"; // String | The pensions' unique identifier. E.g PEN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePension(employerId, pensionId, authorization, apiVersion, (error, data, response) => {
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
 **pensionId** | **String**| The pensions&#39; unique identifier. E.g PEN001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePensionRevision

> deletePensionRevision(employerId, pensionId, effectiveDate, authorization, apiVersion)

Delete an Pension revision matching the specified revision date.

Deletes the specified pension revision for the matching revision date

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let pensionId = "pensionId_example"; // String | The pensions' unique identifier. E.g PEN001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePensionRevision(employerId, pensionId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **pensionId** | **String**| The pensions&#39; unique identifier. E.g PEN001 | 
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


## deletePensionRevisionByNumber

> deletePensionRevisionByNumber(employerId, pensionId, revisionNumber, authorization, apiVersion)

Delete an Pension revision matching the specified revision number.

Deletes the specified pension revision for the matching revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let pensionId = "pensionId_example"; // String | The pensions' unique identifier. E.g PEN001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deletePensionRevisionByNumber(employerId, pensionId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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
 **pensionId** | **String**| The pensions&#39; unique identifier. E.g PEN001 | 
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


## getPensionByEffectiveDate

> Pension getPensionByEffectiveDate(employerId, pensionId, effectiveDate, authorization, apiVersion)

Get pension by effective date.

Returns the penion&#39;s state at the specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let pensionId = "pensionId_example"; // String | The pensions' unique identifier. E.g PEN001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPensionByEffectiveDate(employerId, pensionId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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
 **pensionId** | **String**| The pensions&#39; unique identifier. E.g PEN001 | 
 **effectiveDate** | **Date**| The effective date to be applied. E.g 2016-04-06 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Pension**](Pension.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPensionFromEmployer

> Pension getPensionFromEmployer(employerId, pensionId, authorization, apiVersion)

Get pension from employer

Gets the specified pension from employer by pension code.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let pensionId = "pensionId_example"; // String | The pensions' unique identifier. E.g PEN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPensionFromEmployer(employerId, pensionId, authorization, apiVersion, (error, data, response) => {
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
 **pensionId** | **String**| The pensions&#39; unique identifier. E.g PEN001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Pension**](Pension.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPensionRevisionByNumber

> Pension getPensionRevisionByNumber(employerId, pensionId, revisionNumber, authorization, apiVersion)

Gets the pension by revision number

Get the pension revision matching the specified revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let pensionId = "pensionId_example"; // String | The pensions' unique identifier. E.g PEN001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPensionRevisionByNumber(employerId, pensionId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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
 **pensionId** | **String**| The pensions&#39; unique identifier. E.g PEN001 | 
 **revisionNumber** | **String**| The revision number. E.g. 1 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**Pension**](Pension.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPensionRevisions

> LinkCollection getPensionRevisions(employerId, pensionId, authorization, apiVersion)

Get all pension revisions

Returns links to all revisions of the pension

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let pensionId = "pensionId_example"; // String | The pensions' unique identifier. E.g PEN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPensionRevisions(employerId, pensionId, authorization, apiVersion, (error, data, response) => {
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
 **pensionId** | **String**| The pensions&#39; unique identifier. E.g PEN001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**LinkCollection**](LinkCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPensionsByEffectiveDate

> LinkCollection getPensionsByEffectiveDate(employerId, effectiveDate, authorization, apiVersion)

Get pensions from employer at a given effective date.

Get links to all pensions for the employer on specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPensionsByEffectiveDate(employerId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getPensionsFromEmployer

> LinkCollection getPensionsFromEmployer(employerId, authorization, apiVersion)

Get pensions from employer.

Get links to all pensions for the specified employer.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getPensionsFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## patchPension

> Pension patchPension(employerId, pensionId, authorization, apiVersion, pension)

Patches the pension

Patches the specified pension with the supplied values

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let pensionId = "pensionId_example"; // String | The pensions' unique identifier. E.g PEN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let pension = new PayRunIo.Pension(); // Pension | The pension object.
apiInstance.patchPension(employerId, pensionId, authorization, apiVersion, pension, (error, data, response) => {
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
 **pensionId** | **String**| The pensions&#39; unique identifier. E.g PEN001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **pension** | [**Pension**](Pension.md)| The pension object. | 

### Return type

[**Pension**](Pension.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPensionIntoEmployer

> Link postPensionIntoEmployer(employerId, authorization, apiVersion, pension)

Create a new Pension

Create a new pension object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let pension = new PayRunIo.Pension(); // Pension | The pension object.
apiInstance.postPensionIntoEmployer(employerId, authorization, apiVersion, pension, (error, data, response) => {
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
 **pension** | [**Pension**](Pension.md)| The pension object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPensionIntoEmployer

> Pension putPensionIntoEmployer(employerId, pensionId, authorization, apiVersion, pension)

Updates the Pension

Updates existing or inserts the specified pension object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.PensionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let pensionId = "pensionId_example"; // String | The pensions' unique identifier. E.g PEN001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let pension = new PayRunIo.Pension(); // Pension | The pension object.
apiInstance.putPensionIntoEmployer(employerId, pensionId, authorization, apiVersion, pension, (error, data, response) => {
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
 **pensionId** | **String**| The pensions&#39; unique identifier. E.g PEN001 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]
 **pension** | [**Pension**](Pension.md)| The pension object. | 

### Return type

[**Pension**](Pension.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

