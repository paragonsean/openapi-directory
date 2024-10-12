# CatalogApi.SKUServiceTypeApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtSkuservicetypePost**](SKUServiceTypeApi.md#apiCatalogPvtSkuservicetypePost) | **POST** /api/catalog/pvt/skuservicetype | Create SKU Service Type
[**apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete**](SKUServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete) | **DELETE** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Delete SKU Service Type
[**apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet**](SKUServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet) | **GET** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Get SKU Service Type
[**apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut**](SKUServiceTypeApi.md#apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut) | **PUT** /api/catalog/pvt/skuservicetype/{skuServiceTypeId} | Update SKU Service Type



## apiCatalogPvtSkuservicetypePost

> SKUServiceTypeResponse apiCatalogPvtSkuservicetypePost(contentType, accept, opts)

Create SKU Service Type

Creates a new SKU Service Type.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Test API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;Name\&quot;: \&quot;Teste API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUServiceTypeApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'sKUServiceTypeRequest': new CatalogApi.SKUServiceTypeRequest() // SKUServiceTypeRequest | 
};
apiInstance.apiCatalogPvtSkuservicetypePost(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **sKUServiceTypeRequest** | [**SKUServiceTypeRequest**](SKUServiceTypeRequest.md)|  | [optional] 

### Return type

[**SKUServiceTypeResponse**](SKUServiceTypeResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete

> apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete(contentType, accept, skuServiceTypeId)

Delete SKU Service Type

Deletes an existing SKU Service Type.

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

let apiInstance = new CatalogApi.SKUServiceTypeApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuServiceTypeId = 1; // Number | SKU Service Type unique identifier.
apiInstance.apiCatalogPvtSkuservicetypeSkuServiceTypeIdDelete(contentType, accept, skuServiceTypeId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **skuServiceTypeId** | **Number**| SKU Service Type unique identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet

> SKUServiceTypeResponse apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet(contentType, accept, skuServiceTypeId)

Get SKU Service Type

Retrieves information about an existing SKU Service Type.   ## Response body example:    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test API SKU Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUServiceTypeApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuServiceTypeId = 1; // Number | SKU Service Type unique identifier.
apiInstance.apiCatalogPvtSkuservicetypeSkuServiceTypeIdGet(contentType, accept, skuServiceTypeId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **skuServiceTypeId** | **Number**| SKU Service Type unique identifier. | 

### Return type

[**SKUServiceTypeResponse**](SKUServiceTypeResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut

> SKUServiceTypeResponse apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut(contentType, accept, skuServiceTypeId, opts)

Update SKU Service Type

Updates an existing SKU Service Type.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Test API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;Name\&quot;: \&quot;Teste API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUServiceTypeApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuServiceTypeId = 1; // Number | SKU Service Type unique identifier.
let opts = {
  'sKUServiceTypeRequest': new CatalogApi.SKUServiceTypeRequest() // SKUServiceTypeRequest | 
};
apiInstance.apiCatalogPvtSkuservicetypeSkuServiceTypeIdPut(contentType, accept, skuServiceTypeId, opts, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **skuServiceTypeId** | **Number**| SKU Service Type unique identifier. | 
 **sKUServiceTypeRequest** | [**SKUServiceTypeRequest**](SKUServiceTypeRequest.md)|  | [optional] 

### Return type

[**SKUServiceTypeResponse**](SKUServiceTypeResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

