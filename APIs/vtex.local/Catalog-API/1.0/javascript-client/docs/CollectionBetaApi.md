# CatalogApi.CollectionBetaApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETAllCollections**](CollectionBetaApi.md#gETAllCollections) | **GET** /api/catalog_system/pvt/collection/search | Get All Collections
[**gETAllInactiveCollections**](CollectionBetaApi.md#gETAllInactiveCollections) | **GET** /api/catalog/pvt/collection/inactive | Get All Inactive Collections
[**gETCollectionsbyseachterms**](CollectionBetaApi.md#gETCollectionsbyseachterms) | **GET** /api/catalog_system/pvt/collection/search/{searchTerms} | Get Collections by search terms
[**gETImportfileexample**](CollectionBetaApi.md#gETImportfileexample) | **GET** /api/catalog/pvt/collection/stockkeepingunit/importfileexample | Import Collection file example
[**gETProductsfromacollection**](CollectionBetaApi.md#gETProductsfromacollection) | **GET** /api/catalog/pvt/collection/{collectionId}/products | Get products from a collection
[**pOSTAddproductsbyimportfile**](CollectionBetaApi.md#pOSTAddproductsbyimportfile) | **POST** /api/catalog/pvt/collection/{collectionId}/stockkeepingunit/importinsert | Add products to Collection by imported file
[**pOSTCreateCollection**](CollectionBetaApi.md#pOSTCreateCollection) | **POST** /api/catalog/pvt/collection/ | Create Collection
[**pOSTRemoveproductsbyimportfile**](CollectionBetaApi.md#pOSTRemoveproductsbyimportfile) | **POST** /api/catalog/pvt/collection/{collectionId}/stockkeepingunit/importexclude | Remove products from Collection by imported file



## gETAllCollections

> gETAllCollections(contentType, accept, page, pageSize, orderByAsc)

Get All Collections

Retrieves a list of all collections matching a filter.

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

let apiInstance = new CatalogApi.CollectionBetaApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let page = 2; // Number | Page number.
let pageSize = 15; // Number | Number of the items of the page.
let orderByAsc = true; // Boolean | Defines if the items of the page are in ascending order.
apiInstance.gETAllCollections(contentType, accept, page, pageSize, orderByAsc, (error, data, response) => {
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
 **page** | **Number**| Page number. | 
 **pageSize** | **Number**| Number of the items of the page. | 
 **orderByAsc** | **Boolean**| Defines if the items of the page are in ascending order. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## gETAllInactiveCollections

> gETAllInactiveCollections(contentType, accept)

Get All Inactive Collections

Retrieves a list of Collection IDs of the inactive Collections.

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

let apiInstance = new CatalogApi.CollectionBetaApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.gETAllInactiveCollections(contentType, accept, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## gETCollectionsbyseachterms

> gETCollectionsbyseachterms(contentType, accept, searchTerms, opts)

Get Collections by search terms

Retrieves a list of collections matching a filter.

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

let apiInstance = new CatalogApi.CollectionBetaApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let searchTerms = "costume"; // String | String that will search for a collection related to it.
let opts = {
  'page': 2, // Number | Page number.
  'pageSize': 15, // Number | Number of the items of the page.
  'orderByAsc': true // Boolean | Defines if the items of the page are in ascending order.
};
apiInstance.gETCollectionsbyseachterms(contentType, accept, searchTerms, opts, (error, data, response) => {
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
 **searchTerms** | **String**| String that will search for a collection related to it. | 
 **page** | **Number**| Page number. | [optional] 
 **pageSize** | **Number**| Number of the items of the page. | [optional] 
 **orderByAsc** | **Boolean**| Defines if the items of the page are in ascending order. | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## gETImportfileexample

> gETImportfileexample(contentType, accept)

Import Collection file example

Imports a sample of the imported XLS file. You need to save the response file to your device.

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

let apiInstance = new CatalogApi.CollectionBetaApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.gETImportfileexample(contentType, accept, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## gETProductsfromacollection

> gETProductsfromacollection(contentType, accept, collectionId, opts)

Get products from a collection

Retrieves information about the products from a collection.

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

let apiInstance = new CatalogApi.CollectionBetaApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let collectionId = 1; // Number | Collection's unique identifier.
let opts = {
  'page': 2, // Number | Page number.
  'pageSize': 15, // Number | Number of the items of the page.
  'filter': "Pre launch", // String | Filter used to refine the Collection's products.
  'active': true, // Boolean | Defines if the status of the product is active or not.
  'visible': true, // Boolean | Defines if the product is visible on the store or not.
  'categoryId': 12, // Number | Product's Category unique identifier.
  'brandId': 3, // Number | Product's Brand unique identifier.
  'supplierId': 1, // Number | Product's Supplier unique identifier.
  'salesChannelId': 1, // Number | Product's Trade Policy unique identifier.
  'releaseFrom': "2069-11-26T15:23:00", // String | Product past release date.
  'releaseTo': "2069-11-26T15:23:00", // String | Product future release date.
  'specificationProduct': "M", // String | Product Specification Field Value. You must also fill in `SpecificationFieldId` to use this parameter.
  'specificationFieldId': 40 // Number | Product Specification Field unique identifier.
};
apiInstance.gETProductsfromacollection(contentType, accept, collectionId, opts, (error, data, response) => {
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
 **collectionId** | **Number**| Collection&#39;s unique identifier. | 
 **page** | **Number**| Page number. | [optional] 
 **pageSize** | **Number**| Number of the items of the page. | [optional] 
 **filter** | **String**| Filter used to refine the Collection&#39;s products. | [optional] 
 **active** | **Boolean**| Defines if the status of the product is active or not. | [optional] 
 **visible** | **Boolean**| Defines if the product is visible on the store or not. | [optional] 
 **categoryId** | **Number**| Product&#39;s Category unique identifier. | [optional] 
 **brandId** | **Number**| Product&#39;s Brand unique identifier. | [optional] 
 **supplierId** | **Number**| Product&#39;s Supplier unique identifier. | [optional] 
 **salesChannelId** | **Number**| Product&#39;s Trade Policy unique identifier. | [optional] 
 **releaseFrom** | **String**| Product past release date. | [optional] 
 **releaseTo** | **String**| Product future release date. | [optional] 
 **specificationProduct** | **String**| Product Specification Field Value. You must also fill in &#x60;SpecificationFieldId&#x60; to use this parameter. | [optional] 
 **specificationFieldId** | **Number**| Product Specification Field unique identifier. | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## pOSTAddproductsbyimportfile

> pOSTAddproductsbyimportfile(contentType, accept, collectionId, opts)

Add products to Collection by imported file

Adds products to a collection from the request body file. The file must be an imported template.

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

let apiInstance = new CatalogApi.CollectionBetaApi();
let contentType = "'multipart/form-data'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let collectionId = 1; // Number | Collection's unique identifier.
let opts = {
  'file': null // Object | XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint.
};
apiInstance.pOSTAddproductsbyimportfile(contentType, accept, collectionId, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;multipart/form-data&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **collectionId** | **Number**| Collection&#39;s unique identifier. | 
 **file** | [**Object**](Object.md)| XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint. | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## pOSTCreateCollection

> pOSTCreateCollection(contentType, accept, requestBody)

Create Collection

Creates a new collection.

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

let apiInstance = new CatalogApi.CollectionBetaApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let requestBody = new CatalogApi.RequestBody(); // RequestBody | 
apiInstance.pOSTCreateCollection(contentType, accept, requestBody, (error, data, response) => {
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
 **requestBody** | [**RequestBody**](RequestBody.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## pOSTRemoveproductsbyimportfile

> pOSTRemoveproductsbyimportfile(contentType, accept, collectionId, opts)

Remove products from Collection by imported file

Removes products from a collection from the request body file. The file must be an imported template.

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

let apiInstance = new CatalogApi.CollectionBetaApi();
let contentType = "'multipart/form-data'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let collectionId = 1; // Number | Collection's unique identifier.
let opts = {
  'file': null // Object | XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint.
};
apiInstance.pOSTRemoveproductsbyimportfile(contentType, accept, collectionId, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;multipart/form-data&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **collectionId** | **Number**| Collection&#39;s unique identifier. | 
 **file** | [**Object**](Object.md)| XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint. | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined

