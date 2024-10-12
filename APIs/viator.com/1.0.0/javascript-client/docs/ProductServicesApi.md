# ViatorApiDocumentationAmpSpecificationMerchantPartners.ProductServicesApi

All URIs are relative to *https://viatorapi.viator.com/service*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availableProducts**](ProductServicesApi.md#availableProducts) | **POST** /available/products | /available/products
[**product**](ProductServicesApi.md#product) | **GET** /product | /product
[**productPhotos**](ProductServicesApi.md#productPhotos) | **GET** /product/photos | /product/photos
[**productReviews**](ProductServicesApi.md#productReviews) | **GET** /product/reviews | /product/reviews
[**searchFreetext**](ProductServicesApi.md#searchFreetext) | **POST** /search/freetext | /search/freetext
[**searchProducts**](ProductServicesApi.md#searchProducts) | **POST** /search/products | /search/products
[**searchProductsCodes**](ProductServicesApi.md#searchProductsCodes) | **POST** /search/products/codes | /search/products/codes



## availableProducts

> AvailableProducts200Response availableProducts(acceptLanguage, opts)

/available/products

Find products that are available   This endpoint returns available products filtered by product code, date range or number of adult travelers    - **Note**: Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.    

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.ProductServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'availableProductsRequest': {"currencyCode":"USD","endDate":"2020-12-31","numAdults":1,"productCodes":["5010SYDNEY","2280SUN","9169P50"],"startDate":"2020-12-21"} // AvailableProductsRequest | 
};
apiInstance.availableProducts(acceptLanguage, opts, (error, data, response) => {
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
 **availableProductsRequest** | [**AvailableProductsRequest**](AvailableProductsRequest.md)|  | [optional] 

### Return type

[**AvailableProducts200Response**](AvailableProducts200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## product

> Product200Response product(acceptLanguage, opts)

/product

Get product information This service provides all product details required for a product display page, as well as information required for price checks and booking, such as:  - age bands - tour grades - language options  - booking questions - hotel pickup flags  **currencyCode (in query):**  - use this parameter to specify the currency in which product pricing should be displayed - the default currency is the currency of your account; or, if you have multi-currency enabled, US dollars - \&quot;multi-currency\&quot; allows pricing and booking in various currencies - please speak to the business development team if you&#39;d like this enabled - **Note**: you will be billed in the currency in which the booking was made  **Product photos**  &amp;lt;mark&amp;gt;**&amp;lt;u&amp;gt;Update 13 Feb 2020&amp;lt;/u&amp;gt;**: All supplier-provided photos for the selected product are now available in the &#x60;productPhotos&#x60; array in this endpoint&#39;s response. Previously, only two supplier-provided photos were available – one in the &#x60;productPhotos&#x60; array and one in &#x60;thumbnailHiResURL&#x60;. &amp;lt;/mark&amp;gt;  **Videos**  - Videos are no longer provided via this API 

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.ProductServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'currencyCode': "currencyCode_example", // String | **currency code** for the currency in which pricing is displayed - default=`'USD'` 
  'sortOrder': "sortOrder_example", // String | **specifier** of the order in which to return reviews  Sort order options:    - `\"REVIEW_RATING_A\"`: Traveler Rating (low→high) Average   - `\"REVIEW_RATING_D\"`: Traveler Rating (high→low) Average   - `\"REVIEW_RATING_SUBMISSION_DATE_D\"`: Most recent review 
  'voucherOption': "voucherOption_example", // String | - `\"VOUCHER_PAPER_ONLY\"`: Paper Vouchers only accepted - `\"VOUCHER_E\"`: EVouchers + Paper Vouchers accepted 
  'code': "5010SYDNEY", // String | **unique alphanumeric identifier** of the product
  'showUnavailable': false, // Boolean | **specifier** as to whether or not to show 'unavailable' products:    - `true`: return *both* available and unavailable products   - `false`: return *only* available products (default) 
  'excludeTourGradeAvailability': true // Boolean | **specifier:**  - `true`: return **all** tour grades, including those that are not available - `false`: only display tour grades that *are* available 
};
apiInstance.product(acceptLanguage, opts, (error, data, response) => {
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
 **currencyCode** | **String**| **currency code** for the currency in which pricing is displayed - default&#x3D;&#x60;&#39;USD&#39;&#x60;  | [optional] 
 **sortOrder** | **String**| **specifier** of the order in which to return reviews  Sort order options:    - &#x60;\&quot;REVIEW_RATING_A\&quot;&#x60;: Traveler Rating (low→high) Average   - &#x60;\&quot;REVIEW_RATING_D\&quot;&#x60;: Traveler Rating (high→low) Average   - &#x60;\&quot;REVIEW_RATING_SUBMISSION_DATE_D\&quot;&#x60;: Most recent review  | [optional] 
 **voucherOption** | **String**| - &#x60;\&quot;VOUCHER_PAPER_ONLY\&quot;&#x60;: Paper Vouchers only accepted - &#x60;\&quot;VOUCHER_E\&quot;&#x60;: EVouchers + Paper Vouchers accepted  | [optional] 
 **code** | **String**| **unique alphanumeric identifier** of the product | [optional] 
 **showUnavailable** | **Boolean**| **specifier** as to whether or not to show &#39;unavailable&#39; products:    - &#x60;true&#x60;: return *both* available and unavailable products   - &#x60;false&#x60;: return *only* available products (default)  | [optional] 
 **excludeTourGradeAvailability** | **Boolean**| **specifier:**  - &#x60;true&#x60;: return **all** tour grades, including those that are not available - &#x60;false&#x60;: only display tour grades that *are* available  | [optional] 

### Return type

[**Product200Response**](Product200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productPhotos

> ProductPhotos200Response productPhotos(acceptLanguage, opts)

/product/photos

Get photos of a product submitted by users

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.ProductServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'topX': "1-3", // String | **start and end rows** to return in the format {start}-{end} - e.g. `'1-10'`, `'11-20'`  **Note**:  - the maximum number of rows per request is 100; therefore, `'100-400'` will return the same as `'100-200'` - if `topX` is not specified, the default is `'1-100'` 
  'code': "5010SYDNEY", // String | **unique alphanumeric identifier** of the product
  'showUnavailable': false // Boolean | **specifier** as to whether or not to show 'unavailable' products:    - `true`: return *both* available and unavailable products   - `false`: return *only* available products (default) 
};
apiInstance.productPhotos(acceptLanguage, opts, (error, data, response) => {
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
 **topX** | **String**| **start and end rows** to return in the format {start}-{end} - e.g. &#x60;&#39;1-10&#39;&#x60;, &#x60;&#39;11-20&#39;&#x60;  **Note**:  - the maximum number of rows per request is 100; therefore, &#x60;&#39;100-400&#39;&#x60; will return the same as &#x60;&#39;100-200&#39;&#x60; - if &#x60;topX&#x60; is not specified, the default is &#x60;&#39;1-100&#39;&#x60;  | [optional] 
 **code** | **String**| **unique alphanumeric identifier** of the product | [optional] 
 **showUnavailable** | **Boolean**| **specifier** as to whether or not to show &#39;unavailable&#39; products:    - &#x60;true&#x60;: return *both* available and unavailable products   - &#x60;false&#x60;: return *only* available products (default)  | [optional] 

### Return type

[**ProductPhotos200Response**](ProductPhotos200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productReviews

> ProductReviews200Response productReviews(acceptLanguage, opts)

/product/reviews

Get user-submitted reviews of a product  **Note**:  - The number of reviews that you can obtain via this service will depend on whether your account is limited in terms of the number of reviews you are entitled to receive.  - The number of reviews available through this service is given in the &#x60;reviewCount&#x60; element in the response from [/product](#operation/product) - Please speak to your account manager if you wish to receive more reviews. If your account is not limited, you will be able to receive all available reviews for this product. - Only reviews in the language specified in the Accept-Language request header will be returned  **Example:** \&quot;Get the first three reviews for product &#x60;5010SYDNEY&#x60; sorted by rating in ascending order\&quot;:  &#x60;&#x60;&#x60;javascript https://viatorapi.sandbox.viator.com/service/product/reviews?sortOrder&#x3D;REVIEW_RATING_A&amp;amp;topX&#x3D;1-3&amp;amp;code&#x3D;5010SYDNEY&amp;amp;showUnavailable&#x3D;false &#x60;&#x60;&#x60; 

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.ProductServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'sortOrder': "sortOrder_example", // String | **specifier** of the order in which to return reviews  Sort order options:    - `\"REVIEW_RATING_A\"`: Traveler Rating (low→high) Average   - `\"REVIEW_RATING_D\"`: Traveler Rating (high→low) Average   - `\"REVIEW_RATING_SUBMISSION_DATE_D\"`: Most recent review 
  'topX': "1-3", // String | **start and end rows** to return in the format {start}-{end} - e.g. `'1-10'`, `'11-20'`  **Note**:  - the maximum number of rows per request is 100; therefore, `'100-400'` will return the same as `'100-200'` - if `topX` is not specified, the default is `'1-100'` 
  'code': "5010SYDNEY", // String | **unique alphanumeric identifier** of the product
  'showUnavailable': false // Boolean | **specifier** as to whether or not to show 'unavailable' products:    - `true`: return *both* available and unavailable products   - `false`: return *only* available products (default) 
};
apiInstance.productReviews(acceptLanguage, opts, (error, data, response) => {
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
 **sortOrder** | **String**| **specifier** of the order in which to return reviews  Sort order options:    - &#x60;\&quot;REVIEW_RATING_A\&quot;&#x60;: Traveler Rating (low→high) Average   - &#x60;\&quot;REVIEW_RATING_D\&quot;&#x60;: Traveler Rating (high→low) Average   - &#x60;\&quot;REVIEW_RATING_SUBMISSION_DATE_D\&quot;&#x60;: Most recent review  | [optional] 
 **topX** | **String**| **start and end rows** to return in the format {start}-{end} - e.g. &#x60;&#39;1-10&#39;&#x60;, &#x60;&#39;11-20&#39;&#x60;  **Note**:  - the maximum number of rows per request is 100; therefore, &#x60;&#39;100-400&#39;&#x60; will return the same as &#x60;&#39;100-200&#39;&#x60; - if &#x60;topX&#x60; is not specified, the default is &#x60;&#39;1-100&#39;&#x60;  | [optional] 
 **code** | **String**| **unique alphanumeric identifier** of the product | [optional] 
 **showUnavailable** | **Boolean**| **specifier** as to whether or not to show &#39;unavailable&#39; products:    - &#x60;true&#x60;: return *both* available and unavailable products   - &#x60;false&#x60;: return *only* available products (default)  | [optional] 

### Return type

[**ProductReviews200Response**](ProductReviews200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchFreetext

> SearchFreetext200Response searchFreetext(acceptLanguage, opts)

/search/freetext

Free text search - This service provides a **free text search across all products and destinations** - The &#x60;text&#x60; parameter is required - **Note:** results include a type indicator (&#x60;type&#x60;) that you can use to display each result appropriately based on its content 

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.ProductServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'searchFreetextRequest': {"currencyCode":"EUR","destId":684,"searchTypes":["ATTRACTION","RECOMMENDATION"],"text":"grand","topX":"1-3"} // SearchFreetextRequest | 
};
apiInstance.searchFreetext(acceptLanguage, opts, (error, data, response) => {
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
 **searchFreetextRequest** | [**SearchFreetextRequest**](SearchFreetextRequest.md)|  | [optional] 

### Return type

[**SearchFreetext200Response**](SearchFreetext200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchProducts

> SearchProducts200Response searchProducts(acceptLanguage, opts)

/search/products

Search for products This service is used to search for products based on various criteria; such as: * the destination (locale) in which it operates * its association with a tourist attraction * its category and/or subcategory * the time period during which it operates The fields you include in the request body for this service determine the kind of search that will be performed.  **&amp;lt;u&amp;gt;Note&amp;lt;/u&amp;gt;**:   * You can search **EITHER** by destination (&#x60;destId&#x60;) **OR** by attraction-link (&#x60;seoId&#x60;), but not both. * The destination identifier (&#x60;destId&#x60;) can be retrieved from the [/taxonomy/destinations](#operation/taxonomyDestinations) service. * The category (&#x60;catId&#x60;) and subcategory (&#x60;subCatId&#x60;) identifiers can be retrieved from the [/taxonomy/categories](#operation/taxonomyCategories) service. * The attraction identifier (&#x60;seoId&#x60;) can be retrieved from the [/taxonomy/attractions](#operation/taxonomyAttractions) service.  **&amp;lt;u&amp;gt;Examples&amp;lt;/u&amp;gt;**:  **Search by destination**:  * E.g., \&quot;Top ten highest-rated yoga classes operating in Las Vegas: &#x60;&#x60;&#x60;javascript {     \&quot;destId\&quot;: 684,     \&quot;subCatId\&quot;: 26052,     \&quot;sortOrder\&quot;: \&quot;REVIEW_AVG_RATING_D\&quot;,     \&quot;topX\&quot;: \&quot;1-3\&quot; } &#x60;&#x60;&#x60;  **Search by attraction-link**:  * E.g., \&quot;Products related to Everglades National Park operating 21-26 May 2019 in order of descending price\&quot;: &#x60;&#x60;&#x60;javascript {     \&quot;seoId\&quot;: 1115,     \&quot;sortOrder\&quot;: \&quot;PRICE_FROM_D\&quot;,     \&quot;topX\&quot;: \&quot;1-3\&quot; } &#x60;&#x60;&#x60;  **&amp;lt;u&amp;gt;&#39;Freesale-only&#39; merchants&amp;lt;/u&amp;gt;**: - Merchants with a \&quot;freesale only\&quot; key *must* pass &#x60;startDate&#x60; and &#x60;endDate&#x60; to this service to retrieve a list of all available &#39;freesale&#39; products (and &#39;freesale/on-request&#39; products that are currently &#39;freesale&#39;) in the destination.  - E.g., the following request body will result in &#39;freesale/on-request&#39; products within their on-request period not appearing in the results from this service.  &#x60;&#x60;&#x60;javascript {     \&quot;destId\&quot;: 684,     \&quot;startDate\&quot;: \&quot;2020-02-21\&quot;,     \&quot;endDate\&quot;: \&quot;2020-03-21\&quot;,     \&quot;sortOrder\&quot;: \&quot;PRICE_FROM_D\&quot;,     \&quot;topX\&quot;: \&quot;1-3\&quot; } &#x60;&#x60;&#x60;  - If &#x60;startDate&#x60; and &#x60;endDate&#x60; are omitted, &#39;freesale/on-request&#39; products that are presently within their on-request period may appear to be available to customers, but won&#39;t be available at the time of booking. 

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.ProductServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'searchProductsRequest': {"destId":684,"sortOrder":"REVIEW_AVG_RATING_D","subCatId":26052,"topX":"1-3"} // SearchProductsRequest | 
};
apiInstance.searchProducts(acceptLanguage, opts, (error, data, response) => {
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
 **searchProductsRequest** | [**SearchProductsRequest**](SearchProductsRequest.md)|  | [optional] 

### Return type

[**SearchProducts200Response**](SearchProducts200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchProductsCodes

> SearchProductsCodes200Response searchProductsCodes(acceptLanguage, opts)

/search/products/codes

Search by product code - This service returns an array of products given an array of product identifiers that is useful for wishlist / shopping cart / user account display  - **Note**: requesting an inactive or non-existent product code will return &#x60;0&#x60;, &#x60;null&#x60; and blank values (as per the &#39;invalid_product&#39; example). 

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

let apiInstance = new ViatorApiDocumentationAmpSpecificationMerchantPartners.ProductServicesApi();
let acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
let opts = {
  'searchProductsCodesRequest': {"currencyCode":"USD","productCodes":["123457890"]} // SearchProductsCodesRequest | 
};
apiInstance.searchProductsCodes(acceptLanguage, opts, (error, data, response) => {
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
 **searchProductsCodesRequest** | [**SearchProductsCodesRequest**](SearchProductsCodesRequest.md)|  | [optional] 

### Return type

[**SearchProductsCodes200Response**](SearchProductsCodes200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

