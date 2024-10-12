# 1000000RecipeAndGroceryListApiV2.CollectionApi

All URIs are relative to *https://api2.bigoven.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collectionCollections**](CollectionApi.md#collectionCollections) | **GET** /collections | Get the list of current, seasonal recipe collections. From here, you can use the /collection/{id} endpoint to retrieve the recipes in those collections.
[**collectionGetCollection**](CollectionApi.md#collectionGetCollection) | **GET** /collection/{id} | Gets a recipe collection. A recipe collection is a curated set of recipes.
[**collectionGetCollectionMeta**](CollectionApi.md#collectionGetCollectionMeta) | **GET** /collection/{id}/meta | Gets a recipe collection metadata. A recipe collection is a curated set of recipes.



## collectionCollections

> [BigOvenModelAPI2CollectionInfo] collectionCollections(opts)

Get the list of current, seasonal recipe collections. From here, you can use the /collection/{id} endpoint to retrieve the recipes in those collections.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.CollectionApi();
let opts = {
  'test': "test_example" // String | 
};
apiInstance.collectionCollections(opts, (error, data, response) => {
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
 **test** | **String**|  | [optional] 

### Return type

[**[BigOvenModelAPI2CollectionInfo]**](BigOvenModelAPI2CollectionInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## collectionGetCollection

> BigOvenModelAPI2RecipeSearchResult collectionGetCollection(id, opts)

Gets a recipe collection. A recipe collection is a curated set of recipes.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.CollectionApi();
let id = 56; // Number | the collection identifier
let opts = {
  'rpp': 56, // Number | results per page
  'pg': 56, // Number | page number (starting with 1)
  'test': true, // Boolean | 
  'sessionForLogging': "sessionForLogging_example" // String | 
};
apiInstance.collectionGetCollection(id, opts, (error, data, response) => {
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
 **id** | **Number**| the collection identifier | 
 **rpp** | **Number**| results per page | [optional] 
 **pg** | **Number**| page number (starting with 1) | [optional] 
 **test** | **Boolean**|  | [optional] 
 **sessionForLogging** | **String**|  | [optional] 

### Return type

[**BigOvenModelAPI2RecipeSearchResult**](BigOvenModelAPI2RecipeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## collectionGetCollectionMeta

> BigOvenModelAPI2CollectionInfo collectionGetCollectionMeta(id)

Gets a recipe collection metadata. A recipe collection is a curated set of recipes.

### Example

```javascript
import 1000000RecipeAndGroceryListApiV2 from '1000000_recipe_and_grocery_list_api__v2';

let apiInstance = new 1000000RecipeAndGroceryListApiV2.CollectionApi();
let id = 56; // Number | the collection identifier
apiInstance.collectionGetCollectionMeta(id, (error, data, response) => {
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
 **id** | **Number**| the collection identifier | 

### Return type

[**BigOvenModelAPI2CollectionInfo**](BigOvenModelAPI2CollectionInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

