# ShutterstockApiExplorer.CatalogApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addToCollection**](CatalogApi.md#addToCollection) | **POST** /v2/catalog/collections/{collection_id}/items | Add items to catalog collections
[**createCollection**](CatalogApi.md#createCollection) | **POST** /v2/catalog/collections | Create catalog collections
[**deleteCollection**](CatalogApi.md#deleteCollection) | **DELETE** /v2/catalog/collections/{collection_id} | Delete catalog collections
[**deleteFromCollection**](CatalogApi.md#deleteFromCollection) | **DELETE** /v2/catalog/collections/{collection_id}/items | Remove items from catalog collection
[**getCollections**](CatalogApi.md#getCollections) | **GET** /v2/catalog/collections | List catalog collections
[**searchCatalog**](CatalogApi.md#searchCatalog) | **GET** /v2/catalog/search | Search catalogs for assets
[**updateCollection**](CatalogApi.md#updateCollection) | **PATCH** /v2/catalog/collections/{collection_id} | Update collection metadata



## addToCollection

> CatalogCollection addToCollection(collectionId, createCatalogCollectionItems)

Add items to catalog collections

This endpoint adds assets to a catalog collection. It also automatically adds the assets to the user&#39;s account&#39;s catalog.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.CatalogApi();
let collectionId = "126351028"; // String | The ID of the collection to add assets to
let createCatalogCollectionItems = {"$ref":"#/components/schemas/CreateCatalogCollectionItems/example"}; // CreateCatalogCollectionItems | Collection item attributes to add to collection
apiInstance.addToCollection(collectionId, createCatalogCollectionItems, (error, data, response) => {
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
 **collectionId** | **String**| The ID of the collection to add assets to | 
 **createCatalogCollectionItems** | [**CreateCatalogCollectionItems**](CreateCatalogCollectionItems.md)| Collection item attributes to add to collection | 

### Return type

[**CatalogCollection**](CatalogCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCollection

> CatalogCollection createCollection(createCatalogCollection)

Create catalog collections

This endpoint creates a catalog collection and optionally adds assets. To add assets to the collection later, use &#x60;PATCH /v2/catalog/collections/{collection_id}/items&#x60;.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.CatalogApi();
let createCatalogCollection = {"$ref":"#/components/schemas/CreateCatalogCollection/example"}; // CreateCatalogCollection | Create a catalog collection and, optionally, add items.
apiInstance.createCollection(createCatalogCollection, (error, data, response) => {
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
 **createCatalogCollection** | [**CreateCatalogCollection**](CreateCatalogCollection.md)| Create a catalog collection and, optionally, add items. | 

### Return type

[**CatalogCollection**](CatalogCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCollection

> deleteCollection(collectionId)

Delete catalog collections

This endpoint deletes a catalog collection. It does not remove the assets from the user&#39;s account&#39;s catalog.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.CatalogApi();
let collectionId = "126351028"; // String | The ID of the collection to delete
apiInstance.deleteCollection(collectionId, (error, data, response) => {
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
 **collectionId** | **String**| The ID of the collection to delete | 

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteFromCollection

> CatalogCollection deleteFromCollection(collectionId, removeCatalogCollectionItems)

Remove items from catalog collection

This endpoint removes assets from a catalog collection. It does not remove the assets from the user&#39;s account&#39;s catalog.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.CatalogApi();
let collectionId = "126351028"; // String | The ID of the collection to remove assets from
let removeCatalogCollectionItems = {"$ref":"#/components/schemas/RemoveCatalogCollectionItems/example"}; // RemoveCatalogCollectionItems | Items to remove from the collection
apiInstance.deleteFromCollection(collectionId, removeCatalogCollectionItems, (error, data, response) => {
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
 **collectionId** | **String**| The ID of the collection to remove assets from | 
 **removeCatalogCollectionItems** | [**RemoveCatalogCollectionItems**](RemoveCatalogCollectionItems.md)| Items to remove from the collection | 

### Return type

[**CatalogCollection**](CatalogCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCollections

> CatalogCollectionDataList getCollections(opts)

List catalog collections

This endpoint returns a list of catalog collections.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.CatalogApi();
let opts = {
  'page': 1, // Number | Page number
  'perPage': 20, // Number | Number of results per page
  'sort': "'newest'", // String | Sort by
  'shared': false // Boolean | Set to true to omit collections that you own and return only collections  that are shared with you
};
apiInstance.getCollections(opts, (error, data, response) => {
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
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **sort** | **String**| Sort by | [optional] [default to &#39;newest&#39;]
 **shared** | **Boolean**| Set to true to omit collections that you own and return only collections  that are shared with you | [optional] [default to false]

### Return type

[**CatalogCollectionDataList**](CatalogCollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchCatalog

> CatalogCollectionItemDataList searchCatalog(opts)

Search catalogs for assets

This endpoint searches for assets in the account&#39;s catalog. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.CatalogApi();
let opts = {
  'sort': "'newest'", // String | Sort by
  'page': 1, // Number | Page number
  'perPage': 50, // Number | Number of results per page
  'query': "dogs on the beach", // String | One or more search terms separated by spaces
  'collectionId': ["null"], // [String] | Filter by collection id
  'assetType': ["null"] // [String] | Filter by asset type
};
apiInstance.searchCatalog(opts, (error, data, response) => {
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
 **sort** | **String**| Sort by | [optional] [default to &#39;newest&#39;]
 **page** | **Number**| Page number | [optional] [default to 1]
 **perPage** | **Number**| Number of results per page | [optional] [default to 20]
 **query** | **String**| One or more search terms separated by spaces | [optional] 
 **collectionId** | [**[String]**](String.md)| Filter by collection id | [optional] 
 **assetType** | [**[String]**](String.md)| Filter by asset type | [optional] 

### Return type

[**CatalogCollectionItemDataList**](CatalogCollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCollection

> CatalogCollection updateCollection(collectionId, updateCatalogCollection)

Update collection metadata

This endpoint updates the metadata of a catalog collection.

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';
let defaultClient = ShutterstockApiExplorer.ApiClient.instance;
// Configure OAuth2 access token for authorization: customer_accessCode
let customer_accessCode = defaultClient.authentications['customer_accessCode'];
customer_accessCode.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ShutterstockApiExplorer.CatalogApi();
let collectionId = "126351028"; // String | ID of collection that needs to be modified
let updateCatalogCollection = {"$ref":"#/components/schemas/UpdateCatalogCollection/example"}; // UpdateCatalogCollection | Collections Metadata to update
apiInstance.updateCollection(collectionId, updateCatalogCollection, (error, data, response) => {
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
 **collectionId** | **String**| ID of collection that needs to be modified | 
 **updateCatalogCollection** | [**UpdateCatalogCollection**](UpdateCatalogCollection.md)| Collections Metadata to update | 

### Return type

[**CatalogCollection**](CatalogCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

