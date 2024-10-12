# AdyenTestCardsApi.GeneralApi

All URIs are relative to *https://pal-test.adyen.com/pal/services/TestCard/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postCreateTestCardRanges**](GeneralApi.md#postCreateTestCardRanges) | **POST** /createTestCardRanges | Creates one or more test card ranges.



## postCreateTestCardRanges

> CreateTestCardRangesResult postCreateTestCardRanges(opts)

Creates one or more test card ranges.

Creates one or more test card ranges.

### Example

```javascript
import AdyenTestCardsApi from 'adyen_test_cards_api';
let defaultClient = AdyenTestCardsApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenTestCardsApi.GeneralApi();
let opts = {
  'createTestCardRangesRequest': new AdyenTestCardsApi.CreateTestCardRangesRequest() // CreateTestCardRangesRequest | 
};
apiInstance.postCreateTestCardRanges(opts, (error, data, response) => {
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
 **createTestCardRangesRequest** | [**CreateTestCardRangesRequest**](CreateTestCardRangesRequest.md)|  | [optional] 

### Return type

[**CreateTestCardRangesResult**](CreateTestCardRangesResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

