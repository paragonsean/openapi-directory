# CatalogApi.SKUAttachmentApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtSkuattachmentDelete**](SKUAttachmentApi.md#apiCatalogPvtSkuattachmentDelete) | **DELETE** /api/catalog/pvt/skuattachment | Dissociate attachments and SKUs
[**apiCatalogPvtSkuattachmentPost**](SKUAttachmentApi.md#apiCatalogPvtSkuattachmentPost) | **POST** /api/catalog/pvt/skuattachment | Associate SKU Attachment
[**apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete**](SKUAttachmentApi.md#apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete) | **DELETE** /api/catalog/pvt/skuattachment/{skuAttachmentAssociationId} | Delete SKU Attachment by Attachment Association ID
[**apiCatalogPvtStockkeepingunitSkuIdAttachmentGet**](SKUAttachmentApi.md#apiCatalogPvtStockkeepingunitSkuIdAttachmentGet) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/attachment | Get SKU Attachments by SKU ID
[**associateattachmentstoSKU**](SKUAttachmentApi.md#associateattachmentstoSKU) | **POST** /api/catalog_system/pvt/sku/associateattachments | Associate attachments to an SKU



## apiCatalogPvtSkuattachmentDelete

> apiCatalogPvtSkuattachmentDelete(contentType, accept, opts)

Dissociate attachments and SKUs

Dissociates attachments and SKUs based on an SKU ID or an attachment ID.

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

let apiInstance = new CatalogApi.SKUAttachmentApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'skuId': 1, // Number | SKU ID. By using this query param, you can dissociate all the attachments from an SKU based on its SKU ID.
  'attachmentId': 1 // Number | Attachment ID. By using this query param, you can dissociate the given attachment from all previously associated SKUs.
};
apiInstance.apiCatalogPvtSkuattachmentDelete(contentType, accept, opts, (error, data, response) => {
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
 **skuId** | **Number**| SKU ID. By using this query param, you can dissociate all the attachments from an SKU based on its SKU ID. | [optional] 
 **attachmentId** | **Number**| Attachment ID. By using this query param, you can dissociate the given attachment from all previously associated SKUs. | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtSkuattachmentPost

> ApiCatalogPvtSkuattachmentPost200Response apiCatalogPvtSkuattachmentPost(contentType, accept, opts)

Associate SKU Attachment

Associates an existing SKU to an existing Attachment.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuId\&quot;: 7  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 31,      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuId\&quot;: 7  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUAttachmentApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'requestBody1': new CatalogApi.RequestBody1() // RequestBody1 | 
};
apiInstance.apiCatalogPvtSkuattachmentPost(contentType, accept, opts, (error, data, response) => {
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
 **requestBody1** | [**RequestBody1**](RequestBody1.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSkuattachmentPost200Response**](ApiCatalogPvtSkuattachmentPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete

> apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete(contentType, accept, skuAttachmentAssociationId)

Delete SKU Attachment by Attachment Association ID

Deletes the association of an SKU to an Attachment.

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

let apiInstance = new CatalogApi.SKUAttachmentApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuAttachmentAssociationId = 1; // Number | ID of the association between the attachment and the SKU, which corresponds to the `Id` in the response body of the [Associate SKU Attachment](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-attachment) and the [Get SKU Attachment by SKU ID](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-pvt-stockkeepingunit-skuid-attachment) endpoints.
apiInstance.apiCatalogPvtSkuattachmentSkuAttachmentAssociationIdDelete(contentType, accept, skuAttachmentAssociationId, (error, data, response) => {
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
 **skuAttachmentAssociationId** | **Number**| ID of the association between the attachment and the SKU, which corresponds to the &#x60;Id&#x60; in the response body of the [Associate SKU Attachment](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-attachment) and the [Get SKU Attachment by SKU ID](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-pvt-stockkeepingunit-skuid-attachment) endpoints. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtStockkeepingunitSkuIdAttachmentGet

> [ApiCatalogPvtSkuattachmentPost200Response] apiCatalogPvtStockkeepingunitSkuIdAttachmentGet(contentType, accept, skuId)

Get SKU Attachments by SKU ID

Retrieves existing SKU Attachments by SKU ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 97,          \&quot;AttachmentId\&quot;: 1,          \&quot;SkuId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUAttachmentApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let skuId = 1; // Number | SKU unique identifier.
apiInstance.apiCatalogPvtStockkeepingunitSkuIdAttachmentGet(contentType, accept, skuId, (error, data, response) => {
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
 **skuId** | **Number**| SKU unique identifier. | 

### Return type

[**[ApiCatalogPvtSkuattachmentPost200Response]**](ApiCatalogPvtSkuattachmentPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## associateattachmentstoSKU

> associateattachmentstoSKU(contentType, accept, associateattachmentstoSKURequest)

Associate attachments to an SKU

Associates attachments to an SKU based on a given SKU ID and attachment names.  This request removes existing SKU attachment associations and recreates the associations with the attachments being sent.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 1,      \&quot;AttachmentNames\&quot;: [          \&quot;T-Shirt Customization\&quot;      ]  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SKUAttachmentApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let associateattachmentstoSKURequest = {"AttachmentNames":["T-Shirt Customization"],"SkuId":1}; // AssociateattachmentstoSKURequest | 
apiInstance.associateattachmentstoSKU(contentType, accept, associateattachmentstoSKURequest, (error, data, response) => {
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
 **associateattachmentstoSKURequest** | [**AssociateattachmentstoSKURequest**](AssociateattachmentstoSKURequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

