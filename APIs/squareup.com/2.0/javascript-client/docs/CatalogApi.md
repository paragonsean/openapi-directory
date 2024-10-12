# SquareConnectApi.CatalogApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchDeleteCatalogObjects**](CatalogApi.md#batchDeleteCatalogObjects) | **POST** /v2/catalog/batch-delete | BatchDeleteCatalogObjects
[**batchRetrieveCatalogObjects**](CatalogApi.md#batchRetrieveCatalogObjects) | **POST** /v2/catalog/batch-retrieve | BatchRetrieveCatalogObjects
[**batchUpsertCatalogObjects**](CatalogApi.md#batchUpsertCatalogObjects) | **POST** /v2/catalog/batch-upsert | BatchUpsertCatalogObjects
[**catalogInfo**](CatalogApi.md#catalogInfo) | **GET** /v2/catalog/info | CatalogInfo
[**deleteCatalogObject**](CatalogApi.md#deleteCatalogObject) | **DELETE** /v2/catalog/object/{object_id} | DeleteCatalogObject
[**listCatalog**](CatalogApi.md#listCatalog) | **GET** /v2/catalog/list | ListCatalog
[**retrieveCatalogObject**](CatalogApi.md#retrieveCatalogObject) | **GET** /v2/catalog/object/{object_id} | RetrieveCatalogObject
[**searchCatalogItems**](CatalogApi.md#searchCatalogItems) | **POST** /v2/catalog/search-catalog-items | SearchCatalogItems
[**searchCatalogObjects**](CatalogApi.md#searchCatalogObjects) | **POST** /v2/catalog/search | SearchCatalogObjects
[**updateItemModifierLists**](CatalogApi.md#updateItemModifierLists) | **POST** /v2/catalog/update-item-modifier-lists | UpdateItemModifierLists
[**updateItemTaxes**](CatalogApi.md#updateItemTaxes) | **POST** /v2/catalog/update-item-taxes | UpdateItemTaxes
[**upsertCatalogObject**](CatalogApi.md#upsertCatalogObject) | **POST** /v2/catalog/object | UpsertCatalogObject



## batchDeleteCatalogObjects

> BatchDeleteCatalogObjectsResponse batchDeleteCatalogObjects(batchDeleteCatalogObjectsRequest)

BatchDeleteCatalogObjects

Deletes a set of [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)s based on the provided list of target IDs and returns a set of successfully deleted IDs in the response. Deletion is a cascading event such that all children of the targeted object are also deleted. For example, deleting a CatalogItem will also delete all of its [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) children.  &#x60;BatchDeleteCatalogObjects&#x60; succeeds even if only a portion of the targeted IDs can be deleted. The response will only include IDs that were actually deleted.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let batchDeleteCatalogObjectsRequest = new SquareConnectApi.BatchDeleteCatalogObjectsRequest(); // BatchDeleteCatalogObjectsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.batchDeleteCatalogObjects(batchDeleteCatalogObjectsRequest, (error, data, response) => {
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
 **batchDeleteCatalogObjectsRequest** | [**BatchDeleteCatalogObjectsRequest**](BatchDeleteCatalogObjectsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**BatchDeleteCatalogObjectsResponse**](BatchDeleteCatalogObjectsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchRetrieveCatalogObjects

> BatchRetrieveCatalogObjectsResponse batchRetrieveCatalogObjects(batchRetrieveCatalogObjectsRequest)

BatchRetrieveCatalogObjects

Returns a set of objects based on the provided ID. Each [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) returned in the set includes all of its child information including: all of its [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) objects, references to its [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects, and the ids of any [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to it.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let batchRetrieveCatalogObjectsRequest = new SquareConnectApi.BatchRetrieveCatalogObjectsRequest(); // BatchRetrieveCatalogObjectsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.batchRetrieveCatalogObjects(batchRetrieveCatalogObjectsRequest, (error, data, response) => {
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
 **batchRetrieveCatalogObjectsRequest** | [**BatchRetrieveCatalogObjectsRequest**](BatchRetrieveCatalogObjectsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**BatchRetrieveCatalogObjectsResponse**](BatchRetrieveCatalogObjectsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchUpsertCatalogObjects

> BatchUpsertCatalogObjectsResponse batchUpsertCatalogObjects(batchUpsertCatalogObjectsRequest)

BatchUpsertCatalogObjects

Creates or updates up to 10,000 target objects based on the provided list of objects. The target objects are grouped into batches and each batch is inserted/updated in an all-or-nothing manner. If an object within a batch is malformed in some way, or violates a database constraint, the entire batch containing that item will be disregarded. However, other batches in the same request may still succeed. Each batch may contain up to 1,000 objects, and batches will be processed in order as long as the total object count for the request (items, variations, modifier lists, discounts, and taxes) is no more than 10,000.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let batchUpsertCatalogObjectsRequest = new SquareConnectApi.BatchUpsertCatalogObjectsRequest(); // BatchUpsertCatalogObjectsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.batchUpsertCatalogObjects(batchUpsertCatalogObjectsRequest, (error, data, response) => {
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
 **batchUpsertCatalogObjectsRequest** | [**BatchUpsertCatalogObjectsRequest**](BatchUpsertCatalogObjectsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**BatchUpsertCatalogObjectsResponse**](BatchUpsertCatalogObjectsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## catalogInfo

> CatalogInfoResponse catalogInfo()

CatalogInfo

Retrieves information about the Square Catalog API, such as batch size limits that can be used by the &#x60;BatchUpsertCatalogObjects&#x60; endpoint.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
apiInstance.catalogInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CatalogInfoResponse**](CatalogInfoResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCatalogObject

> DeleteCatalogObjectResponse deleteCatalogObject(objectId)

DeleteCatalogObject

Deletes a single [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) based on the provided ID and returns the set of successfully deleted IDs in the response. Deletion is a cascading event such that all children of the targeted object are also deleted. For example, deleting a [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) will also delete all of its [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) children.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let objectId = "objectId_example"; // String | The ID of the catalog object to be deleted. When an object is deleted, other objects in the graph that depend on that object will be deleted as well (for example, deleting a catalog item will delete its catalog item variations).
apiInstance.deleteCatalogObject(objectId, (error, data, response) => {
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
 **objectId** | **String**| The ID of the catalog object to be deleted. When an object is deleted, other objects in the graph that depend on that object will be deleted as well (for example, deleting a catalog item will delete its catalog item variations). | 

### Return type

[**DeleteCatalogObjectResponse**](DeleteCatalogObjectResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCatalog

> ListCatalogResponse listCatalog(opts)

ListCatalog

Returns a list of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s that includes all objects of a set of desired types (for example, all [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) and [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects) in the catalog. The &#x60;types&#x60; parameter is specified as a comma-separated list of valid [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) types: &#x60;ITEM&#x60;, &#x60;ITEM_VARIATION&#x60;, &#x60;MODIFIER&#x60;, &#x60;MODIFIER_LIST&#x60;, &#x60;CATEGORY&#x60;, &#x60;DISCOUNT&#x60;, &#x60;TAX&#x60;, &#x60;IMAGE&#x60;.  __Important:__ ListCatalog does not return deleted catalog items. To retrieve deleted catalog items, use [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects) and set the &#x60;include_deleted_objects&#x60; attribute value to &#x60;true&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let opts = {
  'cursor': "cursor_example", // String | The pagination cursor returned in the previous response. Leave unset for an initial request. The page size is currently set to be 100. See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
  'types': "types_example", // String | An optional case-insensitive, comma-separated list of object types to retrieve.  The valid values are defined in the [CatalogObjectType](https://developer.squareup.com/reference/square_2021-08-18/enums/CatalogObjectType) enum, including `ITEM`, `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`, `MODIFIER`, `MODIFIER_LIST`, or `IMAGE`.  If this is unspecified, the operation returns objects of all the types at the version of the Square API used to make the request.
  'catalogVersion': 789 // Number | The specific version of the catalog objects to be included in the response.  This allows you to retrieve historical versions of objects. The specified version value is matched against the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s' `version` attribute.
};
apiInstance.listCatalog(opts, (error, data, response) => {
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
 **cursor** | **String**| The pagination cursor returned in the previous response. Leave unset for an initial request. The page size is currently set to be 100. See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. | [optional] 
 **types** | **String**| An optional case-insensitive, comma-separated list of object types to retrieve.  The valid values are defined in the [CatalogObjectType](https://developer.squareup.com/reference/square_2021-08-18/enums/CatalogObjectType) enum, including &#x60;ITEM&#x60;, &#x60;ITEM_VARIATION&#x60;, &#x60;CATEGORY&#x60;, &#x60;DISCOUNT&#x60;, &#x60;TAX&#x60;, &#x60;MODIFIER&#x60;, &#x60;MODIFIER_LIST&#x60;, or &#x60;IMAGE&#x60;.  If this is unspecified, the operation returns objects of all the types at the version of the Square API used to make the request. | [optional] 
 **catalogVersion** | **Number**| The specific version of the catalog objects to be included in the response.  This allows you to retrieve historical versions of objects. The specified version value is matched against the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s&#39; &#x60;version&#x60; attribute. | [optional] 

### Return type

[**ListCatalogResponse**](ListCatalogResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveCatalogObject

> RetrieveCatalogObjectResponse retrieveCatalogObject(objectId, opts)

RetrieveCatalogObject

Returns a single [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) as a [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) based on the provided ID. The returned object includes all of the relevant [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) information including: [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) children, references to its [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects, and the ids of any [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to it.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let objectId = "objectId_example"; // String | The object ID of any type of catalog objects to be retrieved.
let opts = {
  'includeRelatedObjects': true, // Boolean | If `true`, the response will include additional objects that are related to the requested object, as follows:  If the `object` field of the response contains a `CatalogItem`, its associated `CatalogCategory`, `CatalogTax`, `CatalogImage` and `CatalogModifierList` objects will be returned in the `related_objects` field of the response. If the `object` field of the response contains a `CatalogItemVariation`, its parent `CatalogItem` will be returned in the `related_objects` field of the response.  Default value: `false`
  'catalogVersion': 789 // Number | Requests objects as of a specific version of the catalog. This allows you to retrieve historical versions of objects. The value to retrieve a specific version of an object can be found in the version field of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s.
};
apiInstance.retrieveCatalogObject(objectId, opts, (error, data, response) => {
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
 **objectId** | **String**| The object ID of any type of catalog objects to be retrieved. | 
 **includeRelatedObjects** | **Boolean**| If &#x60;true&#x60;, the response will include additional objects that are related to the requested object, as follows:  If the &#x60;object&#x60; field of the response contains a &#x60;CatalogItem&#x60;, its associated &#x60;CatalogCategory&#x60;, &#x60;CatalogTax&#x60;, &#x60;CatalogImage&#x60; and &#x60;CatalogModifierList&#x60; objects will be returned in the &#x60;related_objects&#x60; field of the response. If the &#x60;object&#x60; field of the response contains a &#x60;CatalogItemVariation&#x60;, its parent &#x60;CatalogItem&#x60; will be returned in the &#x60;related_objects&#x60; field of the response.  Default value: &#x60;false&#x60; | [optional] 
 **catalogVersion** | **Number**| Requests objects as of a specific version of the catalog. This allows you to retrieve historical versions of objects. The value to retrieve a specific version of an object can be found in the version field of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s. | [optional] 

### Return type

[**RetrieveCatalogObjectResponse**](RetrieveCatalogObjectResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchCatalogItems

> SearchCatalogItemsResponse searchCatalogItems(searchCatalogItemsRequest)

SearchCatalogItems

Searches for catalog items or item variations by matching supported search attribute values, including custom attribute values, against one or more of the specified query expressions.  This (&#x60;SearchCatalogItems&#x60;) endpoint differs from the [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects) endpoint in the following aspects:  - &#x60;SearchCatalogItems&#x60; can only search for items or item variations, whereas &#x60;SearchCatalogObjects&#x60; can search for any type of catalog objects. - &#x60;SearchCatalogItems&#x60; supports the custom attribute query filters to return items or item variations that contain custom attribute values, where &#x60;SearchCatalogObjects&#x60; does not. - &#x60;SearchCatalogItems&#x60; does not support the &#x60;include_deleted_objects&#x60; filter to search for deleted items or item variations, whereas &#x60;SearchCatalogObjects&#x60; does. - The both endpoints use different call conventions, including the query filter formats.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let searchCatalogItemsRequest = new SquareConnectApi.SearchCatalogItemsRequest(); // SearchCatalogItemsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchCatalogItems(searchCatalogItemsRequest, (error, data, response) => {
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
 **searchCatalogItemsRequest** | [**SearchCatalogItemsRequest**](SearchCatalogItemsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchCatalogItemsResponse**](SearchCatalogItemsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchCatalogObjects

> SearchCatalogObjectsResponse searchCatalogObjects(searchCatalogObjectsRequest)

SearchCatalogObjects

Searches for [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) of any type by matching supported search attribute values, excluding custom attribute values on items or item variations, against one or more of the specified query expressions.  This (&#x60;SearchCatalogObjects&#x60;) endpoint differs from the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items) endpoint in the following aspects:  - &#x60;SearchCatalogItems&#x60; can only search for items or item variations, whereas &#x60;SearchCatalogObjects&#x60; can search for any type of catalog objects. - &#x60;SearchCatalogItems&#x60; supports the custom attribute query filters to return items or item variations that contain custom attribute values, where &#x60;SearchCatalogObjects&#x60; does not. - &#x60;SearchCatalogItems&#x60; does not support the &#x60;include_deleted_objects&#x60; filter to search for deleted items or item variations, whereas &#x60;SearchCatalogObjects&#x60; does. - The both endpoints have different call conventions, including the query filter formats.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let searchCatalogObjectsRequest = new SquareConnectApi.SearchCatalogObjectsRequest(); // SearchCatalogObjectsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchCatalogObjects(searchCatalogObjectsRequest, (error, data, response) => {
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
 **searchCatalogObjectsRequest** | [**SearchCatalogObjectsRequest**](SearchCatalogObjectsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchCatalogObjectsResponse**](SearchCatalogObjectsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateItemModifierLists

> UpdateItemModifierListsResponse updateItemModifierLists(updateItemModifierListsRequest)

UpdateItemModifierLists

Updates the [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects that apply to the targeted [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) without having to perform an upsert on the entire item.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let updateItemModifierListsRequest = new SquareConnectApi.UpdateItemModifierListsRequest(); // UpdateItemModifierListsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateItemModifierLists(updateItemModifierListsRequest, (error, data, response) => {
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
 **updateItemModifierListsRequest** | [**UpdateItemModifierListsRequest**](UpdateItemModifierListsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateItemModifierListsResponse**](UpdateItemModifierListsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateItemTaxes

> UpdateItemTaxesResponse updateItemTaxes(updateItemTaxesRequest)

UpdateItemTaxes

Updates the [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to the targeted [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) without having to perform an upsert on the entire item.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let updateItemTaxesRequest = new SquareConnectApi.UpdateItemTaxesRequest(); // UpdateItemTaxesRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.updateItemTaxes(updateItemTaxesRequest, (error, data, response) => {
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
 **updateItemTaxesRequest** | [**UpdateItemTaxesRequest**](UpdateItemTaxesRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpdateItemTaxesResponse**](UpdateItemTaxesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upsertCatalogObject

> UpsertCatalogObjectResponse upsertCatalogObject(upsertCatalogObjectRequest)

UpsertCatalogObject

Creates or updates the target [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CatalogApi();
let upsertCatalogObjectRequest = new SquareConnectApi.UpsertCatalogObjectRequest(); // UpsertCatalogObjectRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.upsertCatalogObject(upsertCatalogObjectRequest, (error, data, response) => {
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
 **upsertCatalogObjectRequest** | [**UpsertCatalogObjectRequest**](UpsertCatalogObjectRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UpsertCatalogObjectResponse**](UpsertCatalogObjectResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

