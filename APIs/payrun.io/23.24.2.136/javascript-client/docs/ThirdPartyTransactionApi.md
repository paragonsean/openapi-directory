# PayRunIo.ThirdPartyTransactionApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteThirdPartyTransactionTag_0**](ThirdPartyTransactionApi.md#deleteThirdPartyTransactionTag_0) | **DELETE** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId}/Tag/{TagId} | Delete third party transaction tag
[**getAllThirdPartyTransactionTags_0**](ThirdPartyTransactionApi.md#getAllThirdPartyTransactionTags_0) | **GET** /Employer/{EmployerId}/ThirdPartyTransactions/Tags | Get all third party transaction tags
[**getAllThirdPartyTransactionsWithTag_0**](ThirdPartyTransactionApi.md#getAllThirdPartyTransactionsWithTag_0) | **GET** /Employer/{EmployerId}/ThirdPartyTransactions/Tag/{TagId} | Get links to tagged third party transactions
[**getTagFromThirdPartyTransaction_0**](ThirdPartyTransactionApi.md#getTagFromThirdPartyTransaction_0) | **GET** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId}/Tag/{TagId} | Get third party transaction tag
[**getTagsFromThirdPartyTransaction_0**](ThirdPartyTransactionApi.md#getTagsFromThirdPartyTransaction_0) | **GET** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId}/Tags | Get tags from third party transaction
[**putThirdPartyTransactionTag_0**](ThirdPartyTransactionApi.md#putThirdPartyTransactionTag_0) | **PUT** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId}/Tag/{TagId} | insert third party transaction tag



## deleteThirdPartyTransactionTag_0

> deleteThirdPartyTransactionTag_0(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion)

Delete third party transaction tag

Deletes a tag from the third party transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ThirdPartyTransactionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteThirdPartyTransactionTag_0(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getAllThirdPartyTransactionTags_0

> LinkCollection getAllThirdPartyTransactionTags_0(employerId, authorization, apiVersion)

Get all third party transaction tags

Gets all the third party transaction tags

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ThirdPartyTransactionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllThirdPartyTransactionTags_0(employerId, authorization, apiVersion, (error, data, response) => {
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


## getAllThirdPartyTransactionsWithTag_0

> LinkCollection getAllThirdPartyTransactionsWithTag_0(employerId, tagId, authorization, apiVersion)

Get links to tagged third party transactions

Gets the third party transactions with the specified tag

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ThirdPartyTransactionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getAllThirdPartyTransactionsWithTag_0(employerId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagFromThirdPartyTransaction_0

> Tag getTagFromThirdPartyTransaction_0(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion)

Get third party transaction tag

Gets a tag from the third party transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ThirdPartyTransactionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagFromThirdPartyTransaction_0(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion, (error, data, response) => {
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


## getTagsFromThirdPartyTransaction_0

> LinkCollection getTagsFromThirdPartyTransaction_0(employerId, thirdPartyTransactionId, authorization, apiVersion)

Get tags from third party transaction

Gets all tags from the third party transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ThirdPartyTransactionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getTagsFromThirdPartyTransaction_0(employerId, thirdPartyTransactionId, authorization, apiVersion, (error, data, response) => {
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


## putThirdPartyTransactionTag_0

> Tag putThirdPartyTransactionTag_0(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion)

insert third party transaction tag

Inserts a tag on the third party transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ThirdPartyTransactionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
let tagId = "tagId_example"; // String | The tag unique identifier. E.g. MyTag
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.putThirdPartyTransactionTag_0(employerId, thirdPartyTransactionId, tagId, authorization, apiVersion, (error, data, response) => {
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

