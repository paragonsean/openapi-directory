# SwaggerApi2Cart.AttributeApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributeAdd**](AttributeApi.md#attributeAdd) | **POST** /attribute.add.json | 
[**attributeAssignGroup**](AttributeApi.md#attributeAssignGroup) | **POST** /attribute.assign.group.json | 
[**attributeAssignSet**](AttributeApi.md#attributeAssignSet) | **POST** /attribute.assign.set.json | 
[**attributeAttributesetList**](AttributeApi.md#attributeAttributesetList) | **GET** /attribute.attributeset.list.json | 
[**attributeCount**](AttributeApi.md#attributeCount) | **GET** /attribute.count.json | 
[**attributeDelete**](AttributeApi.md#attributeDelete) | **DELETE** /attribute.delete.json | 
[**attributeGroupList**](AttributeApi.md#attributeGroupList) | **GET** /attribute.group.list.json | 
[**attributeInfo**](AttributeApi.md#attributeInfo) | **GET** /attribute.info.json | 
[**attributeList**](AttributeApi.md#attributeList) | **GET** /attribute.list.json | 
[**attributeTypeList**](AttributeApi.md#attributeTypeList) | **GET** /attribute.type.list.json | 
[**attributeUnassignGroup**](AttributeApi.md#attributeUnassignGroup) | **POST** /attribute.unassign.group.json | 
[**attributeUnassignSet**](AttributeApi.md#attributeUnassignSet) | **POST** /attribute.unassign.set.json | 
[**attributeUpdate**](AttributeApi.md#attributeUpdate) | **POST** /attribute.update.json | 



## attributeAdd

> AttributeAdd200Response attributeAdd(type, name, opts)



Add new attribute

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let type = "type_example"; // String | Defines attribute's type
let name = "name_example"; // String | Defines attributes's name
let opts = {
  'code': "code_example", // String | Entity code
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'visible': false, // Boolean | Set visibility status
  'required': false, // Boolean | Defines if the option is required
  'position': 0, // Number | Attribute`s position
  'attributeGroupId': "attributeGroupId_example", // String | Filter by attribute_group_id
  'isGlobal': "'Store'", // String | Attribute saving scope
  'isSearchable': false, // Boolean | Use attribute in Quick Search
  'isFilterable': "'false'", // String | Use In Layered Navigation
  'isComparable': false, // Boolean | Comparable on Front-end
  'isHtmlAllowedOnFront': false, // Boolean | Allow HTML Tags on Frontend
  'isFilterableInSearch': false, // Boolean | Use In Search Results Layered Navigation
  'isConfigurable': false, // Boolean | Use To Create Configurable Product
  'isVisibleInAdvancedSearch': false, // Boolean | Use in Advanced Search
  'isUsedForPromoRules': false, // Boolean | Use for Promo Rule Conditions
  'usedInProductListing': false, // Boolean | Used in Product Listing
  'usedForSortBy': false, // Boolean | Used for Sorting in Product Listing
  'applyTo': "'all_types'" // String | Types of products which can have this attribute
};
apiInstance.attributeAdd(type, name, opts, (error, data, response) => {
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
 **type** | **String**| Defines attribute&#39;s type | 
 **name** | **String**| Defines attributes&#39;s name | 
 **code** | **String**| Entity code | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **visible** | **Boolean**| Set visibility status | [optional] [default to false]
 **required** | **Boolean**| Defines if the option is required | [optional] [default to false]
 **position** | **Number**| Attribute&#x60;s position | [optional] [default to 0]
 **attributeGroupId** | **String**| Filter by attribute_group_id | [optional] 
 **isGlobal** | **String**| Attribute saving scope | [optional] [default to &#39;Store&#39;]
 **isSearchable** | **Boolean**| Use attribute in Quick Search | [optional] [default to false]
 **isFilterable** | **String**| Use In Layered Navigation | [optional] [default to &#39;false&#39;]
 **isComparable** | **Boolean**| Comparable on Front-end | [optional] [default to false]
 **isHtmlAllowedOnFront** | **Boolean**| Allow HTML Tags on Frontend | [optional] [default to false]
 **isFilterableInSearch** | **Boolean**| Use In Search Results Layered Navigation | [optional] [default to false]
 **isConfigurable** | **Boolean**| Use To Create Configurable Product | [optional] [default to false]
 **isVisibleInAdvancedSearch** | **Boolean**| Use in Advanced Search | [optional] [default to false]
 **isUsedForPromoRules** | **Boolean**| Use for Promo Rule Conditions | [optional] [default to false]
 **usedInProductListing** | **Boolean**| Used in Product Listing | [optional] [default to false]
 **usedForSortBy** | **Boolean**| Used for Sorting in Product Listing | [optional] [default to false]
 **applyTo** | **String**| Types of products which can have this attribute | [optional] [default to &#39;all_types&#39;]

### Return type

[**AttributeAdd200Response**](AttributeAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeAssignGroup

> AttributeAssignGroup200Response attributeAssignGroup(id, groupId, opts)



Assign attribute to the group

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let id = "id_example"; // String | Entity id
let groupId = "groupId_example"; // String | Attribute group_id
let opts = {
  'attributeSetId': "attributeSetId_example" // String | Attribute set id
};
apiInstance.attributeAssignGroup(id, groupId, opts, (error, data, response) => {
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
 **id** | **String**| Entity id | 
 **groupId** | **String**| Attribute group_id | 
 **attributeSetId** | **String**| Attribute set id | [optional] 

### Return type

[**AttributeAssignGroup200Response**](AttributeAssignGroup200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeAssignSet

> AttributeAssignGroup200Response attributeAssignSet(id, attributeSetId, opts)



Assign attribute to the attribute set

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let id = "id_example"; // String | Entity id
let attributeSetId = "attributeSetId_example"; // String | Attribute set id
let opts = {
  'groupId': "groupId_example" // String | Attribute group_id
};
apiInstance.attributeAssignSet(id, attributeSetId, opts, (error, data, response) => {
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
 **id** | **String**| Entity id | 
 **attributeSetId** | **String**| Attribute set id | 
 **groupId** | **String**| Attribute group_id | [optional] 

### Return type

[**AttributeAssignGroup200Response**](AttributeAssignGroup200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeAttributesetList

> AttributeAttributesetList200Response attributeAttributesetList(opts)



Get attribute_set list

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'params': "'id,name'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'responseFields': "responseFields_example" // String | Set this parameter in order to choose which entity fields you want to retrieve
};
apiInstance.attributeAttributesetList(opts, (error, data, response) => {
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
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 

### Return type

[**AttributeAttributesetList200Response**](AttributeAttributesetList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeCount

> AttributeCount200Response attributeCount(opts)



Get attributes count

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let opts = {
  'type': "type_example", // String | Defines attribute's type
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'visible': true, // Boolean | Filter items by visibility status
  'required': true, // Boolean | Defines if the option is required
  'system': true // Boolean | True if attribute is system
};
apiInstance.attributeCount(opts, (error, data, response) => {
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
 **type** | **String**| Defines attribute&#39;s type | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **visible** | **Boolean**| Filter items by visibility status | [optional] 
 **required** | **Boolean**| Defines if the option is required | [optional] 
 **system** | **Boolean**| True if attribute is system | [optional] 

### Return type

[**AttributeCount200Response**](AttributeCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeDelete

> AttributeDelete200Response attributeDelete(id, opts)



Delete attribute from store

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let id = "id_example"; // String | Entity id
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.attributeDelete(id, opts, (error, data, response) => {
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
 **id** | **String**| Entity id | 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeGroupList

> AttributeAttributesetList200Response attributeGroupList(opts)



Get attribute group list

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'langId': "langId_example", // String | Language id
  'params': "'id,name'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'attributeSetId': "attributeSetId_example" // String | Attribute set id
};
apiInstance.attributeGroupList(opts, (error, data, response) => {
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
 **langId** | **String**| Language id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **attributeSetId** | **String**| Attribute set id | [optional] 

### Return type

[**AttributeAttributesetList200Response**](AttributeAttributesetList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeInfo

> AttributeInfo200Response attributeInfo(id, opts)



Get attribute info

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let id = "id_example"; // String | Entity id
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'params': "'force_all'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'responseFields': "responseFields_example" // String | Set this parameter in order to choose which entity fields you want to retrieve
};
apiInstance.attributeInfo(id, opts, (error, data, response) => {
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
 **id** | **String**| Entity id | 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;force_all&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 

### Return type

[**AttributeInfo200Response**](AttributeInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeList

> ModelResponseAttributeList attributeList(opts)



Get attributes list

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let opts = {
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'type': "type_example", // String | Defines attribute's type
  'attributeIds': "attributeIds_example", // String | Filter attributes by ids
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Retrieves attributes on specified language id
  'params': "'id,name,code,type'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'visible': true, // Boolean | Filter items by visibility status
  'required': true, // Boolean | Defines if the option is required
  'system': true // Boolean | True if attribute is system
};
apiInstance.attributeList(opts, (error, data, response) => {
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
 **type** | **String**| Defines attribute&#39;s type | [optional] 
 **attributeIds** | **String**| Filter attributes by ids | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Retrieves attributes on specified language id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,code,type&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **visible** | **Boolean**| Filter items by visibility status | [optional] 
 **required** | **Boolean**| Defines if the option is required | [optional] 
 **system** | **Boolean**| True if attribute is system | [optional] 

### Return type

[**ModelResponseAttributeList**](ModelResponseAttributeList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeTypeList

> AttributeTypeList200Response attributeTypeList()



Get list of supported attributes types

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
apiInstance.attributeTypeList((error, data, response) => {
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

[**AttributeTypeList200Response**](AttributeTypeList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeUnassignGroup

> AttributeUnassignGroup200Response attributeUnassignGroup(id, groupId)



Unassign attribute from group

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let id = "id_example"; // String | Entity id
let groupId = "groupId_example"; // String | Customer group_id
apiInstance.attributeUnassignGroup(id, groupId, (error, data, response) => {
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
 **id** | **String**| Entity id | 
 **groupId** | **String**| Customer group_id | 

### Return type

[**AttributeUnassignGroup200Response**](AttributeUnassignGroup200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeUnassignSet

> AttributeUnassignGroup200Response attributeUnassignSet(id, attributeSetId)



Unassign attribute from attribute set

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let id = "id_example"; // String | Entity id
let attributeSetId = "attributeSetId_example"; // String | Attribute set id
apiInstance.attributeUnassignSet(id, attributeSetId, (error, data, response) => {
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
 **id** | **String**| Entity id | 
 **attributeSetId** | **String**| Attribute set id | 

### Return type

[**AttributeUnassignGroup200Response**](AttributeUnassignGroup200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attributeUpdate

> AttributeUpdate200Response attributeUpdate(id, name, opts)



Update attribute data

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

let apiInstance = new SwaggerApi2Cart.AttributeApi();
let id = "id_example"; // String | Entity id
let name = "name_example"; // String | Defines new attributes's name
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example" // String | Language id
};
apiInstance.attributeUpdate(id, name, opts, (error, data, response) => {
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
 **id** | **String**| Entity id | 
 **name** | **String**| Defines new attributes&#39;s name | 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 

### Return type

[**AttributeUpdate200Response**](AttributeUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

