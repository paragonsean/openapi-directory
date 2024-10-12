# AdyenBinLookupApi.GeneralApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/BinLookup/v40*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postGet3dsAvailability**](GeneralApi.md#postGet3dsAvailability) | **POST** /get3dsAvailability | Check if 3D Secure is available
[**postGetCostEstimate**](GeneralApi.md#postGetCostEstimate) | **POST** /getCostEstimate | Get a fees cost estimate



## postGet3dsAvailability

> ThreeDSAvailabilityResponse postGet3dsAvailability(opts)

Check if 3D Secure is available

Verifies whether 3D Secure is available for the specified BIN or card brand. For 3D Secure 2, this endpoint also returns device fingerprinting keys.  For more information, refer to [3D Secure 2](https://docs.adyen.com/online-payments/3d-secure/native-3ds2).

### Example

```javascript
import AdyenBinLookupApi from 'adyen_bin_lookup_api';
let defaultClient = AdyenBinLookupApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenBinLookupApi.GeneralApi();
let opts = {
  'threeDSAvailabilityRequest': new AdyenBinLookupApi.ThreeDSAvailabilityRequest() // ThreeDSAvailabilityRequest | 
};
apiInstance.postGet3dsAvailability(opts, (error, data, response) => {
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
 **threeDSAvailabilityRequest** | [**ThreeDSAvailabilityRequest**](ThreeDSAvailabilityRequest.md)|  | [optional] 

### Return type

[**ThreeDSAvailabilityResponse**](ThreeDSAvailabilityResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postGetCostEstimate

> CostEstimateResponse postGetCostEstimate(opts)

Get a fees cost estimate

&gt;This API is available only for merchants operating in Australia, the EU, and the UK.  Use the Adyen Cost Estimation API to pre-calculate interchange and scheme fee costs. Knowing these costs prior actual payment authorisation gives you an opportunity to charge those costs to the cardholder, if necessary.  To retrieve this information, make the call to the &#x60;/getCostEstimate&#x60; endpoint. The response to this call contains the amount of the interchange and scheme fees charged by the network for this transaction, and also which surcharging policy is possible (based on current regulations).  &gt; Since not all information is known in advance (for example, if the cardholder will successfully authenticate via 3D Secure or if you also plan to provide additional Level 2/3 data), the returned amounts are based on a set of assumption criteria you define in the &#x60;assumptions&#x60; parameter.

### Example

```javascript
import AdyenBinLookupApi from 'adyen_bin_lookup_api';
let defaultClient = AdyenBinLookupApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new AdyenBinLookupApi.GeneralApi();
let opts = {
  'costEstimateRequest': new AdyenBinLookupApi.CostEstimateRequest() // CostEstimateRequest | 
};
apiInstance.postGetCostEstimate(opts, (error, data, response) => {
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
 **costEstimateRequest** | [**CostEstimateRequest**](CostEstimateRequest.md)|  | [optional] 

### Return type

[**CostEstimateResponse**](CostEstimateResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

