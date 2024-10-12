# CommerceApi.ProductsApi

All URIs are relative to *https://api.codat.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listProductCategories**](ProductsApi.md#listProductCategories) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-productCategories | List product categories
[**listProducts**](ProductsApi.md#listProducts) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-products | List products



## listProductCategories

> ProductCategories listProductCategories(page, opts)

List product categories

Product categories are used to classify a group of products together, either by type (eg \&quot;Furniture\&quot;), or sometimes by tax profile.

### Example

```javascript
import CommerceApi from 'commerce_api';
let defaultClient = CommerceApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CommerceApi.ProductsApi();
let page = 1; // Number | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
let opts = {
  'pageSize': 100, // Number | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
  'query': "query_example", // String | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
  'orderBy': "-modifiedDate" // String | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
};
apiInstance.listProductCategories(page, opts, (error, data, response) => {
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
 **page** | **Number**| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [default to 1]
 **pageSize** | **Number**| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | **String**| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **orderBy** | **String**| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**ProductCategories**](ProductCategories.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProducts

> Products listProducts(page, opts)

List products

The Products data type provides the company&#39;s product inventory, and includes the price and quantity of all products, and product variants, available for sale.

### Example

```javascript
import CommerceApi from 'commerce_api';
let defaultClient = CommerceApi.ApiClient.instance;
// Configure API key authorization: auth_header
let auth_header = defaultClient.authentications['auth_header'];
auth_header.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//auth_header.apiKeyPrefix = 'Token';

let apiInstance = new CommerceApi.ProductsApi();
let page = 1; // Number | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
let opts = {
  'pageSize': 100, // Number | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
  'query': "query_example", // String | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
  'orderBy': "-modifiedDate" // String | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
};
apiInstance.listProducts(page, opts, (error, data, response) => {
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
 **page** | **Number**| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [default to 1]
 **pageSize** | **Number**| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100]
 **query** | **String**| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] 
 **orderBy** | **String**| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] 

### Return type

[**Products**](Products.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

