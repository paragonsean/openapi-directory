# ViatorApiDocumentationAmpSpecificationMerchantPartners.TaxonomyServicesApi

All URIs are relative to *https://viatorapi.viator.com/service*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxonomyAttractions**](TaxonomyServicesApi.md#taxonomyAttractions) | **POST** /taxonomy/attractions | /taxonomy/attractions
[**taxonomyCategories**](TaxonomyServicesApi.md#taxonomyCategories) | **GET** /taxonomy/categories | /taxonomy/categories
[**taxonomyDestinations**](TaxonomyServicesApi.md#taxonomyDestinations) | **GET** /taxonomy/destinations | /taxonomy/destinations



## taxonomyAttractions

> TaxonomyAttractions200Response taxonomyAttractions(acceptLanguage, opts)

/taxonomy/attractions

Get attractions - Retrieves a list of attractions (things like the Eiffel Tower or Empire State Building) and their associated unique numeric identifiers - The attraction&#39;s identifier (&#x60;seoId&#x60;) can be used as a means of searching for available products; for example, in the [/search/products](#operation/searchProducts) service. 

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.TaxonomyServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'taxonomyAttractionsRequest': {"destId":684,"sortOrder":"SEO_PUBLISHED_DATE_D","topX":"1-3"} // TaxonomyAttractionsRequest | 
};
apiInstance.taxonomyAttractions(acceptLanguage, opts, (error, data, response) => {
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
 **taxonomyAttractionsRequest** | [**TaxonomyAttractionsRequest**](TaxonomyAttractionsRequest.md)|  | [optional] 

### Return type

[**TaxonomyAttractions200Response**](TaxonomyAttractions200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## taxonomyCategories

> TaxonomyCategories200Response taxonomyCategories(acceptLanguage, opts)

/taxonomy/categories

Get all product categories - Retrieves a list of product categories for a destination that can be used as a means of filtering when searching for products using the [/search/products](/#operation/searchProducts) service - This service can be used to get a list of all categories and subcategories for a destination by including its &#x60;destId&#x60;, or you can omit the &#x60;destId&#x60; to get a list of all categories and subcategories - **Note:** If no &#x60;destId&#x60; is passed, &#x60;productCount&#x60; and &#x60;thumbnailURL&#x60; will be &#x60;null&#x60; as they are destination-specific fields 

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.TaxonomyServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'destId': 684 // Number | **unique numeric identifier** of the destination to enquire about (optional) - `destinationId` is returned by [/taxonomy/destinations](#operation/taxonomyDestinations) 
};
apiInstance.taxonomyCategories(acceptLanguage, opts, (error, data, response) => {
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
 **destId** | **Number**| **unique numeric identifier** of the destination to enquire about (optional) - &#x60;destinationId&#x60; is returned by [/taxonomy/destinations](#operation/taxonomyDestinations)  | [optional] 

### Return type

[**TaxonomyCategories200Response**](TaxonomyCategories200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taxonomyDestinations

> TaxonomyDestinations200Response taxonomyDestinations(acceptLanguage)

/taxonomy/destinations

Get details of all destinations supported by this API - Retrieves all the country taxonomy/city nodes as a flat list - Returns a complete list of Viator destinations, including destination names and parent identifiers - Used to provide navigation through drill down lists or combo boxes 

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.TaxonomyServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
apiInstance.taxonomyDestinations(acceptLanguage, (error, data, response) => {
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

[**TaxonomyDestinations200Response**](TaxonomyDestinations200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

