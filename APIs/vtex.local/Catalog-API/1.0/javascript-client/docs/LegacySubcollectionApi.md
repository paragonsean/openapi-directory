# CatalogApi.LegacySubcollectionApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtCollectionCollectionIdPositionPost**](LegacySubcollectionApi.md#apiCatalogPvtCollectionCollectionIdPositionPost) | **POST** /api/catalog/pvt/collection/{collectionId}/position | Reposition SKU on the Subcollection
[**apiCatalogPvtCollectionCollectionIdSubcollectionGet**](LegacySubcollectionApi.md#apiCatalogPvtCollectionCollectionIdSubcollectionGet) | **GET** /api/catalog/pvt/collection/{collectionId}/subcollection | Get Subcollection by Collection ID
[**apiCatalogPvtSubcollectionPost**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionPost) | **POST** /api/catalog/pvt/subcollection | Create Subcollection
[**apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/brand/{brandId} | Delete Brand from Subcollection
[**apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/brand/{categoryId} | Delete Category from Subcollection
[**apiCatalogPvtSubcollectionSubCollectionIdBrandPost**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/brand | Associate Brand to Subcollection
[**apiCatalogPvtSubcollectionSubCollectionIdCategoryPost**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdCategoryPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/category | Associate Category to Subcollection
[**apiCatalogPvtSubcollectionSubCollectionIdDelete**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId} | Delete Subcollection
[**apiCatalogPvtSubcollectionSubCollectionIdGet**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdGet) | **GET** /api/catalog/pvt/subcollection/{subCollectionId} | Get Subcollection
[**apiCatalogPvtSubcollectionSubCollectionIdPut**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdPut) | **PUT** /api/catalog/pvt/subcollection/{subCollectionId} | Update Subcollection
[**apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit | Add SKU to Subcollection
[**apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit/{skuId} | Delete SKU from Subcollection



## apiCatalogPvtCollectionCollectionIdPositionPost

> apiCatalogPvtCollectionCollectionIdPositionPost(contentType, accept, collectionId, opts)

Reposition SKU on the Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Edits the position of an SKU that already exists in the Subcollection,  which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {       \&quot;skuId\&quot;: 1,       \&quot;position\&quot;: 1,       \&quot;subCollectionId\&quot;: 17  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let collectionId = 151; // Number | Collection’s unique numerical identifier.
let opts = {
  'apiCatalogPvtCollectionCollectionIdPositionPostRequest': new CatalogApi.ApiCatalogPvtCollectionCollectionIdPositionPostRequest() // ApiCatalogPvtCollectionCollectionIdPositionPostRequest | 
};
apiInstance.apiCatalogPvtCollectionCollectionIdPositionPost(contentType, accept, collectionId, opts, (error, data, response) => {
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
 **collectionId** | **Number**| Collection’s unique numerical identifier. | 
 **apiCatalogPvtCollectionCollectionIdPositionPostRequest** | [**ApiCatalogPvtCollectionCollectionIdPositionPostRequest**](ApiCatalogPvtCollectionCollectionIdPositionPostRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiCatalogPvtCollectionCollectionIdSubcollectionGet

> [ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner] apiCatalogPvtCollectionCollectionIdSubcollectionGet(contentType, accept, collectionId)

Get Subcollection by Collection ID

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves all Subcollections given a Collection ID. A Subcollection is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 12,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Subcollection\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: true      },      {          \&quot;Id\&quot;: 13,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Test\&quot;,          \&quot;Type\&quot;: \&quot;Exclusive\&quot;,          \&quot;PreSale\&quot;: true,          \&quot;Release\&quot;: false      },      {          \&quot;Id\&quot;: 14,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;asdfghj\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: false      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let collectionId = 151; // Number | Collection’s unique numerical identifier.
apiInstance.apiCatalogPvtCollectionCollectionIdSubcollectionGet(contentType, accept, collectionId, (error, data, response) => {
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
 **collectionId** | **Number**| Collection’s unique numerical identifier. | 

### Return type

[**[ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner]**](ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtSubcollectionPost

> ApiCatalogPvtSubcollectionPost200Response apiCatalogPvtSubcollectionPost(contentType, accept, opts)

Create Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection. A Subcollection can be either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used).  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'apiCatalogPvtSubcollectionPostRequest': new CatalogApi.ApiCatalogPvtSubcollectionPostRequest() // ApiCatalogPvtSubcollectionPostRequest | 
};
apiInstance.apiCatalogPvtSubcollectionPost(contentType, accept, opts, (error, data, response) => {
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
 **apiCatalogPvtSubcollectionPostRequest** | [**ApiCatalogPvtSubcollectionPostRequest**](ApiCatalogPvtSubcollectionPostRequest.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSubcollectionPost200Response**](ApiCatalogPvtSubcollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete

> apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(contentType, accept, subCollectionId, brandId)

Delete Brand from Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Brand from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let subCollectionId = 1; // Number | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
let brandId = 1; // Number | Brand’s unique numerical identifier.
apiInstance.apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(contentType, accept, subCollectionId, brandId, (error, data, response) => {
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
 **subCollectionId** | **Number**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | 
 **brandId** | **Number**| Brand’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete

> apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(contentType, accept, subCollectionId, categoryId)

Delete Category from Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Category from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let subCollectionId = 1; // Number | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
let categoryId = 1; // Number | Category’s unique numerical identifier.
apiInstance.apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(contentType, accept, subCollectionId, categoryId, (error, data, response) => {
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
 **subCollectionId** | **Number**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | 
 **categoryId** | **Number**| Category’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtSubcollectionSubCollectionIdBrandPost

> ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response apiCatalogPvtSubcollectionSubCollectionIdBrandPost(contentType, accept, subCollectionId, opts)

Associate Brand to Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Brand to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let subCollectionId = 1; // Number | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
let opts = {
  'requestBody10': new CatalogApi.RequestBody10() // RequestBody10 | 
};
apiInstance.apiCatalogPvtSubcollectionSubCollectionIdBrandPost(contentType, accept, subCollectionId, opts, (error, data, response) => {
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
 **subCollectionId** | **Number**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | 
 **requestBody10** | [**RequestBody10**](RequestBody10.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response**](ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSubcollectionSubCollectionIdCategoryPost

> ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(contentType, accept, subCollectionId, opts)

Associate Category to Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Category to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let subCollectionId = 1; // Number | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
let opts = {
  'requestBody11': new CatalogApi.RequestBody11() // RequestBody11 | 
};
apiInstance.apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(contentType, accept, subCollectionId, opts, (error, data, response) => {
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
 **subCollectionId** | **Number**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | 
 **requestBody11** | [**RequestBody11**](RequestBody11.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response**](ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSubcollectionSubCollectionIdDelete

> apiCatalogPvtSubcollectionSubCollectionIdDelete(contentType, accept, subCollectionId)

Delete Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let subCollectionId = 1; // Number | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
apiInstance.apiCatalogPvtSubcollectionSubCollectionIdDelete(contentType, accept, subCollectionId, (error, data, response) => {
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
 **subCollectionId** | **Number**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtSubcollectionSubCollectionIdGet

> ApiCatalogPvtSubcollectionPost200Response apiCatalogPvtSubcollectionSubCollectionIdGet(contentType, accept, subCollectionId)

Get Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves information about a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let subCollectionId = 17; // Number | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
apiInstance.apiCatalogPvtSubcollectionSubCollectionIdGet(contentType, accept, subCollectionId, (error, data, response) => {
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
 **subCollectionId** | **Number**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | 

### Return type

[**ApiCatalogPvtSubcollectionPost200Response**](ApiCatalogPvtSubcollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtSubcollectionSubCollectionIdPut

> ApiCatalogPvtSubcollectionPost200Response apiCatalogPvtSubcollectionSubCollectionIdPut(contentType, accept, subCollectionId, opts)

Update Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.    ## Request or response body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let subCollectionId = 17; // Number | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
let opts = {
  'apiCatalogPvtSubcollectionSubCollectionIdPutRequest': new CatalogApi.ApiCatalogPvtSubcollectionSubCollectionIdPutRequest() // ApiCatalogPvtSubcollectionSubCollectionIdPutRequest | 
};
apiInstance.apiCatalogPvtSubcollectionSubCollectionIdPut(contentType, accept, subCollectionId, opts, (error, data, response) => {
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
 **subCollectionId** | **Number**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | 
 **apiCatalogPvtSubcollectionSubCollectionIdPutRequest** | [**ApiCatalogPvtSubcollectionSubCollectionIdPutRequest**](ApiCatalogPvtSubcollectionSubCollectionIdPutRequest.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSubcollectionPost200Response**](ApiCatalogPvtSubcollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost

> ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(contentType, accept, subCollectionId, opts)

Add SKU to Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single SKU to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let subCollectionId = 1; // Number | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
let opts = {
  'requestBody12': new CatalogApi.RequestBody12() // RequestBody12 | 
};
apiInstance.apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(contentType, accept, subCollectionId, opts, (error, data, response) => {
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
 **subCollectionId** | **Number**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | 
 **requestBody12** | [**RequestBody12**](RequestBody12.md)|  | [optional] 

### Return type

[**ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response**](ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete

> apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(contentType, accept, subCollectionId, skuId)

Delete SKU from Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes an SKU from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

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

let apiInstance = new CatalogApi.LegacySubcollectionApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let subCollectionId = 1; // Number | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
let skuId = 1; // Number | SKU’s unique numerical identifier.
apiInstance.apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(contentType, accept, subCollectionId, skuId, (error, data, response) => {
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
 **subCollectionId** | **Number**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | 
 **skuId** | **Number**| SKU’s unique numerical identifier. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

