# SwaggerApi2Cart.CategoryApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoryAdd**](CategoryApi.md#categoryAdd) | **POST** /category.add.json | 
[**categoryAssign**](CategoryApi.md#categoryAssign) | **POST** /category.assign.json | 
[**categoryCount**](CategoryApi.md#categoryCount) | **GET** /category.count.json | 
[**categoryDelete**](CategoryApi.md#categoryDelete) | **DELETE** /category.delete.json | 
[**categoryFind**](CategoryApi.md#categoryFind) | **GET** /category.find.json | 
[**categoryImageAdd**](CategoryApi.md#categoryImageAdd) | **POST** /category.image.add.json | 
[**categoryImageDelete**](CategoryApi.md#categoryImageDelete) | **DELETE** /category.image.delete.json | 
[**categoryInfo**](CategoryApi.md#categoryInfo) | **GET** /category.info.json | 
[**categoryList**](CategoryApi.md#categoryList) | **GET** /category.list.json | 
[**categoryUnassign**](CategoryApi.md#categoryUnassign) | **POST** /category.unassign.json | 
[**categoryUpdate**](CategoryApi.md#categoryUpdate) | **PUT** /category.update.json | 



## categoryAdd

> CategoryAdd200Response categoryAdd(name, opts)



Add new category in store

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let name = "name_example"; // String | Defines category's name that has to be added
let opts = {
  'parentId': "parentId_example", // String | Adds categories specified by parent id
  'storesIds': "'0'", // String | Create category in the stores that is specified by comma-separated stores' id
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'avail': true, // Boolean | Defines category's visibility status
  'sortOrder': 0, // Number | Sort number in the list
  'createdTime': "createdTime_example", // String | Entity's date creation
  'modifiedTime': "modifiedTime_example", // String | Entity's date modification
  'description': "description_example", // String | Defines category's description
  'metaTitle': "metaTitle_example", // String | Defines unique meta title for each entity
  'metaDescription': "metaDescription_example", // String | Defines unique meta description of a entity
  'metaKeywords': "metaKeywords_example", // String | Defines unique meta keywords for each entity
  'seoUrl': "seoUrl_example" // String | Defines unique category's URL for SEO
};
apiInstance.categoryAdd(name, opts, (error, data, response) => {
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
 **name** | **String**| Defines category&#39;s name that has to be added | 
 **parentId** | **String**| Adds categories specified by parent id | [optional] 
 **storesIds** | **String**| Create category in the stores that is specified by comma-separated stores&#39; id | [optional] [default to &#39;0&#39;]
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true]
 **sortOrder** | **Number**| Sort number in the list | [optional] [default to 0]
 **createdTime** | **String**| Entity&#39;s date creation | [optional] 
 **modifiedTime** | **String**| Entity&#39;s date modification | [optional] 
 **description** | **String**| Defines category&#39;s description | [optional] 
 **metaTitle** | **String**| Defines unique meta title for each entity | [optional] 
 **metaDescription** | **String**| Defines unique meta description of a entity | [optional] 
 **metaKeywords** | **String**| Defines unique meta keywords for each entity | [optional] 
 **seoUrl** | **String**| Defines unique category&#39;s URL for SEO | [optional] 

### Return type

[**CategoryAdd200Response**](CategoryAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryAssign

> CartConfigUpdate200Response categoryAssign(productId, categoryId, opts)



Assign category to product

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let productId = "productId_example"; // String | Defines category assign to the product, specified by product id
let categoryId = "categoryId_example"; // String | Defines category assign, specified by category id
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.categoryAssign(productId, categoryId, opts, (error, data, response) => {
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
 **productId** | **String**| Defines category assign to the product, specified by product id | 
 **categoryId** | **String**| Defines category assign, specified by category id | 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**CartConfigUpdate200Response**](CartConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryCount

> CategoryCount200Response categoryCount(opts)



Count categories in store.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let opts = {
  'parentId': "parentId_example", // String | Counts categories specified by parent id
  'storeId': "storeId_example", // String | Counts category specified by store id
  'langId': "langId_example", // String | Counts category specified by language id
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'avail': true // Boolean | Defines category's visibility status
};
apiInstance.categoryCount(opts, (error, data, response) => {
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
 **parentId** | **String**| Counts categories specified by parent id | [optional] 
 **storeId** | **String**| Counts category specified by store id | [optional] 
 **langId** | **String**| Counts category specified by language id | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true]

### Return type

[**CategoryCount200Response**](CategoryCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryDelete

> BridgeDelete200Response categoryDelete(id)



Delete category in store

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let id = "id_example"; // String | Defines category removal, specified by category id
apiInstance.categoryDelete(id, (error, data, response) => {
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
 **id** | **String**| Defines category removal, specified by category id | 

### Return type

[**BridgeDelete200Response**](BridgeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryFind

> CategoryFind200Response categoryFind(findValue, opts)



Search category in store. \&quot;Laptop\&quot; is specified here by default.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let findValue = "findValue_example"; // String | Entity search that is specified by some value
let opts = {
  'findWhere': "'name'", // String | Entity search that is specified by the comma-separated unique fields
  'findParams': "'whole_words'", // String | Entity search that is specified by comma-separated parameters
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example" // String | Language id
};
apiInstance.categoryFind(findValue, opts, (error, data, response) => {
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
 **findValue** | **String**| Entity search that is specified by some value | 
 **findWhere** | **String**| Entity search that is specified by the comma-separated unique fields | [optional] [default to &#39;name&#39;]
 **findParams** | **String**| Entity search that is specified by comma-separated parameters | [optional] [default to &#39;whole_words&#39;]
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 

### Return type

[**CategoryFind200Response**](CategoryFind200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryImageAdd

> CategoryImageAdd200Response categoryImageAdd(categoryId, imageName, url, type, opts)



Add image to category

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let categoryId = "categoryId_example"; // String | Defines category id where the image should be added
let imageName = "imageName_example"; // String | Defines image's name
let url = "url_example"; // String | Defines URL of the image that has to be added
let type = "type_example"; // String | Defines image's types that are specified by comma-separated list
let opts = {
  'label': "label_example", // String | Defines alternative text that has to be attached to the picture
  'mime': "mime_example", // String | Mime type of image http://en.wikipedia.org/wiki/Internet_media_type.
  'position': 0, // Number | Defines image’s position in the list
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.categoryImageAdd(categoryId, imageName, url, type, opts, (error, data, response) => {
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
 **categoryId** | **String**| Defines category id where the image should be added | 
 **imageName** | **String**| Defines image&#39;s name | 
 **url** | **String**| Defines URL of the image that has to be added | 
 **type** | **String**| Defines image&#39;s types that are specified by comma-separated list | 
 **label** | **String**| Defines alternative text that has to be attached to the picture | [optional] 
 **mime** | **String**| Mime type of image http://en.wikipedia.org/wiki/Internet_media_type. | [optional] 
 **position** | **Number**| Defines image’s position in the list | [optional] [default to 0]
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**CategoryImageAdd200Response**](CategoryImageAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryImageDelete

> AttributeDelete200Response categoryImageDelete(categoryId, imageId, opts)



Delete image

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let categoryId = "categoryId_example"; // String | Defines category id where the image should be deleted
let imageId = "imageId_example"; // String | Define image id
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.categoryImageDelete(categoryId, imageId, opts, (error, data, response) => {
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
 **categoryId** | **String**| Defines category id where the image should be deleted | 
 **imageId** | **String**| Define image id | 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryInfo

> CategoryInfo200Response categoryInfo(id, opts)



Get category info about category ID*** or specify other category ID.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let id = "id_example"; // String | Retrieves category's info specified by category id
let opts = {
  'params': "'id,parent_id,name,description'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'storeId': "storeId_example", // String | Retrieves category info  specified by store id
  'langId': "langId_example" // String | Retrieves category info  specified by language id
};
apiInstance.categoryInfo(id, opts, (error, data, response) => {
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
 **id** | **String**| Retrieves category&#39;s info specified by category id | 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,parent_id,name,description&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **storeId** | **String**| Retrieves category info  specified by store id | [optional] 
 **langId** | **String**| Retrieves category info  specified by language id | [optional] 

### Return type

[**CategoryInfo200Response**](CategoryInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryList

> ModelResponseCategoryList categoryList(opts)



Get list of categories from store.

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'parentId': "parentId_example", // String | Retrieves categories specified by parent id
  'params': "'id,parent_id,name,description'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'storeId': "storeId_example", // String | Retrieves categories specified by store id
  'langId': "langId_example", // String | Retrieves categorys specified by language id
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'avail': true // Boolean | Defines category's visibility status
};
apiInstance.categoryList(opts, (error, data, response) => {
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
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **parentId** | **String**| Retrieves categories specified by parent id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,parent_id,name,description&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **storeId** | **String**| Retrieves categories specified by store id | [optional] 
 **langId** | **String**| Retrieves categorys specified by language id | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true]

### Return type

[**ModelResponseCategoryList**](ModelResponseCategoryList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryUnassign

> CartConfigUpdate200Response categoryUnassign(categoryId, productId, opts)



Unassign category to product

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let categoryId = "categoryId_example"; // String | Defines category unassign, specified by category id
let productId = "productId_example"; // String | Defines category unassign to the product, specified by product id
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.categoryUnassign(categoryId, productId, opts, (error, data, response) => {
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
 **categoryId** | **String**| Defines category unassign, specified by category id | 
 **productId** | **String**| Defines category unassign to the product, specified by product id | 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**CartConfigUpdate200Response**](CartConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoryUpdate

> AccountConfigUpdate200Response categoryUpdate(id, opts)



Update category in store

### Example

```javascript
import SwaggerApi2Cart from 'swagger_api2_cart';
let defaultClient = SwaggerApi2Cart.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: store_key
let store_key = defaultClient.authentications['store_key'];
store_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//store_key.apiKeyPrefix = 'Token';

let apiInstance = new SwaggerApi2Cart.CategoryApi();
let id = "id_example"; // String | Defines category update specified by category id
let opts = {
  'name': "name_example", // String | Defines new category’s name
  'parentId': "parentId_example", // String | Defines new parent category id
  'storesIds': "'0'", // String | Update category in the stores that is specified by comma-separated stores' id
  'avail': true, // Boolean | Defines category's visibility status
  'sortOrder': 56, // Number | Sort number in the list
  'modifiedTime': "modifiedTime_example", // String | Entity's date modification
  'description': "description_example", // String | Defines new category's description
  'metaTitle': "metaTitle_example", // String | Defines unique meta title for each entity
  'metaDescription': "metaDescription_example", // String | Defines unique meta description of a entity
  'metaKeywords': "metaKeywords_example", // String | Defines unique meta keywords for each entity
  'seoUrl': "seoUrl_example", // String | Defines unique category's URL for SEO
  'langId': "langId_example", // String | Language id
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.categoryUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| Defines category update specified by category id | 
 **name** | **String**| Defines new category’s name | [optional] 
 **parentId** | **String**| Defines new parent category id | [optional] 
 **storesIds** | **String**| Update category in the stores that is specified by comma-separated stores&#39; id | [optional] [default to &#39;0&#39;]
 **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] 
 **sortOrder** | **Number**| Sort number in the list | [optional] 
 **modifiedTime** | **String**| Entity&#39;s date modification | [optional] 
 **description** | **String**| Defines new category&#39;s description | [optional] 
 **metaTitle** | **String**| Defines unique meta title for each entity | [optional] 
 **metaDescription** | **String**| Defines unique meta description of a entity | [optional] 
 **metaKeywords** | **String**| Defines unique meta keywords for each entity | [optional] 
 **seoUrl** | **String**| Defines unique category&#39;s URL for SEO | [optional] 
 **langId** | **String**| Language id | [optional] 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

