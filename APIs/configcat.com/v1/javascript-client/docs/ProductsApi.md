# ConfigCatPublicManagementApi.ProductsApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProduct**](ProductsApi.md#createProduct) | **POST** /v1/organizations/{organizationId}/products | Create Product
[**deleteProduct**](ProductsApi.md#deleteProduct) | **DELETE** /v1/products/{productId} | Delete Product
[**getProduct**](ProductsApi.md#getProduct) | **GET** /v1/products/{productId} | Get Product
[**getProducts**](ProductsApi.md#getProducts) | **GET** /v1/products | List Products
[**updateProduct**](ProductsApi.md#updateProduct) | **PUT** /v1/products/{productId} | Update Product



## createProduct

> ProductModelHaljson createProduct(organizationId, createProductRequest)

Create Product

This endpoint creates a new Product in a specified Organization  identified by the &#x60;organizationId&#x60; parameter, which can be obtained from the [List Organizations](#operation/get-organizations) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.ProductsApi();
let organizationId = "organizationId_example"; // String | The identifier of the Organization.
let createProductRequest = new ConfigCatPublicManagementApi.CreateProductRequest(); // CreateProductRequest | 
apiInstance.createProduct(organizationId, createProductRequest, (error, data, response) => {
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
 **organizationId** | **String**| The identifier of the Organization. | 
 **createProductRequest** | [**CreateProductRequest**](CreateProductRequest.md)|  | 

### Return type

[**ProductModelHaljson**](ProductModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## deleteProduct

> deleteProduct(productId)

Delete Product

This endpoint removes a Product identified by the &#x60;productId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.ProductsApi();
let productId = "productId_example"; // String | The identifier of the Product.
apiInstance.deleteProduct(productId, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProduct

> ProductModelHaljson getProduct(productId)

Get Product

This endpoint returns the metadata of a Product  identified by the &#x60;productId&#x60;.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.ProductsApi();
let productId = "productId_example"; // String | The identifier of the Product.
apiInstance.getProduct(productId, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 

### Return type

[**ProductModelHaljson**](ProductModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getProducts

> [ProductModelHaljson] getProducts()

List Products

This endpoint returns the list of the Products that belongs to the user.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.ProductsApi();
apiInstance.getProducts((error, data, response) => {
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

[**[ProductModelHaljson]**](ProductModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## updateProduct

> ProductModelHaljson updateProduct(productId, updateProductRequest)

Update Product

This endpoint updates a Product identified by the &#x60;productId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.ProductsApi();
let productId = "productId_example"; // String | The identifier of the Product.
let updateProductRequest = new ConfigCatPublicManagementApi.UpdateProductRequest(); // UpdateProductRequest | 
apiInstance.updateProduct(productId, updateProductRequest, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 
 **updateProductRequest** | [**UpdateProductRequest**](UpdateProductRequest.md)|  | 

### Return type

[**ProductModelHaljson**](ProductModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json

