# CatalogApi.TradePolicyApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtProductProductIdSalespolicyGet**](TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyGet) | **GET** /api/catalog/pvt/product/{productId}/salespolicy | Get Trade Policies by Product ID
[**apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete**](TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete) | **DELETE** /api/catalog/pvt/product/{productId}/salespolicy/{tradepolicyId} | Remove Product from Trade Policy
[**apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost**](TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost) | **POST** /api/catalog/pvt/product/{productId}/salespolicy/{tradepolicyId} | Associate Product with Trade Policy
[**apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet**](TradePolicyApi.md#apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitidsbysaleschannel | List all SKUs of a Trade Policy



## apiCatalogPvtProductProductIdSalespolicyGet

> [ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner] apiCatalogPvtProductProductIdSalespolicyGet(contentType, accept, productId)

Get Trade Policies by Product ID

Retrieves a list of Trade Policies associated to a Product based on the Product&#39;s ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 1      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 2      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 3      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 4      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.TradePolicyApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
apiInstance.apiCatalogPvtProductProductIdSalespolicyGet(contentType, accept, productId, (error, data, response) => {
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

[**[ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner]**](ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete

> apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete(contentType, accept, productId, tradepolicyId)

Remove Product from Trade Policy

Disassociates a Trade Policy of a Product.

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

let apiInstance = new CatalogApi.TradePolicyApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
let tradepolicyId = 1; // Number | Trade Policy’s unique numerical identifier.
apiInstance.apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete(contentType, accept, productId, tradepolicyId, (error, data, response) => {
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
 **tradepolicyId** | **Number**| Trade Policy’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost

> apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost(contentType, accept, productId, tradepolicyId)

Associate Product with Trade Policy

Associates an existing Trade Policy with a Product.

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

let apiInstance = new CatalogApi.TradePolicyApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
let tradepolicyId = 1; // Number | Trade Policy’s unique numerical identifier.
apiInstance.apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost(contentType, accept, productId, tradepolicyId, (error, data, response) => {
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
 **tradepolicyId** | **Number**| Trade Policy’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet

> [Number] apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet(contentType, accept, sc, opts)

List all SKUs of a Trade Policy

Retrieves a list of SKU IDs of a Trade Policy.   ## Response body example    &#x60;&#x60;&#x60;json  [      405380,      405381,      405382,      405383,      405384,      405385,      405386,      405387,      405388,      405389,      405390,      405391,      405392,      405393,      405394,      405395,      405396,      405397,      405398,      405399,      405400,      405556  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.TradePolicyApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let sc = 1; // Number | Trade Policy’s unique numerical identifier.
let opts = {
  'page': 1, // Number | Page number.
  'pageSize': 1, // Number | Number of items in the page.
  'onlyAssigned': true // Boolean | If set as `false`, it allows the user to decide if the SKUs that are not assigned to a specific trade policy should be also returned.
};
apiInstance.apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet(contentType, accept, sc, opts, (error, data, response) => {
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
 **sc** | **Number**| Trade Policy’s unique numerical identifier. | 
 **page** | **Number**| Page number. | [optional] 
 **pageSize** | **Number**| Number of items in the page. | [optional] 
 **onlyAssigned** | **Boolean**| If set as &#x60;false&#x60;, it allows the user to decide if the SKUs that are not assigned to a specific trade policy should be also returned. | [optional] 

### Return type

**[Number]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

