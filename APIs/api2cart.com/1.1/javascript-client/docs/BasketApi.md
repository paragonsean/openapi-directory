# SwaggerApi2Cart.BasketApi

All URIs are relative to *https://api.api2cart.com/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**basketInfo**](BasketApi.md#basketInfo) | **GET** /basket.info.json | 
[**basketItemAdd**](BasketApi.md#basketItemAdd) | **POST** /basket.item.add.json | 
[**basketLiveShippingServiceCreate**](BasketApi.md#basketLiveShippingServiceCreate) | **POST** /basket.live_shipping_service.create.json | 
[**basketLiveShippingServiceDelete**](BasketApi.md#basketLiveShippingServiceDelete) | **DELETE** /basket.live_shipping_service.delete.json | 
[**basketLiveShippingServiceList**](BasketApi.md#basketLiveShippingServiceList) | **GET** /basket.live_shipping_service.list.json | 



## basketInfo

> BasketInfo200Response basketInfo(id, opts)



Retrieve basket information.

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

let apiInstance = new SwaggerApi2Cart.BasketApi();
let id = "id_example"; // String | Entity id
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'params': "'force_all'", // String | Set this parameter in order to choose which entity fields you want to retrieve
  'exclude': "exclude_example", // String | Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter `params` equal force_all
  'responseFields': "responseFields_example" // String | Set this parameter in order to choose which entity fields you want to retrieve
};
apiInstance.basketInfo(id, opts, (error, data, response) => {
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
 **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to &#39;force_all&#39;]
 **exclude** | **String**| Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all | [optional] 
 **responseFields** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] 

### Return type

[**BasketInfo200Response**](BasketInfo200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## basketItemAdd

> BasketItemAdd200Response basketItemAdd(customerId, productId, opts)



Add item to basket

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

let apiInstance = new SwaggerApi2Cart.BasketApi();
let customerId = "customerId_example"; // String | Retrieves orders specified by customer id
let productId = "productId_example"; // String | Defines id of the product which should be added to the basket
let opts = {
  'variantId': "variantId_example", // String | Defines product's variants specified by variant id
  'quantity': 0, // Number | Defines new items quantity
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.basketItemAdd(customerId, productId, opts, (error, data, response) => {
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
 **productId** | **String**| Defines id of the product which should be added to the basket | 
 **variantId** | **String**| Defines product&#39;s variants specified by variant id | [optional] 
 **quantity** | **Number**| Defines new items quantity | [optional] [default to 0]
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**BasketItemAdd200Response**](BasketItemAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## basketLiveShippingServiceCreate

> BasketLiveShippingServiceCreate200Response basketLiveShippingServiceCreate(name, callback, opts)



Create live shipping rate service.

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

let apiInstance = new SwaggerApi2Cart.BasketApi();
let name = "name_example"; // String | Shipping Service Name
let callback = "callback_example"; // String | Callback url that returns shipping rates. It should be able to accept POST requests with json data.
let opts = {
  'storeId': "storeId_example" // String | Store Id
};
apiInstance.basketLiveShippingServiceCreate(name, callback, opts, (error, data, response) => {
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
 **name** | **String**| Shipping Service Name | 
 **callback** | **String**| Callback url that returns shipping rates. It should be able to accept POST requests with json data. | 
 **storeId** | **String**| Store Id | [optional] 

### Return type

[**BasketLiveShippingServiceCreate200Response**](BasketLiveShippingServiceCreate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## basketLiveShippingServiceDelete

> BasketLiveShippingServiceDelete200Response basketLiveShippingServiceDelete(id)



Delete live shipping rate service.

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

let apiInstance = new SwaggerApi2Cart.BasketApi();
let id = 56; // Number | Entity id
apiInstance.basketLiveShippingServiceDelete(id, (error, data, response) => {
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
 **id** | **Number**| Entity id | 

### Return type

[**BasketLiveShippingServiceDelete200Response**](BasketLiveShippingServiceDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## basketLiveShippingServiceList

> BasketLiveShippingServiceList200Response basketLiveShippingServiceList(opts)



Retrieve a list of live shipping rate services.

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

let apiInstance = new SwaggerApi2Cart.BasketApi();
let opts = {
  'storeId': "storeId_example", // String | Store Id
  'start': 0, // Number | This parameter sets the number from which you want to get entities
  'count': 10 // Number | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
};
apiInstance.basketLiveShippingServiceList(opts, (error, data, response) => {
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
 **storeId** | **String**| Store Id | [optional] 
 **start** | **Number**| This parameter sets the number from which you want to get entities | [optional] [default to 0]
 **count** | **Number**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10]

### Return type

[**BasketLiveShippingServiceList200Response**](BasketLiveShippingServiceList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

