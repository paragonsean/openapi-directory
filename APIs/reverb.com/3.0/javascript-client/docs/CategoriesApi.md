# Reverb.CategoriesApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesFlatGet**](CategoriesApi.md#categoriesFlatGet) | **GET** /categories/flat | 
[**categoriesGet**](CategoriesApi.md#categoriesGet) | **GET** /categories | List of supported product categories
[**categoriesProductTypeCategoryGet**](CategoriesApi.md#categoriesProductTypeCategoryGet) | **GET** /categories/{product_type}/{category} | Get subcategory details
[**categoriesTaxonomyGet**](CategoriesApi.md#categoriesTaxonomyGet) | **GET** /categories/taxonomy | Full taxonomy tree of categories including middle categories
[**categoriesUuidGet**](CategoriesApi.md#categoriesUuidGet) | **GET** /categories/{uuid} | Get category details



## categoriesFlatGet

> categoriesFlatGet()



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CategoriesApi();
apiInstance.categoriesFlatGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## categoriesGet

> categoriesGet()

List of supported product categories

List of supported product categories

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CategoriesApi();
apiInstance.categoriesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## categoriesProductTypeCategoryGet

> categoriesProductTypeCategoryGet(productType, category)

Get subcategory details

Get subcategory details

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CategoriesApi();
let productType = "productType_example"; // String | 
let category = "category_example"; // String | 
apiInstance.categoriesProductTypeCategoryGet(productType, category, (error, data, response) => {
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
 **productType** | **String**|  | 
 **category** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## categoriesTaxonomyGet

> categoriesTaxonomyGet()

Full taxonomy tree of categories including middle categories

Full taxonomy tree of categories including middle categories

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CategoriesApi();
apiInstance.categoriesTaxonomyGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## categoriesUuidGet

> categoriesUuidGet(uuid)

Get category details

Get category details

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CategoriesApi();
let uuid = "uuid_example"; // String | 
apiInstance.categoriesUuidGet(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

