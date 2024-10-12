# SwaggerApi2Cart.CustomerApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAdd**](CustomerApi.md#customerAdd) | **POST** /customer.add.json | 
[**customerAttributeList**](CustomerApi.md#customerAttributeList) | **GET** /customer.attribute.list.json | 
[**customerCount**](CustomerApi.md#customerCount) | **GET** /customer.count.json | 
[**customerFind**](CustomerApi.md#customerFind) | **GET** /customer.find.json | 
[**customerGroupAdd**](CustomerApi.md#customerGroupAdd) | **POST** /customer.group.add.json | 
[**customerGroupList**](CustomerApi.md#customerGroupList) | **GET** /customer.group.list.json | 
[**customerInfo**](CustomerApi.md#customerInfo) | **GET** /customer.info.json | 
[**customerList**](CustomerApi.md#customerList) | **GET** /customer.list.json | 
[**customerUpdate**](CustomerApi.md#customerUpdate) | **PUT** /customer.update.json | 
[**customerWishlistList**](CustomerApi.md#customerWishlistList) | **GET** /customer.wishlist.list.json | 



## customerAdd

> CustomerAdd200Response customerAdd(customerAdd)



Add customer into store.

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

let apiInstance = new SwaggerApi2Cart.CustomerApi();
let customerAdd = new SwaggerApi2Cart.CustomerAdd(); // CustomerAdd | 
apiInstance.customerAdd(customerAdd, (error, data, response) => {
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
 **customerAdd** | [**CustomerAdd**](CustomerAdd.md)|  | 

### Return type

[**CustomerAdd200Response**](CustomerAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerAttributeList

> ModelResponseCustomerAttributeList customerAttributeList(customerId, opts)



Get attributes for specific customer

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

let apiInstance = new SwaggerApi2Cart.CustomerApi();
let customerId = "customerId_example"; // String | Retrieves orders specified by customer id
let opts = {
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'params': "'force_all'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'responseFields': "responseFields_example" // String | Set this parameter in order to choose which entity fields you want to retrieve
};
apiInstance.customerAttributeList(customerId, opts, (error, data, response) => {
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
 **customerId** | **String**| Retrieves orders specified by customer id | 
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;force_all&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 

### Return type

[**ModelResponseCustomerAttributeList**](ModelResponseCustomerAttributeList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerCount

> CustomerCount200Response customerCount(opts)



Get number of customers from store.

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

let apiInstance = new SwaggerApi2Cart.CustomerApi();
let opts = {
  'groupId': "groupId_example", // String | Customer group_id
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'storeId': "storeId_example", // String | Counts customer specified by store id
  'customerListId': "customerListId_example", // String | The numeric ID of the customer list in Demandware.
  'avail': true // Boolean | Defines category's visibility status
};
apiInstance.customerCount(opts, (error, data, response) => {
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
 **groupId** | **String**| Customer group_id | [optional] 
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **storeId** | **String**| Counts customer specified by store id | [optional] 
 **customerListId** | **String**| The numeric ID of the customer list in Demandware. | [optional] 
 **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true]

### Return type

[**CustomerCount200Response**](CustomerCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerFind

> CustomerFind200Response customerFind(findValue, opts)



Find customers in store.

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

let apiInstance = new SwaggerApi2Cart.CustomerApi();
let findValue = "findValue_example"; // String | Entity search that is specified by some value
let opts = {
  'findWhere': "'email'", // String | Entity search that is specified by the comma-separated unique fields
  'findParams': "'whole_words'", // String | Entity search that is specified by comma-separated parameters
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.customerFind(findValue, opts, (error, data, response) => {
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
 **findWhere** | **String**| Entity search that is specified by the comma-separated unique fields | [optional] [default to &#39;email&#39;]
 **findParams** | **String**| Entity search that is specified by comma-separated parameters | [optional] [default to &#39;whole_words&#39;]
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**CustomerFind200Response**](CustomerFind200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerGroupAdd

> CustomerGroupAdd200Response customerGroupAdd(name, opts)



Create customer group.

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

let apiInstance = new SwaggerApi2Cart.CustomerApi();
let name = "name_example"; // String | Customer group name
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'storesIds': "storesIds_example" // String | Assign customer group to the stores that is specified by comma-separated stores' id
};
apiInstance.customerGroupAdd(name, opts, (error, data, response) => {
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
 **name** | **String**| Customer group name | 
 **storeId** | **String**| Store Id | [optional] 
 **storesIds** | **String**| Assign customer group to the stores that is specified by comma-separated stores&#39; id | [optional] 

### Return type

[**CustomerGroupAdd200Response**](CustomerGroupAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerGroupList

> ModelResponseCustomerGroupList customerGroupList(opts)



Get list of customers groups.

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

let apiInstance = new SwaggerApi2Cart.CustomerApi();
let opts = {
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'storeId': "storeId_example", // String | Store Id
  'langId': "langId_example", // String | Language id
  'groupIds': "groupIds_example", // String | Groups that will be assigned to a customer
  'params': "'id,name,additional_fields'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'responseFields': "responseFields_example" // String | Set this parameter in order to choose which entity fields you want to retrieve
};
apiInstance.customerGroupList(opts, (error, data, response) => {
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
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **storeId** | **String**| Store Id | [optional] 
 **langId** | **String**| Language id | [optional] 
 **groupIds** | **String**| Groups that will be assigned to a customer | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,name,additional_fields&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 

### Return type

[**ModelResponseCustomerGroupList**](ModelResponseCustomerGroupList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerInfo

> CustomerInfo200Response customerInfo(id, opts)



Get customers&#39; details from store.

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

let apiInstance = new SwaggerApi2Cart.CustomerApi();
let id = "id_example"; // String | Retrieves customer's info specified by customer id
let opts = {
  'params': "'id,email,first_name,last_name'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'storeId': "storeId_example" // String | Retrieves customer info specified by store id
};
apiInstance.customerInfo(id, opts, (error, data, response) => {
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
 **id** | **String**| Retrieves customer&#39;s info specified by customer id | 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,email,first_name,last_name&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **storeId** | **String**| Retrieves customer info specified by store id | [optional] 

### Return type

[**CustomerInfo200Response**](CustomerInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerList

> ModelResponseCustomerList customerList(opts)



Get list of customers from store.

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

let apiInstance = new SwaggerApi2Cart.CustomerApi();
let opts = {
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'createdFrom': "createdFrom_example", // String | Retrieve entities from their creation date
  'createdTo': "createdTo_example", // String | Retrieve entities to their creation date
  'modifiedFrom': "modifiedFrom_example", // String | Retrieve entities from their modification date
  'modifiedTo': "modifiedTo_example", // String | Retrieve entities to their modification date
  'params': "'id,email,first_name,last_name'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'responseFields': "responseFields_example", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'groupId': "groupId_example", // String | Customer group_id
  'storeId': "storeId_example", // String | Retrieves customers specified by store id
  'customerListId': "customerListId_example", // String | The numeric ID of the customer list in Demandware.
  'avail': true // Boolean | Defines category's visibility status
};
apiInstance.customerList(opts, (error, data, response) => {
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
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **createdFrom** | **String**| Retrieve entities from their creation date | [optional] 
 **createdTo** | **String**| Retrieve entities to their creation date | [optional] 
 **modifiedFrom** | **String**| Retrieve entities from their modification date | [optional] 
 **modifiedTo** | **String**| Retrieve entities to their modification date | [optional] 
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;id,email,first_name,last_name&#39;]
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **groupId** | **String**| Customer group_id | [optional] 
 **storeId** | **String**| Retrieves customers specified by store id | [optional] 
 **customerListId** | **String**| The numeric ID of the customer list in Demandware. | [optional] 
 **avail** | **Boolean**| Defines category&#39;s visibility status | [optional] [default to true]

### Return type

[**ModelResponseCustomerList**](ModelResponseCustomerList.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customerUpdate

> CustomerUpdate200Response customerUpdate(customerUpdate)



Update information of customer in store.

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

let apiInstance = new SwaggerApi2Cart.CustomerApi();
let customerUpdate = new SwaggerApi2Cart.CustomerUpdate(); // CustomerUpdate | 
apiInstance.customerUpdate(customerUpdate, (error, data, response) => {
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
 **customerUpdate** | [**CustomerUpdate**](CustomerUpdate.md)|  | 

### Return type

[**CustomerUpdate200Response**](CustomerUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customerWishlistList

> CustomerWishlistList200Response customerWishlistList(customerId, opts)



Get a Wish List of customer from the store.

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

let apiInstance = new SwaggerApi2Cart.CustomerApi();
let customerId = "customerId_example"; // String | Retrieves orders specified by customer id
let opts = {
  'id': "id_example", // String | Entity id
  'storeId': "storeId_example", // String | Store Id
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10, // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
  'pageCursor': "pageCursor_example", // String | Used to retrieve entities via cursor-based pagination (it can't be used with any other filtering parameter)
  'responseFields': "'{return_code,return_message,pagination,result}'" // String | Set this parameter in order to choose which entity fields you want to retrieve
};
apiInstance.customerWishlistList(customerId, opts, (error, data, response) => {
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
 **customerId** | **String**| Retrieves orders specified by customer id | 
 **id** | **String**| Entity id | [optional] 
 **storeId** | **String**| Store Id | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]
 **pageCursor** | **String**| Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter) | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;{return_code,return_message,pagination,result}&#39;]

### Return type

[**CustomerWishlistList200Response**](CustomerWishlistList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

