# PayRunIo.RTIApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRtiTransaction**](RTIApi.md#deleteRtiTransaction) | **DELETE** /Employer/{EmployerId}/RtiTransaction/{RtiTransactionId} | Delete the RTI transaction
[**getAllRtiTransactionTags_0**](RTIApi.md#getAllRtiTransactionTags_0) | **GET** /Employer/{EmployerId}/RtiTransactions/Tags | Get all RTI transaction tags
[**getRtiTransactionFromEmployer**](RTIApi.md#getRtiTransactionFromEmployer) | **GET** /Employer/{EmployerId}/RtiTransaction/{RtiTransactionId} | Get the RTI transaction
[**getRtiTransactionSummariesFromEmployer**](RTIApi.md#getRtiTransactionSummariesFromEmployer) | **GET** /Employer/{EmployerId}/RtiTransactions/Summary | Get all RTI transaction summaries for the employer
[**getRtiTransactionSummaryFromEmployer**](RTIApi.md#getRtiTransactionSummaryFromEmployer) | **GET** /Employer/{EmployerId}/RtiTransaction/{RtiTransactionId}/Summary | Get the RTI transaction summary
[**getRtiTransactionsFromEmployer**](RTIApi.md#getRtiTransactionsFromEmployer) | **GET** /Employer/{EmployerId}/RtiTransactions | Get all RTI transactions for the employer
[**getRtiTransactionsWithTag_0**](RTIApi.md#getRtiTransactionsWithTag_0) | **GET** /Employer/{EmployerId}/RtiTransactions/Tag/{TagId} | Get RTI transactions with tag



## deleteRtiTransaction

> deleteRtiTransaction(employerId, rtiTransactionId, authorization, apiVersion)

Delete the RTI transaction

Deletes the specified RTI transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.RTIApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let rtiTransactionId = "rtiTransactionId_example"; // String | The RTI transaction unique identifier. E.g. FPS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteRtiTransaction(employerId, rtiTransactionId, authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllRtiTransactionTags_0

> LinkCollection getAllRtiTransactionTags_0(employerId, authorization, apiVersion)

Get all RTI transaction tags

Gets all the RTI transaction tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.RTIApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllRtiTransactionTags_0(employerId, authorization, apiVersion, (error, data, response) => {
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


## getRtiTransactionFromEmployer

> RtiTransactionBase getRtiTransactionFromEmployer(employerId, rtiTransactionId, authorization, apiVersion)

Get the RTI transaction

Returns the specified RTI transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.RTIApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let rtiTransactionId = "rtiTransactionId_example"; // String | The RTI transaction unique identifier. E.g. FPS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getRtiTransactionFromEmployer(employerId, rtiTransactionId, authorization, apiVersion, (error, data, response) => {
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

[**RtiTransactionBase**](RtiTransactionBase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRtiTransactionSummariesFromEmployer

> LinkCollection getRtiTransactionSummariesFromEmployer(employerId, authorization, apiVersion)

Get all RTI transaction summaries for the employer

Get links for all RTI transaction summaries for the specified employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.RTIApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getRtiTransactionSummariesFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## getRtiTransactionSummaryFromEmployer

> RtiTransactionBase getRtiTransactionSummaryFromEmployer(employerId, rtiTransactionId, authorization, apiVersion)

Get the RTI transaction summary

Returns the specified RTI transaction summary data excluding some poroperties

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.RTIApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let rtiTransactionId = "rtiTransactionId_example"; // String | The RTI transaction unique identifier. E.g. FPS001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getRtiTransactionSummaryFromEmployer(employerId, rtiTransactionId, authorization, apiVersion, (error, data, response) => {
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

[**RtiTransactionBase**](RtiTransactionBase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRtiTransactionsFromEmployer

> LinkCollection getRtiTransactionsFromEmployer(employerId, authorization, apiVersion)

Get all RTI transactions for the employer

Get links for all RTI transactions for the specified employer

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.RTIApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getRtiTransactionsFromEmployer(employerId, authorization, apiVersion, (error, data, response) => {
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


## getRtiTransactionsWithTag_0

> LinkCollection getRtiTransactionsWithTag_0(employerId, tagId, authorization, apiVersion)

Get RTI transactions with tag

Gets the RTI transactions with the tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.RTIApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getRtiTransactionsWithTag_0(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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

