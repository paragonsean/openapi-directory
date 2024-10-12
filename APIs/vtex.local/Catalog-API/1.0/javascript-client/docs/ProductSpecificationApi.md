# CatalogApi.ProductSpecificationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtProductProductIdSpecificationPost**](ProductSpecificationApi.md#apiCatalogPvtProductProductIdSpecificationPost) | **POST** /api/catalog/pvt/product/{productId}/specification | Associate Product Specification
[**apiCatalogPvtProductProductIdSpecificationvaluePut**](ProductSpecificationApi.md#apiCatalogPvtProductProductIdSpecificationvaluePut) | **PUT** /api/catalog/pvt/product/{productId}/specificationvalue | Associate product specification using specification name and group name
[**deleteAllProductSpecifications**](ProductSpecificationApi.md#deleteAllProductSpecifications) | **DELETE** /api/catalog/pvt/product/{productId}/specification | Delete all Product Specifications by Product ID
[**deleteaProductSpecification**](ProductSpecificationApi.md#deleteaProductSpecification) | **DELETE** /api/catalog/pvt/product/{productId}/specification/{specificationId} | Delete a specific Product Specification
[**getProductSpecification**](ProductSpecificationApi.md#getProductSpecification) | **GET** /api/catalog_system/pvt/products/{productId}/specification | Get Product Specification by Product ID
[**getProductSpecificationbyProductID**](ProductSpecificationApi.md#getProductSpecificationbyProductID) | **GET** /api/catalog/pvt/product/{productId}/specification | Get Product Specification and its information by Product ID
[**updateProductSpecification**](ProductSpecificationApi.md#updateProductSpecification) | **POST** /api/catalog_system/pvt/products/{productId}/specification | Update Product Specification by Product ID



## apiCatalogPvtProductProductIdSpecificationPost

> ApiCatalogPvtProductProductIdSpecificationPost200Response apiCatalogPvtProductProductIdSpecificationPost(contentType, accept, productId, opts)

Associate Product Specification

Associates a previously defined Specification to a Product.    ### Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 41,      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.ProductSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
let opts = {
  'apiCatalogPvtProductProductIdSpecificationPostRequest': new CatalogApi.ApiCatalogPvtProductProductIdSpecificationPostRequest() // ApiCatalogPvtProductProductIdSpecificationPostRequest | 
};
apiInstance.apiCatalogPvtProductProductIdSpecificationPost(contentType, accept, productId, opts, (error, data, response) => {
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
 **apiCatalogPvtProductProductIdSpecificationPostRequest** | [**ApiCatalogPvtProductProductIdSpecificationPostRequest**](ApiCatalogPvtProductProductIdSpecificationPostRequest.md)|  | [optional] 

### Return type

[**ApiCatalogPvtProductProductIdSpecificationPost200Response**](ApiCatalogPvtProductProductIdSpecificationPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtProductProductIdSpecificationvaluePut

> [ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner] apiCatalogPvtProductProductIdSpecificationvaluePut(contentType, accept, productId, opts)

Associate product specification using specification name and group name

Associates a specification to a product using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Material\&quot;,      \&quot;GroupName\&quot;: \&quot;Additional Information\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;Cotton\&quot;,         \&quot;Polyester\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 53,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 60,          \&quot;Text\&quot;: \&quot;Cotton\&quot;      },      {          \&quot;Id\&quot;: 54,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 61,          \&quot;Text\&quot;: \&quot;Polyester\&quot;      }  ]  &#x60;&#x60;&#x60;  

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

let apiInstance = new CatalogApi.ProductSpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
let opts = {
  'apiCatalogPvtProductProductIdSpecificationvaluePutRequest': new CatalogApi.ApiCatalogPvtProductProductIdSpecificationvaluePutRequest() // ApiCatalogPvtProductProductIdSpecificationvaluePutRequest | 
};
apiInstance.apiCatalogPvtProductProductIdSpecificationvaluePut(contentType, accept, productId, opts, (error, data, response) => {
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
 **apiCatalogPvtProductProductIdSpecificationvaluePutRequest** | [**ApiCatalogPvtProductProductIdSpecificationvaluePutRequest**](ApiCatalogPvtProductProductIdSpecificationvaluePutRequest.md)|  | [optional] 

### Return type

[**[ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner]**](ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAllProductSpecifications

> deleteAllProductSpecifications(contentType, accept, productId)

Delete all Product Specifications by Product ID

Deletes all Product Specifications given a specific Product ID.

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

let apiInstance = new CatalogApi.ProductSpecificationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
apiInstance.deleteAllProductSpecifications(contentType, accept, productId, (error, data, response) => {
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
 **productId** | **Number**| Product’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteaProductSpecification

> deleteaProductSpecification(contentType, accept, productId, specificationId)

Delete a specific Product Specification

Deletes a specific Product Specification given a Product ID and a Specification ID.

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

let apiInstance = new CatalogApi.ProductSpecificationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
let specificationId = 7; // Number | Product Specification’s unique numerical identifier.
apiInstance.deleteaProductSpecification(contentType, accept, productId, specificationId, (error, data, response) => {
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
 **productId** | **Number**| Product’s unique numerical identifier. | 
 **specificationId** | **Number**| Product Specification’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductSpecification

> [GetorUpdateProductSpecification] getProductSpecification(contentType, accept, productId)

Get Product Specification by Product ID

Retrieves all specifications of a product by the product&#39;s ID.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.ProductSpecificationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
apiInstance.getProductSpecification(contentType, accept, productId, (error, data, response) => {
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

[**[GetorUpdateProductSpecification]**](GetorUpdateProductSpecification.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductSpecificationbyProductID

> [GetProductSpecificationbyProductID200ResponseInner] getProductSpecificationbyProductID(contentType, accept, productId)

Get Product Specification and its information by Product ID

Retrieves information of all specifications of a product by the product&#39;s ID.     ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 227,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;FieldValueId\&quot;: 135,          \&quot;Text\&quot;: \&quot;ValueA\&quot;      },      {          \&quot;Id\&quot;: 228,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;FieldValueId\&quot;: 1,          \&quot;Text\&quot;: \&quot;Giant\&quot;      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.ProductSpecificationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique numerical identifier.
apiInstance.getProductSpecificationbyProductID(contentType, accept, productId, (error, data, response) => {
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

[**[GetProductSpecificationbyProductID200ResponseInner]**](GetProductSpecificationbyProductID200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateProductSpecification

> updateProductSpecification(contentType, accept, productId, getorUpdateProductSpecification)

Update Product Specification by Product ID

Updates the value of a product specification by the product&#39;s ID. The ID or name can be used to identify what product specification will be updated. Specification fields must be previously created in your Catalog.    ### Request body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.ProductSpecificationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let productId = 1; // Number | Product’s unique identifier.
let getorUpdateProductSpecification = [new CatalogApi.GetorUpdateProductSpecification()]; // [GetorUpdateProductSpecification] | 
apiInstance.updateProductSpecification(contentType, accept, productId, getorUpdateProductSpecification, (error, data, response) => {
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
 **productId** | **Number**| Product’s unique identifier. | 
 **getorUpdateProductSpecification** | [**[GetorUpdateProductSpecification]**](GetorUpdateProductSpecification.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

