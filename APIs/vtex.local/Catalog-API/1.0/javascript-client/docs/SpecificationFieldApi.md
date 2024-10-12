# CatalogApi.SpecificationFieldApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**specificationsField**](SpecificationFieldApi.md#specificationsField) | **GET** /api/catalog_system/pub/specification/fieldGet/{fieldId} | Get Specification Field
[**specificationsInsertField**](SpecificationFieldApi.md#specificationsInsertField) | **POST** /api/catalog_system/pvt/specification/field | Create Specification Field
[**specificationsInsertFieldUpdate**](SpecificationFieldApi.md#specificationsInsertFieldUpdate) | **PUT** /api/catalog_system/pvt/specification/field | Update Specification Field



## specificationsField

> SpecificationsField200Response specificationsField(contentType, accept, fieldId)

Get Specification Field

Retrieves details from a specification field by this field&#39;s ID.   &gt;⚠️ This is a legacy endpoint. We recommend using [Get Specification](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-pvt-specification-specificationid) instead.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldId\&quot;: 88,      \&quot;IsActive\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;FieldTypeId\&quot;: 1,      \&quot;FieldTypeName\&quot;: \&quot;Texto\&quot;,      \&quot;FieldValueId\&quot;: null,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsFilter\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;Position\&quot;: 1,      \&quot;IsWizard\&quot;: false,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: null,      \&quot;FieldGroupId\&quot;: 20,      \&quot;FieldGroupName\&quot;: \&quot;Clothes specifications\&quot;  }  &#x60;&#x60;&#x60;    

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

let apiInstance = new CatalogApi.SpecificationFieldApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let fieldId = 88; // Number | Specification Field ID.
apiInstance.specificationsField(contentType, accept, fieldId, (error, data, response) => {
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
 **fieldId** | **Number**| Specification Field ID. | 

### Return type

[**SpecificationsField200Response**](SpecificationsField200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## specificationsInsertField

> Number specificationsInsertField(contentType, accept, specificationsInsertFieldRequest)

Create Specification Field

Creates a specification field in a category.   &gt;⚠️ This is a legacy endpoint. We recommend using [Create Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-specification) instead.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldId\&quot;: 88,      \&quot;IsActive\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;FieldTypeId\&quot;: 1,      \&quot;FieldValueId\&quot;: 1,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;IsFilter\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;Position\&quot;: 1,      \&quot;IsWizard\&quot;: false,      \&quot;IsTopMenuLinkActive\&quot;: true,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: null,      \&quot;FieldGroupId\&quot;: 20,      \&quot;FieldGroupName\&quot;: \&quot;Clothes specifications\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  89  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationFieldApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let specificationsInsertFieldRequest = {"CategoryId":4,"DefaultValue":null,"Description":"Composition of the product.","FieldGroupId":20,"FieldGroupName":"Clothes specifications","FieldId":88,"FieldTypeId":1,"FieldValueId":1,"IsActive":true,"IsFilter":true,"IsOnProductDetails":false,"IsRequired":true,"IsSideMenuLinkActive":true,"IsStockKeepingUnit":false,"IsTopMenuLinkActive":true,"IsWizard":false,"Name":"Material","Position":1}; // SpecificationsInsertFieldRequest | 
apiInstance.specificationsInsertField(contentType, accept, specificationsInsertFieldRequest, (error, data, response) => {
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
 **specificationsInsertFieldRequest** | [**SpecificationsInsertFieldRequest**](SpecificationsInsertFieldRequest.md)|  | 

### Return type

**Number**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## specificationsInsertFieldUpdate

> Number specificationsInsertFieldUpdate(contentType, accept, specificationsInsertFieldUpdateRequest)

Update Specification Field

Updates a specification field in a category.   &gt;⚠️ This is a legacy endpoint. We recommend using [Update Specification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-put-specification) instead.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 89,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;CategoryId\&quot;: 4,      \&quot;IsActive\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;FieldTypeId\&quot;: 1,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsFilter\&quot;: true,      \&quot;IsOnProductDetails\&quot;: true,      \&quot;Position\&quot;: 1,      \&quot;IsWizard\&quot;: false,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: false,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;,      \&quot;FieldGroupId\&quot;: 20,      \&quot;FieldGroupName\&quot;: \&quot;Clothes specifications\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  89  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.SpecificationFieldApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let specificationsInsertFieldUpdateRequest = {"CategoryId":4,"DefaultValue":"Cotton","Description":"Composition of the product.","FieldGroupId":20,"FieldGroupName":"Clothes specifications","FieldId":89,"FieldTypeId":1,"IsActive":true,"IsFilter":true,"IsOnProductDetails":true,"IsRequired":true,"IsSideMenuLinkActive":false,"IsStockKeepingUnit":false,"IsTopMenuLinkActive":false,"IsWizard":false,"Name":"Material","Position":1}; // SpecificationsInsertFieldUpdateRequest | 
apiInstance.specificationsInsertFieldUpdate(contentType, accept, specificationsInsertFieldUpdateRequest, (error, data, response) => {
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
 **specificationsInsertFieldUpdateRequest** | [**SpecificationsInsertFieldUpdateRequest**](SpecificationsInsertFieldUpdateRequest.md)|  | 

### Return type

**Number**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

