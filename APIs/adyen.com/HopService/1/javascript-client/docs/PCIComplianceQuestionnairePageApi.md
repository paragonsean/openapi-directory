# HostedOnboardingApi.PCIComplianceQuestionnairePageApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Hop/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postGetPciQuestionnaireUrl**](PCIComplianceQuestionnairePageApi.md#postGetPciQuestionnaireUrl) | **POST** /getPciQuestionnaireUrl | Get a link to a PCI compliance questionnaire



## postGetPciQuestionnaireUrl

> GetPciUrlResponse postGetPciQuestionnaireUrl(opts)

Get a link to a PCI compliance questionnaire

Returns a link to a PCI compliance questionnaire that you can send to your account holder.  &gt; You should only use this endpoint if you have a [partner platform setup](https://docs.adyen.com/marketplaces-and-platforms/classic/platforms-for-partners).

### Example

```javascript
import HostedOnboardingApi from 'hosted_onboarding_api';
let defaultClient = HostedOnboardingApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new HostedOnboardingApi.PCIComplianceQuestionnairePageApi();
let opts = {
  'getPciUrlRequest': new HostedOnboardingApi.GetPciUrlRequest() // GetPciUrlRequest | 
};
apiInstance.postGetPciQuestionnaireUrl(opts, (error, data, response) => {
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
 **getPciUrlRequest** | [**GetPciUrlRequest**](GetPciUrlRequest.md)|  | [optional] 

### Return type

[**GetPciUrlResponse**](GetPciUrlResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

