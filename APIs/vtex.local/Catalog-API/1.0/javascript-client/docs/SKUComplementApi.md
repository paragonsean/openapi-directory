# CatalogApi.SKUComplementApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSKUComplement**](SKUComplementApi.md#createSKUComplement) | **POST** /api/catalog/pvt/skucomplement | Create SKU Complement
[**deleteSKUComplementbySKUComplementID**](SKUComplementApi.md#deleteSKUComplementbySKUComplementID) | **DELETE** /api/catalog/pvt/skucomplement/{skuComplementId} | Delete SKU Complement by SKU Complement ID
[**getSKUComplementbySKUComplementID**](SKUComplementApi.md#getSKUComplementbySKUComplementID) | **GET** /api/catalog/pvt/skucomplement/{skuComplementId} | Get SKU Complement by SKU Complement ID
[**getSKUComplementbySKUID**](SKUComplementApi.md#getSKUComplementbySKUID) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/complement | Get SKU Complement by SKU ID
[**getSKUComplementsbyComplementTypeID**](SKUComplementApi.md#getSKUComplementsbyComplementTypeID) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/complement/{complementTypeId} | Get SKU Complements by Complement Type ID
[**getSKUcomplementsbytype**](SKUComplementApi.md#getSKUcomplementsbytype) | **GET** /api/catalog_system/pvt/sku/complements/{parentSkuId}/{type} | Get SKU complements by type



## createSKUComplement

> [SkuComplementInner] createSKUComplement(contentType, accept, opts)

Create SKU Complement

Creates a new SKU Complement on a Parent SKU.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUComplementApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'requestBody2': new CatalogApi.RequestBody2() // RequestBody2 | 
};
apiInstance.createSKUComplement(contentType, accept, opts, (error, data, response) => {
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
 **requestBody2** | [**RequestBody2**](RequestBody2.md)|  | [optional] 

### Return type

[**[SkuComplementInner]**](SkuComplementInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSKUComplementbySKUComplementID

> deleteSKUComplementbySKUComplementID(contentType, accept, skuComplementId)

Delete SKU Complement by SKU Complement ID

Deletes a previously existing SKU Complement by SKU Complement ID.

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

let apiInstance = new CatalogApi.SKUComplementApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuComplementId = 1; // Number | SKU Complement’s unique numerical identifier.
apiInstance.deleteSKUComplementbySKUComplementID(contentType, accept, skuComplementId, (error, data, response) => {
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
 **skuComplementId** | **Number**| SKU Complement’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSKUComplementbySKUComplementID

> [SkuComplementInner] getSKUComplementbySKUComplementID(contentType, accept, skuComplementId)

Get SKU Complement by SKU Complement ID

Retrieves an existing SKU Complement by its SKU Complement ID.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUComplementApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuComplementId = 1; // Number | SKU Complement’s unique numerical identifier.
apiInstance.getSKUComplementbySKUComplementID(contentType, accept, skuComplementId, (error, data, response) => {
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
 **skuComplementId** | **Number**| SKU Complement’s unique numerical identifier. | 

### Return type

[**[SkuComplementInner]**](SkuComplementInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSKUComplementbySKUID

> [SkuComplementInner] getSKUComplementbySKUID(contentType, accept, skuId)

Get SKU Complement by SKU ID

Retrieves an existing SKU Complement by its SKU ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUComplementApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
apiInstance.getSKUComplementbySKUID(contentType, accept, skuId, (error, data, response) => {
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

[**[SkuComplementInner]**](SkuComplementInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSKUComplementsbyComplementTypeID

> [SkuComplementInner] getSKUComplementsbyComplementTypeID(contentType, accept, skuId, complementTypeId)

Get SKU Complements by Complement Type ID

Retrieves all the existing SKU Complements with the same Complement Type ID of a specific SKU.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUComplementApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | ID of the SKU which will be inserted as a Complement in the Parent SKU.
let complementTypeId = 1; // Number | Complement Type ID. This represents the type of the complement. The possible values are: `1` for Accessory; `2` for Suggestion; `3` for Similar Product; `5` for Show Together.
apiInstance.getSKUComplementsbyComplementTypeID(contentType, accept, skuId, complementTypeId, (error, data, response) => {
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
 **skuId** | **Number**| ID of the SKU which will be inserted as a Complement in the Parent SKU. | 
 **complementTypeId** | **Number**| Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. | 

### Return type

[**[SkuComplementInner]**](SkuComplementInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSKUcomplementsbytype

> GetSKUcomplementsbytype200Response getSKUcomplementsbytype(contentType, accept, parentSkuId, type)

Get SKU complements by type

Retrieves all the existing SKU complements with the same complement type ID of a specific SKU.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementSkuIds\&quot;: [          7      ],      \&quot;Type\&quot;: \&quot;1\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUComplementApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let parentSkuId = 1; // Number | ID of the Parent SKU, where the Complement is inserted.
let type = 1; // Number | Complement Type ID. This represents the type of the complement. The possible values are: `1` for Accessory; `2` for Suggestion; `3` for Similar Product; `5` for Show Together.
apiInstance.getSKUcomplementsbytype(contentType, accept, parentSkuId, type, (error, data, response) => {
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
 **parentSkuId** | **Number**| ID of the Parent SKU, where the Complement is inserted. | 
 **type** | **Number**| Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. | 

### Return type

[**GetSKUcomplementsbytype200Response**](GetSKUcomplementsbytype200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

