# AdyenDataProtectionApi.GeneralApi

All URIs are relative to *https://ca-test.adyen.com/ca/services/DataProtectionService/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postRequestSubjectErasure**](GeneralApi.md#postRequestSubjectErasure) | **POST** /requestSubjectErasure | Submit a Subject Erasure Request.



## postRequestSubjectErasure

> SubjectErasureResponse postRequestSubjectErasure(opts)

Submit a Subject Erasure Request.

Sends the PSP reference containing the shopper data that should be deleted.

### Example

```javascript
import AdyenDataProtectionApi from 'adyen_data_protection_api';
let defaultClient = AdyenDataProtectionApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenDataProtectionApi.GeneralApi();
let opts = {
  'subjectErasureByPspReferenceRequest': new AdyenDataProtectionApi.SubjectErasureByPspReferenceRequest() // SubjectErasureByPspReferenceRequest | 
};
apiInstance.postRequestSubjectErasure(opts, (error, data, response) => {
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
 **subjectErasureByPspReferenceRequest** | [**SubjectErasureByPspReferenceRequest**](SubjectErasureByPspReferenceRequest.md)|  | [optional] 

### Return type

[**SubjectErasureResponse**](SubjectErasureResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

