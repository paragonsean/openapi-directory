# CatalogApi.CategorySpecificationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**specificationsByCategoryId**](CategorySpecificationApi.md#specificationsByCategoryId) | **GET** /api/catalog_system/pub/specification/field/listByCategoryId/{categoryId} | Get Specifications By Category ID
[**specificationsTreeByCategoryId**](CategorySpecificationApi.md#specificationsTreeByCategoryId) | **GET** /api/catalog_system/pub/specification/field/listTreeByCategoryId/{categoryId} | Get Specifications Tree By Category ID



## specificationsByCategoryId

> [CategorySpecificationInner] specificationsByCategoryId(contentType, accept, categoryId)

Get Specifications By Category ID

Retrieves all specifications from a category by its ID.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Name\&quot;: \&quot;Specification A\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification B\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification C\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 35,          \&quot;IsActive\&quot;: false,          \&quot;IsStockKeepingUnit\&quot;: false      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.CategorySpecificationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let categoryId = 1; // Number | Category ID.
apiInstance.specificationsByCategoryId(contentType, accept, categoryId, (error, data, response) => {
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
 **categoryId** | **Number**| Category ID. | 

### Return type

[**[CategorySpecificationInner]**](CategorySpecificationInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## specificationsTreeByCategoryId

> [CategorySpecificationInner] specificationsTreeByCategoryId(contentType, accept, categoryId)

Get Specifications Tree By Category ID

Lists all specifications including the current category and the level zero specifications from a category by its ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Name\&quot;: \&quot;Specification A\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification B\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;IsActive\&quot;: true,          \&quot;IsStockKeepingUnit\&quot;: false      },      {          \&quot;Name\&quot;: \&quot;Specification C\&quot;,          \&quot;CategoryId\&quot;: 1,          \&quot;FieldId\&quot;: 35,          \&quot;IsActive\&quot;: false,          \&quot;IsStockKeepingUnit\&quot;: false      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.CategorySpecificationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let categoryId = 1; // Number | Category ID.
apiInstance.specificationsTreeByCategoryId(contentType, accept, categoryId, (error, data, response) => {
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
 **categoryId** | **Number**| Category ID. | 

### Return type

[**[CategorySpecificationInner]**](CategorySpecificationInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

