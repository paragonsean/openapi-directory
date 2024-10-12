# PayRunIo.ReferenceApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJournalExpressionSchema**](ReferenceApi.md#getJournalExpressionSchema) | **GET** /ReferenceData/JournalExpressionDataTable | Gets the journal expression data schema



## getJournalExpressionSchema

> JournalExpressionDataTable getJournalExpressionSchema(authorization, apiVersion)

Gets the journal expression data schema

Gets the data schema for all available journal expression values. Includes table names, column names and data types.

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ReferenceApi();
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getJournalExpressionSchema(authorization, apiVersion, (error, data, response) => {
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

[**JournalExpressionDataTable**](JournalExpressionDataTable.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

