# CatalogApi.SKUFileApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut**](SKUFileApi.md#apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut) | **PUT** /api/catalog/pvt/stockkeepingunit/copy/{skuIdfrom}/{skuIdto}/file/ | Copy Files from an SKU to another SKU
[**apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete**](SKUFileApi.md#apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/disassociate/{skuId}/file/{skuFileId} | Disassociate SKU File
[**apiCatalogPvtStockkeepingunitSkuIdFileDelete**](SKUFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Delete All SKU Files
[**apiCatalogPvtStockkeepingunitSkuIdFileGet**](SKUFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Get SKU Files
[**apiCatalogPvtStockkeepingunitSkuIdFilePost**](SKUFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFilePost) | **POST** /api/catalog/pvt/stockkeepingunit/{skuId}/file | Create SKU File
[**apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete**](SKUFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId} | Delete SKU Image File
[**apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut**](SKUFileApi.md#apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut) | **PUT** /api/catalog/pvt/stockkeepingunit/{skuId}/file/{skuFileId} | Update SKU File



## apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut

> [ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner] apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut(contentType, accept, skuIdfrom, skuIdto)

Copy Files from an SKU to another SKU

Copy all existing files from an SKU to another SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1964,          \&quot;ArchiveId\&quot;: 155404,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;\&quot;      },      {          \&quot;Id\&quot;: 1965,          \&quot;ArchiveId\&quot;: 155429,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUFileApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuIdfrom = 1; // Number | __Origin__ SKU’s unique numerical identifier.
let skuIdto = 2; // Number | __Target__ SKU’s unique numerical identifier.
apiInstance.apiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut(contentType, accept, skuIdfrom, skuIdto, (error, data, response) => {
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
 **skuIdfrom** | **Number**| __Origin__ SKU’s unique numerical identifier. | 
 **skuIdto** | **Number**| __Target__ SKU’s unique numerical identifier. | 

### Return type

[**[ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner]**](ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete

> apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete(contentType, accept, skuId, skuFileId)

Disassociate SKU File

Disassociates an SKU File from an SKU.

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

let apiInstance = new CatalogApi.SKUFileApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
let skuFileId = 32; // Number | ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the `Id` field.
apiInstance.apiCatalogPvtStockkeepingunitDisassociateSkuIdFileSkuFileIdDelete(contentType, accept, skuId, skuFileId, (error, data, response) => {
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
 **skuFileId** | **Number**| ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtStockkeepingunitSkuIdFileDelete

> apiCatalogPvtStockkeepingunitSkuIdFileDelete(contentType, accept, skuId)

Delete All SKU Files

Deletes all SKU Image Files.

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

let apiInstance = new CatalogApi.SKUFileApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
apiInstance.apiCatalogPvtStockkeepingunitSkuIdFileDelete(contentType, accept, skuId, (error, data, response) => {
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


## apiCatalogPvtStockkeepingunitSkuIdFileGet

> [ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner] apiCatalogPvtStockkeepingunitSkuIdFileGet(contentType, accept, skuId)

Get SKU Files

Gets general information about all Files in the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 549,          \&quot;ArchiveId\&quot;: 155485,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;chimera-cat-quimera-5\&quot;,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;miau\&quot;      },      {          \&quot;Id\&quot;: 550,          \&quot;ArchiveId\&quot;: 155486,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Gato-siames\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;Gato siames\&quot;      },      {          \&quot;Id\&quot;: 555,          \&quot;ArchiveId\&quot;: 155491,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Cat-Sleeping-Pics\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: null      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUFileApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
apiInstance.apiCatalogPvtStockkeepingunitSkuIdFileGet(contentType, accept, skuId, (error, data, response) => {
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

[**[ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner]**](ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtStockkeepingunitSkuIdFilePost

> ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response apiCatalogPvtStockkeepingunitSkuIdFilePost(contentType, accept, skuId, opts)

Create SKU File

Creates a new Image for an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;Text\&quot;: null,        \&quot;Url\&quot;: \&quot;https://1.bp.blogspot.com/_SLQk9aAv9-o/S7NNbJPv7NI/AAAAAAAAAN8/V1LcO0ViDc4/s1600/waterbottle.jpg\&quot;          }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {        \&quot;Id\&quot;: 503,        \&quot;ArchiveId\&quot;: 155491,        \&quot;SkuId\&quot;: 1,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUFileApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 123456; // Number | SKU’s unique numerical identifier.
let opts = {
  'sKUFileURL': new CatalogApi.SKUFileURL() // SKUFileURL | 
};
apiInstance.apiCatalogPvtStockkeepingunitSkuIdFilePost(contentType, accept, skuId, opts, (error, data, response) => {
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
 **sKUFileURL** | [**SKUFileURL**](SKUFileURL.md)|  | [optional] 

### Return type

[**ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response**](ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json, form-data
- **Accept**: application/json


## apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete

> apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete(contentType, accept, skuId, skuFileId)

Delete SKU Image File

Deletes a specific SKU Image File.

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

let apiInstance = new CatalogApi.SKUFileApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
let skuFileId = 1; // Number | ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the `Id` field.
apiInstance.apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdDelete(contentType, accept, skuId, skuFileId, (error, data, response) => {
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
 **skuFileId** | **Number**| ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut

> ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut(contentType, accept, skuId, skuFileId, opts)

Update SKU File

Updates a new Image on an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null,      \&quot;Name\&quot;: \&quot;toilet-paper\&quot;,      \&quot;Text\&quot;: null,      \&quot;Url\&quot;: \&quot;https://images-na.ssl-images-amazon.com/images/I/81DLLXaGI7L._SL1500_.jpg\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 508,      \&quot;ArchiveId\&quot;: 155491,      \&quot;SkuId\&quot;: 7,      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUFileApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 123456; // Number | SKU’s unique numerical identifier.
let skuFileId = 517; // Number | ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the `Id` field.
let opts = {
  'sKUFileURL': new CatalogApi.SKUFileURL() // SKUFileURL | 
};
apiInstance.apiCatalogPvtStockkeepingunitSkuIdFileSkuFileIdPut(contentType, accept, skuId, skuFileId, opts, (error, data, response) => {
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
 **skuFileId** | **Number**| ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field. | 
 **sKUFileURL** | [**SKUFileURL**](SKUFileURL.md)|  | [optional] 

### Return type

[**ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response**](ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

