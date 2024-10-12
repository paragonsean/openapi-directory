# SwaggerApi2Cart.ProductApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productAdd**](ProductApi.md#productAdd) | **POST** /product.add.json | 
[**productAttributeList**](ProductApi.md#productAttributeList) | **GET** /product.attribute.list.json | 
[**productAttributeValueSet**](ProductApi.md#productAttributeValueSet) | **POST** /product.attribute.value.set.json | 
[**productAttributeValueUnset**](ProductApi.md#productAttributeValueUnset) | **POST** /product.attribute.value.unset.json | 
[**productBrandList**](ProductApi.md#productBrandList) | **GET** /product.brand.list.json | 
[**productChildItemFind**](ProductApi.md#productChildItemFind) | **GET** /product.child_item.find.json | 
[**productChildItemInfo**](ProductApi.md#productChildItemInfo) | **GET** /product.child_item.info.json | 
[**productChildItemList**](ProductApi.md#productChildItemList) | **GET** /product.child_item.list.json | 
[**productCount**](ProductApi.md#productCount) | **GET** /product.count.json | 
[**productCurrencyAdd**](ProductApi.md#productCurrencyAdd) | **POST** /product.currency.add.json | 
[**productCurrencyList**](ProductApi.md#productCurrencyList) | **GET** /product.currency.list.json | 
[**productDelete**](ProductApi.md#productDelete) | **DELETE** /product.delete.json | 
[**productFields**](ProductApi.md#productFields) | **GET** /product.fields.json | 
[**productFind**](ProductApi.md#productFind) | **GET** /product.find.json | 
[**productImageAdd**](ProductApi.md#productImageAdd) | **POST** /product.image.add.json | 
[**productImageDelete**](ProductApi.md#productImageDelete) | **DELETE** /product.image.delete.json | 
[**productImageUpdate**](ProductApi.md#productImageUpdate) | **PUT** /product.image.update.json | 
[**productInfo**](ProductApi.md#productInfo) | **GET** /product.info.json | 
[**productList**](ProductApi.md#productList) | **GET** /product.list.json | 
[**productManufacturerAdd**](ProductApi.md#productManufacturerAdd) | **POST** /product.manufacturer.add.json | 
[**productOptionAdd**](ProductApi.md#productOptionAdd) | **POST** /product.option.add.json | 
[**productOptionAssign**](ProductApi.md#productOptionAssign) | **POST** /product.option.assign.json | 
[**productOptionList**](ProductApi.md#productOptionList) | **GET** /product.option.list.json | 
[**productOptionValueAdd**](ProductApi.md#productOptionValueAdd) | **POST** /product.option.value.add.json | 
[**productOptionValueAssign**](ProductApi.md#productOptionValueAssign) | **POST** /product.option.value.assign.json | 
[**productOptionValueUpdate**](ProductApi.md#productOptionValueUpdate) | **PUT** /product.option.value.update.json | 
[**productPriceAdd**](ProductApi.md#productPriceAdd) | **POST** /product.price.add.json | 
[**productPriceDelete**](ProductApi.md#productPriceDelete) | **DELETE** /product.price.delete.json | 
[**productPriceUpdate**](ProductApi.md#productPriceUpdate) | **PUT** /product.price.update.json | 
[**productReviewList**](ProductApi.md#productReviewList) | **GET** /product.review.list.json | 
[**productStoreAssign**](ProductApi.md#productStoreAssign) | **POST** /product.store.assign.json | 
[**productTaxAdd**](ProductApi.md#productTaxAdd) | **POST** /product.tax.add.json | 
[**productUpdate**](ProductApi.md#productUpdate) | **PUT** /product.update.json | 
[**productVariantAdd**](ProductApi.md#productVariantAdd) | **POST** /product.variant.add.json | 
[**productVariantCount**](ProductApi.md#productVariantCount) | **GET** /product.variant.count.json | 
[**productVariantDelete**](ProductApi.md#productVariantDelete) | **DELETE** /product.variant.delete.json | 
[**productVariantImageAdd**](ProductApi.md#productVariantImageAdd) | **POST** /product.variant.image.add.json | 
[**productVariantImageDelete**](ProductApi.md#productVariantImageDelete) | **DELETE** /product.variant.image.delete.json | 
[**productVariantInfo**](ProductApi.md#productVariantInfo) | **GET** /product.variant.info.json | 
[**productVariantList**](ProductApi.md#productVariantList) | **GET** /product.variant.list.json | 
[**productVariantPriceAdd**](ProductApi.md#productVariantPriceAdd) | **POST** /product.variant.price.add.json | 
[**productVariantPriceDelete**](ProductApi.md#productVariantPriceDelete) | **DELETE** /product.variant.price.delete.json | 
[**productVariantPriceUpdate**](ProductApi.md#productVariantPriceUpdate) | **PUT** /product.variant.price.update.json | 
[**productVariantUpdate**](ProductApi.md#productVariantUpdate) | **PUT** /product.variant.update.json | 



## productAdd

> ProductAdd200Response productAdd(productAdd)



Add new product to store.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productAdd = new SwaggerApi2Cart.ProductAdd(); // ProductAdd | 
apiInstance.productAdd(productAdd, (error, data, response) => {
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
 **productAdd** | [**ProductAdd**](ProductAdd.md)|  | 

### Return type

[**ProductAdd200Response**](ProductAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productAttributeList

> ModelResponseProductAttributeList productAttributeList(productId, opts)



Get list of attributes and values.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Retrieves attributes specified by product id
let opts = {
  'attributeId': "attributeId_example", // String | Retrieves info for specified attribute_id
  'variantId': "variantId_example", // String | Defines product's variants specified by variant id
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'attributeGroupId': "attributeGroupId_example", // String | Filter by attribute_group_id
  'setName': "setName_example", // String | Retrieves attributes specified by set_name in Magento
  'langId': "langId_example", // String | Retrieves attributes specified by language id
  'storeId': "storeId_example", // String | Retrieves attributes specified by store id
  'sortBy': "'attribute_id'", // String | Set field to sort by
  'sortDirection': "'asc'", // String | Set sorting direction
  'params': "'attribute_id,name'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example" // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
};
apiInstance.productAttributeList(productId, opts, (error, data, response) => {
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
 **productId** | **String**| Retrieves attributes specified by product id | 
 **attributeId** | **String**| Retrieves info for specified attribute_id | [optional] 
 **variantId** | **String**| Defines product&#39;s variants specified by variant id | [optional] 
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **attributeGroupId** | **String**| Filter by attribute_group_id | [optional] 
 **setName** | **String**| Retrieves attributes specified by set_name in Magento | [optional] 
 **langId** | **String**| Retrieves attributes specified by language id | [optional] 
 **storeId** | **String**| Retrieves attributes specified by store id | [optional] 
 **sortBy** | **String**| Set field to sort by | [optional] [default to &#39;attribute_id&#39;]
 **sortDirection** | **String**| Set sorting direction | [optional] [default to &#39;asc&#39;]
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;attribute_id,name&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 

### Return type

[**ModelResponseProductAttributeList**](ModelResponseProductAttributeList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productAttributeValueSet

> ProductAttributeValueSet200Response productAttributeValueSet(productId, opts)



Set attribute value to product.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Defines product id where the attribute should be added
let opts = {
  'attributeId': "attributeId_example", // String | Filter by attribute_id
  'attributeGroupId': "attributeGroupId_example", // String | Filter by attribute_group_id
  'attributeName': "attributeName_example", // String | Define attribute name
  'value': "value_example", // String | Define attribute value
  'valueId': 56, // Number | Define attribute value id
  'langId': "langId_example", // String | Language id
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.productAttributeValueSet(productId, opts, (error, data, response) => {
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
 **productId** | **String**| Defines product id where the attribute should be added | 
 **attributeId** | **String**| Filter by attribute_id | [optional] 
 **attributeGroupId** | **String**| Filter by attribute_group_id | [optional] 
 **attributeName** | **String**| Define attribute name | [optional] 
 **value** | **String**| Define attribute value | [optional] 
 **valueId** | **Number**| Define attribute value id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**ProductAttributeValueSet200Response**](ProductAttributeValueSet200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productAttributeValueUnset

> ProductAttributeValueUnset200Response productAttributeValueUnset(productId, attributeId, opts)



Removes attribute value for a product.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Product id
let attributeId = "attributeId_example"; // String | Attribute Id
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'includeDefault': false, // Boolean | Boolean, whether or not to unset default value of the attribute, if applicable
  'reindex': true, // Boolean | Is reindex required
  'clearCache': true // Boolean | Is cache clear required
};
apiInstance.productAttributeValueUnset(productId, attributeId, opts, (error, data, response) => {
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
 **productId** | **String**| Product id | 
 **attributeId** | **String**| Attribute Id | 
 **storeId** | **String**| Store Id | [optional] 
 **includeDefault** | **Boolean**| Boolean, whether or not to unset default value of the attribute, if applicable | [optional] [default to false]
 **reindex** | **Boolean**| Is reindex required | [optional] [default to true]
 **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true]

### Return type

[**ProductAttributeValueUnset200Response**](ProductAttributeValueUnset200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productBrandList

> ProductBrandList200Response productBrandList(opts)



Get list of brands from your store.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'params': "'id,name,short_description,active,url'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'brandIds': "brandIds_example", // String | Retrieves brands specified by brand ids
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'responseFields': "responseFields_example" // String | Set this parameter in order to choose which entity fields you want to retrieve
};
apiInstance.productBrandList(opts, (error, data, response) => {
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
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,short_description,active,url&#39;]
 **brandIds** | **String**| Retrieves brands specified by brand ids | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 

### Return type

[**ProductBrandList200Response**](ProductBrandList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productChildItemFind

> ProductChildItemFind200Response productChildItemFind(findValue, opts)



Search product child item (bundled item or configurable product variant) in store catalog.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let findValue = "findValue_example"; // String | Entity search that is specified by some value
let opts = {
  'findWhere': "'name'", // String | Entity search that is specified by the comma-separated unique fields
  'findParams': "'whole_words'", // String | Entity search that is specified by comma-separated parameters
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.productChildItemFind(findValue, opts, (error, data, response) => {
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

### Return type

[**ProductChildItemFind200Response**](ProductChildItemFind200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productChildItemInfo

> ProductChildItemInfo200Response productChildItemInfo(productId, id, opts)



Get child for specific product.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Filter by parent product id
let id = "id_example"; // String | Entity id
let opts = {
  'params': "'force_all'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'currencyId': "currencyId_example" // String | Currency Id
};
apiInstance.productChildItemInfo(productId, id, opts, (error, data, response) => {
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
 **productId** | **String**| Filter by parent product id | 
 **id** | **String**| Entity id | 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;force_all&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **currencyId** | **String**| Currency Id | [optional] 

### Return type

[**ProductChildItemInfo200Response**](ProductChildItemInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productChildItemList

> ModelResponseProductChildItemList productChildItemList(opts)



Get child items list of specific product(s).

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let opts = {
  'pageCursor': "pageCursor_example", // String | Used to retrieve products child items via cursor-based pagination (it can't be used with any other filtering parameter)
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'params': "'force_all'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'productId': "productId_example", // String | Filter by parent product id
  'productIds': "productIds_example", // String | Filter by parent product ids
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'currencyId': "currencyId_example", // String | Currency Id
  'availSale': true, // Boolean | Specifies the set of available/not available products for sale
  'reportRequestId': "reportRequestId_example", // String | Report request id
  'disableReportCache': false // Boolean | Disable report cache for current request
};
apiInstance.productChildItemList(opts, (error, data, response) => {
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
 **pageCursor** | **String**| Used to retrieve products child items via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;force_all&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **productId** | **String**| Filter by parent product id | [optional] 
 **productIds** | **String**| Filter by parent product ids | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **currencyId** | **String**| Currency Id | [optional] 
 **availSale** | **Boolean**| Specifies the set of available/not available products for sale | [optional] 
 **reportRequestId** | **String**| Report request id | [optional] 
 **disableReportCache** | **Boolean**| Disable report cache for current request | [optional] [default to false]

### Return type

[**ModelResponseProductChildItemList**](ModelResponseProductChildItemList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productCount

> ProductCount200Response productCount(opts)



Count products in store.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let opts = {
  'categoryId': "categoryId_example", // String | Counts products specified by category id
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'availView': true, // Boolean | Specifies the set of visible/invisible products
  'availSale': true, // Boolean | Specifies the set of available/not available products for sale
  'storeId': "storeId_example", // String | Counts products specified by store id
  'langId': "langId_example", // String | Counts products specified by language id
  'productIds': "productIds_example", // String | Counts products specified by product ids
  'reportRequestId': "reportRequestId_example", // String | Report request id
  'disableReportCache': false, // Boolean | Disable report cache for current request
  'brandName': "brandName_example", // String | Retrieves brands specified by brand name
  'productAttributes': ["null"], // [String] | Defines product attributes
  'status': "status_example", // String | Defines product's status
  'type': "type_example" // String | Defines products's type
};
apiInstance.productCount(opts, (error, data, response) => {
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
 **categoryId** | **String**| Counts products specified by category id | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **availView** | **Boolean**| Specifies the set of visible/invisible products | [optional] 
 **availSale** | **Boolean**| Specifies the set of available/not available products for sale | [optional] 
 **storeId** | **String**| Counts products specified by store id | [optional] 
 **langId** | **String**| Counts products specified by language id | [optional] 
 **productIds** | **String**| Counts products specified by product ids | [optional] 
 **reportRequestId** | **String**| Report request id | [optional] 
 **disableReportCache** | **Boolean**| Disable report cache for current request | [optional] [default to false]
 **brandName** | **String**| Retrieves brands specified by brand name | [optional] 
 **productAttributes** | [**[String]**](String.md)| Defines product attributes | [optional] 
 **status** | **String**| Defines product&#39;s status | [optional] 
 **type** | **String**| Defines products&#39;s type | [optional] 

### Return type

[**ProductCount200Response**](ProductCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productCurrencyAdd

> ProductCurrencyAdd200Response productCurrencyAdd(iso3, rate, opts)



Add currency and/or set default in store

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let iso3 = "iso3_example"; // String | Specifies standardized currency code
let rate = 3.4; // Number | Defines the numerical identifier against to the major currency
let opts = {
  'name': "name_example", // String | Defines currency's name
  'avail': true, // Boolean | Specifies whether the currency is available
  'symbolLeft': "symbolLeft_example", // String | Defines the symbol that is located before the currency
  'symbolRight': "symbolRight_example", // String | Defines the symbol that is located after the currency
  '_default': false // Boolean | Specifies currency's default meaning
};
apiInstance.productCurrencyAdd(iso3, rate, opts, (error, data, response) => {
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
 **iso3** | **String**| Specifies standardized currency code | 
 **rate** | **Number**| Defines the numerical identifier against to the major currency | 
 **name** | **String**| Defines currency&#39;s name | [optional] 
 **avail** | **Boolean**| Specifies whether the currency is available | [optional] [default to true]
 **symbolLeft** | **String**| Defines the symbol that is located before the currency | [optional] 
 **symbolRight** | **String**| Defines the symbol that is located after the currency | [optional] 
 **_default** | **Boolean**| Specifies currency&#39;s default meaning | [optional] [default to false]

### Return type

[**ProductCurrencyAdd200Response**](ProductCurrencyAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productCurrencyList

> ProductCurrencyList200Response productCurrencyList(opts)



Get list of currencies

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'params': "'name,iso3,default,avail'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  '_default': true, // Boolean | Specifies the set of default/not default currencies
  'avail': true // Boolean | Specifies the set of available/not available currencies
};
apiInstance.productCurrencyList(opts, (error, data, response) => {
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
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;name,iso3,default,avail&#39;]
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **_default** | **Boolean**| Specifies the set of default/not default currencies | [optional] 
 **avail** | **Boolean**| Specifies the set of available/not available currencies | [optional] 

### Return type

[**ProductCurrencyList200Response**](ProductCurrencyList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productDelete

> ProductDelete200Response productDelete(id)



Product delete

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let id = "id_example"; // String | Product id that will be removed
apiInstance.productDelete(id, (error, data, response) => {
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
 **id** | **String**| Product id that will be removed | 

### Return type

[**ProductDelete200Response**](ProductDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productFields

> CartConfigUpdate200Response productFields()



Retrieve all available fields for product item in store.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
apiInstance.productFields((error, data, response) => {
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

[**CartConfigUpdate200Response**](CartConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productFind

> ProductFind200Response productFind(findValue, opts)



Search product in store catalog. \&quot;Apple\&quot; is specified here by default.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let findValue = "findValue_example"; // String | Entity search that is specified by some value
let opts = {
  'findWhere': "'name'", // String | Entity search that is specified by the comma-separated unique fields
  'findParams': "'whole_words'", // String | Entity search that is specified by comma-separated parameters
  'findWhat': "'product'", // String | Parameter's value specifies the entity that has to be found
  'langId': "langId_example", // String | Search products specified by language id
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.productFind(findValue, opts, (error, data, response) => {
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
 **findWhat** | **String**| Parameter&#39;s value specifies the entity that has to be found | [optional] [default to &#39;product&#39;]
 **langId** | **String**| Search products specified by language id | [optional] 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**ProductFind200Response**](ProductFind200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productImageAdd

> ProductImageAdd200Response productImageAdd(productImageAdd)



Add image to product

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productImageAdd = new SwaggerApi2Cart.ProductImageAdd(); // ProductImageAdd | 
apiInstance.productImageAdd(productImageAdd, (error, data, response) => {
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
 **productImageAdd** | [**ProductImageAdd**](ProductImageAdd.md)|  | 

### Return type

[**ProductImageAdd200Response**](ProductImageAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productImageDelete

> AttributeDelete200Response productImageDelete(productId, id, opts)



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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Defines product id where the image should be deleted
let id = "id_example"; // String | Entity id
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.productImageDelete(productId, id, opts, (error, data, response) => {
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
 **productId** | **String**| Defines product id where the image should be deleted | 
 **id** | **String**| Entity id | 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productImageUpdate

> ProductImageUpdate200Response productImageUpdate(productId, id, opts)



Update details of image

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Defines product id where the image should be updated
let id = "id_example"; // String | Defines image update specified by image id
let opts = {
  'variantIds': "variantIds_example", // String | Defines product's variants ids
  'imageName': "imageName_example", // String | Defines image's name
  'type': "'additional'", // String | Defines image's types that are specified by comma-separated list
  'label': "label_example", // String | Defines alternative text that has to be attached to the picture
  'position': 56, // Number | Defines image’s position in the list
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'hidden': true // Boolean | Define is hide image
};
apiInstance.productImageUpdate(productId, id, opts, (error, data, response) => {
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
 **productId** | **String**| Defines product id where the image should be updated | 
 **id** | **String**| Defines image update specified by image id | 
 **variantIds** | **String**| Defines product&#39;s variants ids | [optional] 
 **imageName** | **String**| Defines image&#39;s name | [optional] 
 **type** | **String**| Defines image&#39;s types that are specified by comma-separated list | [optional] [default to &#39;additional&#39;]
 **label** | **String**| Defines alternative text that has to be attached to the picture | [optional] 
 **position** | **Number**| Defines image’s position in the list | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **hidden** | **Boolean**| Define is hide image | [optional] 

### Return type

[**ProductImageUpdate200Response**](ProductImageUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productInfo

> ProductInfo200Response productInfo(id, opts)



Get product info about product ID *** or specify other product ID.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let id = "id_example"; // String | Retrieves product's info specified by product id
let opts = {
  'params': "'id,name,description,price,categories_ids'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'storeId': "storeId_example", // String | Retrieves product info specified by store id
  'langId': "langId_example", // String | Retrieves product info specified by language id
  'currencyId': "currencyId_example", // String | Currency Id
  'reportRequestId': "reportRequestId_example", // String | Report request id
  'disableReportCache': false // Boolean | Disable report cache for current request
};
apiInstance.productInfo(id, opts, (error, data, response) => {
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
 **id** | **String**| Retrieves product&#39;s info specified by product id | 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,description,price,categories_ids&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **storeId** | **String**| Retrieves product info specified by store id | [optional] 
 **langId** | **String**| Retrieves product info specified by language id | [optional] 
 **currencyId** | **String**| Currency Id | [optional] 
 **reportRequestId** | **String**| Report request id | [optional] 
 **disableReportCache** | **Boolean**| Disable report cache for current request | [optional] [default to false]

### Return type

[**ProductInfo200Response**](ProductInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productList

> ModelResponseProductList productList(opts)



Get list of products from your store. Returns 10 products by default.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let opts = {
  'pageCursor': "pageCursor_example", // String | Used to retrieve products via cursor-based pagination (it can't be used with any other filtering parameter)
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'params': "'id,name,description,price,categories_ids'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'categoryId': "categoryId_example", // String | Retrieves products specified by category id
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'availView': true, // Boolean | Specifies the set of visible/invisible products
  'availSale': true, // Boolean | Specifies the set of available/not available products for sale
  'storeId': "storeId_example", // String | Retrieves products specified by store id
  'langId': "langId_example", // String | Retrieves products specified by language id
  'currencyId': "currencyId_example", // String | Currency Id
  'productIds': "productIds_example", // String | Retrieves products specified by product ids
  'sinceId': 56, // Number | Retrieve entities starting from the specified id.
  'reportRequestId': "reportRequestId_example", // String | Report request id
  'disableReportCache': false, // Boolean | Disable report cache for current request
  'sortBy': "'id'", // String | Set field to sort by
  'sortDirection': "'asc'", // String | Set sorting direction
  'sku': "sku_example", // String | Filter by product's sku
  'disableCache': false, // Boolean | Disable cache for current request
  'brandName': "brandName_example", // String | Retrieves brands specified by brand name
  'productAttributes': ["null"], // [String] | Defines product attributes
  'status': "status_example", // String | Defines product's status
  'type': "type_example" // String | Defines products's type
};
apiInstance.productList(opts, (error, data, response) => {
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
 **pageCursor** | **String**| Used to retrieve products via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,description,price,categories_ids&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **categoryId** | **String**| Retrieves products specified by category id | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **availView** | **Boolean**| Specifies the set of visible/invisible products | [optional] 
 **availSale** | **Boolean**| Specifies the set of available/not available products for sale | [optional] 
 **storeId** | **String**| Retrieves products specified by store id | [optional] 
 **langId** | **String**| Retrieves products specified by language id | [optional] 
 **currencyId** | **String**| Currency Id | [optional] 
 **productIds** | **String**| Retrieves products specified by product ids | [optional] 
 **sinceId** | **Number**| Retrieve entities starting from the specified id. | [optional] 
 **reportRequestId** | **String**| Report request id | [optional] 
 **disableReportCache** | **Boolean**| Disable report cache for current request | [optional] [default to false]
 **sortBy** | **String**| Set field to sort by | [optional] [default to &#39;id&#39;]
 **sortDirection** | **String**| Set sorting direction | [optional] [default to &#39;asc&#39;]
 **sku** | **String**| Filter by product&#39;s sku | [optional] 
 **disableCache** | **Boolean**| Disable cache for current request | [optional] [default to false]
 **brandName** | **String**| Retrieves brands specified by brand name | [optional] 
 **productAttributes** | [**[String]**](String.md)| Defines product attributes | [optional] 
 **status** | **String**| Defines product&#39;s status | [optional] 
 **type** | **String**| Defines products&#39;s type | [optional] 

### Return type

[**ModelResponseProductList**](ModelResponseProductList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productManufacturerAdd

> ProductManufacturerAdd200Response productManufacturerAdd(productId, manufacturer)



Add manufacturer to store and assign to product

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Defines products specified by product id
let manufacturer = "manufacturer_example"; // String | Defines product’s manufacturer's name
apiInstance.productManufacturerAdd(productId, manufacturer, (error, data, response) => {
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
 **productId** | **String**| Defines products specified by product id | 
 **manufacturer** | **String**| Defines product’s manufacturer&#39;s name | 

### Return type

[**ProductManufacturerAdd200Response**](ProductManufacturerAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productOptionAdd

> ProductOptionAdd200Response productOptionAdd(name, type, opts)



Add product option from store.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let name = "name_example"; // String | Defines option's name
let type = "type_example"; // String | Defines option's type that has to be added
let opts = {
  'productId': "productId_example", // String | Defines product id where the option should be added
  'defaultOptionValue': "defaultOptionValue_example", // String | Defines default option value that has to be added
  'optionValues': "optionValues_example", // String | Defines option values that has to be added
  'description': "description_example", // String | Defines option's description
  'avail': true, // Boolean | Defines whether the option is available
  'sortOrder': 0, // Number | Sort number in the list
  'required': false, // Boolean | Defines if the option is required
  'clearCache': true // Boolean | Is cache clear required
};
apiInstance.productOptionAdd(name, type, opts, (error, data, response) => {
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
 **name** | **String**| Defines option&#39;s name | 
 **type** | **String**| Defines option&#39;s type that has to be added | 
 **productId** | **String**| Defines product id where the option should be added | [optional] 
 **defaultOptionValue** | **String**| Defines default option value that has to be added | [optional] 
 **optionValues** | **String**| Defines option values that has to be added | [optional] 
 **description** | **String**| Defines option&#39;s description | [optional] 
 **avail** | **Boolean**| Defines whether the option is available | [optional] [default to true]
 **sortOrder** | **Number**| Sort number in the list | [optional] [default to 0]
 **required** | **Boolean**| Defines if the option is required | [optional] [default to false]
 **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true]

### Return type

[**ProductOptionAdd200Response**](ProductOptionAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productOptionAssign

> ProductOptionAssign200Response productOptionAssign(productId, optionId, opts)



Assign option from product.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Defines product id where the option should be assigned
let optionId = "optionId_example"; // String | Defines option id which has to be assigned
let opts = {
  'required': false, // Boolean | Defines if the option is required
  'sortOrder': 0, // Number | Sort number in the list
  'optionValues': "optionValues_example", // String | Defines option values that has to be assigned
  'clearCache': true // Boolean | Is cache clear required
};
apiInstance.productOptionAssign(productId, optionId, opts, (error, data, response) => {
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
 **productId** | **String**| Defines product id where the option should be assigned | 
 **optionId** | **String**| Defines option id which has to be assigned | 
 **required** | **Boolean**| Defines if the option is required | [optional] [default to false]
 **sortOrder** | **Number**| Sort number in the list | [optional] [default to 0]
 **optionValues** | **String**| Defines option values that has to be assigned | [optional] 
 **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true]

### Return type

[**ProductOptionAssign200Response**](ProductOptionAssign200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productOptionList

> ProductOptionList200Response productOptionList(opts)



Get list of options.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'params': "'id,name,description'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'productId': "productId_example", // String | Retrieves products' options specified by product id
  'langId': "langId_example", // String | Language id
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.productOptionList(opts, (error, data, response) => {
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
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,description&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **productId** | **String**| Retrieves products&#39; options specified by product id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**ProductOptionList200Response**](ProductOptionList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productOptionValueAdd

> ProductOptionValueAdd200Response productOptionValueAdd(productId, optionId, optionValue, opts)



Add product option item from option.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Defines product id where the option value should be added
let optionId = "optionId_example"; // String | Defines option id where the value has to be added
let optionValue = "optionValue_example"; // String | Defines option value that has to be added
let opts = {
  'sortOrder': 0, // Number | Sort number in the list
  'clearCache': true // Boolean | Is cache clear required
};
apiInstance.productOptionValueAdd(productId, optionId, optionValue, opts, (error, data, response) => {
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
 **productId** | **String**| Defines product id where the option value should be added | 
 **optionId** | **String**| Defines option id where the value has to be added | 
 **optionValue** | **String**| Defines option value that has to be added | 
 **sortOrder** | **Number**| Sort number in the list | [optional] [default to 0]
 **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true]

### Return type

[**ProductOptionValueAdd200Response**](ProductOptionValueAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productOptionValueAssign

> ProductOptionValueAssign200Response productOptionValueAssign(productOptionId, optionValueId, opts)



Assign product option item from product.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productOptionId = 56; // Number | Defines product's option id where the value has to be assigned
let optionValueId = 56; // Number | Defines value id that has to be assigned
let opts = {
  'clearCache': true // Boolean | Is cache clear required
};
apiInstance.productOptionValueAssign(productOptionId, optionValueId, opts, (error, data, response) => {
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
 **productOptionId** | **Number**| Defines product&#39;s option id where the value has to be assigned | 
 **optionValueId** | **Number**| Defines value id that has to be assigned | 
 **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true]

### Return type

[**ProductOptionValueAssign200Response**](ProductOptionValueAssign200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productOptionValueUpdate

> AccountConfigUpdate200Response productOptionValueUpdate(productId, optionId, optionValueId, optionValue, opts)



Update product option item from option.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Defines product id where the option value should be updated
let optionId = "optionId_example"; // String | Defines option id where the value has to be updated
let optionValueId = 56; // Number | Defines value id that has to be assigned
let optionValue = "optionValue_example"; // String | Defines option value that has to be added
let opts = {
  'price': 3.4, // Number | Defines new product option price
  'quantity': 3.4, // Number | Defines new products' options quantity
  'clearCache': true // Boolean | Is cache clear required
};
apiInstance.productOptionValueUpdate(productId, optionId, optionValueId, optionValue, opts, (error, data, response) => {
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
 **productId** | **String**| Defines product id where the option value should be updated | 
 **optionId** | **String**| Defines option id where the value has to be updated | 
 **optionValueId** | **Number**| Defines value id that has to be assigned | 
 **optionValue** | **String**| Defines option value that has to be added | 
 **price** | **Number**| Defines new product option price | [optional] 
 **quantity** | **Number**| Defines new products&#39; options quantity | [optional] 
 **clearCache** | **Boolean**| Is cache clear required | [optional] [default to true]

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productPriceAdd

> CartValidate200Response productPriceAdd(productPriceAdd)



Add some prices to the product.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productPriceAdd = new SwaggerApi2Cart.ProductPriceAdd(); // ProductPriceAdd | 
apiInstance.productPriceAdd(productPriceAdd, (error, data, response) => {
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
 **productPriceAdd** | [**ProductPriceAdd**](ProductPriceAdd.md)|  | 

### Return type

[**CartValidate200Response**](CartValidate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productPriceDelete

> AttributeDelete200Response productPriceDelete(productId, opts)



Delete some prices of the product

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Defines the product where the price has to be deleted
let opts = {
  'groupPrices': "groupPrices_example" // String | Defines product's group prices
};
apiInstance.productPriceDelete(productId, opts, (error, data, response) => {
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
 **productId** | **String**| Defines the product where the price has to be deleted | 
 **groupPrices** | **String**| Defines product&#39;s group prices | [optional] 

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productPriceUpdate

> AccountConfigUpdate200Response productPriceUpdate(productPriceUpdate)



Update some prices of the product.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productPriceUpdate = new SwaggerApi2Cart.ProductPriceUpdate(); // ProductPriceUpdate | 
apiInstance.productPriceUpdate(productPriceUpdate, (error, data, response) => {
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
 **productPriceUpdate** | [**ProductPriceUpdate**](ProductPriceUpdate.md)|  | 

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productReviewList

> ProductReviewList200Response productReviewList(productId, opts)



Get reviews of a specific product.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Product id
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'ids': "ids_example", // String | Retrieves reviews specified by ids
  'storeId': "storeId_example", // String | Store Id
  'status': "status_example", // String | Defines status
  'params': "'id,customer_id,email,message,status,product_id,nick_name,summary,rating,ratings,status,created_time'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'responseFields': "responseFields_example" // String | Set this parameter in order to choose which entity fields you want to retrieve
};
apiInstance.productReviewList(productId, opts, (error, data, response) => {
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
 **productId** | **String**| Product id | 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **ids** | **String**| Retrieves reviews specified by ids | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **status** | **String**| Defines status | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,customer_id,email,message,status,product_id,nick_name,summary,rating,ratings,status,created_time&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 

### Return type

[**ProductReviewList200Response**](ProductReviewList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productStoreAssign

> AccountConfigUpdate200Response productStoreAssign(productId, storeId)



Assign product to store

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Defines id of the product which should be assigned to a store
let storeId = "storeId_example"; // String | Defines id of the store product should be assigned to
apiInstance.productStoreAssign(productId, storeId, (error, data, response) => {
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
 **productId** | **String**| Defines id of the product which should be assigned to a store | 
 **storeId** | **String**| Defines id of the store product should be assigned to | 

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productTaxAdd

> ProductTaxAdd200Response productTaxAdd(productTaxAdd)



Add tax class and tax rate to store and assign to product.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productTaxAdd = new SwaggerApi2Cart.ProductTaxAdd(); // ProductTaxAdd | 
apiInstance.productTaxAdd(productTaxAdd, (error, data, response) => {
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
 **productTaxAdd** | [**ProductTaxAdd**](ProductTaxAdd.md)|  | 

### Return type

[**ProductTaxAdd200Response**](ProductTaxAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productUpdate

> AccountConfigUpdate200Response productUpdate(productUpdate)



Update price and quantity for a specific product

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productUpdate = new SwaggerApi2Cart.ProductUpdate(); // ProductUpdate | 
apiInstance.productUpdate(productUpdate, (error, data, response) => {
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
 **productUpdate** | [**ProductUpdate**](ProductUpdate.md)|  | 

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productVariantAdd

> ProductVariantAdd200Response productVariantAdd(productVariantAdd)



Add variant to product.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productVariantAdd = new SwaggerApi2Cart.ProductVariantAdd(); // ProductVariantAdd | 
apiInstance.productVariantAdd(productVariantAdd, (error, data, response) => {
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
 **productVariantAdd** | [**ProductVariantAdd**](ProductVariantAdd.md)|  | 

### Return type

[**ProductVariantAdd200Response**](ProductVariantAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productVariantCount

> ProductVariantCount200Response productVariantCount(productId, opts)



Get count variants.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Retrieves products' variants specified by product id
let opts = {
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'categoryId': "categoryId_example", // String | Counts products’ variants specified by category id
  'storeId': "storeId_example" // String | Retrieves variants specified by store id
};
apiInstance.productVariantCount(productId, opts, (error, data, response) => {
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
 **productId** | **String**| Retrieves products&#39; variants specified by product id | 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **categoryId** | **String**| Counts products’ variants specified by category id | [optional] 
 **storeId** | **String**| Retrieves variants specified by store id | [optional] 

### Return type

[**ProductVariantCount200Response**](ProductVariantCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productVariantDelete

> AttributeDelete200Response productVariantDelete(id, productId)



Delete variant.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let id = "id_example"; // String | Defines variant removal, specified by variant id
let productId = "productId_example"; // String | Defines product's id where the variant has to be deleted
apiInstance.productVariantDelete(id, productId, (error, data, response) => {
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
 **id** | **String**| Defines variant removal, specified by variant id | 
 **productId** | **String**| Defines product&#39;s id where the variant has to be deleted | 

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productVariantImageAdd

> ProductImageAdd200Response productVariantImageAdd(productVariantImageAdd)



Add image to product

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productVariantImageAdd = new SwaggerApi2Cart.ProductVariantImageAdd(); // ProductVariantImageAdd | 
apiInstance.productVariantImageAdd(productVariantImageAdd, (error, data, response) => {
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
 **productVariantImageAdd** | [**ProductVariantImageAdd**](ProductVariantImageAdd.md)|  | 

### Return type

[**ProductImageAdd200Response**](ProductImageAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productVariantImageDelete

> AttributeDelete200Response productVariantImageDelete(productId, productVariantId, id, opts)



Delete  image to product

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productId = "productId_example"; // String | Defines product id where the variant image should be deleted
let productVariantId = 56; // Number | Defines product's variants specified by variant id
let id = "id_example"; // String | Entity id
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.productVariantImageDelete(productId, productVariantId, id, opts, (error, data, response) => {
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
 **productId** | **String**| Defines product id where the variant image should be deleted | 
 **productVariantId** | **Number**| Defines product&#39;s variants specified by variant id | 
 **id** | **String**| Entity id | 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productVariantInfo

> ProductInfo200Response productVariantInfo(id, opts)



Get variant info. This method is deprecated, and its development is stopped. Please use \&quot;product.child_item.info\&quot; instead.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let id = "id_example"; // String | Retrieves variant's info specified by variant id
let opts = {
  'params': "'id,name,description,price'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'storeId': "storeId_example" // String | Retrieves variant info specified by store id
};
apiInstance.productVariantInfo(id, opts, (error, data, response) => {
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
 **id** | **String**| Retrieves variant&#39;s info specified by variant id | 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,description,price&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **storeId** | **String**| Retrieves variant info specified by store id | [optional] 

### Return type

[**ProductInfo200Response**](ProductInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productVariantList

> ProductVariantList200Response productVariantList(opts)



Get a list of variants. This method is deprecated, and its development is stopped. Please use \&quot;product.child_item.list\&quot; instead.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'params': "'id,name,description,price'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'categoryId': "categoryId_example", // String | Retrieves products’ variants specified by category id
  'productId': "productId_example", // String | Retrieves products' variants specified by product id
  'storeId': "storeId_example" // String | Retrieves variants specified by store id
};
apiInstance.productVariantList(opts, (error, data, response) => {
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
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,description,price&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **categoryId** | **String**| Retrieves products’ variants specified by category id | [optional] 
 **productId** | **String**| Retrieves products&#39; variants specified by product id | [optional] 
 **storeId** | **String**| Retrieves variants specified by store id | [optional] 

### Return type

[**ProductVariantList200Response**](ProductVariantList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productVariantPriceAdd

> CartValidate200Response productVariantPriceAdd(productVariantPriceAdd)



Add some prices to the product variant.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productVariantPriceAdd = new SwaggerApi2Cart.ProductVariantPriceAdd(); // ProductVariantPriceAdd | 
apiInstance.productVariantPriceAdd(productVariantPriceAdd, (error, data, response) => {
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
 **productVariantPriceAdd** | [**ProductVariantPriceAdd**](ProductVariantPriceAdd.md)|  | 

### Return type

[**CartValidate200Response**](CartValidate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productVariantPriceDelete

> AttributeDelete200Response productVariantPriceDelete(id, productId, groupPrices)



Delete some prices of the product variant.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let id = "id_example"; // String | Defines the variant where the price has to be deleted
let productId = "productId_example"; // String | Product id
let groupPrices = "groupPrices_example"; // String | Defines variants's group prices
apiInstance.productVariantPriceDelete(id, productId, groupPrices, (error, data, response) => {
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
 **id** | **String**| Defines the variant where the price has to be deleted | 
 **productId** | **String**| Product id | 
 **groupPrices** | **String**| Defines variants&#39;s group prices | 

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productVariantPriceUpdate

> AccountConfigUpdate200Response productVariantPriceUpdate(productVariantPriceUpdate)



Update some prices of the product variant.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productVariantPriceUpdate = new SwaggerApi2Cart.ProductVariantPriceUpdate(); // ProductVariantPriceUpdate | 
apiInstance.productVariantPriceUpdate(productVariantPriceUpdate, (error, data, response) => {
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
 **productVariantPriceUpdate** | [**ProductVariantPriceUpdate**](ProductVariantPriceUpdate.md)|  | 

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productVariantUpdate

> AccountConfigUpdate200Response productVariantUpdate(productVariantUpdate)



Update variant.

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

let apiInstance = new SwaggerApi2Cart.ProductApi();
let productVariantUpdate = new SwaggerApi2Cart.ProductVariantUpdate(); // ProductVariantUpdate | 
apiInstance.productVariantUpdate(productVariantUpdate, (error, data, response) => {
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
 **productVariantUpdate** | [**ProductVariantUpdate**](ProductVariantUpdate.md)|  | 

### Return type

[**AccountConfigUpdate200Response**](AccountConfigUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

