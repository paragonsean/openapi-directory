# CatalogApi.NonStructuredSpecificationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtSpecificationNonstructuredDelete**](NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredDelete) | **DELETE** /api/catalog/pvt/specification/nonstructured | Delete Non Structured Specification by SKU ID
[**apiCatalogPvtSpecificationNonstructuredGet**](NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredGet) | **GET** /api/catalog/pvt/specification/nonstructured | Get Non Structured Specification by SKU ID
[**apiCatalogPvtSpecificationNonstructuredIdDelete**](NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredIdDelete) | **DELETE** /api/catalog/pvt/specification/nonstructured/{Id} | Delete Non Structured Specification
[**apiCatalogPvtSpecificationNonstructuredIdGet**](NonStructuredSpecificationApi.md#apiCatalogPvtSpecificationNonstructuredIdGet) | **GET** /api/catalog/pvt/specification/nonstructured/{Id} | Get Non Structured Specification by ID



## apiCatalogPvtSpecificationNonstructuredDelete

> apiCatalogPvtSpecificationNonstructuredDelete(contentType, accept, skuId)

Delete Non Structured Specification by SKU ID

Deletes unmapped Specifications of a Seller&#39;S SKU in a Marketplace by SKU ID.

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

let apiInstance = new CatalogApi.NonStructuredSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
apiInstance.apiCatalogPvtSpecificationNonstructuredDelete(contentType, accept, skuId, (error, data, response) => {
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


## apiCatalogPvtSpecificationNonstructuredGet

> [ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner] apiCatalogPvtSpecificationNonstructuredGet(contentType, accept, skuId)

Get Non Structured Specification by SKU ID

Gets general information about unmapped Specifications of a Seller&#39;s SKU in a Marketplace by SKU ID.   ## Response body example    &#x60;&#x60;&#x60;json  [  {      \&quot;Id\&quot;: 1010,      \&quot;SkuId\&quot;: 310119072,      \&quot;SpecificationName\&quot;: \&quot;size\&quot;,      \&quot;SpecificationValue\&quot;: \&quot;Small\&quot;  }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.NonStructuredSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU’s unique numerical identifier.
apiInstance.apiCatalogPvtSpecificationNonstructuredGet(contentType, accept, skuId, (error, data, response) => {
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

[**[ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner]**](ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtSpecificationNonstructuredIdDelete

> apiCatalogPvtSpecificationNonstructuredIdDelete(contentType, accept, id)

Delete Non Structured Specification

Deletes unmapped Specifications of a Seller&#39;S SKU in a Marketplace by its unique ID.

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

let apiInstance = new CatalogApi.NonStructuredSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let id = 1; // Number | Non Structured Specification’s unique numerical identifier.
apiInstance.apiCatalogPvtSpecificationNonstructuredIdDelete(contentType, accept, id, (error, data, response) => {
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
 **id** | **Number**| Non Structured Specification’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtSpecificationNonstructuredIdGet

> [ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner] apiCatalogPvtSpecificationNonstructuredIdGet(contentType, accept, id)

Get Non Structured Specification by ID

Retrieves general information about unmapped Specifications of a Seller&#39;s SKU in a Marketplace.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1010,      \&quot;SkuId\&quot;: 310119072,      \&quot;SpecificationName\&quot;: \&quot;size\&quot;,      \&quot;SpecificationValue\&quot;: \&quot;Small\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.NonStructuredSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let id = 1010; // Number | Non Structured Specification’s unique numerical identifier.
apiInstance.apiCatalogPvtSpecificationNonstructuredIdGet(contentType, accept, id, (error, data, response) => {
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
 **id** | **Number**| Non Structured Specification’s unique numerical identifier. | 

### Return type

[**[ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner]**](ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

