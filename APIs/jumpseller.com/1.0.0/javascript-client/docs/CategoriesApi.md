# JumpsellerApi.CategoriesApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoriesCountJsonGet**](CategoriesApi.md#categoriesCountJsonGet) | **GET** /categories/count.json | Count all Categories.
[**categoriesIdJsonDelete**](CategoriesApi.md#categoriesIdJsonDelete) | **DELETE** /categories/{id}.json | Delete an existing Category.
[**categoriesIdJsonGet**](CategoriesApi.md#categoriesIdJsonGet) | **GET** /categories/{id}.json | Retrieve a single Category.
[**categoriesIdJsonPut**](CategoriesApi.md#categoriesIdJsonPut) | **PUT** /categories/{id}.json | Modify an existing Category.
[**categoriesJsonGet**](CategoriesApi.md#categoriesJsonGet) | **GET** /categories.json | Retrieve all Categories.
[**categoriesJsonPost**](CategoriesApi.md#categoriesJsonPost) | **POST** /categories.json | Create a new Category.



## categoriesCountJsonGet

> Count categoriesCountJsonGet(login, authtoken)

Count all Categories.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.categoriesCountJsonGet(login, authtoken, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesIdJsonDelete

> String categoriesIdJsonDelete(login, authtoken, id)

Delete an existing Category.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Category
apiInstance.categoriesIdJsonDelete(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Category | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesIdJsonGet

> Category categoriesIdJsonGet(login, authtoken, id)

Retrieve a single Category.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Category
apiInstance.categoriesIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Category | 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesIdJsonPut

> Category categoriesIdJsonPut(login, authtoken, id, categoryEdit)

Modify an existing Category.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Category
let categoryEdit = new JumpsellerApi.CategoryEdit(); // CategoryEdit | Category parameters.
apiInstance.categoriesIdJsonPut(login, authtoken, id, categoryEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Category | 
 **categoryEdit** | [**CategoryEdit**](CategoryEdit.md)| Category parameters. | 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## categoriesJsonGet

> Category categoriesJsonGet(login, authtoken)

Retrieve all Categories.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.categoriesJsonGet(login, authtoken, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## categoriesJsonPost

> Category categoriesJsonPost(login, authtoken, categoryEdit)

Create a new Category.

Category&#39;s permalink is automatically generated from the given category&#39;s name.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CategoriesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let categoryEdit = new JumpsellerApi.CategoryEdit(); // CategoryEdit | Category parameters.
apiInstance.categoriesJsonPost(login, authtoken, categoryEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **categoryEdit** | [**CategoryEdit**](CategoryEdit.md)| Category parameters. | 

### Return type

[**Category**](Category.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

