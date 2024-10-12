# ApiManagementClient.ProductsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productCreateOrUpdate**](ProductsApi.md#productCreateOrUpdate) | **PUT** /products/{productId} | 
[**productDelete**](ProductsApi.md#productDelete) | **DELETE** /products/{productId} | 
[**productGet**](ProductsApi.md#productGet) | **GET** /products/{productId} | 
[**productList**](ProductsApi.md#productList) | **GET** /products | 
[**productUpdate**](ProductsApi.md#productUpdate) | **PATCH** /products/{productId} | 



## productCreateOrUpdate

> ProductContract productCreateOrUpdate(productId, apiVersion, parameters)



Creates or Updates a product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.ProductsApi();
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new ApiManagementClient.ProductContract(); // ProductContract | Create or update parameters.
apiInstance.productCreateOrUpdate(productId, apiVersion, parameters, (error, data, response) => {
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
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**ProductContract**](ProductContract.md)| Create or update parameters. | 

### Return type

[**ProductContract**](ProductContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productDelete

> productDelete(productId, ifMatch, apiVersion, opts)



Delete product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.ProductsApi();
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let ifMatch = "ifMatch_example"; // String | ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'deleteSubscriptions': true // Boolean | Delete existing subscriptions to the product or not.
};
apiInstance.productDelete(productId, ifMatch, apiVersion, opts, (error, data, response) => {
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
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **ifMatch** | **String**| ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **deleteSubscriptions** | **Boolean**| Delete existing subscriptions to the product or not. | [optional] 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productGet

> ProductContract productGet(productId, apiVersion)



Gets the details of the product specified by its identifier.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.ProductsApi();
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.productGet(productId, apiVersion, (error, data, response) => {
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
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**ProductContract**](ProductContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productList

> ProductCollection productList(apiVersion, opts)



Lists a collection of products in the specified service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.ProductsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | terms       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state       | eq                     |                                             |
  'top': 56, // Number | Number of records to return.
  'skip': 56, // Number | Number of records to skip.
  'expandGroups': true // Boolean | When set to true, the response contains an array of groups that have visibility to the product. The default is false.
};
apiInstance.productList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **filter** | **String**| | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | terms       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state       | eq                     |                                             | | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 
 **expandGroups** | **Boolean**| When set to true, the response contains an array of groups that have visibility to the product. The default is false. | [optional] 

### Return type

[**ProductCollection**](ProductCollection.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productUpdate

> productUpdate(productId, ifMatch, apiVersion, parameters)



Update product.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ApiManagementClient.ProductsApi();
let productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
let ifMatch = "ifMatch_example"; // String | ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new ApiManagementClient.ProductUpdateParameters(); // ProductUpdateParameters | Update parameters.
apiInstance.productUpdate(productId, ifMatch, apiVersion, parameters, (error, data, response) => {
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
 **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | 
 **ifMatch** | **String**| ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**ProductUpdateParameters**](ProductUpdateParameters.md)| Update parameters. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

