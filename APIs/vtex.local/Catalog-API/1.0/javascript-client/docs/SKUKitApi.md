# CatalogApi.SKUKitApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtStockkeepingunitkitDelete**](SKUKitApi.md#apiCatalogPvtStockkeepingunitkitDelete) | **DELETE** /api/catalog/pvt/stockkeepingunitkit | Delete SKU Kit by SKU ID or Parent SKU ID
[**apiCatalogPvtStockkeepingunitkitGet**](SKUKitApi.md#apiCatalogPvtStockkeepingunitkitGet) | **GET** /api/catalog/pvt/stockkeepingunitkit | Get SKU Kit by SKU ID or Parent SKU ID
[**apiCatalogPvtStockkeepingunitkitKitIdDelete**](SKUKitApi.md#apiCatalogPvtStockkeepingunitkitKitIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunitkit/{kitId} | Delete SKU Kit by KitId
[**apiCatalogPvtStockkeepingunitkitKitIdGet**](SKUKitApi.md#apiCatalogPvtStockkeepingunitkitKitIdGet) | **GET** /api/catalog/pvt/stockkeepingunitkit/{kitId} | Get SKU Kit
[**apiCatalogPvtStockkeepingunitkitPost**](SKUKitApi.md#apiCatalogPvtStockkeepingunitkitPost) | **POST** /api/catalog/pvt/stockkeepingunitkit | Create SKU Kit



## apiCatalogPvtStockkeepingunitkitDelete

> apiCatalogPvtStockkeepingunitkitDelete(contentType, accept, opts)

Delete SKU Kit by SKU ID or Parent SKU ID

Deletes all Kit’s components based on the Parent SKU ID or deletes a specific Kit’s component based on the SKU ID.

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

let apiInstance = new CatalogApi.SKUKitApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'skuId': 1, // Number | SKU’s unique numerical identifier.
  'parentSkuId': 1 // Number | Parent SKU’s unique numerical identifier.
};
apiInstance.apiCatalogPvtStockkeepingunitkitDelete(contentType, accept, opts, (error, data, response) => {
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
 **skuId** | **Number**| SKU’s unique numerical identifier. | [optional] 
 **parentSkuId** | **Number**| Parent SKU’s unique numerical identifier. | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtStockkeepingunitkitGet

> SkuKit apiCatalogPvtStockkeepingunitkitGet(contentType, accept, opts)

Get SKU Kit by SKU ID or Parent SKU ID

Retrieves general information about the components of an SKU Kit by SKU ID or Parent SKU ID.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 7,      \&quot;StockKeepingUnitParent\&quot;: 7,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;Quantity\&quot;: 1,      \&quot;UnitPrice\&quot;: 50.0000  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUKitApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'skuId': 1, // Number | SKU’s unique numerical identifier.
  'parentSkuId': 1 // Number | Parent SKU’s unique numerical identifier.
};
apiInstance.apiCatalogPvtStockkeepingunitkitGet(contentType, accept, opts, (error, data, response) => {
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
 **skuId** | **Number**| SKU’s unique numerical identifier. | [optional] 
 **parentSkuId** | **Number**| Parent SKU’s unique numerical identifier. | [optional] 

### Return type

[**SkuKit**](SkuKit.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtStockkeepingunitkitKitIdDelete

> apiCatalogPvtStockkeepingunitkitKitIdDelete(contentType, accept, kitId)

Delete SKU Kit by KitId

Deletes a specific Kit’s component based on its Kit ID.

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

let apiInstance = new CatalogApi.SKUKitApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let kitId = 1; // Number | Kit’s unique numerical identifier.
apiInstance.apiCatalogPvtStockkeepingunitkitKitIdDelete(contentType, accept, kitId, (error, data, response) => {
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
 **kitId** | **Number**| Kit’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtStockkeepingunitkitKitIdGet

> SkuKit apiCatalogPvtStockkeepingunitkitKitIdGet(contentType, accept, kitId)

Get SKU Kit

Retrieves general information about a component of a Kit.

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

let apiInstance = new CatalogApi.SKUKitApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let kitId = 1; // Number | Kit’s unique numerical identifier
apiInstance.apiCatalogPvtStockkeepingunitkitKitIdGet(contentType, accept, kitId, (error, data, response) => {
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
 **kitId** | **Number**| Kit’s unique numerical identifier | 

### Return type

[**SkuKit**](SkuKit.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtStockkeepingunitkitPost

> SkuKit apiCatalogPvtStockkeepingunitkitPost(contentType, accept, opts)

Create SKU Kit

Adds a component to a specific Kit.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;StockKeepingUnitParent\&quot;: 7,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;Quantity\&quot;: 1,      \&quot;UnitPrice\&quot;: 50.0000  }  &#x60;&#x60;&#x60;   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 7,      \&quot;StockKeepingUnitParent\&quot;: 7,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;Quantity\&quot;: 1,      \&quot;UnitPrice\&quot;: 50.0000  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUKitApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'requestBody9': new CatalogApi.RequestBody9() // RequestBody9 | 
};
apiInstance.apiCatalogPvtStockkeepingunitkitPost(contentType, accept, opts, (error, data, response) => {
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
 **requestBody9** | [**RequestBody9**](RequestBody9.md)|  | [optional] 

### Return type

[**SkuKit**](SkuKit.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

