# Semantria.CategoriesApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addCategories**](CategoriesApi.md#addCategories) | **POST** /categories.{content_type} | Add user categories
[**deleteCategories**](CategoriesApi.md#deleteCategories) | **DELETE** /categories.{content_type} | Remove user categories
[**getCategories**](CategoriesApi.md#getCategories) | **GET** /categories.{content_type} | Retrieve user categories
[**updateCategories**](CategoriesApi.md#updateCategories) | **PUT** /categories.{content_type} | Updates user categories



## addCategories

> [CategoryResponseVersion] addCategories(contentType, categories, opts)

Add user categories

This method adds user categories on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.CategoriesApi();
let contentType = "contentType_example"; // String | 
let categories = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration user categories linked to.
};
apiInstance.addCategories(contentType, categories, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **categories** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration user categories linked to. | [optional] 

### Return type

[**[CategoryResponseVersion]**](CategoryResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteCategories

> deleteCategories(contentType, categoryIDs, opts)

Remove user categories

This method removes certain user categories by their IDs on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.CategoriesApi();
let contentType = "contentType_example"; // String | 
let categoryIDs = ["null"]; // [String] | List of user category identifiers.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration user categories linked to.
};
apiInstance.deleteCategories(contentType, categoryIDs, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **categoryIDs** | [**[String]**](String.md)| List of user category identifiers. | 
 **configId** | **String**| Identifier of configuration user categories linked to. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCategories

> [CategoryResponseVersion] getCategories(contentType, opts)

Retrieve user categories

This method retrieves list of user categories available on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.CategoriesApi();
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration user categories linked to.
};
apiInstance.getCategories(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration user categories linked to. | [optional] 

### Return type

[**[CategoryResponseVersion]**](CategoryResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateCategories

> [CategoryResponseVersion] updateCategories(contentType, categories, opts)

Updates user categories

This method updates user categories by unique IDs on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.CategoriesApi();
let contentType = "contentType_example"; // String | 
let categories = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration user categories linked to.
};
apiInstance.updateCategories(contentType, categories, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **categories** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration user categories linked to. | [optional] 

### Return type

[**[CategoryResponseVersion]**](CategoryResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

