# CatalogApiSellerPortal.CategoryApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCategory**](CategoryApi.md#createCategory) | **POST** /api/catalog-seller-portal/category-tree/categories | Create Category
[**getCategoryTree**](CategoryApi.md#getCategoryTree) | **GET** /api/catalog-seller-portal/category-tree | Get Category Tree
[**getbyid**](CategoryApi.md#getbyid) | **GET** /api/catalog-seller-portal/category-tree/categories/{categoryId} | Get Category by ID
[**updateCategoryTree**](CategoryApi.md#updateCategoryTree) | **PUT** /api/catalog-seller-portal/category-tree | Update Category Tree



## createCategory

> RootsInner createCategory(contentType, accept, createCategoryRequest)

Create Category

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Creates a new category.    ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;parentId\&quot;: \&quot;567\&quot;,    \&quot;Name\&quot;: \&quot;Beauty\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;value\&quot;: {      \&quot;id\&quot;: \&quot;1\&quot;,      \&quot;name\&quot;: \&quot;Beauty\&quot;,      \&quot;isActive\&quot;: false    },    \&quot;children\&quot;: [      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;2\&quot;,          \&quot;name\&quot;: \&quot;Perfumes\&quot;,          \&quot;isActive\&quot;: false        }      }    ]  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
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

let apiInstance = new CatalogApiSellerPortal.CategoryApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let createCategoryRequest = {"Name":"Beauty","parentId":"567"}; // CreateCategoryRequest | 
apiInstance.createCategory(contentType, accept, createCategoryRequest, (error, data, response) => {
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
 **createCategoryRequest** | [**CreateCategoryRequest**](CreateCategoryRequest.md)|  | 

### Return type

[**RootsInner**](RootsInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCategoryTree

> GetCategoryTree200Response getCategoryTree(contentType, accept, opts)

Get Category Tree

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about the category tree from the store.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;roots\&quot;: [          {              \&quot;value\&quot;: {                  \&quot;id\&quot;: \&quot;2\&quot;,                  \&quot;name\&quot;: \&quot;Departamento Artesanato\&quot;,                  \&quot;isActive\&quot;: true              },              \&quot;children\&quot;: [                  {                      \&quot;value\&quot;: {                          \&quot;id\&quot;: \&quot;3\&quot;,                          \&quot;name\&quot;: \&quot;Artesanato de Barro\&quot;,                          \&quot;isActive\&quot;: false                      },                      \&quot;children\&quot;: [                          {                              \&quot;value\&quot;: {                                  \&quot;id\&quot;: \&quot;4\&quot;,                                  \&quot;name\&quot;: \&quot;Artesanato de Barro Vermelho\&quot;,                                  \&quot;isActive\&quot;: false                              },                              \&quot;children\&quot;: []                          }                      ]                  }              ]          },          {              \&quot;value\&quot;: {                  \&quot;id\&quot;: \&quot;5\&quot;,                  \&quot;name\&quot;: \&quot;Perfumes\&quot;,                  \&quot;isActive\&quot;: false              },              \&quot;children\&quot;: [                  {                      \&quot;value\&quot;: {                          \&quot;id\&quot;: \&quot;6\&quot;,                          \&quot;name\&quot;: \&quot;Perfume Feminino\&quot;,                          \&quot;isActive\&quot;: false                      },                      \&quot;children\&quot;: []                  },                  {                      \&quot;value\&quot;: {                          \&quot;id\&quot;: \&quot;7\&quot;,                          \&quot;name\&quot;: \&quot;Perfume Masculino\&quot;,                          \&quot;isActive\&quot;: false,                          \&quot;displayOnMenu\&quot;: false,                          \&quot;score\&quot;: 0,                          \&quot;filterByBrand\&quot;: false,                          \&quot;isClickable\&quot;: false                      },                      \&quot;children\&quot;: []                  }              ]          }      ],      \&quot;createdAt\&quot;: \&quot;2021-08-16T20:57:13.070813Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-07-07T14:24:56.416337Z\&quot;  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
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

let apiInstance = new CatalogApiSellerPortal.CategoryApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'depth': 1 // Number | Category tree level.
};
apiInstance.getCategoryTree(contentType, accept, opts, (error, data, response) => {
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
 **depth** | **Number**| Category tree level. | [optional] 

### Return type

[**GetCategoryTree200Response**](GetCategoryTree200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getbyid

> Getbyid200Response getbyid(contentType, accept, categoryId)

Get Category by ID

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about a category by its ID.     ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;value\&quot;: {      \&quot;id\&quot;: \&quot;1\&quot;,      \&quot;name\&quot;: \&quot;sandboxintegracao\&quot;,      \&quot;isActive\&quot;: false    },    \&quot;children\&quot;: [      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;2\&quot;,          \&quot;name\&quot;: \&quot;Perfumes\&quot;,          \&quot;isActive\&quot;: false        }      }    ]  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
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

let apiInstance = new CatalogApiSellerPortal.CategoryApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let categoryId = "1"; // String | Category unique identifier number.
apiInstance.getbyid(contentType, accept, categoryId, (error, data, response) => {
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
 **categoryId** | **String**| Category unique identifier number. | 

### Return type

[**Getbyid200Response**](Getbyid200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCategoryTree

> updateCategoryTree(contentType, accept, updateCategoryTreeRequest)

Update Category Tree

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Updates the existing categories in the category tree.    ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;roots\&quot;: [      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;2\&quot;,          \&quot;name\&quot;: \&quot;Departamento Artesanato\&quot;,          \&quot;isActive\&quot;: true        },        \&quot;children\&quot;: [          {            \&quot;value\&quot;: {              \&quot;id\&quot;: \&quot;3\&quot;,              \&quot;name\&quot;: \&quot;Artesanato de Barro\&quot;,              \&quot;isActive\&quot;: false            },            \&quot;children\&quot;: [              {                \&quot;value\&quot;: {                  \&quot;id\&quot;: \&quot;4\&quot;,                  \&quot;name\&quot;: \&quot;Artesanato de Barro Vermelho\&quot;,                  \&quot;isActive\&quot;: false                },                \&quot;children\&quot;: []              }            ]          }        ]      },      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;5\&quot;,          \&quot;name\&quot;: \&quot;Perfumes\&quot;,          \&quot;isActive\&quot;: false        },        \&quot;children\&quot;: [          {            \&quot;value\&quot;: {              \&quot;id\&quot;: \&quot;6\&quot;,              \&quot;name\&quot;: \&quot;Perfume Feminino\&quot;,              \&quot;isActive\&quot;: false            },            \&quot;children\&quot;: []          },          {            \&quot;value\&quot;: {              \&quot;id\&quot;: \&quot;7\&quot;,              \&quot;name\&quot;: \&quot;Perfume Masculino\&quot;,              \&quot;isActive\&quot;: false,              \&quot;displayOnMenu\&quot;: false,              \&quot;score\&quot;: 0,              \&quot;filterByBrand\&quot;: false,              \&quot;isClickable\&quot;: false            },            \&quot;children\&quot;: []          }        ]      }    ]  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApiSellerPortal from 'catalog_api_seller_portal';
let defaultClient = CatalogApiSellerPortal.ApiClient.instance;
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

let apiInstance = new CatalogApiSellerPortal.CategoryApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let updateCategoryTreeRequest = {"roots":[{"children":[{"children":[{"children":[],"value":{"id":"4","isActive":false,"name":"Artesanato de Barro Vermelho"}}],"value":{"id":"3","isActive":false,"name":"Artesanato de Barro"}}],"value":{"id":"2","isActive":true,"name":"Departamento Artesanato"}},{"children":[{"children":[],"value":{"id":"6","isActive":false,"name":"Perfume Feminino"}},{"children":[],"value":{"id":"7","isActive":false,"name":"Perfume Masculino"}}],"value":{"id":"5","isActive":false,"name":"Perfumes"}}]}; // UpdateCategoryTreeRequest | OK
apiInstance.updateCategoryTree(contentType, accept, updateCategoryTreeRequest, (error, data, response) => {
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
 **updateCategoryTreeRequest** | [**UpdateCategoryTreeRequest**](UpdateCategoryTreeRequest.md)| OK | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

