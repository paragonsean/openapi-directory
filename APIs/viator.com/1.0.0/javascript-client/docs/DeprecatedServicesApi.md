# ViatorApiDocumentationAmpSpecificationMerchantPartners.DeprecatedServicesApi

All URIs are relative to *https://viatorapi.viator.com/service*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchantCancellation**](DeprecatedServicesApi.md#merchantCancellation) | **POST** /merchant/cancellation | /merchant/cancellation



## merchantCancellation

> MerchantCancellation200Response merchantCancellation(acceptLanguage, opts)

/merchant/cancellation

Cancel a booking **Note**: This service has been replaced by the [cancellationReasons](#operation/cancellationReasons), [bookingQuote](#operation/bookingQuote) and [cancelBooking](#operation/cancelBooking) endpoints 

### Example

```javascript
import ViatorApiDocumentationAmpSpecificationMerchantPartners from 'viator_api_documentation_amp_specification__merchant_partners';
let defaultClient = ViatorApiDocumentationAmpSpecificationMerchantPartners.ApiClient.instance;
// Configure API key authorization: Legacy-API-key
let Legacy-API-key = defaultClient.authentications['Legacy-API-key'];
Legacy-API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Legacy-API-key.apiKeyPrefix = 'Token';
// Configure API key authorization: API-key
let API-key = defaultClient.authentications['API-key'];
API-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-key.apiKeyPrefix = 'Token';

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.DeprecatedServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'merchantCancellationRequest': new ViatorApiDocumentationAmpSpecificationMerchantPartners.MerchantCancellationRequest() // MerchantCancellationRequest | 
};
apiInstance.merchantCancellation(acceptLanguage, opts, (error, data, response) => {
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
 **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | 
 **merchantCancellationRequest** | [**MerchantCancellationRequest**](MerchantCancellationRequest.md)|  | [optional] 

### Return type

[**MerchantCancellation200Response**](MerchantCancellation200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

