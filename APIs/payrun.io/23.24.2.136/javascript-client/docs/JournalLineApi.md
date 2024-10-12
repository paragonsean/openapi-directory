# PayRunIo.JournalLineApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteJournalLineTag_0**](JournalLineApi.md#deleteJournalLineTag_0) | **DELETE** /Employer/{EmployerId}/JournalLine/{JournalLineId}/Tag/{TagId} | Delete journal line tag
[**getAllJournalLineTags_0**](JournalLineApi.md#getAllJournalLineTags_0) | **GET** /Employer/{EmployerId}/JournalLines/Tags | Get all journal line tags
[**getAllJournalLinesWithTag_0**](JournalLineApi.md#getAllJournalLinesWithTag_0) | **GET** /Employer/{EmployerId}/JournalLines/Tag/{TagId} | Get links to tagged journal lines
[**getTagFromJournalLine_0**](JournalLineApi.md#getTagFromJournalLine_0) | **GET** /Employer/{EmployerId}/JournalLine/{JournalLineId}/Tag/{TagId} | Get journal line tag
[**getTagsFromJournalLine_0**](JournalLineApi.md#getTagsFromJournalLine_0) | **GET** /Employer/{EmployerId}/JournalLine/{JournalLineId}/Tags | Get tags from journal line
[**putJournalLineTag_0**](JournalLineApi.md#putJournalLineTag_0) | **PUT** /Employer/{EmployerId}/JournalLine/{JournalLineId}/Tag/{TagId} | Insert journal line tag



## deleteJournalLineTag_0

> deleteJournalLineTag_0(employerId, journalLineId, tagId, authorization, apiVersion)

Delete journal line tag

Deletes a tag from the journal line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalLineApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalLineId = "journalLineId_example"; // String | The journal line unique identifier. E.g JL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteJournalLineTag_0(employerId, journalLineId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getAllJournalLineTags_0

> LinkCollection getAllJournalLineTags_0(employerId, authorization, apiVersion)

Get all journal line tags

Gets all the journal line tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalLineApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllJournalLineTags_0(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllJournalLinesWithTag_0

> LinkCollection getAllJournalLinesWithTag_0(employerId, tagId, authorization, apiVersion)

Get links to tagged journal lines

Gets the journal lines with the specified tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalLineApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllJournalLinesWithTag_0(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromJournalLine_0

> Tag getTagFromJournalLine_0(employerId, journalLineId, tagId, authorization, apiVersion)

Get journal line tag

Gets a tag from the journal line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalLineApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalLineId = "journalLineId_example"; // String | The journal line unique identifier. E.g JL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromJournalLine_0(employerId, journalLineId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromJournalLine_0

> LinkCollection getTagsFromJournalLine_0(employerId, journalLineId, authorization, apiVersion)

Get tags from journal line

Gets all tags from the journal line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalLineApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalLineId = "journalLineId_example"; // String | The journal line unique identifier. E.g JL001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromJournalLine_0(employerId, journalLineId, authorization, apiVersion, (error, data, response) => {
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


## putJournalLineTag_0

> Tag putJournalLineTag_0(employerId, journalLineId, tagId, authorization, apiVersion)

Insert journal line tag

Inserts a tag on the journal line

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.JournalLineApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let journalLineId = "journalLineId_example"; // String | The journal line unique identifier. E.g JL001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putJournalLineTag_0(employerId, journalLineId, tagId, authorization, apiVersion, (error, data, response) => {
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

