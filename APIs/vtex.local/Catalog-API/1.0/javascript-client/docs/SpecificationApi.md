# CatalogApi.SpecificationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtSpecificationPost**](SpecificationApi.md#apiCatalogPvtSpecificationPost) | **POST** /api/catalog/pvt/specification | Create Specification
[**apiCatalogPvtSpecificationSpecificationIdGet**](SpecificationApi.md#apiCatalogPvtSpecificationSpecificationIdGet) | **GET** /api/catalog/pvt/specification/{specificationId} | Get Specification
[**apiCatalogPvtSpecificationSpecificationIdPut**](SpecificationApi.md#apiCatalogPvtSpecificationSpecificationIdPut) | **PUT** /api/catalog/pvt/specification/{specificationId} | Update Specification



## apiCatalogPvtSpecificationPost

> ApiCatalogPvtSpecificationPost200Response apiCatalogPvtSpecificationPost(contentType, accept, opts)

Create Specification

Creates a new Product or SKU Specification.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 88,      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsWizard\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;  }  &#x60;&#x60;&#x60;  

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

let apiInstance = new CatalogApi.SpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'apiCatalogPvtSpecificationPostRequest': new CatalogApi.ApiCatalogPvtSpecificationPostRequest() // ApiCatalogPvtSpecificationPostRequest | 
};
apiInstance.apiCatalogPvtSpecificationPost(contentType, accept, opts, (error, data, response) => {
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
 **apiCatalogPvtSpecificationPostRequest** | [**ApiCatalogPvtSpecificationPostRequest**](ApiCatalogPvtSpecificationPostRequest.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSpecificationPost200Response**](ApiCatalogPvtSpecificationPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSpecificationSpecificationIdGet

> RequestBody6 apiCatalogPvtSpecificationSpecificationIdGet(contentType, accept, specificationId)

Get Specification

Retrieves information of a Product or SKU Specification.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 88,      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsWizard\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;  }  &#x60;&#x60;&#x60;  

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

let apiInstance = new CatalogApi.SpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let specificationId = 1; // Number | Specification’s unique numerical identifier.
apiInstance.apiCatalogPvtSpecificationSpecificationIdGet(contentType, accept, specificationId, (error, data, response) => {
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
 **specificationId** | **Number**| Specification’s unique numerical identifier. | 

### Return type

[**RequestBody6**](RequestBody6.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtSpecificationSpecificationIdPut

> ApiCatalogPvtSpecificationPost200Response apiCatalogPvtSpecificationSpecificationIdPut(contentType, accept, specificationId, opts)

Update Specification

Updates a Product or SKU Specification.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Leather\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 88,      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsWizard\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Leather\&quot;  }  &#x60;&#x60;&#x60;  

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

let apiInstance = new CatalogApi.SpecificationApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let specificationId = 88; // Number | Specification’s unique numerical identifier.
let opts = {
  'requestBody7': new CatalogApi.RequestBody7() // RequestBody7 | 
};
apiInstance.apiCatalogPvtSpecificationSpecificationIdPut(contentType, accept, specificationId, opts, (error, data, response) => {
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
 **specificationId** | **Number**| Specification’s unique numerical identifier. | 
 **requestBody7** | [**RequestBody7**](RequestBody7.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSpecificationPost200Response**](ApiCatalogPvtSpecificationPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

