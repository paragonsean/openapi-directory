# CatalogApi.SKUServiceValueApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtSkuservicevaluePost**](SKUServiceValueApi.md#apiCatalogPvtSkuservicevaluePost) | **POST** /api/catalog/pvt/skuservicevalue | Create SKU Service Value
[**apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete**](SKUServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete) | **DELETE** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Delete SKU Service Value
[**apiCatalogPvtSkuservicevalueSkuServiceValueIdGet**](SKUServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdGet) | **GET** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Get SKU Service Value
[**apiCatalogPvtSkuservicevalueSkuServiceValueIdPut**](SKUServiceValueApi.md#apiCatalogPvtSkuservicevalueSkuServiceValueIdPut) | **PUT** /api/catalog/pvt/skuservicevalue/{skuServiceValueId} | Update SKU Service Value



## apiCatalogPvtSkuservicevaluePost

> SKUServiceValueResponse apiCatalogPvtSkuservicevaluePost(contentType, accept, opts)

Create SKU Service Value

Creates an SKU Service Value for an existing SKU Service Type.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUServiceValueApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'sKUServiceValueRequest': new CatalogApi.SKUServiceValueRequest() // SKUServiceValueRequest | 
};
apiInstance.apiCatalogPvtSkuservicevaluePost(contentType, accept, opts, (error, data, response) => {
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
 **sKUServiceValueRequest** | [**SKUServiceValueRequest**](SKUServiceValueRequest.md)|  | [optional] 

### Return type

[**SKUServiceValueResponse**](SKUServiceValueResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete

> apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete(contentType, accept, skuServiceValueId)

Delete SKU Service Value

Deletes an existing SKU Service Value.

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

let apiInstance = new CatalogApi.SKUServiceValueApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuServiceValueId = 1; // Number | SKU Service Value unique identifier.
apiInstance.apiCatalogPvtSkuservicevalueSkuServiceValueIdDelete(contentType, accept, skuServiceValueId, (error, data, response) => {
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
 **skuServiceValueId** | **Number**| SKU Service Value unique identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtSkuservicevalueSkuServiceValueIdGet

> SKUServiceValueResponse apiCatalogPvtSkuservicevalueSkuServiceValueIdGet(contentType, accept, skuServiceValueId)

Get SKU Service Value

Retrieves an existing SKU Service Value.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUServiceValueApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuServiceValueId = 1; // Number | SKU Service Value unique identifier.
apiInstance.apiCatalogPvtSkuservicevalueSkuServiceValueIdGet(contentType, accept, skuServiceValueId, (error, data, response) => {
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
 **skuServiceValueId** | **Number**| SKU Service Value unique identifier. | 

### Return type

[**SKUServiceValueResponse**](SKUServiceValueResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtSkuservicevalueSkuServiceValueIdPut

> SKUServiceValueResponse apiCatalogPvtSkuservicevalueSkuServiceValueIdPut(contentType, accept, skuServiceValueId, opts)

Update SKU Service Value

Updates an existing SKU Service Value.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUServiceValueApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuServiceValueId = 1; // Number | SKU Service Value unique identifier.
let opts = {
  'sKUServiceValueRequest': new CatalogApi.SKUServiceValueRequest() // SKUServiceValueRequest | 
};
apiInstance.apiCatalogPvtSkuservicevalueSkuServiceValueIdPut(contentType, accept, skuServiceValueId, opts, (error, data, response) => {
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
 **skuServiceValueId** | **Number**| SKU Service Value unique identifier. | 
 **sKUServiceValueRequest** | [**SKUServiceValueRequest**](SKUServiceValueRequest.md)|  | [optional] 

### Return type

[**SKUServiceValueResponse**](SKUServiceValueResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

