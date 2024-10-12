# AppStoreConnectApi.DiagnosticSignaturesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagnosticSignaturesLogsGetToManyRelated**](DiagnosticSignaturesApi.md#diagnosticSignaturesLogsGetToManyRelated) | **GET** /v1/diagnosticSignatures/{id}/logs | 



## diagnosticSignaturesLogsGetToManyRelated

> DiagnosticLogsResponse diagnosticSignaturesLogsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.DiagnosticSignaturesApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'limit': 56 // Number | maximum resources per page
};
apiInstance.diagnosticSignaturesLogsGetToManyRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**DiagnosticLogsResponse**](DiagnosticLogsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

