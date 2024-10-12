# DiscourseApiDocumentation.CategoriesApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCategory**](CategoriesApi.md#createCategory) | **POST** /categories.json | Creates a category
[**getCategory**](CategoriesApi.md#getCategory) | **GET** /c/{id}/show.json | Show category
[**getSite_0**](CategoriesApi.md#getSite_0) | **GET** /site.json | Get site info
[**listCategories**](CategoriesApi.md#listCategories) | **GET** /categories.json | Retrieves a list of categories
[**listCategoryTopics**](CategoriesApi.md#listCategoryTopics) | **GET** /c/{slug}/{id}.json | List topics
[**updateCategory**](CategoriesApi.md#updateCategory) | **PUT** /categories/{id}.json | Updates a category



## createCategory

> GetCategory200Response createCategory(opts)

Creates a category

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.CategoriesApi();
let opts = {
  'createCategoryRequest': new DiscourseApiDocumentation.CreateCategoryRequest() // CreateCategoryRequest | 
};
apiInstance.createCategory(opts, (error, data, response) => {
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
 **createCategoryRequest** | [**CreateCategoryRequest**](CreateCategoryRequest.md)|  | [optional] 

### Return type

[**GetCategory200Response**](GetCategory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCategory

> GetCategory200Response getCategory(id)

Show category

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.CategoriesApi();
let id = 56; // Number | 
apiInstance.getCategory(id, (error, data, response) => {
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

[**GetCategory200Response**](GetCategory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSite_0

> GetSite200Response getSite_0()

Get site info

Can be used to fetch all categories and subcategories

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.CategoriesApi();
apiInstance.getSite_0((error, data, response) => {
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

[**GetSite200Response**](GetSite200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCategories

> ListCategories200Response listCategories(opts)

Retrieves a list of categories

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.CategoriesApi();
let opts = {
  'includeSubcategories': true // Boolean | 
};
apiInstance.listCategories(opts, (error, data, response) => {
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
 **includeSubcategories** | **Boolean**|  | [optional] 

### Return type

[**ListCategories200Response**](ListCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCategoryTopics

> ListCategoryTopics200Response listCategoryTopics(slug, id)

List topics

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.CategoriesApi();
let slug = "slug_example"; // String | 
let id = 56; // Number | 
apiInstance.listCategoryTopics(slug, id, (error, data, response) => {
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
 **slug** | **String**|  | 
 **id** | **Number**|  | 

### Return type

[**ListCategoryTopics200Response**](ListCategoryTopics200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCategory

> UpdateCategory200Response updateCategory(id, opts)

Updates a category

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.CategoriesApi();
let id = 56; // Number | 
let opts = {
  'createCategoryRequest': new DiscourseApiDocumentation.CreateCategoryRequest() // CreateCategoryRequest | 
};
apiInstance.updateCategory(id, opts, (error, data, response) => {
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
 **createCategoryRequest** | [**CreateCategoryRequest**](CreateCategoryRequest.md)|  | [optional] 

### Return type

[**UpdateCategory200Response**](UpdateCategory200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

