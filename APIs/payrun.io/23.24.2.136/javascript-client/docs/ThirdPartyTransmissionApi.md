# PayRunIo.ThirdPartyTransmissionApi

All URIs are relative to *https://api.test.payrun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteThirdPartyTransaction**](ThirdPartyTransmissionApi.md#deleteThirdPartyTransaction) | **DELETE** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId} | Delete third party transaction
[**getThirdPartyTransaction**](ThirdPartyTransmissionApi.md#getThirdPartyTransaction) | **GET** /Employer/{EmployerId}/ThirdPartyTransaction/{ThirdPartyTransactionId} | Get a third party transaction
[**getThirdPartyTransactions**](ThirdPartyTransmissionApi.md#getThirdPartyTransactions) | **GET** /Employer/{EmployerId}/ThirdPartyTransactions | Get all third party transaction links



## deleteThirdPartyTransaction

> deleteThirdPartyTransaction(employerId, thirdPartyTransactionId, authorization, apiVersion)

Delete third party transaction

Deletes a third party transaction record from the given resource location

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ThirdPartyTransmissionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.deleteThirdPartyTransaction(employerId, thirdPartyTransactionId, authorization, apiVersion, (error, data, response) => {
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
 **authorization** | **String**| The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete. | [default to &#39;Auto&#39;]
 **apiVersion** | **String**| The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version. | [default to &#39;default&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getThirdPartyTransaction

> ThirdPartyTransaction getThirdPartyTransaction(employerId, thirdPartyTransactionId, authorization, apiVersion)

Get a third party transaction

Get a third party transaction

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ThirdPartyTransmissionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let thirdPartyTransactionId = "thirdPartyTransactionId_example"; // String | The third party transaction unique identifier. E.g TP001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getThirdPartyTransaction(employerId, thirdPartyTransactionId, authorization, apiVersion, (error, data, response) => {
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

[**ThirdPartyTransaction**](ThirdPartyTransaction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getThirdPartyTransactions

> LinkCollection getThirdPartyTransactions(employerId, authorization, apiVersion)

Get all third party transaction links

Get all third party transaction links

### Example

```javascript
import PayRunIo from 'pay_run_io';

let apiInstance = new PayRunIo.ThirdPartyTransmissionApi();
let employerId = "employerId_example"; // String | The employers' unique identifier. E.g ER001
let authorization = "'Auto'"; // String | The OAuth 1 authorization header. &apos;Auto&apos; enables auto complete.
let apiVersion = "'default'"; // String | The version of the api to target. Omit or set as &apos;default&apos; to target the current api version.
apiInstance.getThirdPartyTransactions(employerId, authorization, apiVersion, (error, data, response) => {
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

