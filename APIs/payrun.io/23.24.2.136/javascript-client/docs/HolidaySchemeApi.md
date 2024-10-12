# PayRunIo.HolidaySchemeApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteHolidayScheme**](HolidaySchemeApi.md#deleteHolidayScheme) | **DELETE** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId} | Delete an holiday scheme
[**deleteHolidaySchemeRevision**](HolidaySchemeApi.md#deleteHolidaySchemeRevision) | **DELETE** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/{EffectiveDate} | Delete an holiday scheme revision matching the specified revision date.
[**deleteHolidaySchemeRevisionByNumber**](HolidaySchemeApi.md#deleteHolidaySchemeRevisionByNumber) | **DELETE** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Revision/{RevisionNumber} | Delete an HolidayScheme revision matching the specified revision number.
[**deleteHolidaySchemeTag_0**](HolidaySchemeApi.md#deleteHolidaySchemeTag_0) | **DELETE** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId} | Delete holiday scheme tag
[**getAllHolidaySchemeTags_0**](HolidaySchemeApi.md#getAllHolidaySchemeTags_0) | **GET** /Employer/{EmployerId}/HolidaySchemes/Tags | Get all holiday scheme tags
[**getHolidaySchemeByEffectiveDate**](HolidaySchemeApi.md#getHolidaySchemeByEffectiveDate) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/{EffectiveDate} | Get holiday scheme by effective date.
[**getHolidaySchemeFromEmployer**](HolidaySchemeApi.md#getHolidaySchemeFromEmployer) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId} | Get holiday scheme from employer
[**getHolidaySchemeRevisionByNumber**](HolidaySchemeApi.md#getHolidaySchemeRevisionByNumber) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Revision/{RevisionNumber} | Gets the holiday scheme revision by revision number
[**getHolidaySchemeRevisions**](HolidaySchemeApi.md#getHolidaySchemeRevisions) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Revisions | Get all holiday scheme revisions
[**getHolidaySchemesByEffectiveDate**](HolidaySchemeApi.md#getHolidaySchemesByEffectiveDate) | **GET** /Employer/{EmployerId}/HolidaySchemes/{EffectiveDate} | Get holiday schemes from employer at a given effective date.
[**getHolidaySchemesFromEmployer**](HolidaySchemeApi.md#getHolidaySchemesFromEmployer) | **GET** /Employer/{EmployerId}/HolidaySchemes | Get holiday schemes from employer.
[**getHolidaySchemesWithTag_0**](HolidaySchemeApi.md#getHolidaySchemesWithTag_0) | **GET** /Employer/{EmployerId}/HolidaySchemes/Tag/{TagId} | Get holiday schemes with tag
[**getTagFromHolidaySchemeRevision_0**](HolidaySchemeApi.md#getTagFromHolidaySchemeRevision_0) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId}/{EffectiveDate} | Get holiday scheme revision tag
[**getTagFromHolidayScheme_0**](HolidaySchemeApi.md#getTagFromHolidayScheme_0) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId} | Get holiday scheme tag
[**getTagsFromHolidaySchemeRevision_0**](HolidaySchemeApi.md#getTagsFromHolidaySchemeRevision_0) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tags/{EffectiveDate} | Get all holiday scheme revision tags
[**getTagsFromHolidayScheme_0**](HolidaySchemeApi.md#getTagsFromHolidayScheme_0) | **GET** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tags | Get all tags from the holiday scheme
[**patchHolidayScheme**](HolidaySchemeApi.md#patchHolidayScheme) | **PATCH** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId} | Patches the holiday scheme
[**postHolidaySchemeIntoEmployer**](HolidaySchemeApi.md#postHolidaySchemeIntoEmployer) | **POST** /Employer/{EmployerId}/HolidaySchemes | Create a new holiday scheme
[**putHolidaySchemeIntoEmployer**](HolidaySchemeApi.md#putHolidaySchemeIntoEmployer) | **PUT** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId} | Updates the holiday scheme
[**putHolidaySchemeTag_0**](HolidaySchemeApi.md#putHolidaySchemeTag_0) | **PUT** /Employer/{EmployerId}/HolidayScheme/{HolidaySchemeId}/Tag/{TagId} | Insert holiday scheme tag



## deleteHolidayScheme

> deleteHolidayScheme(employerId, holidaySchemeId, authorization, apiVersion)

Delete an holiday scheme

Delete the specified holiday scheme

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteHolidayScheme(employerId, holidaySchemeId, authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteHolidaySchemeRevision

> deleteHolidaySchemeRevision(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion)

Delete an holiday scheme revision matching the specified revision date.

Deletes the specified holiday scheme revision for the matching revision date

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteHolidaySchemeRevision(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## deleteHolidaySchemeRevisionByNumber

> deleteHolidaySchemeRevisionByNumber(employerId, holidaySchemeId, revisionNumber, authorization, apiVersion)

Delete an HolidayScheme revision matching the specified revision number.

Deletes the specified holiday scheme revision for the matching revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteHolidaySchemeRevisionByNumber(employerId, holidaySchemeId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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


## deleteHolidaySchemeTag_0

> deleteHolidaySchemeTag_0(employerId, holidaySchemeId, tagId, authorization, apiVersion)

Delete holiday scheme tag

Deletes a tag from the holiday scheme

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteHolidaySchemeTag_0(employerId, holidaySchemeId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getAllHolidaySchemeTags_0

> LinkCollection getAllHolidaySchemeTags_0(employerId, authorization, apiVersion)

Get all holiday scheme tags

Gets all the holiday scheme tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllHolidaySchemeTags_0(employerId, authorization, apiVersion, (error, data, response) => {
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


## getHolidaySchemeByEffectiveDate

> HolidayScheme getHolidaySchemeByEffectiveDate(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion)

Get holiday scheme by effective date.

Returns the holiday scheme&#39;s state at the specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getHolidaySchemeByEffectiveDate(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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

[**HolidayScheme**](HolidayScheme.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHolidaySchemeFromEmployer

> HolidayScheme getHolidaySchemeFromEmployer(employerId, holidaySchemeId, authorization, apiVersion)

Get holiday scheme from employer

Gets the specified holiday scheme from employer.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getHolidaySchemeFromEmployer(employerId, holidaySchemeId, authorization, apiVersion, (error, data, response) => {
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

[**HolidayScheme**](HolidayScheme.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHolidaySchemeRevisionByNumber

> HolidayScheme getHolidaySchemeRevisionByNumber(employerId, holidaySchemeId, revisionNumber, authorization, apiVersion)

Gets the holiday scheme revision by revision number

Get the holiday scheme revision matching the specified revision number

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let revisionNumber = "revisionNumber_example"; // String | The revision number. E.g. 1
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getHolidaySchemeRevisionByNumber(employerId, holidaySchemeId, revisionNumber, authorization, apiVersion, (error, data, response) => {
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
 **revisionNumber** | **String**| The revision number. E.g. 1 | 
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

[**HolidayScheme**](HolidayScheme.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHolidaySchemeRevisions

> LinkCollection getHolidaySchemeRevisions(employerId, holidaySchemeId, authorization, apiVersion)

Get all holiday scheme revisions

Gets links to all the holiday scheme revisions

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getHolidaySchemeRevisions(employerId, holidaySchemeId, authorization, apiVersion, (error, data, response) => {
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


## getHolidaySchemesByEffectiveDate

> LinkCollection getHolidaySchemesByEffectiveDate(employerId, effectiveDate, authorization, apiVersion)

Get holiday schemes from employer at a given effective date.

Get links to all holiday schemes for the employer on specified effective date.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getHolidaySchemesByEffectiveDate(employerId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getHolidaySchemesFromEmployer

> LinkCollection getHolidaySchemesFromEmployer(employerId, authorization, apiVersion)

Get holiday schemes from employer.

Get links to all holiday schemes for the specified employer.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getHolidaySchemesFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## getHolidaySchemesWithTag_0

> LinkCollection getHolidaySchemesWithTag_0(employerId, tagId, authorization, apiVersion)

Get holiday schemes with tag

Gets the holiday scheme with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getHolidaySchemesWithTag_0(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromHolidaySchemeRevision_0

> Tag getTagFromHolidaySchemeRevision_0(employerId, holidaySchemeId, tagId, effectiveDate, authorization, apiVersion)

Get holiday scheme revision tag

Gets the tag from the holiday scheme revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromHolidaySchemeRevision_0(employerId, holidaySchemeId, tagId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getTagFromHolidayScheme_0

> Tag getTagFromHolidayScheme_0(employerId, holidaySchemeId, tagId, authorization, apiVersion)

Get holiday scheme tag

Gets the tag from the holiday scheme

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromHolidayScheme_0(employerId, holidaySchemeId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromHolidaySchemeRevision_0

> LinkCollection getTagsFromHolidaySchemeRevision_0(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion)

Get all holiday scheme revision tags

Gets all the tags from the holiday scheme revision

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let effectiveDate = new Date("2013-10-20"); // Date | The effective date to be applied. E.g 2016-04-06
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromHolidaySchemeRevision_0(employerId, holidaySchemeId, effectiveDate, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromHolidayScheme_0

> LinkCollection getTagsFromHolidayScheme_0(employerId, holidaySchemeId, authorization, apiVersion)

Get all tags from the holiday scheme

Gets all the tags from the holiday scheme

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromHolidayScheme_0(employerId, holidaySchemeId, authorization, apiVersion, (error, data, response) => {
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


## patchHolidayScheme

> HolidayScheme patchHolidayScheme(employerId, holidaySchemeId, authorization, apiVersion, holidayScheme)

Patches the holiday scheme

Patches the specified holiday scheme with the supplied values

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let holidayScheme = new PayRunIo.HolidayScheme(); // HolidayScheme | The holiday scheme object.
apiInstance.patchHolidayScheme(employerId, holidaySchemeId, authorization, apiVersion, holidayScheme, (error, data, response) => {
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
 **holidayScheme** | [**HolidayScheme**](HolidayScheme.md)| The holiday scheme object. | 

### Return type

[**HolidayScheme**](HolidayScheme.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postHolidaySchemeIntoEmployer

> Link postHolidaySchemeIntoEmployer(employerId, authorization, apiVersion, holidayScheme)

Create a new holiday scheme

Create a new holiday scheme object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let holidayScheme = new PayRunIo.HolidayScheme(); // HolidayScheme | The holiday scheme object.
apiInstance.postHolidaySchemeIntoEmployer(employerId, authorization, apiVersion, holidayScheme, (error, data, response) => {
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
 **holidayScheme** | [**HolidayScheme**](HolidayScheme.md)| The holiday scheme object. | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putHolidaySchemeIntoEmployer

> HolidayScheme putHolidaySchemeIntoEmployer(employerId, holidaySchemeId, authorization, apiVersion, holidayScheme)

Updates the holiday scheme

Updates the existing specified holiday scheme object

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
let holidayScheme = new PayRunIo.HolidayScheme(); // HolidayScheme | The holiday scheme object.
apiInstance.putHolidaySchemeIntoEmployer(employerId, holidaySchemeId, authorization, apiVersion, holidayScheme, (error, data, response) => {
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
 **holidayScheme** | [**HolidayScheme**](HolidayScheme.md)| The holiday scheme object. | 

### Return type

[**HolidayScheme**](HolidayScheme.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putHolidaySchemeTag_0

> Tag putHolidaySchemeTag_0(employerId, holidaySchemeId, tagId, authorization, apiVersion)

Insert holiday scheme tag

Inserts a new tag on the holiday scheme

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.HolidaySchemeApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let holidaySchemeId = "holidaySchemeId_example"; // String | The holiday schemes' unique identifier. E.g HOLSCH001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putHolidaySchemeTag_0(employerId, holidaySchemeId, tagId, authorization, apiVersion, (error, data, response) => {
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

