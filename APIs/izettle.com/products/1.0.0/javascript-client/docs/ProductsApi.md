# ProductLibraryApi.ProductsApi

All URIs are relative to *https://products.izettle.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countAllProducts**](ProductsApi.md#countAllProducts) | **GET** /organizations/{organizationUuid}/products/v2/count | Retrieve the count of existing products
[**createProduct**](ProductsApi.md#createProduct) | **POST** /organizations/{organizationUuid}/products | Create a new product
[**deleteProduct**](ProductsApi.md#deleteProduct) | **DELETE** /organizations/{organizationUuid}/products/{productUuid} | Delete a single product
[**deleteProducts**](ProductsApi.md#deleteProducts) | **DELETE** /organizations/{organizationUuid}/products | Delete a list of products
[**getAllOptions**](ProductsApi.md#getAllOptions) | **GET** /organizations/{organizationUuid}/products/options | Retrieve an aggregate of active Options in the library
[**getAllProductsInPos**](ProductsApi.md#getAllProductsInPos) | **GET** /organizations/{organizationUuid}/products | Retrieve all products visible in POS
[**getAllProductsV2**](ProductsApi.md#getAllProductsV2) | **GET** /organizations/{organizationUuid}/products/v2 | Retrieve all products visible in POS – v2
[**getProduct**](ProductsApi.md#getProduct) | **GET** /organizations/{organizationUuid}/products/{productUuid} | Retrieve a single product
[**updateProduct**](ProductsApi.md#updateProduct) | **PUT** /organizations/{organizationUuid}/products/v2/{productUuid} | Update a single product



## countAllProducts

> [ProductCountResponse] countAllProducts(organizationUuid)

Retrieve the count of existing products

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ProductsApi();
let organizationUuid = "organizationUuid_example"; // String | 
apiInstance.countAllProducts(organizationUuid, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 

### Return type

[**[ProductCountResponse]**](ProductCountResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createProduct

> ProductResponse createProduct(organizationUuid, productCreateRequest, opts)

Create a new product

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ProductsApi();
let organizationUuid = "organizationUuid_example"; // String | 
let productCreateRequest = new ProductLibraryApi.ProductCreateRequest(); // ProductCreateRequest | 
let opts = {
  'returnEntity': false // Boolean | 
};
apiInstance.createProduct(organizationUuid, productCreateRequest, opts, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **productCreateRequest** | [**ProductCreateRequest**](ProductCreateRequest.md)|  | 
 **returnEntity** | **Boolean**|  | [optional] [default to false]

### Return type

[**ProductResponse**](ProductResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteProduct

> deleteProduct(organizationUuid, productUuid)

Delete a single product

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ProductsApi();
let organizationUuid = "organizationUuid_example"; // String | 
let productUuid = "productUuid_example"; // String | 
apiInstance.deleteProduct(organizationUuid, productUuid, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **productUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteProducts

> deleteProducts(organizationUuid, uuid)

Delete a list of products

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ProductsApi();
let organizationUuid = "organizationUuid_example"; // String | 
let uuid = ["null"]; // [String] | List of product UUIDs to be deleted
apiInstance.deleteProducts(organizationUuid, uuid, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **uuid** | [**[String]**](String.md)| List of product UUIDs to be deleted | 

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAllOptions

> [VariantOptionsResponse] getAllOptions(organizationUuid)

Retrieve an aggregate of active Options in the library

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ProductsApi();
let organizationUuid = "organizationUuid_example"; // String | 
apiInstance.getAllOptions(organizationUuid, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 

### Return type

[**[VariantOptionsResponse]**](VariantOptionsResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllProductsInPos

> [ProductResponse] getAllProductsInPos(organizationUuid)

Retrieve all products visible in POS

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ProductsApi();
let organizationUuid = "organizationUuid_example"; // String | 
apiInstance.getAllProductsInPos(organizationUuid, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 

### Return type

[**[ProductResponse]**](ProductResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllProductsV2

> [ProductResponse] getAllProductsV2(organizationUuid, opts)

Retrieve all products visible in POS – v2

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ProductsApi();
let organizationUuid = "organizationUuid_example"; // String | 
let opts = {
  'sort': true // Boolean | If true, sorts response by created date
};
apiInstance.getAllProductsV2(organizationUuid, opts, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **sort** | **Boolean**| If true, sorts response by created date | [optional] 

### Return type

[**[ProductResponse]**](ProductResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProduct

> ProductResponse getProduct(organizationUuid, productUuid, opts)

Retrieve a single product

Get the full product with the provided UUID. The method supports conditional GET through providing a HttpHeaders.IF_NONE_MATCH header. If the conditional prerequisite is fullfilled, the full product is returned, otherwise a 304 not modified will be returned with an empty body.

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ProductsApi();
let organizationUuid = "organizationUuid_example"; // String | 
let productUuid = "productUuid_example"; // String | 
let opts = {
  'ifNoneMatch': "ifNoneMatch_example" // String | 
};
apiInstance.getProduct(organizationUuid, productUuid, opts, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **productUuid** | **String**|  | 
 **ifNoneMatch** | **String**|  | [optional] 

### Return type

[**ProductResponse**](ProductResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateProduct

> updateProduct(organizationUuid, productUuid, fullProductUpdateRequest, opts)

Update a single product

Updates a product entity using JSON merge patch (https://tools.ietf.org/html/rfc7386). This means that only included fields will be changed: null values removes the field on the target entity, and other values updates the field. Conditional updates are supported through the HttpHeaders.IF_MATCH header. If the conditional prerequisite is fullfilled, the product is updated: otherwise a 412 (precondition failed) will be returned with an empty body.

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.ProductsApi();
let organizationUuid = "organizationUuid_example"; // String | 
let productUuid = "productUuid_example"; // String | 
let fullProductUpdateRequest = new ProductLibraryApi.FullProductUpdateRequest(); // FullProductUpdateRequest | 
let opts = {
  'ifMatch': "ifMatch_example" // String | 
};
apiInstance.updateProduct(organizationUuid, productUuid, fullProductUpdateRequest, opts, (error, data, response) => {
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
 **organizationUuid** | **String**|  | 
 **productUuid** | **String**|  | 
 **fullProductUpdateRequest** | [**FullProductUpdateRequest**](FullProductUpdateRequest.md)|  | 
 **ifMatch** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

