# HostedOnboardingApi.HostedOnboardingPageApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Hop/v5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postGetOnboardingUrl**](HostedOnboardingPageApi.md#postGetOnboardingUrl) | **POST** /getOnboardingUrl | Get a link to a Adyen-hosted onboarding page



## postGetOnboardingUrl

> GetOnboardingUrlResponse postGetOnboardingUrl(opts)

Get a link to a Adyen-hosted onboarding page

Returns a link to an Adyen-hosted onboarding page (HOP) that you can send to your account holder. For more information on how to use HOP, refer to [Hosted onboarding](https://docs.adyen.com/marketplaces-and-platforms/classic/collect-verification-details/hosted-onboarding-page). 

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

let apiInstance = new HostedOnboardingApi.HostedOnboardingPageApi();
let opts = {
  'getOnboardingUrlRequest': new HostedOnboardingApi.GetOnboardingUrlRequest() // GetOnboardingUrlRequest | 
};
apiInstance.postGetOnboardingUrl(opts, (error, data, response) => {
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
 **getOnboardingUrlRequest** | [**GetOnboardingUrlRequest**](GetOnboardingUrlRequest.md)|  | [optional] 

### Return type

[**GetOnboardingUrlResponse**](GetOnboardingUrlResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

