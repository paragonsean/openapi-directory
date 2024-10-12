# ProductLibraryApi.CategoriesApi

All URIs are relative to *https://products.izettle.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCategories**](CategoriesApi.md#createCategories) | **POST** /organizations/{organizationUuid}/categories/v2 | Create a new category
[**deleteCategory**](CategoriesApi.md#deleteCategory) | **DELETE** /organizations/{organizationUuid}/categories/v2/{categoryUuid} | Delete a category
[**getProductTypes**](CategoriesApi.md#getProductTypes) | **GET** /organizations/{organizationUuid}/categories/v2 | Retrieve all categories
[**renameCategory**](CategoriesApi.md#renameCategory) | **PATCH** /organizations/{organizationUuid}/categories/v2/{categoryUuid} | Rename a category



## createCategories

> createCategories(organizationUuid, createCategoriesRequest)

Create a new category

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.CategoriesApi();
let organizationUuid = "organizationUuid_example"; // String | 
let createCategoriesRequest = new ProductLibraryApi.CreateCategoriesRequest(); // CreateCategoriesRequest | 
apiInstance.createCategories(organizationUuid, createCategoriesRequest, (error, data, response) => {
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
 **createCategoriesRequest** | [**CreateCategoriesRequest**](CreateCategoriesRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteCategory

> deleteCategory(organizationUuid, categoryUuid)

Delete a category

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.CategoriesApi();
let organizationUuid = "organizationUuid_example"; // String | 
let categoryUuid = "categoryUuid_example"; // String | 
apiInstance.deleteCategory(organizationUuid, categoryUuid, (error, data, response) => {
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
 **categoryUuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductTypes

> CategoryResponse getProductTypes(organizationUuid)

Retrieve all categories

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.CategoriesApi();
let organizationUuid = "organizationUuid_example"; // String | 
apiInstance.getProductTypes(organizationUuid, (error, data, response) => {
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

[**CategoryResponse**](CategoryResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## renameCategory

> renameCategory(organizationUuid, categoryUuid, renameCategoryRequest)

Rename a category

### Example

```javascript
import ProductLibraryApi from 'product_library_api';
let defaultClient = ProductLibraryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: ZettleOauth
let ZettleOauth = defaultClient.authentications['ZettleOauth'];
ZettleOauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ProductLibraryApi.CategoriesApi();
let organizationUuid = "organizationUuid_example"; // String | 
let categoryUuid = "categoryUuid_example"; // String | 
let renameCategoryRequest = new ProductLibraryApi.RenameCategoryRequest(); // RenameCategoryRequest | 
apiInstance.renameCategory(organizationUuid, categoryUuid, renameCategoryRequest, (error, data, response) => {
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
 **categoryUuid** | **String**|  | 
 **renameCategoryRequest** | [**RenameCategoryRequest**](RenameCategoryRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

