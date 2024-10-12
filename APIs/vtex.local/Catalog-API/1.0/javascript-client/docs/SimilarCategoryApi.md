# CatalogApi.SimilarCategoryApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete**](SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete) | **DELETE** /api/catalog/pvt/product/{productId}/similarcategory/{categoryId} | Delete Similar Category
[**apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost**](SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost) | **POST** /api/catalog/pvt/product/{productId}/similarcategory/{categoryId} | Add Similar Category
[**apiCatalogPvtProductProductIdSimilarcategoryGet**](SimilarCategoryApi.md#apiCatalogPvtProductProductIdSimilarcategoryGet) | **GET** /api/catalog/pvt/product/{productId}/similarcategory/ | Get Similar Categories



## apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete

> apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete(contentType, accept, productId, categoryId)

Delete Similar Category

Deletes a Similar Category from a Product.

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApi.SimilarCategoryApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
let categoryId = 1; // Number | Similar Category’s unique numerical identifier.
apiInstance.apiCatalogPvtProductProductIdSimilarcategoryCategoryIdDelete(contentType, accept, productId, categoryId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **Number**| Product’s unique numerical identifier. | 
 **categoryId** | **Number**| Similar Category’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost

> ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost(contentType, accept, productId, categoryId)

Add Similar Category

Adds a Similar Category to a Product.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;ProductId\&quot;: 1,      \&quot;StoreId\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApi.SimilarCategoryApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
let categoryId = 1; // Number | Similar Category’s unique numerical identifier.
apiInstance.apiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost(contentType, accept, productId, categoryId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **Number**| Product’s unique numerical identifier. | 
 **categoryId** | **Number**| Similar Category’s unique numerical identifier. | 

### Return type

[**ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response**](ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtProductProductIdSimilarcategoryGet

> [ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner] apiCatalogPvtProductProductIdSimilarcategoryGet(contentType, accept, productId)

Get Similar Categories

Retrieves Similar Categories from a Product.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;ProductId\&quot;: 1,          \&quot;CategoryId\&quot;: 1      },      {          \&quot;ProductId\&quot;: 1,          \&quot;CategoryId\&quot;: 20      }  ]  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApi.SimilarCategoryApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
apiInstance.apiCatalogPvtProductProductIdSimilarcategoryGet(contentType, accept, productId, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **productId** | **Number**| Product’s unique numerical identifier. | 

### Return type

[**[ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner]**](ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

