# CatalogApi.SKUServiceAttachmentApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtSkuservicetypeattachmentDelete**](SKUServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentDelete) | **DELETE** /api/catalog/pvt/skuservicetypeattachment | Dissociate Attachment by Attachment ID or SKU Service Type ID
[**apiCatalogPvtSkuservicetypeattachmentPost**](SKUServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentPost) | **POST** /api/catalog/pvt/skuservicetypeattachment | Associate SKU Service Attachment
[**apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete**](SKUServiceAttachmentApi.md#apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete) | **DELETE** /api/catalog/pvt/skuservicetypeattachment/{skuServiceTypeAttachmentId} | Dissociate Attachment from SKU Service Type



## apiCatalogPvtSkuservicetypeattachmentDelete

> apiCatalogPvtSkuservicetypeattachmentDelete(contentType, accept, opts)

Dissociate Attachment by Attachment ID or SKU Service Type ID

Dissociates an Attachment by its Attachment ID or SKU Service Type ID from an SKU Service Type.

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

let apiInstance = new CatalogApi.SKUServiceAttachmentApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'attachmentId': 1, // Number | SKU Service Attachment unique identifier.
  'skuServiceTypeId': 1 // Number | SKU Service Type unique identifier.
};
apiInstance.apiCatalogPvtSkuservicetypeattachmentDelete(contentType, accept, opts, (error, data, response) => {
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
 **attachmentId** | **Number**| SKU Service Attachment unique identifier. | [optional] 
 **skuServiceTypeId** | **Number**| SKU Service Type unique identifier. | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtSkuservicetypeattachmentPost

> ApiCatalogPvtSkuservicetypeattachmentPost200Response apiCatalogPvtSkuservicetypeattachmentPost(contentType, accept, opts)

Associate SKU Service Attachment

Associates an Attachment for an existing SKU Service Type.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUServiceAttachmentApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'requestBody5': new CatalogApi.RequestBody5() // RequestBody5 | 
};
apiInstance.apiCatalogPvtSkuservicetypeattachmentPost(contentType, accept, opts, (error, data, response) => {
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
 **requestBody5** | [**RequestBody5**](RequestBody5.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSkuservicetypeattachmentPost200Response**](ApiCatalogPvtSkuservicetypeattachmentPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete

> apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete(contentType, accept, skuServiceTypeAttachmentId)

Dissociate Attachment from SKU Service Type

Dissociates an Attachment from an SKU Service Type

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

let apiInstance = new CatalogApi.SKUServiceAttachmentApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuServiceTypeAttachmentId = 1; // Number | SKU Service Attachment unique identifier.
apiInstance.apiCatalogPvtSkuservicetypeattachmentSkuServiceTypeAttachmentIdDelete(contentType, accept, skuServiceTypeAttachmentId, (error, data, response) => {
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
 **skuServiceTypeAttachmentId** | **Number**| SKU Service Attachment unique identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

