# ActiveDocumentationForV1.AccountApi

All URIs are relative to *https://api.idtbeyond.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iatuBalanceGet**](AccountApi.md#iatuBalanceGet) | **GET** /iatu/balance | Account balance



## iatuBalanceGet

> iatuBalanceGet(xIdtBeyondAppId, xIdtBeyondAppKey)

Account balance

Returns a JSON of the account balance.

### Example

```javascript
import ActiveDocumentationForV1 from 'active_documentation_for__v1';

let apiInstance = new ActiveDocumentationForV1.AccountApi();
let xIdtBeyondAppId = "'APP_ID'"; // String | Application ID you would like to use
let xIdtBeyondAppKey = "'APP_KEY'"; // String | Application KEY you would like to use
apiInstance.iatuBalanceGet(xIdtBeyondAppId, xIdtBeyondAppKey, (error, data, response) => {
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
 **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to &#39;APP_ID&#39;]
 **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to &#39;APP_KEY&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

