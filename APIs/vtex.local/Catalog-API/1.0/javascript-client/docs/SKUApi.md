# CatalogApi.SKUApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtStockkeepingunitGet**](SKUApi.md#apiCatalogPvtStockkeepingunitGet) | **GET** /api/catalog/pvt/stockkeepingunit | Get SKU by RefId
[**apiCatalogPvtStockkeepingunitPost**](SKUApi.md#apiCatalogPvtStockkeepingunitPost) | **POST** /api/catalog/pvt/stockkeepingunit | Create SKU
[**apiCatalogPvtStockkeepingunitSkuIdPut**](SKUApi.md#apiCatalogPvtStockkeepingunitSkuIdPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId} | Update SKU
[**listallSKUIDs**](SKUApi.md#listallSKUIDs) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitids | List all SKU IDs
[**sku**](SKUApi.md#sku) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId} | Get SKU
[**skuContext**](SKUApi.md#skuContext) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitbyid/{skuId} | Get SKU and context
[**skuIdbyRefId**](SKUApi.md#skuIdbyRefId) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitidbyrefid/{refId} | Get SKU ID by Reference ID
[**skuIdlistbyRefIdlist**](SKUApi.md#skuIdlistbyRefIdlist) | **POST** /api/catalog_system/pub/sku/stockkeepingunitidsbyrefids | Retrieve SKU ID list by Reference ID list
[**skubyAlternateId**](SKUApi.md#skubyAlternateId) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitbyalternateId/{alternateId} | Get SKU by Alternate ID
[**skulistbyProductId**](SKUApi.md#skulistbyProductId) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitByProductId/{productId} | Get SKU list by Product ID



## apiCatalogPvtStockkeepingunitGet

> ApiCatalogPvtStockkeepingunitGet200Response apiCatalogPvtStockkeepingunitGet(contentType, accept, refId)

Get SKU by RefId

Retrieves information about a specific SKU by its &#x60;RefId&#x60;.     ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;Name\&quot;: \&quot;Royal Canin Feline Urinary 500g\&quot;,      \&quot;RefId\&quot;: \&quot;0001\&quot;,      \&quot;PackagedHeight\&quot;: 6.0000,      \&quot;PackagedLength\&quot;: 24.0000,      \&quot;PackagedWidth\&quot;: 14.0000,      \&quot;PackagedWeightKg\&quot;: 550.0000,      \&quot;Height\&quot;: null,      \&quot;Length\&quot;: null,      \&quot;Width\&quot;: null,      \&quot;WeightKg\&quot;: null,      \&quot;CubicWeight\&quot;: 1.0000,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2020-03-12T15:42:00\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 1.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: null  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let refId = "1"; // String | SKU Reference ID.
apiInstance.apiCatalogPvtStockkeepingunitGet(contentType, accept, refId, (error, data, response) => {
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
 **refId** | **String**| SKU Reference ID. | 

### Return type

[**ApiCatalogPvtStockkeepingunitGet200Response**](ApiCatalogPvtStockkeepingunitGet200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtStockkeepingunitPost

> ApiCatalogPvtStockkeepingunitPost200Response apiCatalogPvtStockkeepingunitPost(contentType, accept, opts)

Create SKU

    Creates a new SKU.    If there is a need to create a new SKU with a specific custom ID, specify the &#x60;Id&#x60; (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ### Request body example (custom ID)    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;     ### Request body example (automatically generated ID)    &#x60;&#x60;&#x60;json  {     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;     ### Response body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;:1,     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;Ean\&quot;: \&quot;8949461894984\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'apiCatalogPvtStockkeepingunitPostRequest': new CatalogApi.ApiCatalogPvtStockkeepingunitPostRequest() // ApiCatalogPvtStockkeepingunitPostRequest | 
};
apiInstance.apiCatalogPvtStockkeepingunitPost(contentType, accept, opts, (error, data, response) => {
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
 **apiCatalogPvtStockkeepingunitPostRequest** | [**ApiCatalogPvtStockkeepingunitPostRequest**](ApiCatalogPvtStockkeepingunitPostRequest.md)|  | [optional] 

### Return type

[**ApiCatalogPvtStockkeepingunitPost200Response**](ApiCatalogPvtStockkeepingunitPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtStockkeepingunitSkuIdPut

> ApiCatalogPvtStockkeepingunitSkuIdPut200Response apiCatalogPvtStockkeepingunitSkuIdPut(contentType, accept, skuId, opts)

Update SKU

Updates an existing SKU.     ### Request body example    &#x60;&#x60;&#x60;json  {     \&quot;Id\&quot;: 310118448,     \&quot;ProductId\&quot;: 310117069,     \&quot;IsActive\&quot;: true,     \&quot;ActivateIfPossible\&quot;: true,     \&quot;Name\&quot;: \&quot;sku test\&quot;,     \&quot;RefId\&quot;: \&quot;125478\&quot;,     \&quot;PackagedHeight\&quot;: 10,     \&quot;PackagedLength\&quot;: 10,     \&quot;PackagedWidth\&quot;: 10,     \&quot;PackagedWeightKg\&quot;: 10,     \&quot;Height\&quot;: null,     \&quot;Length\&quot;: null,     \&quot;Width\&quot;: null,     \&quot;WeightKg\&quot;: null,     \&quot;CubicWeight\&quot;: 0.1667,     \&quot;IsKit\&quot;: false,     \&quot;CreationDate\&quot;: null,     \&quot;RewardValue\&quot;: null,     \&quot;EstimatedDateArrival\&quot;: null,     \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,     \&quot;CommercialConditionId\&quot;: 1,     \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,     \&quot;UnitMultiplier\&quot;: 2.0000,     \&quot;ModalType\&quot;: null,     \&quot;KitItensSellApart\&quot;: false,     \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 310118449,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;ActivateIfPossible\&quot;: true,      \&quot;Name\&quot;: \&quot;sku test\&quot;,      \&quot;RefId\&quot;: \&quot;1254789\&quot;,      \&quot;PackagedHeight\&quot;: 10.0,      \&quot;PackagedLength\&quot;: 10.0,      \&quot;PackagedWidth\&quot;: 10.0,      \&quot;PackagedWeightKg\&quot;: 10.0,      \&quot;Height\&quot;: null,      \&quot;Length\&quot;: null,      \&quot;Width\&quot;: null,      \&quot;WeightKg\&quot;: null,      \&quot;CubicWeight\&quot;: 0.1667,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2020-04-22T12:12:47.5219561\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: [ \&quot;https://www.youtube.com/\&quot; ]  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
let opts = {
  'apiCatalogPvtStockkeepingunitSkuIdPutRequest': new CatalogApi.ApiCatalogPvtStockkeepingunitSkuIdPutRequest() // ApiCatalogPvtStockkeepingunitSkuIdPutRequest | 
};
apiInstance.apiCatalogPvtStockkeepingunitSkuIdPut(contentType, accept, skuId, opts, (error, data, response) => {
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
 **apiCatalogPvtStockkeepingunitSkuIdPutRequest** | [**ApiCatalogPvtStockkeepingunitSkuIdPutRequest**](ApiCatalogPvtStockkeepingunitSkuIdPutRequest.md)|  | [optional] 

### Return type

[**ApiCatalogPvtStockkeepingunitSkuIdPut200Response**](ApiCatalogPvtStockkeepingunitSkuIdPut200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listallSKUIDs

> [Number] listallSKUIDs(page, pagesize, contentType, accept)

List all SKU IDs

Retrieves the IDs of all SKUs in your store. Presents the results with page size and pagination.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    ### Response body example    &#x60;&#x60;&#x60;json  [    1,    2,    3,    4,    5,    6,    7,    8,    9,    10  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUApi();
let page = 1; // Number | Number of the page from where you need to retrieve SKU IDs.
let pagesize = 25; // Number | Size of the page from where you need retrieve SKU IDs. The maximum value is `1000`.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.listallSKUIDs(page, pagesize, contentType, accept, (error, data, response) => {
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
 **page** | **Number**| Number of the page from where you need to retrieve SKU IDs. | 
 **pagesize** | **Number**| Size of the page from where you need retrieve SKU IDs. The maximum value is &#x60;1000&#x60;. | 
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

**[Number]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sku

> Sku200Response sku(contentType, accept, skuId)

Get SKU

Retrieves a specific SKU by its ID.    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;ProductId\&quot;: 1,      \&quot;IsActive\&quot;: true,      \&quot;ActivateIfPossible\&quot;: true,      \&quot;Name\&quot;: \&quot;Ração Royal Canin Feline Urinary 500g\&quot;,      \&quot;RefId\&quot;: \&quot;0001\&quot;,      \&quot;PackagedHeight\&quot;: 6.5000,      \&quot;PackagedLength\&quot;: 24.0000,      \&quot;PackagedWidth\&quot;: 14.0000,      \&quot;PackagedWeightKg\&quot;: 550.0000,      \&quot;Height\&quot;: 2.2000,      \&quot;Length\&quot;: 4.4000,      \&quot;Width\&quot;: 3.3000,      \&quot;WeightKg\&quot;: 1.1000,      \&quot;CubicWeight\&quot;: 0.4550,      \&quot;IsKit\&quot;: false,      \&quot;CreationDate\&quot;: \&quot;2021-06-08T15:25:00\&quot;,      \&quot;RewardValue\&quot;: null,      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;CommercialConditionId\&quot;: 1,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 300.0000,      \&quot;ModalType\&quot;: null,      \&quot;KitItensSellApart\&quot;: false,      \&quot;Videos\&quot;: [          \&quot;www.google.com\&quot;      ]  }  &#x60;&#x60;&#x60;    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.

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

let apiInstance = new CatalogApi.SKUApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU unique identifier number.
apiInstance.sku(contentType, accept, skuId, (error, data, response) => {
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
 **skuId** | **Number**| SKU unique identifier number. | 

### Return type

[**Sku200Response**](Sku200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skuContext

> GetSKUandContext skuContext(contentType, accept, skuId, opts)

Get SKU and context

Retrieves context of an SKU.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2001773,      \&quot;ProductId\&quot;: 2001426,      \&quot;NameComplete\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ComplementName\&quot;: \&quot;\&quot;,      \&quot;ProductName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductDescription\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;SkuName\&quot;: \&quot;Tabela de Basquete\&quot;,      \&quot;ProductRefId\&quot;: \&quot;0987\&quot;,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952-55-55/7508800GG.jpg\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/tabela-de-basquete/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000018\&quot;,      \&quot;BrandName\&quot;: \&quot;MARCA ARGOLO TESTE\&quot;,      \&quot;IsBrandActive\&quot;: true,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 81.6833,          \&quot;height\&quot;: 65,          \&quot;length\&quot;: 58,          \&quot;weight\&quot;: 10000,          \&quot;width\&quot;: 130      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 274.1375,          \&quot;realHeight\&quot;: 241,          \&quot;realLength\&quot;: 65,          \&quot;realWeight\&quot;: 9800,          \&quot;realWidth\&quot;: 105      },      \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;CategoriesFullPath\&quot;: [          \&quot;/1/10/\&quot;,          \&quot;/1/\&quot;,          \&quot;/20/\&quot;      ],      \&quot;Attachments\&quot;: [          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Mensagem\&quot;,              \&quot;Keys\&quot;: [                  \&quot;nome;20\&quot;,                  \&quot;foto;40\&quot;              ],              \&quot;Fields\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;nome\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;20\&quot;,                      \&quot;DomainValues\&quot;: \&quot;Adalberto,Pedro,João\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;foto\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;40\&quot;,                      \&quot;DomainValues\&quot;: null                  }              ],              \&quot;IsActive\&quot;: true,              \&quot;IsRequired\&quot;: false          }      ],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 2001773,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;2001773\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0,              \&quot;ProductCommissionPercentage\&quot;: 0          }      ],      \&quot;SalesChannels\&quot;: [          1,          2,          3,          10      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168952/7508800GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168952          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168953/7508800_1GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168953          },          {              \&quot;ImageUrl\&quot;: \&quot;http://ambienteqa.vteximg.com.br/arquivos/ids/168954/7508800_2GG.jpg\&quot;,              \&quot;ImageName\&quot;: \&quot;\&quot;,              \&quot;FileId\&quot;: 168954          }      ],      \&quot;Videos\&quot;: [          \&quot;www.google.com\&quot;      ],      \&quot;SkuSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 102,              \&quot;FieldName\&quot;: \&quot;Cor\&quot;,              \&quot;FieldValueIds\&quot;: [                  266              ],              \&quot;FieldValues\&quot;: [                  \&quot;Padrão\&quot;              ],              \&quot;IsFilter\&quot;: false,              \&quot;FieldGroupId\&quot;: 11,              \&quot;FieldGroupName\&quot;: \&quot;Especificações\&quot;          }      ],      \&quot;ProductSpecifications\&quot;: [          {              \&quot;FieldId\&quot;: 7,              \&quot;FieldName\&quot;: \&quot;Faixa Etária\&quot;,              \&quot;FieldValueIds\&quot;: [                  58,                  56,                  55,                  52              ],              \&quot;FieldValues\&quot;: [                  \&quot;5 a 6 anos\&quot;,                  \&quot;7 a 8 anos\&quot;,                  \&quot;9 a 10 anos\&quot;,                  \&quot;Acima de 10 anos\&quot;              ],              \&quot;IsFilter\&quot;: true,              \&quot;FieldGroupId\&quot;: 17,              \&quot;FieldGroupName\&quot;: \&quot;NewGroupName 2\&quot;          },          {              \&quot;FieldId\&quot;: 23,              \&quot;FieldName\&quot;: \&quot;Fabricante\&quot;,              \&quot;FieldValueIds\&quot;: [],              \&quot;FieldValues\&quot;: [                  \&quot;Xalingo\&quot;              ],              \&quot;IsFilter\&quot;: false,              \&quot;FieldGroupId\&quot;: 17,              \&quot;FieldGroupName\&quot;: \&quot;NewGroupName 2\&quot;          }      ],      \&quot;ProductClustersIds\&quot;: \&quot;176,187,192,194,211,217,235,242\&quot;,      \&quot;PositionsInClusters\&quot;: {          \&quot;151\&quot;: 3,          \&quot;152\&quot;: 0,          \&quot;158\&quot;: 1      },      \&quot;ProductClusterNames\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;152\&quot;: \&quot;George\&quot;,          \&quot;158\&quot;: \&quot;Coleção halloween\&quot;      },      \&quot;ProductClusterHighlights\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;152\&quot;: \&quot;George\&quot;      },      \&quot;ProductCategoryIds\&quot;: \&quot;/59/\&quot;,      \&quot;IsDirectCategoryActive\&quot;: false,      \&quot;ProductGlobalCategoryId\&quot;: null,      \&quot;ProductCategories\&quot;: {          \&quot;59\&quot;: \&quot;Brinquedos\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 100.0,      \&quot;AlternateIds\&quot;: {          \&quot;Ean\&quot;: \&quot;8781\&quot;,          \&quot;RefId\&quot;: \&quot;878181\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;8781\&quot;,          \&quot;878181\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 2.0000,      \&quot;InformationSource\&quot;: \&quot;Indexer\&quot;,      \&quot;ModalType\&quot;: \&quot;\&quot;,      \&quot;KeyWords\&quot;: \&quot;basquete, tabela\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2020-01-06T00:00:00\&quot;,      \&quot;ProductIsVisible\&quot;: true,      \&quot;ShowIfNotAvailable\&quot;: true,      \&quot;IsProductActive\&quot;: true,      \&quot;ProductFinalScore\&quot;: 0  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 2001773; // Number | SKU's unique identifier number.
let opts = {
  'sc': 1 // Number | Trade Policy's unique identifier number.
};
apiInstance.skuContext(contentType, accept, skuId, opts, (error, data, response) => {
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
 **skuId** | **Number**| SKU&#39;s unique identifier number. | 
 **sc** | **Number**| Trade Policy&#39;s unique identifier number. | [optional] 

### Return type

[**GetSKUandContext**](GetSKUandContext.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skuIdbyRefId

> String skuIdbyRefId(contentType, accept, refId)

Get SKU ID by Reference ID

Retrieves an SKU ID by the SKU&#39;s Reference ID.     ### Response body example    &#x60;&#x60;&#x60;json  \&quot;310118450\&quot;  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let refId = "0001"; // String | SKU Reference ID.
apiInstance.skuIdbyRefId(contentType, accept, refId, (error, data, response) => {
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
 **refId** | **String**| SKU Reference ID. | 

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skuIdlistbyRefIdlist

> {String: String} skuIdlistbyRefIdlist(contentType, accept, opts)

Retrieve SKU ID list by Reference ID list

Receives a list of Reference IDs and returns a list with the corresponding SKU IDs.    &gt;⚠️ The list of Reference IDs in the request body cannot have repeated Reference IDs, or the API will return an error 500.     ## Request body example    &#x60;&#x60;&#x60;json  [      \&quot;123\&quot;,      \&quot;D25133K-B2\&quot;,      \&quot;14-556\&quot;,      \&quot;DCF880L2-BR\&quot;  ]  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;123\&quot;: \&quot;435\&quot;,      \&quot;D25133K-B2\&quot;: \&quot;4351\&quot;,      \&quot;14-556\&quot;: \&quot;3155\&quot;,      \&quot;DCF880L2-BR\&quot;: \&quot;4500\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'requestBody': ["799"] // [String] | 
};
apiInstance.skuIdlistbyRefIdlist(contentType, accept, opts, (error, data, response) => {
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
 **requestBody** | [**[String]**](String.md)|  | [optional] 

### Return type

**{String: String}**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## skubyAlternateId

> GetSKUAltID skubyAlternateId(contentType, accept, alternateId)

Get SKU by Alternate ID

Retrieves an SKU by its Alternate ID.    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 310118450,      \&quot;ProductId\&quot;: 2,      \&quot;NameComplete\&quot;: \&quot;Caixa de Areia Azul Petmate sku test\&quot;,      \&quot;ComplementName\&quot;: \&quot;\&quot;,      \&quot;ProductName\&quot;: \&quot;Caixa de Areia Azul Petmate\&quot;,      \&quot;ProductDescription\&quot;: \&quot;\&quot;,      \&quot;ProductRefId\&quot;: \&quot;\&quot;,      \&quot;TaxCode\&quot;: \&quot;\&quot;,      \&quot;SkuName\&quot;: \&quot;sku test\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;IsTransported\&quot;: true,      \&quot;IsInventoried\&quot;: true,      \&quot;IsGiftCardRecharge\&quot;: false,      \&quot;ImageUrl\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155451-55-55/caixa-areia-azul-petmate.jpg?v&#x3D;637139451191670000\&quot;,      \&quot;DetailUrl\&quot;: \&quot;/caixa-de-areia-azul-petmate/p\&quot;,      \&quot;CSCIdentification\&quot;: null,      \&quot;BrandId\&quot;: \&quot;2000005\&quot;,      \&quot;BrandName\&quot;: \&quot;Petmate\&quot;,      \&quot;IsBrandActive\&quot;: true,      \&quot;Dimension\&quot;: {          \&quot;cubicweight\&quot;: 0.2083,          \&quot;height\&quot;: 10.0000,          \&quot;length\&quot;: 10.0000,          \&quot;weight\&quot;: 10.0000,          \&quot;width\&quot;: 10.0000      },      \&quot;RealDimension\&quot;: {          \&quot;realCubicWeight\&quot;: 0.000,          \&quot;realHeight\&quot;: 0.0,          \&quot;realLength\&quot;: 0.0,          \&quot;realWeight\&quot;: 0.0,          \&quot;realWidth\&quot;: 0.0      },      \&quot;ManufacturerCode\&quot;: \&quot;123\&quot;,      \&quot;IsKit\&quot;: false,      \&quot;KitItems\&quot;: [],      \&quot;Services\&quot;: [],      \&quot;Categories\&quot;: [],      \&quot;CategoriesFullPath\&quot;: [          \&quot;/3/15/\&quot;,          \&quot;/3/\&quot;,          \&quot;/1/\&quot;      ],      \&quot;Attachments\&quot;: [],      \&quot;Collections\&quot;: [],      \&quot;SkuSellers\&quot;: [          {              \&quot;SellerId\&quot;: \&quot;1\&quot;,              \&quot;StockKeepingUnitId\&quot;: 310118450,              \&quot;SellerStockKeepingUnitId\&quot;: \&quot;310118450\&quot;,              \&quot;IsActive\&quot;: true,              \&quot;FreightCommissionPercentage\&quot;: 0.0,              \&quot;ProductCommissionPercentage\&quot;: 0.0          }      ],      \&quot;SalesChannels\&quot;: [          1,          3      ],      \&quot;Images\&quot;: [          {              \&quot;ImageUrl\&quot;: \&quot;https://lojadobreno.vteximg.com.br/arquivos/ids/155451/caixa-areia-azul-petmate.jpg?v&#x3D;637139451191670000\&quot;,              \&quot;ImageName\&quot;: null,              \&quot;FileId\&quot;: 155451          }      ],      \&quot;Videos\&quot;: [],      \&quot;SkuSpecifications\&quot;: [],      \&quot;ProductSpecifications\&quot;: [],      \&quot;ProductClustersIds\&quot;: \&quot;151,158\&quot;,      \&quot;PositionsInClusters\&quot;: {          \&quot;151\&quot;: 1,          \&quot;158\&quot;: 2      },      \&quot;ProductClusterNames\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;,          \&quot;158\&quot;: \&quot;Coleção halloween\&quot;      },      \&quot;ProductClusterHighlights\&quot;: {          \&quot;151\&quot;: \&quot;asdfghj\&quot;      },      \&quot;ProductCategoryIds\&quot;: \&quot;/3/15/\&quot;,      \&quot;IsDirectCategoryActive\&quot;: true,      \&quot;ProductGlobalCategoryId\&quot;: 5000,      \&quot;ProductCategories\&quot;: {          \&quot;15\&quot;: \&quot;Caixa de Areia\&quot;,          \&quot;3\&quot;: \&quot;Higiene\&quot;,          \&quot;1\&quot;: \&quot;Alimentação\&quot;      },      \&quot;CommercialConditionId\&quot;: 1,      \&quot;RewardValue\&quot;: 0.0,      \&quot;AlternateIds\&quot;: {          \&quot;RefId\&quot;: \&quot;1\&quot;      },      \&quot;AlternateIdValues\&quot;: [          \&quot;1\&quot;      ],      \&quot;EstimatedDateArrival\&quot;: null,      \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,      \&quot;UnitMultiplier\&quot;: 1.0000,      \&quot;InformationSource\&quot;: null,      \&quot;ModalType\&quot;: null,      \&quot;KeyWords\&quot;: \&quot;\&quot;,      \&quot;ReleaseDate\&quot;: \&quot;2020-01-06T00:00:00Z\&quot;,      \&quot;ProductIsVisible\&quot;: true,      \&quot;ShowIfNotAvailable\&quot;: true,      \&quot;IsProductActive\&quot;: true,      \&quot;ProductFinalScore\&quot;: 0  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let alternateId = 10; // Number | Product EAN or RefId.
apiInstance.skubyAlternateId(contentType, accept, alternateId, (error, data, response) => {
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
 **alternateId** | **Number**| Product EAN or RefId. | 

### Return type

[**GetSKUAltID**](GetSKUAltID.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skulistbyProductId

> [SkulistbyProductId] skulistbyProductId(contentType, accept, productId)

Get SKU list by Product ID

Retrieves a list with the SKUs related to a product by the product&#39;s ID.    ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;IsPersisted\&quot;: true,          \&quot;IsRemoved\&quot;: false,          \&quot;Id\&quot;: 2000035,          \&quot;ProductId\&quot;: 2000024,          \&quot;IsActive\&quot;: true,          \&quot;Name\&quot;: \&quot;33 - Preto\&quot;,          \&quot;Height\&quot;: 8,          \&quot;RealHeight\&quot;: null,          \&quot;Width\&quot;: 15,          \&quot;RealWidth\&quot;: null,          \&quot;Length\&quot;: 8,          \&quot;RealLength\&quot;: null,          \&quot;WeightKg\&quot;: 340,          \&quot;RealWeightKg\&quot;: null,          \&quot;ModalId\&quot;: 1,          \&quot;RefId\&quot;: \&quot;\&quot;,          \&quot;CubicWeight\&quot;: 0.2,          \&quot;IsKit\&quot;: false,          \&quot;IsDynamicKit\&quot;: null,          \&quot;InternalNote\&quot;: null,          \&quot;DateUpdated\&quot;: \&quot;2015-11-06T19:10:00\&quot;,          \&quot;RewardValue\&quot;: 0.01,          \&quot;CommercialConditionId\&quot;: 1,          \&quot;EstimatedDateArrival\&quot;: \&quot;\&quot;,          \&quot;FlagKitItensSellApart\&quot;: false,          \&quot;ManufacturerCode\&quot;: \&quot;\&quot;,          \&quot;ReferenceStockKeepingUnitId\&quot;: null,          \&quot;Position\&quot;: 0,          \&quot;EditionSkuId\&quot;: null,          \&quot;ApprovedAdminId\&quot;: 123,          \&quot;EditionAdminId\&quot;: 123,          \&quot;ActivateIfPossible\&quot;: true,          \&quot;SupplierCode\&quot;: null,          \&quot;MeasurementUnit\&quot;: \&quot;un\&quot;,          \&quot;UnitMultiplier\&quot;: 2.0000,          \&quot;IsInventoried\&quot;: null,          \&quot;IsTransported\&quot;: null,          \&quot;IsGiftCardRecharge\&quot;: null,          \&quot;ModalType\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
apiInstance.skulistbyProductId(contentType, accept, productId, (error, data, response) => {
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
 **productId** | **Number**| Product’s unique numerical identifier. | 

### Return type

[**[SkulistbyProductId]**](SkulistbyProductId.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

