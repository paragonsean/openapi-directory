# BillingoApiV3.ProductApi

All URIs are relative to *https://api.billingo.hu/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProduct**](ProductApi.md#createProduct) | **POST** /products | Create a product
[**deleteProduct**](ProductApi.md#deleteProduct) | **DELETE** /products/{id} | Delete a product
[**getProduct**](ProductApi.md#getProduct) | **GET** /products/{id} | Retrieve a product
[**listProduct**](ProductApi.md#listProduct) | **GET** /products | List all product
[**updateProduct**](ProductApi.md#updateProduct) | **PUT** /products/{id} | Update a product



## createProduct

> Product createProduct(product)

Create a product

Create a new product. Returns a product object if the create is succeded.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.ProductApi();
let product = new BillingoApiV3.Product(); // Product | Product object that you would like to store.
apiInstance.createProduct(product, (error, data, response) => {
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
 **product** | [**Product**](Product.md)| Product object that you would like to store. | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteProduct

> deleteProduct(id)

Delete a product

Delete an existing product.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.ProductApi();
let id = 56; // Number | 
apiInstance.deleteProduct(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProduct

> Product getProduct(id)

Retrieve a product

Retrieves the details of an existing product.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.ProductApi();
let id = 56; // Number | 
apiInstance.getProduct(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProduct

> ProductList listProduct(opts)

List all product

Returns a list of your products. The partners are returned sorted by creation date, with the most recent partners appearing first.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.ProductApi();
let opts = {
  'page': 56, // Number | 
  'perPage': 25 // Number | 
};
apiInstance.listProduct(opts, (error, data, response) => {
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
 **page** | **Number**|  | [optional] 
 **perPage** | **Number**|  | [optional] [default to 25]

### Return type

[**ProductList**](ProductList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateProduct

> Product updateProduct(id, product)

Update a product

Update an existing product. Returns a product object if the update is succeded.

### Example

```javascript
import BillingoApiV3 from 'billingo_api_v3';
let defaultClient = BillingoApiV3.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BillingoApiV3.ProductApi();
let id = 56; // Number | 
let product = new BillingoApiV3.Product(); // Product | Product object that you would like to update.
apiInstance.updateProduct(id, product, (error, data, response) => {
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
 **id** | **Number**|  | 
 **product** | [**Product**](Product.md)| Product object that you would like to update. | 

### Return type

[**Product**](Product.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

