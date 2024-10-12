# CatalogApi.SKUServiceApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtSkuservicePost**](SKUServiceApi.md#apiCatalogPvtSkuservicePost) | **POST** /api/catalog/pvt/skuservice | Associate SKU Service
[**apiCatalogPvtSkuserviceSkuServiceIdDelete**](SKUServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdDelete) | **DELETE** /api/catalog/pvt/skuservice/{skuServiceId} | Dissociate SKU Service
[**apiCatalogPvtSkuserviceSkuServiceIdGet**](SKUServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdGet) | **GET** /api/catalog/pvt/skuservice/{skuServiceId} | Get SKU Service
[**apiCatalogPvtSkuserviceSkuServiceIdPut**](SKUServiceApi.md#apiCatalogPvtSkuserviceSkuServiceIdPut) | **PUT** /api/catalog/pvt/skuservice/{skuServiceId} | Update SKU Service



## apiCatalogPvtSkuservicePost

> SKUService apiCatalogPvtSkuservicePost(contentType, accept, opts)

Associate SKU Service

Associates an SKU Service to an SKU.

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

let apiInstance = new CatalogApi.SKUServiceApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'requestBody3': new CatalogApi.RequestBody3() // RequestBody3 | 
};
apiInstance.apiCatalogPvtSkuservicePost(contentType, accept, opts, (error, data, response) => {
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
 **requestBody3** | [**RequestBody3**](RequestBody3.md)|  | [optional] 

### Return type

[**SKUService**](SKUService.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSkuserviceSkuServiceIdDelete

> apiCatalogPvtSkuserviceSkuServiceIdDelete(contentType, accept, skuServiceId)

Dissociate SKU Service

Dissociates an SKU Service from an SKU.

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

let apiInstance = new CatalogApi.SKUServiceApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuServiceId = 1; // Number | SKU Service unique identifier.
apiInstance.apiCatalogPvtSkuserviceSkuServiceIdDelete(contentType, accept, skuServiceId, (error, data, response) => {
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
 **skuServiceId** | **Number**| SKU Service unique identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtSkuserviceSkuServiceIdGet

> SKUService apiCatalogPvtSkuserviceSkuServiceIdGet(contentType, accept, skuServiceId)

Get SKU Service

Retrieves an SKU Service.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1,      \&quot;SkuServiceValueId\&quot;: 1,      \&quot;SkuId\&quot;: 1,      \&quot;Name\&quot;: \&quot;name\&quot;,      \&quot;Text\&quot;: \&quot;text\&quot;,      \&quot;IsActive\&quot;: false  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUServiceApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuServiceId = 5; // Number | SKU Service unique identifier.
apiInstance.apiCatalogPvtSkuserviceSkuServiceIdGet(contentType, accept, skuServiceId, (error, data, response) => {
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
 **skuServiceId** | **Number**| SKU Service unique identifier. | 

### Return type

[**SKUService**](SKUService.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtSkuserviceSkuServiceIdPut

> SKUService apiCatalogPvtSkuserviceSkuServiceIdPut(contentType, accept, skuServiceId, opts)

Update SKU Service

Updates an SKU Service.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;name\&quot;,      \&quot;Text\&quot;: \&quot;text\&quot;,      \&quot;IsActive\&quot;: false  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1,      \&quot;SkuServiceValueId\&quot;: 1,      \&quot;SkuId\&quot;: 1,      \&quot;Name\&quot;: \&quot;name\&quot;,      \&quot;Text\&quot;: \&quot;text\&quot;,      \&quot;IsActive\&quot;: false  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUServiceApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuServiceId = 5; // Number | SKU Service unique identifier.
let opts = {
  'requestBody4': new CatalogApi.RequestBody4() // RequestBody4 | 
};
apiInstance.apiCatalogPvtSkuserviceSkuServiceIdPut(contentType, accept, skuServiceId, opts, (error, data, response) => {
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
 **skuServiceId** | **Number**| SKU Service unique identifier. | 
 **requestBody4** | [**RequestBody4**](RequestBody4.md)|  | [optional] 

### Return type

[**SKUService**](SKUService.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

