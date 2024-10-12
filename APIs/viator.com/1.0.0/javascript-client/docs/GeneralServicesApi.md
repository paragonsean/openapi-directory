# ViatorApiDocumentationAmpSpecificationMerchantPartners.GeneralServicesApi

All URIs are relative to *https://viatorapi.viator.com/service*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthCheck**](GeneralServicesApi.md#healthCheck) | **GET** /health/check | /health/check



## healthCheck

> HealthCheck200Response healthCheck(acceptLanguage)

/health/check

Health check Use this service to determine whether the Viator API is presently online and that your API key is valid. You should receive a response identical to the example shown. If you have not yet received an API key, please request one from your business development partner. If you have not yet signed up as a Viator merchant partner and would like to, please visit our [distribution partner website](https://www.viator.com/distribution-partners?mcid&#x3D;58463#api-solutions).\&quot; 

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.GeneralServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
apiInstance.healthCheck(acceptLanguage, (error, data, response) => {
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

### Return type

[**HealthCheck200Response**](HealthCheck200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

