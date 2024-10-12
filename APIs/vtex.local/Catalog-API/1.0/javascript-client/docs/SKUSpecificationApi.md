# CatalogApi.SKUSpecificationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete**](SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Delete all SKU Specifications
[**apiCatalogPvtStockkeepingunitSkuIdSpecificationGet**](SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Get SKU Specifications
[**apiCatalogPvtStockkeepingunitSkuIdSpecificationPost**](SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationPost) | **POST** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Associate SKU Specification
[**apiCatalogPvtStockkeepingunitSkuIdSpecificationPut**](SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/specification | Update SKU Specification
[**apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete**](SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/specification/{specificationId} | Delete SKU Specification
[**apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut**](SKUSpecificationApi.md#apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/specificationvalue | Associate SKU specification using specification name and group name



## apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete

> apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete(contentType, accept, skuId)

Delete all SKU Specifications

Deletes all SKU Specifications.

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

let apiInstance = new CatalogApi.SKUSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationDelete(contentType, accept, skuId, (error, data, response) => {
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
 **skuId** | **Number**| SKU’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtStockkeepingunitSkuIdSpecificationGet

> [SKUSpecificationResponse] apiCatalogPvtStockkeepingunitSkuIdSpecificationGet(contentType, accept, skuId)

Get SKU Specifications

Retrieves information about an SKU&#39;s Specifications.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 427,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 32,          \&quot;FieldValueId\&quot;: 131,          \&quot;Text\&quot;: \&quot;500g\&quot;      },      {          \&quot;Id\&quot;: 428,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 40,          \&quot;FieldValueId\&quot;: 133,          \&quot;Text\&quot;: \&quot;A\&quot;      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationGet(contentType, accept, skuId, (error, data, response) => {
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
 **skuId** | **Number**| SKU’s unique numerical identifier. | 

### Return type

[**[SKUSpecificationResponse]**](SKUSpecificationResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtStockkeepingunitSkuIdSpecificationPost

> SKUSpecificationResponse apiCatalogPvtStockkeepingunitSkuIdSpecificationPost(contentType, accept, skuId, opts)

Associate SKU Specification

Associates a previously created Specification to an SKU.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 730,      \&quot;SkuId\&quot;: 31,      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138,      \&quot;Text\&quot;: \&quot;Size\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1234568387; // Number | SKU’s unique numerical identifier.
let opts = {
  'apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest': new CatalogApi.ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest() // ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest | 
};
apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationPost(contentType, accept, skuId, opts, (error, data, response) => {
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
 **skuId** | **Number**| SKU’s unique numerical identifier. | 
 **apiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest** | [**ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest**](ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest.md)|  | [optional] 

### Return type

[**SKUSpecificationResponse**](SKUSpecificationResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtStockkeepingunitSkuIdSpecificationPut

> [SKUSpecificationResponse] apiCatalogPvtStockkeepingunitSkuIdSpecificationPut(contentType, accept, skuId, opts)

Update SKU Specification

Updates an existing Specification on an existing SKU. This endpoint only updates the &#x60;FieldValueId&#x60;.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 21; // Number | SKU’s unique numerical identifier.
let opts = {
  'requestBody': new CatalogApi.RequestBody() // RequestBody | 
};
apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationPut(contentType, accept, skuId, opts, (error, data, response) => {
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
 **skuId** | **Number**| SKU’s unique numerical identifier. | 
 **requestBody** | [**RequestBody**](RequestBody.md)|  | [optional] 

### Return type

[**[SKUSpecificationResponse]**](SKUSpecificationResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete

> apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete(contentType, accept, skuId, specificationId)

Delete SKU Specification

Deletes a specific SKU Specification.

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

let apiInstance = new CatalogApi.SKUSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
let specificationId = 1; // Number | Specification’s unique numerical identifier.
apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationSpecificationIdDelete(contentType, accept, skuId, specificationId, (error, data, response) => {
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
 **skuId** | **Number**| SKU’s unique numerical identifier. | 
 **specificationId** | **Number**| Specification’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut

> [ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner] apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut(contentType, accept, skuId, opts)

Associate SKU specification using specification name and group name

Associates a specification to an SKU using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Size\&quot;,      \&quot;GroupName\&quot;: \&quot;Sizes\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;M\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 419,          \&quot;SkuId\&quot;: 5,          \&quot;FieldId\&quot;: 22,          \&quot;FieldValueId\&quot;: 62,          \&quot;Text\&quot;: \&quot;M\&quot;      }  ]  &#x60;&#x60;&#x60;  

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

let apiInstance = new CatalogApi.SKUSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
let opts = {
  'apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest': new CatalogApi.ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest() // ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest | 
};
apiInstance.apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut(contentType, accept, skuId, opts, (error, data, response) => {
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
 **skuId** | **Number**| SKU’s unique numerical identifier. | 
 **apiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest** | [**ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest**](ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest.md)|  | [optional] 

### Return type

[**[ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner]**](ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

